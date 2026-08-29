"""Start the official vendored MinIE HTTP service on 127.0.0.1:8080."""
from pathlib import Path
import socket
import subprocess

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "vendor" / "minie"

if __name__ == "__main__":
    if not (VENDOR / "pom.xml").exists():
        raise SystemExit("MinIE source is missing. See extraction_pipeline/README.md.")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
            if probe.connect_ex(("127.0.0.1", 8080)) == 0:
                raise SystemExit("Port 8080 is already in use. Stop the existing MinIE service with Ctrl+C before restarting it.")
    except PermissionError:
        # Restricted execution sandboxes may prohibit socket probes. Maven will
        # still report any real bind error when the service is started.
        pass
    command = ["mvn", "-ntp", "-Dmaven.repo.local=../../.m2",
               "-Dexec.mainClass=uk.ac.ucl.cs.mr.Main", "exec:java"]
    raise SystemExit(subprocess.run(command, cwd=VENDOR).returncode)
