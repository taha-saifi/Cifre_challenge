#!/usr/bin/env python3
"""OpenRouter client: fixed fallback chain for chat, one model for embeddings.

Relationship to the 45 recorded cells -- state this plainly rather than blur it
--------------------------------------------------------------------------------
The 45 cells of `experiments/results/` were produced by isolated Claude Code subagents,
one call each, no retry. A web server cannot spawn those, so this client is a DIFFERENT
TRANSPORT. What is preserved is the thing the methodology actually rests on: the decision
prompt is byte-identical across configurations, and only the context varies. What changes
is which model answers. Any claim that this tool "replays" the recorded cells would be
false; it is an exploration tool built on the same prompt contract.

Fallback is on availability, not on quality: the order below is fixed and no comparison
between models is made or implied.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

BASE_URL = os.environ.get("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
API_KEY = os.environ.get("OPENROUTER_API_KEY", "")

# Fixed order. Position, not merit.
CHAT_MODELS = [
    "nvidia/nemotron-3.5-lightning:free",
    "poolside/laguna-s-2.1:free",
    "inclusionai/ling-3.0-flash-fin:free",
]
EMBEDDING_MODEL = "liquid/lfm-2.5-embedding-350m:free"

# All three chat models emit chain-of-thought into a separate `reasoning` field and can
# return content=None if the token budget is spent reasoning. Budget generously and treat
# an empty content as a failure of that model, not as an empty answer.
# Generous: the first model spends ~2000 tokens on chain-of-thought before it
# begins the answer, and a truncated answer is unusable.
MAX_TOKENS = 6000
TIMEOUT_SECONDS = 120


class ModelUnavailable(RuntimeError):
    """Every model in the chain failed. The caller shows 'configuration indisponible'."""


# The first model in the chain emits its chain-of-thought into `content` and ignores any
# instruction not to (verified directly, including with reasoning.exclude=true). The
# order of the chain is fixed by decision, so the fix is display-side: strip the
# preamble, keep the raw text available, never drop content silently.
_COT_OPENERS = re.compile(
    r"^\s*(?:here'?s (?:a|my) (?:thinking|thought) process|let me think|"
    r"okay,? (?:let'?s|i)\b|first,? (?:let me|i'll) (?:analyz|understand))",
    re.I)
_ANSWER_MARKER = re.compile(
    r"(?:^|\n)\s*(?:\*\*|##\s*)?(?:D[ée]cision|Conclusion|R[ée]ponse)\b\s*(?:finale)?\s*(?:\*\*)?\s*:",
    re.I)
_TRAILER = re.compile(
    r"(?:^|\n)\s*(?:Check against constraint|Let me verify|Self-check|"
    r"V[ée]rification (?:de|des) contrainte)", re.I)
# English deliberation markers left inside a French answer. The expected output is
# French prose, so these discriminate reliably without rejecting a legitimate answer.
_STILL_REASONING = re.compile(
    r"\b(?:let me (?:draft|think|write|check)|i need to (?:decide|check)|"
    r"key considerations|i'?ll (?:draft|write)|\[list |strictly\]|"
    r"based on the provided information,? i)\b", re.I)


def strip_reasoning_preamble(text: str) -> str:
    """Remove a leaked chain-of-thought preamble and any trailing self-check.

    Conservative by design: if no answer marker is found the original text is returned
    untouched. Losing an answer would be worse than showing a verbose one.
    """
    if not _COT_OPENERS.search(text):
        return text
    matches = list(_ANSWER_MARKER.finditer(text))
    if not matches:
        return text
    cleaned = text[matches[-1].start():].strip()
    trailer = _TRAILER.search(cleaned)
    if trailer:
        cleaned = cleaned[:trailer.start()].strip()
    return cleaned or text


def _headers() -> dict:
    return {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def have_key() -> bool:
    return bool(API_KEY)


def chat(prompt: str) -> dict:
    """Send one prompt through the fallback chain.

    Returns {"text", "model", "attempts"}. Raises ModelUnavailable if all three fail.
    A 429 (rate limit) is treated exactly like any other failure: move to the next model.
    """
    if not API_KEY:
        raise ModelUnavailable("OPENROUTER_API_KEY absent (.env non chargé)")

    attempts = []
    for model in CHAT_MODELS:
        try:
            response = requests.post(
                f"{BASE_URL}/chat/completions",
                headers=_headers(),
                timeout=TIMEOUT_SECONDS,
                json={"model": model,
                      "messages": [{"role": "user", "content": prompt}],
                      "max_tokens": MAX_TOKENS},
            )
        except requests.RequestException as exc:
            attempts.append({"model": model, "outcome": f"{type(exc).__name__}"})
            continue

        if response.status_code == 429:
            attempts.append({"model": model, "outcome": "429 rate-limited"})
            continue
        if response.status_code != 200:
            attempts.append({"model": model, "outcome": f"HTTP {response.status_code}"})
            continue

        try:
            payload = response.json()
            choice = (payload.get("choices") or [{}])[0]
            text = (choice.get("message") or {}).get("content")
        except (ValueError, IndexError, AttributeError):
            attempts.append({"model": model, "outcome": "réponse illisible"})
            continue

        if not (text or "").strip():
            # Reasoning model that spent its budget before writing an answer.
            attempts.append({"model": model, "outcome": "contenu vide"})
            continue

        raw = text.strip()
        cleaned = strip_reasoning_preamble(raw)
        # A model that emitted only chain-of-thought and ran out of budget before writing
        # a conclusion has not answered. Showing that as an answer would be misleading, so
        # it counts as a failure of this model and the chain moves on -- which is exactly
        # what the fallback exists for.
        if _COT_OPENERS.search(raw) and cleaned == raw:
            attempts.append({"model": model,
                             "outcome": f"raisonnement sans conclusion "
                                        f"(finish={choice.get('finish_reason')})"})
            continue
        # Same principle one step later: the preamble was stripped but what remains is
        # still visible deliberation rather than an answer. This is a usability gate on
        # the output, not a judgement of the model -- the chain order stays as declared.
        if _STILL_REASONING.search(cleaned):
            attempts.append({"model": model, "outcome": "sortie encore délibérative"})
            continue
        # Truncated mid-answer: incomplete, so unusable. Fall through rather than show it.
        if choice.get("finish_reason") == "length":
            attempts.append({"model": model, "outcome": "réponse tronquée (budget épuisé)"})
            continue

        attempts.append({"model": model, "outcome": "ok"})
        return {"text": cleaned, "raw": raw, "model": model, "attempts": attempts}

    raise ModelUnavailable("; ".join(f"{a['model']}: {a['outcome']}" for a in attempts))


def embed(texts: list[str]) -> list[list[float]]:
    """Embed a batch. Retrieval only -- this model does not do chat."""
    if not API_KEY:
        raise ModelUnavailable("OPENROUTER_API_KEY absent (.env non chargé)")
    response = requests.post(
        f"{BASE_URL}/embeddings",
        headers=_headers(),
        timeout=TIMEOUT_SECONDS,
        json={"model": EMBEDDING_MODEL, "input": texts},
    )
    if response.status_code != 200:
        raise ModelUnavailable(f"embeddings HTTP {response.status_code}: {response.text[:200]}")
    data = sorted(response.json()["data"], key=lambda d: d.get("index", 0))
    return [d["embedding"] for d in data]
