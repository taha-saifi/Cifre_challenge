# Relation clusters for human review

Edit `clusters_validation.json`: set `decision` to `accept`, `reject`, or `split`. The canonical relation is filled automatically from the cluster representative and can be overridden only when needed. If `review_status` is `needs_reconfirmation`, check the `diff` field before deciding, then add `"reconfirm": true` alongside your decision to clear it -- otherwise the next export will downgrade it back to pending.

## exploit

- Cluster ID: `rc2_04da09655d48e492`
- Assertions: 63
- Phrases: exploit, exploits, exploited, Exploited, exploiting, Exploit, Exploits, are exploited, can exploit, could exploit, has exploited, have exploited, is exploiting
- Suggested normal forms: exploit
- Decision: reject (review_status: confirmed)

## has affected version bound

- Cluster ID: `rc2_f0e9ea38bd12793a`
- Assertions: 39
- Phrases: has affected version bound
- Suggested normal forms: affect version bound
- Decision: accept (review_status: confirmed)

## requires

- Cluster ID: `rc2_c4d0cf241a1bfa1c`
- Assertions: 39
- Phrases: requires, require, does require, Requires
- Suggested normal forms: require
- Decision: reject (review_status: confirmed)

## include

- Cluster ID: `rc2_c0cbff04cc90f5b4`
- Assertions: 31
- Phrases: include, includes
- Suggested normal forms: include
- Decision: accept (review_status: confirmed)

## has affected product

- Cluster ID: `rc2_2266f742faf7c6b6`
- Assertions: 29
- Phrases: has affected product
- Suggested normal forms: affect product
- Decision: accept (review_status: confirmed)

## has vendor

- Cluster ID: `rc2_630ba09448af5221`
- Assertions: 29
- Phrases: has vendor
- Suggested normal forms: vendor
- Decision: accept (review_status: confirmed)

## provides

- Cluster ID: `rc2_405abc33f5f3b06b`
- Assertions: 29
- Phrases: provides, provide
- Suggested normal forms: provide
- Decision: accept (review_status: confirmed)

## use

- Cluster ID: `rc2_a3b142af6e97cfc3`
- Assertions: 25
- Phrases: use, uses, do use, Uses
- Suggested normal forms: use
- Decision: accept (review_status: confirmed)

## references

- Cluster ID: `rc2_52367a6622b19f08`
- Assertions: 24
- Phrases: references, reference
- Suggested normal forms: reference
- Decision: accept (review_status: confirmed)

## contains

- Cluster ID: `rc2_dd9245cc1ddc69c8`
- Assertions: 23
- Phrases: contains, contain, contained /
- Suggested normal forms: contain, contain /
- Decision: pending (review_status: pending)

## patch

- Cluster ID: `rc2_a4895eb44afc336f`
- Assertions: 22
- Phrases: patch, has patch, patched, patching
- Suggested normal forms: patch
- Decision: split (review_status: confirmed)

## allows

- Cluster ID: `rc2_410083735735a10e`
- Assertions: 21
- Phrases: allows, allow, has allowed
- Suggested normal forms: allow
- Decision: reject (review_status: confirmed)

## be exploit

- Cluster ID: `rc2_9293ae39dcfa6f06`
- Assertions: 19
- Phrases: be exploit, be exploited
- Suggested normal forms: be exploit
- Decision: pending (review_status: pending)

## be using

- Cluster ID: `rc2_74a20c907c6a07e5`
- Assertions: 19
- Phrases: be using, be used, be Using
- Suggested normal forms: be us
- Decision: pending (review_status: pending)

## is required

- Cluster ID: `rc2_0675956a2697b250`
- Assertions: 19
- Phrases: is required, Required, required
- Suggested normal forms: requir
- Decision: reject (review_status: confirmed)

## be scored

- Cluster ID: `rc2_d8a88e99aa993a8a`
- Assertions: 18
- Phrases: be scored, be scoring
- Suggested normal forms: be scor
- Decision: accept (review_status: confirmed)

## used

- Cluster ID: `rc2_79adb2a2fce5c6ba`
- Assertions: 18
- Phrases: used, is used, are using
- Suggested normal forms: us
- Decision: reject (review_status: confirmed)

## affect

- Cluster ID: `rc2_8528058461899c6b`
- Assertions: 17
- Phrases: affect, affected, affects, can affect, do affect, does affect, is affected
- Suggested normal forms: affect
- Decision: reject (review_status: confirmed)

## applies to

- Cluster ID: `rc2_46bda8dbf814d82d`
- Assertions: 16
- Phrases: applies to, apply to, Do apply to, do apply to, does apply to
- Suggested normal forms: apply to
- Decision: pending (review_status: pending)

## like to thank

- Cluster ID: `rc2_fba0ba56f9bb6429`
- Assertions: 16
- Phrases: like to thank
- Suggested normal forms: like to thank
- Decision: accept (review_status: confirmed)

## publish

- Cluster ID: `rc2_a5d47a4311d759db`
- Assertions: 15
- Phrases: publish, publishing, published, are published, are publishing, has published
- Suggested normal forms: publish
- Decision: reject (review_status: confirmed)

## refers to accessibility of

- Cluster ID: `rc2_e4d4f53ec38cb5f3`
- Assertions: 15
- Phrases: refers to accessibility of
- Suggested normal forms: refer to accessibility of
- Decision: accept (review_status: confirmed)

## reflects

- Cluster ID: `rc2_909ca0096d519dcf`
- Assertions: 15
- Phrases: reflects, reflect, do reflect
- Suggested normal forms: reflect
- Decision: pending (review_status: pending)

## refers to

- Cluster ID: `rc2_d786cce7a4f88ea0`
- Assertions: 13
- Phrases: refers to, refer to
- Suggested normal forms: refer to
- Decision: pending (review_status: pending)

## are specified by

- Cluster ID: `rc2_cf574be87e690837`
- Assertions: 12
- Phrases: are specified by
- Suggested normal forms: specifi by
- Decision: pending (review_status: pending)

## be considered

- Cluster ID: `rc2_4e847988505abca8`
- Assertions: 12
- Phrases: be considered
- Suggested normal forms: be consider
- Decision: accept (review_status: confirmed)

## be scored relative to impacted component If

- Cluster ID: `rc2_596395a31a3a2cd3`
- Assertions: 12
- Phrases: be scored relative to impacted component If
- Suggested normal forms: be scor relative to impact component if
- Decision: accept (review_status: confirmed)

## cause

- Cluster ID: `rc2_6a7ef1ed9f15c2f5`
- Assertions: 12
- Phrases: cause, causes
- Suggested normal forms: cause
- Decision: reject (review_status: confirmed)

## is provided without

- Cluster ID: `rc2_9df3135d3d4ca7ef`
- Assertions: 12
- Phrases: is provided without
- Suggested normal forms: provid without
- Decision: accept (review_status: confirmed)

## support

- Cluster ID: `rc2_a18603086e5bdf9d`
- Assertions: 12
- Phrases: support, supports, do support, does support, supported
- Suggested normal forms: support
- Decision: pending (review_status: pending)

## assign

- Cluster ID: `rc2_9300b4d2567aad13`
- Assertions: 11
- Phrases: assign, are assigned, is assigned
- Suggested normal forms: assign
- Decision: pending (review_status: pending)

## be rated as

- Cluster ID: `rc2_cf73f63c190bdb43`
- Assertions: 11
- Phrases: be rated as
- Suggested normal forms: be rat a
- Decision: pending (review_status: pending)

## produce

- Cluster ID: `rc2_1198780b3af7203c`
- Assertions: 11
- Phrases: produce, produces
- Suggested normal forms: produce
- Decision: pending (review_status: pending)

## added

- Cluster ID: `rc2_7e9e5ac30f2216fd`
- Assertions: 10
- Phrases: added, Added, add, adds
- Suggested normal forms: add
- Decision: reject (review_status: confirmed)

## be provided by

- Cluster ID: `rc2_1c59287574d6df11`
- Assertions: 10
- Phrases: be provided by
- Suggested normal forms: be provid by
- Decision: accept (review_status: confirmed)

## change over

- Cluster ID: `rc2_fa7789930ddcff16`
- Assertions: 10
- Phrases: change over, changes over, do change over
- Suggested normal forms: change over
- Decision: accept (review_status: confirmed)

## consider

- Cluster ID: `rc2_2181584795ff5511`
- Assertions: 10
- Phrases: consider, is considered, considers
- Suggested normal forms: consider
- Decision: pending (review_status: pending)

## help

- Cluster ID: `rc2_106a5842fc5fce6f`
- Assertions: 10
- Phrases: help
- Suggested normal forms: help
- Decision: accept (review_status: confirmed)

## provided

- Cluster ID: `rc2_d5c9290c84274e90`
- Assertions: 10
- Phrases: provided, has provided, is provided
- Suggested normal forms: provid
- Decision: reject (review_status: confirmed)

## refers to limiting

- Cluster ID: `rc2_42029673f5d664af`
- Assertions: 10
- Phrases: refers to limiting
- Suggested normal forms: refer to limit
- Decision: pending (review_status: pending)

## result in

- Cluster ID: `rc2_d98927794af5b99e`
- Assertions: 10
- Phrases: result in, resulted in, results in
- Suggested normal forms: result in
- Decision: accept (review_status: confirmed)

## be listed in

- Cluster ID: `rc2_c45ef91dfc58af94`
- Assertions: 9
- Phrases: be listed in
- Suggested normal forms: be list in
- Decision: accept (review_status: confirmed)

## be used by

- Cluster ID: `rc2_1876f5789bf1158f`
- Assertions: 9
- Phrases: be used by
- Suggested normal forms: be us by
- Decision: accept (review_status: confirmed)

## captures

- Cluster ID: `rc2_460ee6aa3a803591`
- Assertions: 9
- Phrases: captures, capture
- Suggested normal forms: capture
- Decision: pending (review_status: pending)

## has confirmed presence of

- Cluster ID: `rc2_d9deff6cb8f7c46c`
- Assertions: 9
- Phrases: has confirmed presence of
- Suggested normal forms: confirm presence of
- Decision: pending (review_status: pending)

## make

- Cluster ID: `rc2_d05aa2a15fb3c40e`
- Assertions: 9
- Phrases: make, makes
- Suggested normal forms: make
- Decision: accept (review_status: confirmed)

## are constant over

- Cluster ID: `rc2_d6c5c908230ec133`
- Assertions: 8
- Phrases: are constant over
- Suggested normal forms: constant over
- Decision: accept (review_status: confirmed)

## be amended based on

- Cluster ID: `rc2_66b2b51878cd46a4`
- Assertions: 8
- Phrases: be amended based on
- Suggested normal forms: be amend bas on
- Decision: pending (review_status: pending)

## be based on

- Cluster ID: `rc2_243631d92c205fd7`
- Assertions: 8
- Phrases: be based on
- Suggested normal forms: be bas on
- Decision: accept (review_status: confirmed)

## be managed by

- Cluster ID: `rc2_01d91d622e8cea4f`
- Assertions: 8
- Phrases: be managed by
- Suggested normal forms: be manag by
- Decision: accept (review_status: confirmed)

## be used to derive

- Cluster ID: `rc2_dbe26d4a0e6edac0`
- Assertions: 8
- Phrases: be used to derive
- Suggested normal forms: be us to derive
- Decision: accept (review_status: confirmed)

## disclosed

- Cluster ID: `rc2_ff8ad187ba7d0fbd`
- Assertions: 8
- Phrases: disclosed
- Suggested normal forms: disclos
- Decision: accept (review_status: confirmed)

## install

- Cluster ID: `rc2_1e142e6277b12b7e`
- Assertions: 8
- Phrases: install, installed, installs
- Suggested normal forms: install
- Decision: pending (review_status: pending)

## protect

- Cluster ID: `rc2_680dce633db1189e`
- Assertions: 8
- Phrases: protect, are protect, protects
- Suggested normal forms: protect
- Decision: pending (review_status: pending)

## assign greater value

- Cluster ID: `rc2_dd0d08c856036556`
- Assertions: 7
- Phrases: assign greater value
- Suggested normal forms: assign greater value
- Decision: pending (review_status: pending)

## be rated

- Cluster ID: `rc2_cdfff80875ac5126`
- Assertions: 7
- Phrases: be rated
- Suggested normal forms: be rat
- Decision: accept (review_status: confirmed)

## becomes

- Cluster ID: `rc2_9ebb1e6f5b2adf42`
- Assertions: 7
- Phrases: becomes, has become
- Suggested normal forms: become
- Decision: accept (review_status: confirmed)

## define

- Cluster ID: `rc2_ecd38f260821a09a`
- Assertions: 7
- Phrases: define, defines
- Suggested normal forms: define
- Decision: accept (review_status: confirmed)

## enable analyst to customize

- Cluster ID: `rc2_549986ce6821d053`
- Assertions: 7
- Phrases: enable analyst to customize, enable consumer analyst to customize, enable consumer to customize
- Suggested normal forms: enable analyst to customize, enable consumer analyst to customize, enable consumer to customize
- Decision: pending (review_status: pending)

## possess

- Cluster ID: `rc2_67d6b00baf086ced`
- Assertions: 7
- Phrases: possess
- Suggested normal forms: posses
- Decision: accept (review_status: confirmed)

## represents characteristics of

- Cluster ID: `rc2_d36e61560239108c`
- Assertions: 7
- Phrases: represents characteristics of, represent characteristics of
- Suggested normal forms: represent characteristic of
- Decision: pending (review_status: pending)

## adjust

- Cluster ID: `rc2_2549c096fc692b12`
- Assertions: 6
- Phrases: adjust, adjusts
- Suggested normal forms: adjust
- Decision: pending (review_status: pending)

## allow industry sectors such as

- Cluster ID: `rc2_c45fb9cd6e8bd1a8`
- Assertions: 6
- Phrases: allow industry sectors such as
- Suggested normal forms: allow industry sector such a
- Decision: pending (review_status: pending)

## are across

- Cluster ID: `rc2_bb4882c6a32eefc0`
- Assertions: 6
- Phrases: are across
- Suggested normal forms: acros
- Decision: accept (review_status: confirmed)

## are across user environments over

- Cluster ID: `rc2_088b9923b580e9a6`
- Assertions: 6
- Phrases: are across user environments over
- Suggested normal forms: acros user environment over
- Decision: accept (review_status: confirmed)

## are considered in calculation of

- Cluster ID: `rc2_5e54813c65a42b5e`
- Assertions: 6
- Phrases: are considered in calculation of
- Suggested normal forms: consider in calculation of
- Decision: pending (review_status: pending)

## are part of

- Cluster ID: `rc2_6e955beae4e5872e`
- Assertions: 6
- Phrases: are part of, is part of
- Suggested normal forms: part of
- Decision: accept (review_status: confirmed)

## are same In

- Cluster ID: `rc2_56a5792f88433e9c`
- Assertions: 6
- Phrases: are same In
- Suggested normal forms: same in
- Decision: accept (review_status: confirmed)

## authorizes Secretary of

- Cluster ID: `rc2_8c77e558321bfb12`
- Assertions: 6
- Phrases: authorizes Secretary of
- Suggested normal forms: authorize secretary of
- Decision: pending (review_status: pending)

## be Serving as central hub for

- Cluster ID: `rc2_576b2fa6aeec9521`
- Assertions: 6
- Phrases: be Serving as central hub for
- Suggested normal forms: be serv a central hub for
- Decision: pending (review_status: pending)

## be access

- Cluster ID: `rc2_a893e272b5a6b8be`
- Assertions: 6
- Phrases: be access
- Suggested normal forms: be acces
- Decision: accept (review_status: confirmed)

## be achieve

- Cluster ID: `rc2_764993ef665b1a96`
- Assertions: 6
- Phrases: be achieve
- Suggested normal forms: be achieve
- Decision: accept (review_status: confirmed)

## be delivered as payload of

- Cluster ID: `rc2_52f3f4244b8e60f9`
- Assertions: 6
- Phrases: be delivered as payload of
- Suggested normal forms: be deliver a payload of
- Decision: pending (review_status: pending)

## be examine

- Cluster ID: `rc2_88ee37a0312eb3ff`
- Assertions: 6
- Phrases: be examine
- Suggested normal forms: be examine
- Decision: accept (review_status: confirmed)

## be in to exploit

- Cluster ID: `rc2_384183a35a8e4201`
- Assertions: 6
- Phrases: be in to exploit, be assessed in to exploit
- Suggested normal forms: be assess in to exploit, be in to exploit
- Decision: pending (review_status: pending)

## be manufactured by

- Cluster ID: `rc2_18889783e1a5e90d`
- Assertions: 6
- Phrases: be manufactured by
- Suggested normal forms: be manufactur by
- Decision: accept (review_status: confirmed)

## be prevent

- Cluster ID: `rc2_4754544a4eebef6a`
- Assertions: 6
- Phrases: be prevent
- Suggested normal forms: be prevent
- Decision: accept (review_status: confirmed)

## be protected by

- Cluster ID: `rc2_e886d92f447b204c`
- Assertions: 6
- Phrases: be protected by
- Suggested normal forms: be protect by
- Decision: accept (review_status: confirmed)

## be resulting from

- Cluster ID: `rc2_5af6dd361bada391`
- Assertions: 6
- Phrases: be resulting from
- Suggested normal forms: be result from
- Decision: accept (review_status: confirmed)

## be support

- Cluster ID: `rc2_3fa8ed7cb91e8cee`
- Assertions: 6
- Phrases: be support, be supporting
- Suggested normal forms: be support
- Decision: accept (review_status: confirmed)

## be used in

- Cluster ID: `rc2_0ecd8c60fbbbbf42`
- Assertions: 6
- Phrases: be used in
- Suggested normal forms: be us in
- Decision: accept (review_status: confirmed)

## captures principal technical characteristics of

- Cluster ID: `rc2_83e843830f6b3c52`
- Assertions: 6
- Phrases: captures principal technical characteristics of
- Suggested normal forms: capture principal technical characteristic of
- Decision: pending (review_status: pending)

## define standard method of extending CVSS to include additional metrics while

- Cluster ID: `rc2_00b4cad698f820d9`
- Assertions: 6
- Phrases: define standard method of extending CVSS to include additional metrics while, define standard method of extending CVSS to include metric groups while
- Suggested normal forms: define standard method of extend cvs to include additional metric while, define standard method of extend cvs to include metric group while
- Decision: pending (review_status: pending)

## executed

- Cluster ID: `rc2_a000c0a43188f7fa`
- Assertions: 6
- Phrases: executed, executing, is executed
- Suggested normal forms: execut
- Decision: split (review_status: confirmed)

## gives attacker

- Cluster ID: `rc2_89ceb280448be99a`
- Assertions: 6
- Phrases: gives attacker
- Suggested normal forms: give attacker
- Decision: accept (review_status: confirmed)

## has description

- Cluster ID: `rc2_c9046f7a37ad0ea7`
- Assertions: 6
- Phrases: has description
- Suggested normal forms: description
- Decision: accept (review_status: confirmed)

## has issued

- Cluster ID: `rc2_8029917f039e0845`
- Assertions: 6
- Phrases: has issued
- Suggested normal forms: issu
- Decision: accept (review_status: confirmed)

## have been advised of possibility of

- Cluster ID: `rc2_8ab2eb15c0d94429`
- Assertions: 6
- Phrases: have been advised of possibility of
- Suggested normal forms: been advis of possibility of
- Decision: pending (review_status: pending)

## included

- Cluster ID: `rc2_0801948b891ba5a8`
- Assertions: 6
- Phrases: included, is included
- Suggested normal forms: includ
- Decision: reject (review_status: confirmed)

## involve

- Cluster ID: `rc2_873f8161e2c69fa3`
- Assertions: 6
- Phrases: involve, involves
- Suggested normal forms: involve
- Decision: accept (review_status: confirmed)

## is responsibility of

- Cluster ID: `rc2_937b75660e59a5d5`
- Assertions: 6
- Phrases: is responsibility of
- Suggested normal forms: responsibility of
- Decision: accept (review_status: confirmed)

## is trusted by enterprises worldwide to store

- Cluster ID: `rc2_6e8258a2beaa6459`
- Assertions: 6
- Phrases: is trusted by enterprises worldwide to store
- Suggested normal forms: trust by enterprise worldwide to store
- Decision: pending (review_status: pending)

## mean

- Cluster ID: `rc2_82523faea1b0f2da`
- Assertions: 6
- Phrases: mean, means
- Suggested normal forms: mean
- Decision: pending (review_status: pending)

## read

- Cluster ID: `rc2_3316348dbadfb7b1`
- Assertions: 6
- Phrases: read, reads
- Suggested normal forms: read
- Decision: pending (review_status: pending)

## recommends

- Cluster ID: `rc2_0eb15ad185af2b35`
- Assertions: 6
- Phrases: recommends
- Suggested normal forms: recommend
- Decision: accept (review_status: confirmed)

## represents boundary between qualitative severity scores to be

- Cluster ID: `rc2_7e6f55371521b11d`
- Assertions: 6
- Phrases: represents boundary between qualitative severity scores to be
- Suggested normal forms: represent boundary between qualitative severity score to be
- Decision: accept (review_status: confirmed)

## requires attention from

- Cluster ID: `rc2_07451f5555679a34`
- Assertions: 6
- Phrases: requires attention from
- Suggested normal forms: require attention from
- Decision: accept (review_status: confirmed)

## see

- Cluster ID: `rc2_aa9e9b5c907d50fe`
- Assertions: 6
- Phrases: see
- Suggested normal forms: see
- Decision: accept (review_status: confirmed)

## send

- Cluster ID: `rc2_27ce1d1bf4270020`
- Assertions: 6
- Phrases: send, sends
- Suggested normal forms: send
- Decision: accept (review_status: confirmed)

## set

- Cluster ID: `rc2_6ee0eb490ff83210`
- Assertions: 6
- Phrases: set
- Suggested normal forms: set
- Decision: accept (review_status: confirmed)

## trigger

- Cluster ID: `rc2_683259feabbf5eb3`
- Assertions: 6
- Phrases: trigger, triggers
- Suggested normal forms: trigger
- Decision: pending (review_status: pending)

## worked

- Cluster ID: `rc2_00e13ed7af55b276`
- Assertions: 6
- Phrases: worked, work
- Suggested normal forms: work
- Decision: pending (review_status: pending)

## account for largest share of

- Cluster ID: `rc2_b11b97ce0006c62f`
- Assertions: 5
- Phrases: account for largest share of
- Suggested normal forms: account for largest share of
- Decision: pending (review_status: pending)

## account for largest share of compromised hosts at very top of

- Cluster ID: `rc2_c9ab344b6836e043`
- Assertions: 5
- Phrases: account for largest share of compromised hosts at very top of
- Suggested normal forms: account for largest share of compromis host at very top of
- Decision: pending (review_status: pending)

## account for largest share of compromised hosts with

- Cluster ID: `rc2_77e027b2cde960a3`
- Assertions: 5
- Phrases: account for largest share of compromised hosts with
- Suggested normal forms: account for largest share of compromis host with
- Decision: pending (review_status: pending)

## acknowledges

- Cluster ID: `rc2_085afa73a88616ef`
- Assertions: 5
- Phrases: acknowledges
- Suggested normal forms: acknowledge
- Decision: accept (review_status: confirmed)

## address

- Cluster ID: `rc2_5c30e4d1421ae511`
- Assertions: 5
- Phrases: address
- Suggested normal forms: addres
- Decision: accept (review_status: confirmed)

## allows attacker

- Cluster ID: `rc2_986f49369804809c`
- Assertions: 5
- Phrases: allows attacker, allow attacker
- Suggested normal forms: allow attacker
- Decision: pending (review_status: pending)

## allows unauthorized attacker to execute

- Cluster ID: `rc2_54bd902527b4fd72`
- Assertions: 5
- Phrases: allows unauthorized attacker to execute, allows attacker to execute
- Suggested normal forms: allow attacker to execute, allow unauthoriz attacker to execute
- Decision: pending (review_status: pending)

## are defined

- Cluster ID: `rc2_75b32591bf282bf8`
- Assertions: 5
- Phrases: are defined, defined, has defined
- Suggested normal forms: defin
- Decision: accept (review_status: confirmed)

## are established

- Cluster ID: `rc2_3a19589098bc0e3a`
- Assertions: 5
- Phrases: are established, establish, have established
- Suggested normal forms: establish
- Decision: pending (review_status: pending)

## are unique to

- Cluster ID: `rc2_bdc646a232df69e5`
- Assertions: 5
- Phrases: are unique to
- Suggested normal forms: unique to
- Decision: accept (review_status: confirmed)

## be Sharing without

- Cluster ID: `rc2_58f56d20a3af34ee`
- Assertions: 5
- Phrases: be Sharing without
- Suggested normal forms: be shar without
- Decision: accept (review_status: confirmed)

## be develop

- Cluster ID: `rc2_6b474fc2d9175796`
- Assertions: 5
- Phrases: be develop
- Suggested normal forms: be develop
- Decision: pending (review_status: pending)

## be exploited at will of

- Cluster ID: `rc2_78b754971a1c3392`
- Assertions: 5
- Phrases: be exploited at will of
- Suggested normal forms: be exploit at of
- Decision: accept (review_status: confirmed)

## be participate in successful compromise

- Cluster ID: `rc2_15080359d07593ec`
- Assertions: 5
- Phrases: be participate in successful compromise, be participate in successful compromise of
- Suggested normal forms: be participate in successful compromise, be participate in successful compromise of
- Decision: pending (review_status: pending)

## be score

- Cluster ID: `rc2_1fdda3016c934319`
- Assertions: 5
- Phrases: be score
- Suggested normal forms: be score
- Decision: pending (review_status: pending)

## be targeting

- Cluster ID: `rc2_f103537c7074fa21`
- Assertions: 5
- Phrases: be targeting, be targeted
- Suggested normal forms: be target
- Decision: pending (review_status: pending)

## calls

- Cluster ID: `rc2_7edb360f06acaef2`
- Assertions: 5
- Phrases: calls, call, called
- Suggested normal forms: call
- Decision: pending (review_status: pending)

## change

- Cluster ID: `rc2_12ea12eace7d655f`
- Assertions: 5
- Phrases: change, changes
- Suggested normal forms: change
- Decision: accept (review_status: confirmed)

## confirms

- Cluster ID: `rc2_3f267c2ab422e502`
- Assertions: 5
- Phrases: confirms, confirmed
- Suggested normal forms: confirm
- Decision: pending (review_status: pending)

## consume

- Cluster ID: `rc2_96f39e3569ec878e`
- Assertions: 5
- Phrases: consume
- Suggested normal forms: consume
- Decision: accept (review_status: confirmed)

## describes level of

- Cluster ID: `rc2_4acf60654e8dee56`
- Assertions: 5
- Phrases: describes level of
- Suggested normal forms: describe level of
- Decision: accept (review_status: confirmed)

## give

- Cluster ID: `rc2_0895a532e404a5c9`
- Assertions: 5
- Phrases: give, gives, Gives
- Suggested normal forms: give
- Decision: pending (review_status: pending)

## has EPSS percentile

- Cluster ID: `rc2_71dfbd1e6dbb1ac3`
- Assertions: 5
- Phrases: has EPSS percentile
- Suggested normal forms: eps percentile
- Decision: accept (review_status: confirmed)

## has EPSS probability

- Cluster ID: `rc2_f3ad70f8a2aacdb8`
- Assertions: 5
- Phrases: has EPSS probability
- Suggested normal forms: eps probability
- Decision: accept (review_status: confirmed)

## has SSVC automatable

- Cluster ID: `rc2_90ebc444124a2d70`
- Assertions: 5
- Phrases: has SSVC automatable
- Suggested normal forms: ssvc automatable
- Decision: accept (review_status: confirmed)

## has SSVC exploitation

- Cluster ID: `rc2_51356d74c189b760`
- Assertions: 5
- Phrases: has SSVC exploitation
- Suggested normal forms: ssvc exploitation
- Decision: accept (review_status: confirmed)

## has SSVC technicalImpact

- Cluster ID: `rc2_e5f281ab9dadda65`
- Assertions: 5
- Phrases: has SSVC technicalImpact
- Suggested normal forms: ssvc technicalimpact
- Decision: accept (review_status: confirmed)

## has attackComplexity

- Cluster ID: `rc2_dcf2283cd3a91062`
- Assertions: 5
- Phrases: has attackComplexity
- Suggested normal forms: attackcomplexity
- Decision: accept (review_status: confirmed)

## has attackVector

- Cluster ID: `rc2_c0b0d28ffbd469e6`
- Assertions: 5
- Phrases: has attackVector
- Suggested normal forms: attackvector
- Decision: accept (review_status: confirmed)

## has availabilityImpact

- Cluster ID: `rc2_df005b1357fc001a`
- Assertions: 5
- Phrases: has availabilityImpact
- Suggested normal forms: availabilityimpact
- Decision: accept (review_status: confirmed)

## has baseScore

- Cluster ID: `rc2_3fcdc57a9c304843`
- Assertions: 5
- Phrases: has baseScore
- Suggested normal forms: basescore
- Decision: accept (review_status: confirmed)

## has baseSeverity

- Cluster ID: `rc2_f9d0e6a19a1a73c2`
- Assertions: 5
- Phrases: has baseSeverity
- Suggested normal forms: baseseverity
- Decision: accept (review_status: confirmed)

## has confidentialityImpact

- Cluster ID: `rc2_e6f8df61aa9032cb`
- Assertions: 5
- Phrases: has confidentialityImpact
- Suggested normal forms: confidentialityimpact
- Decision: accept (review_status: confirmed)

## has corresponding Base values of

- Cluster ID: `rc2_55693eaaeebfc6f2`
- Assertions: 5
- Phrases: has corresponding Base values of, has corresponding Base value of
- Suggested normal forms: correspond base value of
- Decision: pending (review_status: pending)

## has exploitabilityScore

- Cluster ID: `rc2_d221dbb323dfd34c`
- Assertions: 5
- Phrases: has exploitabilityScore
- Suggested normal forms: exploitabilityscore
- Decision: accept (review_status: confirmed)

## has impactScore

- Cluster ID: `rc2_ab50e9ac2ecdf4f6`
- Assertions: 5
- Phrases: has impactScore
- Suggested normal forms: impactscore
- Decision: accept (review_status: confirmed)

## has integrityImpact

- Cluster ID: `rc2_70068aecc888fb1a`
- Assertions: 5
- Phrases: has integrityImpact
- Suggested normal forms: integrityimpact
- Decision: accept (review_status: confirmed)

## has last modified date

- Cluster ID: `rc2_c0d9c6e046f48a77`
- Assertions: 5
- Phrases: has last modified date
- Suggested normal forms: last modifi date
- Decision: accept (review_status: confirmed)

## has observation date

- Cluster ID: `rc2_8bd519bf0ea10f11`
- Assertions: 5
- Phrases: has observation date
- Suggested normal forms: observation date
- Decision: accept (review_status: confirmed)

## has privilegesRequired

- Cluster ID: `rc2_c5503cc12dc800d5`
- Assertions: 5
- Phrases: has privilegesRequired
- Suggested normal forms: privilegesrequir
- Decision: accept (review_status: confirmed)

## has published date

- Cluster ID: `rc2_47f15d203dca7c13`
- Assertions: 5
- Phrases: has published date
- Suggested normal forms: publish date
- Decision: accept (review_status: confirmed)

## has scope

- Cluster ID: `rc2_5f161c9149882e0e`
- Assertions: 5
- Phrases: has scope
- Suggested normal forms: scope
- Decision: accept (review_status: confirmed)

## has source identifier

- Cluster ID: `rc2_80bcdf566f82fd37`
- Assertions: 5
- Phrases: has source identifier
- Suggested normal forms: source identifier
- Decision: accept (review_status: confirmed)

## has userInteraction

- Cluster ID: `rc2_e406329760d24951`
- Assertions: 5
- Phrases: has userInteraction
- Suggested normal forms: userinteraction
- Decision: accept (review_status: confirmed)

## has vectorString

- Cluster ID: `rc2_fafa1a08c77f2586`
- Assertions: 5
- Phrases: has vectorString
- Suggested normal forms: vectorstr
- Decision: accept (review_status: confirmed)

## has vulnerability status

- Cluster ID: `rc2_110880262b046440`
- Assertions: 5
- Phrases: has vulnerability status
- Suggested normal forms: vulnerability statu
- Decision: accept (review_status: confirmed)

## has weakness

- Cluster ID: `rc2_5cb82a24b0ca5910`
- Assertions: 5
- Phrases: has weakness
- Suggested normal forms: weaknes
- Decision: accept (review_status: confirmed)

## impact

- Cluster ID: `rc2_6f61f46c23a66607`
- Assertions: 5
- Phrases: impact, does impact
- Suggested normal forms: impact
- Decision: pending (review_status: pending)

## is determined by

- Cluster ID: `rc2_bc06080d1ee5be93`
- Assertions: 5
- Phrases: is determined by
- Suggested normal forms: determin by
- Decision: accept (review_status: confirmed)

## is in

- Cluster ID: `rc2_582967534d0f909d`
- Assertions: 5
- Phrases: is in, are in
- Suggested normal forms: in
- Decision: pending (review_status: pending)

## is outside scope of

- Cluster ID: `rc2_b976b037287a2374`
- Assertions: 5
- Phrases: is outside scope of, are outside scope of
- Suggested normal forms: outside scope of
- Decision: pending (review_status: pending)

## maintains

- Cluster ID: `rc2_91bb720d0df35005`
- Assertions: 5
- Phrases: maintains, maintained
- Suggested normal forms: maintain
- Decision: pending (review_status: pending)

## meet

- Cluster ID: `rc2_8ccb033c0e48b27f`
- Assertions: 5
- Phrases: meet
- Suggested normal forms: meet
- Decision: accept (review_status: confirmed)

## modify

- Cluster ID: `rc2_9106d6212bb4dfc9`
- Assertions: 5
- Phrases: modify, do modify
- Suggested normal forms: modify
- Decision: pending (review_status: pending)

## observes

- Cluster ID: `rc2_74e892c91130daa5`
- Assertions: 5
- Phrases: observes
- Suggested normal forms: observe
- Decision: accept (review_status: confirmed)

## recognizes

- Cluster ID: `rc2_1b00de68c4c9617c`
- Assertions: 5
- Phrases: recognizes
- Suggested normal forms: recognize
- Decision: accept (review_status: confirmed)

## reduce

- Cluster ID: `rc2_4c7e98bfa0c750be`
- Assertions: 5
- Phrases: reduce, reduces
- Suggested normal forms: reduce
- Decision: pending (review_status: pending)

## refers to preventing

- Cluster ID: `rc2_ba73ea5cb9fc2cc2`
- Assertions: 5
- Phrases: refers to preventing
- Suggested normal forms: refer to prevent
- Decision: pending (review_status: pending)

## refers to trustworthiness of

- Cluster ID: `rc2_06c0e54f55252990`
- Assertions: 5
- Phrases: refers to trustworthiness of
- Suggested normal forms: refer to trustworthines of
- Decision: pending (review_status: pending)

## represents

- Cluster ID: `rc2_8cfc12e7f78033dc`
- Assertions: 5
- Phrases: represents, represent
- Suggested normal forms: represent
- Decision: pending (review_status: pending)

## suggests

- Cluster ID: `rc2_dc726d0a525fdaf7`
- Assertions: 5
- Phrases: suggests
- Suggested normal forms: suggest
- Decision: accept (review_status: confirmed)

## was discovered by

- Cluster ID: `rc2_abdddb466a309f9e`
- Assertions: 5
- Phrases: was discovered by, were discovered by
- Suggested normal forms: discover by
- Decision: pending (review_status: pending)

## worked in 2020

- Cluster ID: `rc2_34fa4b7a3de8eb17`
- Assertions: 5
- Phrases: worked in 2020
- Suggested normal forms: work in 2020
- Decision: pending (review_status: pending)

## worked with SEI

- Cluster ID: `rc2_0ee73aa898937ec3`
- Assertions: 5
- Phrases: worked with SEI
- Suggested normal forms: work with sei
- Decision: pending (review_status: pending)

## write

- Cluster ID: `rc2_10fd874b68dad080`
- Assertions: 5
- Phrases: write
- Suggested normal forms: write
- Decision: accept (review_status: confirmed)

## Based on

- Cluster ID: `rc2_e3146a9b53e192dd`
- Assertions: 4
- Phrases: Based on
- Suggested normal forms: bas on
- Decision: accept (review_status: confirmed)

## accepts

- Cluster ID: `rc2_c125d0397b605657`
- Assertions: 4
- Phrases: accepts, accept, accepted
- Suggested normal forms: accept
- Decision: accept (review_status: confirmed)

## added CVE-2026-55040 to

- Cluster ID: `rc2_e520d78e7076dbc5`
- Assertions: 4
- Phrases: added CVE-2026-55040 to, adds CVE-2026-55040 to
- Suggested normal forms: add cve-2026-55040 to
- Decision: accept (review_status: confirmed)

## allows other processes to impact

- Cluster ID: `rc2_b3f8e34a4af20476`
- Assertions: 4
- Phrases: allows other processes to impact
- Suggested normal forms: allow other processe to impact
- Decision: pending (review_status: pending)

## allows unauthorized attacker to execute code over

- Cluster ID: `rc2_fd26dc9c138e3ea3`
- Assertions: 4
- Phrases: allows unauthorized attacker to execute code over
- Suggested normal forms: allow unauthoriz attacker to execute code over
- Decision: pending (review_status: pending)

## applies whether

- Cluster ID: `rc2_a0c90d86a905dc50`
- Assertions: 4
- Phrases: applies whether
- Suggested normal forms: apply whether
- Decision: accept (review_status: confirmed)

## apply to loss of

- Cluster ID: `rc2_7a63a5526ed3b633`
- Assertions: 4
- Phrases: apply to loss of
- Suggested normal forms: apply to los of
- Decision: accept (review_status: confirmed)

## are designed

- Cluster ID: `rc2_a77de8a6daa11295`
- Assertions: 4
- Phrases: are designed, is designed
- Suggested normal forms: design
- Decision: pending (review_status: pending)

## are disclosing first vulnerability in

- Cluster ID: `rc2_c9a49575fcd37289`
- Assertions: 4
- Phrases: are disclosing first vulnerability in, are disclosing first vulnerability in chain
- Suggested normal forms: disclos first vulnerability in, disclos first vulnerability in chain
- Decision: pending (review_status: pending)

## are disclosing second vulnerability in

- Cluster ID: `rc2_93ee85889f5372b1`
- Assertions: 4
- Phrases: are disclosing second vulnerability in, are disclosing second vulnerability in chain
- Suggested normal forms: disclos second vulnerability in, disclos second vulnerability in chain
- Decision: pending (review_status: pending)

## are enabling detection of

- Cluster ID: `rc2_b40b48b4cc17de37`
- Assertions: 4
- Phrases: are enabling detection of
- Suggested normal forms: enabl detection of
- Decision: pending (review_status: pending)

## are exposed such as

- Cluster ID: `rc2_dfa07dbeceadd277`
- Assertions: 4
- Phrases: are exposed such as
- Suggested normal forms: expos such a
- Decision: accept (review_status: confirmed)

## are for VPN infrastructure enabling detection of

- Cluster ID: `rc2_19b5d456e5d3bcee`
- Assertions: 4
- Phrases: are for VPN infrastructure enabling detection of
- Suggested normal forms: for vpn infrastructure enabl detection of
- Decision: pending (review_status: pending)

## are in place enabling detection of

- Cluster ID: `rc2_dc3f90a22705cb69`
- Assertions: 4
- Phrases: are in place enabling detection of
- Suggested normal forms: in place enabl detection of
- Decision: pending (review_status: pending)

## are protected better from threats described here through

- Cluster ID: `rc2_f0a1190de51f3b36`
- Assertions: 4
- Phrases: are protected better from threats described here through, are protected from threats described here through
- Suggested normal forms: protect better from threat describ here through, protect from threat describ here through
- Decision: pending (review_status: pending)

## be Required to

- Cluster ID: `rc2_425208d86b4a1c1f`
- Assertions: 4
- Phrases: be Required to
- Suggested normal forms: be requir to
- Decision: accept (review_status: confirmed)

## be Required to High Privileges Required to None to reflect more serious condition in

- Cluster ID: `rc2_361114a69c8326e0`
- Assertions: 4
- Phrases: be Required to High Privileges Required to None to reflect more serious condition in, be Required to Modified Privileges Required to None to reflect more serious condition in
- Suggested normal forms: be requir to high privilege requir to none to reflect more seriou condition in, be requir to modifi privilege requir to none to reflect more seriou condition in
- Decision: pending (review_status: pending)

## be Sharing

- Cluster ID: `rc2_e6fb28b560c43b15`
- Assertions: 4
- Phrases: be Sharing, be shared
- Suggested normal forms: be shar
- Decision: pending (review_status: pending)

## be amended based on applicable threat intelligence To

- Cluster ID: `rc2_a176cc2d27c6d486`
- Assertions: 4
- Phrases: be amended based on applicable threat intelligence To
- Suggested normal forms: be amend bas on applicable threat intelligence to
- Decision: pending (review_status: pending)

## be amended based on environmental considerations To

- Cluster ID: `rc2_5157cffcae98979a`
- Assertions: 4
- Phrases: be amended based on environmental considerations To
- Suggested normal forms: be amend bas on environmental consideration to
- Decision: pending (review_status: pending)

## be based on evidence of

- Cluster ID: `rc2_dbe34bb2281d4dcd`
- Assertions: 4
- Phrases: be based on evidence of
- Suggested normal forms: be bas on evidence of
- Decision: accept (review_status: confirmed)

## be confirmed through

- Cluster ID: `rc2_ecf956f745d89113`
- Assertions: 4
- Phrases: be confirmed through
- Suggested normal forms: be confirm through
- Decision: pending (review_status: pending)

## be controlled

- Cluster ID: `rc2_2c91c3089ce60f51`
- Assertions: 4
- Phrases: be controlled, be controlling
- Suggested normal forms: be controll
- Decision: pending (review_status: pending)

## be deny

- Cluster ID: `rc2_cc2e50a18560406c`
- Assertions: 4
- Phrases: be deny
- Suggested normal forms: be deny
- Decision: accept (review_status: confirmed)

## be discuss research for

- Cluster ID: `rc2_a4e357bfec0d78b2`
- Assertions: 4
- Phrases: be discuss research for
- Suggested normal forms: be discus research for
- Decision: pending (review_status: pending)

## be embedded into

- Cluster ID: `rc2_969fa468a734ff9e`
- Assertions: 4
- Phrases: be embedded into
- Suggested normal forms: be embedd into
- Decision: pending (review_status: pending)

## be execute

- Cluster ID: `rc2_66474ea2932357ca`
- Assertions: 4
- Phrases: be execute
- Suggested normal forms: be execute
- Decision: accept (review_status: confirmed)

## be identified by

- Cluster ID: `rc2_140494c07b5a8cc7`
- Assertions: 4
- Phrases: be identified by
- Suggested normal forms: be identifi by
- Decision: accept (review_status: confirmed)

## be launched from

- Cluster ID: `rc2_d20b363364f29916`
- Assertions: 4
- Phrases: be launched from
- Suggested normal forms: be launch from
- Decision: accept (review_status: confirmed)

## be leading to

- Cluster ID: `rc2_b0b2d21a6de6731a`
- Assertions: 4
- Phrases: be leading to
- Suggested normal forms: be lead to
- Decision: accept (review_status: confirmed)

## be listed in CISA 's KEV Catalog on

- Cluster ID: `rc2_0cf2e7754155c6f9`
- Assertions: 4
- Phrases: be listed in CISA 's KEV Catalog on
- Suggested normal forms: be list in cisa 's kev catalog on
- Decision: accept (review_status: confirmed)

## be perform

- Cluster ID: `rc2_fac4e61e8b76b506`
- Assertions: 4
- Phrases: be perform
- Suggested normal forms: be perform
- Decision: accept (review_status: confirmed)

## be providing transparency to

- Cluster ID: `rc2_76744cebec0c2ecf`
- Assertions: 4
- Phrases: be providing transparency to
- Suggested normal forms: be provid transparency to
- Decision: accept (review_status: confirmed)

## be refined by

- Cluster ID: `rc2_9c9319e8c5bcd1ad`
- Assertions: 4
- Phrases: be refined by
- Suggested normal forms: be refin by
- Decision: pending (review_status: pending)

## be required into consideration when

- Cluster ID: `rc2_2ec33b36c1d39205`
- Assertions: 4
- Phrases: be required into consideration when
- Suggested normal forms: be requir into consideration when
- Decision: accept (review_status: confirmed)

## be requiring

- Cluster ID: `rc2_f6ea96ad8383243b`
- Assertions: 4
- Phrases: be requiring
- Suggested normal forms: be requir
- Decision: accept (review_status: confirmed)

## be requiring precise conditions for

- Cluster ID: `rc2_52b994f9a80da4eb`
- Assertions: 4
- Phrases: be requiring precise conditions for
- Suggested normal forms: be requir precise condition for
- Decision: pending (review_status: pending)

## be requiring significant effort for

- Cluster ID: `rc2_69ad6afb80003872`
- Assertions: 4
- Phrases: be requiring significant effort for
- Suggested normal forms: be requir significant effort for
- Decision: pending (review_status: pending)

## be used for

- Cluster ID: `rc2_da65701719b262d0`
- Assertions: 4
- Phrases: be used for
- Suggested normal forms: be us for
- Decision: accept (review_status: confirmed)

## continue to add

- Cluster ID: `rc2_b09a957b6290e8b6`
- Assertions: 4
- Phrases: continue to add
- Suggested normal forms: continue to add
- Decision: accept (review_status: confirmed)

## convey additional extrinsic characteristics of

- Cluster ID: `rc2_e6aab994be97e6c3`
- Assertions: 4
- Phrases: convey additional extrinsic characteristics of
- Suggested normal forms: convey additional extrinsic characteristic of
- Decision: pending (review_status: pending)

## covers

- Cluster ID: `rc2_3fa405a8301ace34`
- Assertions: 4
- Phrases: covers
- Suggested normal forms: cover
- Decision: pending (review_status: pending)

## deployed

- Cluster ID: `rc2_b7bd55c11b781b0c`
- Assertions: 4
- Phrases: deployed, deploy, is deployed
- Suggested normal forms: deploy
- Decision: pending (review_status: pending)

## describes conditions beyond

- Cluster ID: `rc2_d3e1ee1be48816b6`
- Assertions: 4
- Phrases: describes conditions beyond
- Suggested normal forms: describe condition beyond
- Decision: accept (review_status: confirmed)

## differ on

- Cluster ID: `rc2_c68009acfd3eda93`
- Assertions: 4
- Phrases: differ on
- Suggested normal forms: differ on
- Decision: accept (review_status: confirmed)

## enable

- Cluster ID: `rc2_e97166b54500da3a`
- Assertions: 4
- Phrases: enable
- Suggested normal forms: enable
- Decision: accept (review_status: confirmed)

## examine

- Cluster ID: `rc2_ccb261d43dccffa7`
- Assertions: 4
- Phrases: examine, examines
- Suggested normal forms: examine
- Decision: pending (review_status: pending)

## exist in to exploit

- Cluster ID: `rc2_7dcc993e62c60ae2`
- Assertions: 4
- Phrases: exist in to exploit
- Suggested normal forms: exist in to exploit
- Decision: pending (review_status: pending)

## exploitation in-the-wild publication of details occur

- Cluster ID: `rc2_85c803bd7f8bdfc0`
- Assertions: 4
- Phrases: exploitation in-the-wild publication of details occur, exploitation in-the-wild publication of details occur proviso
- Suggested normal forms: exploitation in-the-wild publication of detail occur, exploitation in-the-wild publication of detail occur proviso
- Decision: accept (review_status: confirmed)

## exploitation third-party publication of details occur

- Cluster ID: `rc2_4318baadc44c7159`
- Assertions: 4
- Phrases: exploitation third-party publication of details occur, exploitation third-party publication of details occur proviso
- Suggested normal forms: exploitation third-party publication of detail occur, exploitation third-party publication of detail occur proviso
- Decision: accept (review_status: confirmed)

## has CISA action due date

- Cluster ID: `rc2_6630b2469404c56b`
- Assertions: 4
- Phrases: has CISA action due date
- Suggested normal forms: cisa action due date
- Decision: accept (review_status: confirmed)

## has CISA exploit addition date

- Cluster ID: `rc2_9308b0c92839d8a9`
- Assertions: 4
- Phrases: has CISA exploit addition date
- Suggested normal forms: cisa exploit addition date
- Decision: accept (review_status: confirmed)

## has CISA required action

- Cluster ID: `rc2_7ab19f71a95491b6`
- Assertions: 4
- Phrases: has CISA required action
- Suggested normal forms: cisa requir action
- Decision: accept (review_status: confirmed)

## has been added to identify

- Cluster ID: `rc2_41c5b126d9b6f8a0`
- Assertions: 4
- Phrases: has been added to identify
- Suggested normal forms: been add to identify
- Decision: pending (review_status: pending)

## has evaluated severity of issue to be in

- Cluster ID: `rc2_2f492c95e6e06005`
- Assertions: 4
- Phrases: has evaluated severity of issue to be in
- Suggested normal forms: evaluat severity of issue to be in
- Decision: pending (review_status: pending)

## has exploited issue by

- Cluster ID: `rc2_7d04b4702e285c43`
- Assertions: 4
- Phrases: has exploited issue by, have exploited issue by
- Suggested normal forms: exploit issue by
- Decision: accept (review_status: confirmed)

## has technical impact

- Cluster ID: `rc2_88a5f4a2c3f52f51`
- Assertions: 4
- Phrases: has technical impact
- Suggested normal forms: technical impact
- Decision: accept (review_status: confirmed)

## have been identified

- Cluster ID: `rc2_5393444b1971e25c`
- Assertions: 4
- Phrases: have been identified
- Suggested normal forms: been identifi
- Decision: pending (review_status: pending)

## identifies

- Cluster ID: `rc2_0f780b5c735e7025`
- Assertions: 4
- Phrases: identifies, identify
- Suggested normal forms: identify
- Decision: accept (review_status: confirmed)

## include provision of

- Cluster ID: `rc2_b083aeec8d5966c8`
- Assertions: 4
- Phrases: include provision of, include provisioning of
- Suggested normal forms: include provision of
- Decision: pending (review_status: pending)

## information exposure gives threat actor low stochastic opportunity for

- Cluster ID: `rc2_8a67ca00fbc76edd`
- Assertions: 4
- Phrases: information exposure gives threat actor low stochastic opportunity for
- Suggested normal forms: information exposure give threat actor low stochastic opportunity for
- Decision: accept (review_status: confirmed)

## is complex

- Cluster ID: `rc2_ea4b35e8f83279ea`
- Assertions: 4
- Phrases: is complex
- Suggested normal forms: complex
- Decision: accept (review_status: confirmed)

## is compulsory direction to

- Cluster ID: `rc2_ce72f4ae6072ffe2`
- Assertions: 4
- Phrases: is compulsory direction to
- Suggested normal forms: compulsory direction to
- Decision: pending (review_status: pending)

## is important factor for

- Cluster ID: `rc2_db138182f802dc9f`
- Assertions: 4
- Phrases: is important factor for
- Suggested normal forms: important factor for
- Decision: accept (review_status: confirmed)

## is included in

- Cluster ID: `rc2_3246377a8605c8e1`
- Assertions: 4
- Phrases: is included in
- Suggested normal forms: includ in
- Decision: pending (review_status: pending)

## is known to exist with

- Cluster ID: `rc2_42af27718926cf7c`
- Assertions: 4
- Phrases: is known to exist with
- Suggested normal forms: known to exist with
- Decision: accept (review_status: confirmed)

## is more

- Cluster ID: `rc2_187897ce0afcf20b`
- Assertions: 4
- Phrases: is more
- Suggested normal forms: more
- Decision: accept (review_status: confirmed)

## is more than

- Cluster ID: `rc2_7b6d26a261f2aa67`
- Assertions: 4
- Phrases: is more than
- Suggested normal forms: more than
- Decision: pending (review_status: pending)

## is open framework

- Cluster ID: `rc2_a87b2862d3aa3fa1`
- Assertions: 4
- Phrases: is open framework
- Suggested normal forms: open framework
- Decision: pending (review_status: pending)

## is set to

- Cluster ID: `rc2_fb63e99a8d1faf6e`
- Assertions: 4
- Phrases: is set to, are set to, was set to
- Suggested normal forms: set to
- Decision: pending (review_status: pending)

## is time‑consuming

- Cluster ID: `rc2_a561b1082e130e7e`
- Assertions: 4
- Phrases: is time‑consuming
- Suggested normal forms: time‑consum
- Decision: accept (review_status: confirmed)

## is unpatched when

- Cluster ID: `rc2_7ed45318ec469d4a`
- Assertions: 4
- Phrases: is unpatched when
- Suggested normal forms: unpatch when
- Decision: accept (review_status: confirmed)

## lead to

- Cluster ID: `rc2_6a9733481118f8f0`
- Assertions: 4
- Phrases: lead to
- Suggested normal forms: lead to
- Decision: accept (review_status: confirmed)

## modify environmental score by

- Cluster ID: `rc2_88ac1f0dd81f948e`
- Assertions: 4
- Phrases: modify environmental score by, modify Environmental Score by
- Suggested normal forms: modify environmental score by
- Decision: pending (review_status: pending)

## pose

- Cluster ID: `rc2_60f7e0d37e178bba`
- Assertions: 4
- Phrases: pose, poses
- Suggested normal forms: pose
- Decision: pending (review_status: pending)

## possess before exploiting vulnerability

- Cluster ID: `rc2_faab33cfb5819af9`
- Assertions: 4
- Phrases: possess before exploiting vulnerability
- Suggested normal forms: posses before exploit vulnerability
- Decision: accept (review_status: confirmed)

## present high-risk attack surface

- Cluster ID: `rc2_be0ce74ff9661ff2`
- Assertions: 4
- Phrases: present high-risk attack surface
- Suggested normal forms: present high-risk attack surface
- Decision: accept (review_status: confirmed)

## provide Base Scores enumerated as

- Cluster ID: `rc2_489ca3bf74b75832`
- Assertions: 4
- Phrases: provide Base Scores enumerated as
- Suggested normal forms: provide base score enumerat a
- Decision: pending (review_status: pending)

## refer

- Cluster ID: `rc2_a4b64ad329a8b29e`
- Assertions: 4
- Phrases: refer
- Suggested normal forms: refer
- Decision: pending (review_status: pending)

## refer thing to formally as

- Cluster ID: `rc2_cd8cf51777bc6e45`
- Assertions: 4
- Phrases: refer thing to formally as
- Suggested normal forms: refer th to formally a
- Decision: accept (review_status: confirmed)

## request 30-day score history

- Cluster ID: `rc2_3c1e2f438d6e1496`
- Assertions: 4
- Phrases: request 30-day score history, request 30-day score history for
- Suggested normal forms: request 30-day score history, request 30-day score history for
- Decision: pending (review_status: pending)

## required per

- Cluster ID: `rc2_4802c548ff4cbea4`
- Assertions: 4
- Phrases: required per
- Suggested normal forms: requir per
- Decision: accept (review_status: confirmed)

## runs

- Cluster ID: `rc2_acba25512100f80b`
- Assertions: 4
- Phrases: runs, Runs, run
- Suggested normal forms: run
- Decision: pending (review_status: pending)

## starts with

- Cluster ID: `rc2_6f60c858b018969e`
- Assertions: 4
- Phrases: starts with
- Suggested normal forms: start with
- Decision: pending (review_status: pending)

## stay

- Cluster ID: `rc2_39be15289c7942a8`
- Assertions: 4
- Phrases: stay
- Suggested normal forms: stay
- Decision: accept (review_status: confirmed)

## subvert

- Cluster ID: `rc2_1cf4e93e21a785f4`
- Assertions: 4
- Phrases: subvert
- Suggested normal forms: subvert
- Decision: accept (review_status: confirmed)

## subvert protection mechanisms

- Cluster ID: `rc2_7e55ce220338b40e`
- Assertions: 4
- Phrases: subvert protection mechanisms
- Suggested normal forms: subvert protection mechanism
- Decision: accept (review_status: confirmed)

## take additional information on effort required into

- Cluster ID: `rc2_5c9aceb6b5671b13`
- Assertions: 4
- Phrases: take additional information on effort required into
- Suggested normal forms: take additional information on effort requir into
- Decision: pending (review_status: pending)

## threaten

- Cluster ID: `rc2_75ed840ef9368550`
- Assertions: 4
- Phrases: threaten
- Suggested normal forms: threaten
- Decision: accept (review_status: confirmed)

## to provide

- Cluster ID: `rc2_93508f24e49beb45`
- Assertions: 4
- Phrases: to provide
- Suggested normal forms: to provide
- Decision: accept (review_status: confirmed)

## to publish occur

- Cluster ID: `rc2_b0551d97bbc5b71c`
- Assertions: 4
- Phrases: to publish occur
- Suggested normal forms: to publish occur
- Decision: accept (review_status: confirmed)

## to publish occur proviso

- Cluster ID: `rc2_8298037afc1dcbb0`
- Assertions: 4
- Phrases: to publish occur proviso
- Suggested normal forms: to publish occur proviso
- Decision: accept (review_status: confirmed)

## use intelligence to deploy

- Cluster ID: `rc2_0dad6bd6f1832de3`
- Assertions: 4
- Phrases: use intelligence to deploy
- Suggested normal forms: use intelligence to deploy
- Decision: pending (review_status: pending)

## used Hermes Agent with DeepSeek

- Cluster ID: `rc2_2fa711d163678789`
- Assertions: 4
- Phrases: used Hermes Agent with DeepSeek, used Hermes Agent with, used Hermes Agent with DeepSeek as
- Suggested normal forms: us herme agent with, us herme agent with deepseek, us herme agent with deepseek a
- Decision: accept (review_status: confirmed)

## was addressed with

- Cluster ID: `rc2_a85dac207412a7c5`
- Assertions: 4
- Phrases: was addressed with
- Suggested normal forms: address with
- Decision: accept (review_status: confirmed)

## were reported to

- Cluster ID: `rc2_f0264c693c9d6c3f`
- Assertions: 4
- Phrases: were reported to
- Suggested normal forms: report to
- Decision: pending (review_status: pending)

## with high privileges assume

- Cluster ID: `rc2_8391878fd14a0dfa`
- Assertions: 4
- Phrases: with high privileges assume, with high privileges assume high privileges
- Suggested normal forms: with high privilege assume, with high privilege assume high privilege
- Decision: pending (review_status: pending)

## 's

- Cluster ID: `rc2_edc00d4db80ddc3e`
- Assertions: 3
- Phrases: 's
- Suggested normal forms: 's
- Decision: accept (review_status: confirmed)

## Defused warned

- Cluster ID: `rc2_8b0dfe93e67dd74b`
- Assertions: 3
- Phrases: Defused warned
- Suggested normal forms: defus warn
- Decision: accept (review_status: confirmed)

## Defused warned on X that attackers

- Cluster ID: `rc2_99681a270b205a25`
- Assertions: 3
- Phrases: Defused warned on X that attackers
- Suggested normal forms: defus warn on x that attacker
- Decision: accept (review_status: confirmed)

## Process from

- Cluster ID: `rc2_e48a9d252f8a5aa9`
- Assertions: 3
- Phrases: Process from
- Suggested normal forms: proces from
- Decision: pending (review_status: pending)

## account for

- Cluster ID: `rc2_bbb3c95e291c5f8f`
- Assertions: 3
- Phrases: account for, accounts for
- Suggested normal forms: account for
- Decision: accept (review_status: confirmed)

## added CVE-2026-55040 On

- Cluster ID: `rc2_c0a0ab3f890c6722`
- Assertions: 3
- Phrases: added CVE-2026-55040 On, added CVE-2026-55040 on
- Suggested normal forms: add cve-2026-55040 on
- Decision: pending (review_status: pending)

## addressed

- Cluster ID: `rc2_d80c9bf910f14473`
- Assertions: 3
- Phrases: addressed, was addressed
- Suggested normal forms: address
- Decision: pending (review_status: pending)

## affect resources managed by

- Cluster ID: `rc2_80bf56e20a715adf`
- Assertions: 3
- Phrases: affect resources managed by
- Suggested normal forms: affect resource manag by
- Decision: pending (review_status: pending)

## aim to compromise

- Cluster ID: `rc2_37bb97c0a907ba0d`
- Assertions: 3
- Phrases: aim to compromise
- Suggested normal forms: aim to compromise
- Decision: accept (review_status: confirmed)

## allows unauthorized attacker to bypass security feature over

- Cluster ID: `rc2_ea57493fad8dcb2f`
- Assertions: 3
- Phrases: allows unauthorized attacker to bypass security feature over
- Suggested normal forms: allow unauthoriz attacker to bypas security feature over
- Decision: accept (review_status: confirmed)

## applies

- Cluster ID: `rc2_97a5e41b45ddd2b2`
- Assertions: 3
- Phrases: applies, apply
- Suggested normal forms: apply
- Decision: pending (review_status: pending)

## are available in

- Cluster ID: `rc2_122fa611f87f2e67`
- Assertions: 3
- Phrases: are available in, is available in
- Suggested normal forms: available in
- Decision: pending (review_status: pending)

## are frequent attack vector for

- Cluster ID: `rc2_b5d09669573722aa`
- Assertions: 3
- Phrases: are frequent attack vector for, is frequent attack vector for
- Suggested normal forms: frequent attack vector for
- Decision: pending (review_status: pending)

## are listed on

- Cluster ID: `rc2_cf296cd61d857ab4`
- Assertions: 3
- Phrases: are listed on
- Suggested normal forms: list on
- Decision: pending (review_status: pending)

## are managed by

- Cluster ID: `rc2_f6a81d76583d90e1`
- Assertions: 3
- Phrases: are managed by
- Suggested normal forms: manag by
- Decision: accept (review_status: confirmed)

## are with

- Cluster ID: `rc2_0695b563acde461f`
- Assertions: 3
- Phrases: are with
- Suggested normal forms: with
- Decision: accept (review_status: confirmed)

## assess

- Cluster ID: `rc2_dc2abe4ed2d8a549`
- Assertions: 3
- Phrases: assess
- Suggested normal forms: asses
- Decision: accept (review_status: confirmed)

## assess full blast radius of

- Cluster ID: `rc2_2b5a437ff3c8c4d5`
- Assertions: 3
- Phrases: assess full blast radius of
- Suggested normal forms: asses full blast radiu of
- Decision: pending (review_status: pending)

## assess full blast radius of compromised SharePoint session before treating this as

- Cluster ID: `rc2_de5b5f3dd4bbe517`
- Assertions: 3
- Phrases: assess full blast radius of compromised SharePoint session before treating this as
- Suggested normal forms: asses full blast radiu of compromis sharepoint session before treat thi a
- Decision: pending (review_status: pending)

## assign greater value to

- Cluster ID: `rc2_e46a98350885e111`
- Assertions: 3
- Phrases: assign greater value to
- Suggested normal forms: assign greater value to
- Decision: pending (review_status: pending)

## be Local For

- Cluster ID: `rc2_2f14290d781a6613`
- Assertions: 3
- Phrases: be Local For
- Suggested normal forms: be local for
- Decision: pending (review_status: pending)

## be Local in

- Cluster ID: `rc2_4396237cec93af62`
- Assertions: 3
- Phrases: be Local in
- Suggested normal forms: be local in
- Decision: accept (review_status: confirmed)

## be Tracked as

- Cluster ID: `rc2_fbd95bc7e1318dd6`
- Assertions: 3
- Phrases: be Tracked as
- Suggested normal forms: be track a
- Decision: accept (review_status: confirmed)

## be affecting

- Cluster ID: `rc2_9ecf403053f9ad6b`
- Assertions: 3
- Phrases: be affecting
- Suggested normal forms: be affect
- Decision: accept (review_status: confirmed)

## be allowing

- Cluster ID: `rc2_b3379ef6993f26df`
- Assertions: 3
- Phrases: be allowing
- Suggested normal forms: be allow
- Decision: accept (review_status: confirmed)

## be assess

- Cluster ID: `rc2_edf4047b2d616f79`
- Assertions: 3
- Phrases: be assess
- Suggested normal forms: be asses
- Decision: accept (review_status: confirmed)

## be based on specific characteristics of

- Cluster ID: `rc2_dd6fe8c4cd7fe9b0`
- Assertions: 3
- Phrases: be based on specific characteristics of
- Suggested normal forms: be bas on specific characteristic of
- Decision: pending (review_status: pending)

## be become

- Cluster ID: `rc2_65acbc92e482ed2e`
- Assertions: 3
- Phrases: be become
- Suggested normal forms: be become
- Decision: pending (review_status: pending)

## be confirmed through acknowledgement by

- Cluster ID: `rc2_bd2946f6059f527e`
- Assertions: 3
- Phrases: be confirmed through acknowledgement by
- Suggested normal forms: be confirm through acknowledgement by
- Decision: pending (review_status: pending)

## be depending on importance of

- Cluster ID: `rc2_f320d96bf025bec3`
- Assertions: 3
- Phrases: be depending on importance of
- Suggested normal forms: be depend on importance of
- Decision: pending (review_status: pending)

## be determine

- Cluster ID: `rc2_d8b4bcbb4c869b19`
- Assertions: 3
- Phrases: be determine
- Suggested normal forms: be determine
- Decision: accept (review_status: confirmed)

## be evaluate adherence with

- Cluster ID: `rc2_2251250637fbe382`
- Assertions: 3
- Phrases: be evaluate adherence with
- Suggested normal forms: be evaluate adherence with
- Decision: accept (review_status: confirmed)

## be following for

- Cluster ID: `rc2_478878efb4f44cc7`
- Assertions: 3
- Phrases: be following for
- Suggested normal forms: be follow for
- Decision: pending (review_status: pending)

## be found at

- Cluster ID: `rc2_b18a7d978d9c209f`
- Assertions: 3
- Phrases: be found at
- Suggested normal forms: be found at
- Decision: pending (review_status: pending)

## be included in

- Cluster ID: `rc2_42a3b376823ff547`
- Assertions: 3
- Phrases: be included in
- Suggested normal forms: be includ in
- Decision: accept (review_status: confirmed)

## be indicating

- Cluster ID: `rc2_d88bc36a5bec1124`
- Assertions: 3
- Phrases: be indicating
- Suggested normal forms: be indicat
- Decision: accept (review_status: confirmed)

## be launched from outside

- Cluster ID: `rc2_7468c9d1f099f633`
- Assertions: 3
- Phrases: be launched from outside
- Suggested normal forms: be launch from outside
- Decision: accept (review_status: confirmed)

## be launched over

- Cluster ID: `rc2_785d2c8e6d8758c8`
- Assertions: 3
- Phrases: be launched over
- Suggested normal forms: be launch over
- Decision: accept (review_status: confirmed)

## be listed

- Cluster ID: `rc2_9d04ce8483d740ac`
- Assertions: 3
- Phrases: be listed
- Suggested normal forms: be list
- Decision: accept (review_status: confirmed)

## be maintaining

- Cluster ID: `rc2_1749618f7afffb59`
- Assertions: 3
- Phrases: be maintaining, be maintain
- Suggested normal forms: be maintain
- Decision: pending (review_status: pending)

## be mentioned in

- Cluster ID: `rc2_3e67de7b7d236124`
- Assertions: 3
- Phrases: be mentioned in
- Suggested normal forms: be mention in
- Decision: accept (review_status: confirmed)

## be outlining

- Cluster ID: `rc2_4dc345ad87c9002b`
- Assertions: 3
- Phrases: be outlining
- Suggested normal forms: be outlin
- Decision: accept (review_status: confirmed)

## be overcome

- Cluster ID: `rc2_37e5ace462283078`
- Assertions: 3
- Phrases: be overcome
- Suggested normal forms: be overcome
- Decision: accept (review_status: confirmed)

## be owned by

- Cluster ID: `rc2_f8d433b1d2086946`
- Assertions: 3
- Phrases: be owned by
- Suggested normal forms: be own by
- Decision: pending (review_status: pending)

## be posed by

- Cluster ID: `rc2_ffde162fe0a0bbea`
- Assertions: 3
- Phrases: be posed by
- Suggested normal forms: be pos by
- Decision: accept (review_status: confirmed)

## be present present on

- Cluster ID: `rc2_116981313a742f7a`
- Assertions: 3
- Phrases: be present present on
- Suggested normal forms: be present present on
- Decision: accept (review_status: confirmed)

## be providing

- Cluster ID: `rc2_8a3afe3ec5464f4b`
- Assertions: 3
- Phrases: be providing, be provided
- Suggested normal forms: be provid
- Decision: accept (review_status: confirmed)

## be required for

- Cluster ID: `rc2_276b43ab4599e15a`
- Assertions: 3
- Phrases: be required for
- Suggested normal forms: be requir for
- Decision: accept (review_status: confirmed)

## be simplify Software including exploit frameworks such as

- Cluster ID: `rc2_84d95d8f84e4a998`
- Assertions: 3
- Phrases: be simplify Software including exploit frameworks such as
- Suggested normal forms: be simplify software includ exploit framework such a
- Decision: pending (review_status: pending)

## be update

- Cluster ID: `rc2_8a2a6246326edcec`
- Assertions: 3
- Phrases: be update
- Suggested normal forms: be update
- Decision: pending (review_status: pending)

## be used to

- Cluster ID: `rc2_8b06a453c732c4ee`
- Assertions: 3
- Phrases: be used to
- Suggested normal forms: be us to
- Decision: pending (review_status: pending)

## be used to make

- Cluster ID: `rc2_a9887e50eae4bae6`
- Assertions: 3
- Phrases: be used to make
- Suggested normal forms: be us to make
- Decision: accept (review_status: confirmed)

## break

- Cluster ID: `rc2_14ebe56a5008e7c2`
- Assertions: 3
- Phrases: break
- Suggested normal forms: break
- Decision: accept (review_status: confirmed)

## bypass

- Cluster ID: `rc2_276acb2e9b548081`
- Assertions: 3
- Phrases: bypass
- Suggested normal forms: bypas
- Decision: accept (review_status: confirmed)

## causes MLflow server to query

- Cluster ID: `rc2_f342620097e914c0`
- Assertions: 3
- Phrases: causes MLflow server to query
- Suggested normal forms: cause mlflow server to query
- Decision: pending (review_status: pending)

## causes service to become

- Cluster ID: `rc2_48710636be850967`
- Assertions: 3
- Phrases: causes service to become
- Suggested normal forms: cause service to become
- Decision: pending (review_status: pending)

## constrain

- Cluster ID: `rc2_91d2d7aa4a277bc7`
- Assertions: 3
- Phrases: constrain
- Suggested normal forms: constrain
- Decision: accept (review_status: confirmed)

## constrain impacts to

- Cluster ID: `rc2_ae60af9af09d2f33`
- Assertions: 3
- Phrases: constrain impacts to
- Suggested normal forms: constrain impact to
- Decision: accept (review_status: confirmed)

## contains directory traversal vulnerability in

- Cluster ID: `rc2_a3c366dab2da37fd`
- Assertions: 3
- Phrases: contains directory traversal vulnerability in, is directory-traversal vulnerability in
- Suggested normal forms: contain directory traversal vulnerability in, directory-traversal vulnerability in
- Decision: pending (review_status: pending)

## depends on sub-formulas for

- Cluster ID: `rc2_ba0a66142a691588`
- Assertions: 3
- Phrases: depends on sub-formulas for
- Suggested normal forms: depend on sub-formula for
- Decision: pending (review_status: pending)

## disrupt

- Cluster ID: `rc2_bee0164d53b0209a`
- Assertions: 3
- Phrases: disrupt
- Suggested normal forms: disrupt
- Decision: pending (review_status: pending)

## do not allow

- Cluster ID: `rc2_f11fdcbf8a900c15`
- Assertions: 3
- Phrases: do not allow
- Suggested normal forms: not allow
- Decision: pending (review_status: pending)

## exploit along with Snort rules

- Cluster ID: `rc2_8422525222bbc86a`
- Assertions: 3
- Phrases: exploit along with Snort rules
- Suggested normal forms: exploit along with snort rule
- Decision: accept (review_status: confirmed)

## exploit along with Suricata

- Cluster ID: `rc2_7ba289bf7ce09ba1`
- Assertions: 3
- Phrases: exploit along with Suricata
- Suggested normal forms: exploit along with suricata
- Decision: accept (review_status: confirmed)

## exploit along with version scanner

- Cluster ID: `rc2_394c79ac052d5d3d`
- Assertions: 3
- Phrases: exploit along with version scanner
- Suggested normal forms: exploit along with version scanner
- Decision: accept (review_status: confirmed)

## exploit issue to execute

- Cluster ID: `rc2_16c82bc43ba315fd`
- Assertions: 3
- Phrases: exploit issue to execute
- Suggested normal forms: exploit issue to execute
- Decision: pending (review_status: pending)

## focuses

- Cluster ID: `rc2_7f3c5fa53fec2dac`
- Assertions: 3
- Phrases: focuses
- Suggested normal forms: focuse
- Decision: pending (review_status: pending)

## has analysis of

- Cluster ID: `rc2_4eb99241fa233d59`
- Assertions: 3
- Phrases: has analysis of
- Suggested normal forms: analysi of
- Decision: accept (review_status: confirmed)

## has released

- Cluster ID: `rc2_fe90db394919f86a`
- Assertions: 3
- Phrases: has released, is released, released
- Suggested normal forms: releas
- Decision: accept (review_status: confirmed)

## hone autonomous attack processes

- Cluster ID: `rc2_951c5b3913632a32`
- Assertions: 3
- Phrases: hone autonomous attack processes, hone autonomous attack processes to
- Suggested normal forms: hone autonomou attack processe, hone autonomou attack processe to
- Decision: pending (review_status: pending)

## impact Subsequent System For

- Cluster ID: `rc2_64357d58d242983d`
- Assertions: 3
- Phrases: impact Subsequent System For
- Suggested normal forms: impact subsequent system for
- Decision: pending (review_status: pending)

## implement

- Cluster ID: `rc2_f9bb818d84838e08`
- Assertions: 3
- Phrases: implement, implements
- Suggested normal forms: implement
- Decision: accept (review_status: confirmed)

## include assessment for

- Cluster ID: `rc2_11d11313e6455be6`
- Assertions: 3
- Phrases: include assessment for
- Suggested normal forms: include assessment for
- Decision: accept (review_status: confirmed)

## include assessment for Subsequent System In

- Cluster ID: `rc2_52b400032d195104`
- Assertions: 3
- Phrases: include assessment for Subsequent System In
- Suggested normal forms: include assessment for subsequent system in
- Decision: pending (review_status: pending)

## include assessment for Subsequent System if

- Cluster ID: `rc2_381b68288bd9be3b`
- Assertions: 3
- Phrases: include assessment for Subsequent System if
- Suggested normal forms: include assessment for subsequent system if
- Decision: accept (review_status: confirmed)

## increase

- Cluster ID: `rc2_e20a548f23fa36bc`
- Assertions: 3
- Phrases: increase
- Suggested normal forms: increase
- Decision: accept (review_status: confirmed)

## increases number of

- Cluster ID: `rc2_0beaf94a1d034bd2`
- Assertions: 3
- Phrases: increases number of
- Suggested normal forms: increase number of
- Decision: pending (review_status: pending)

## increases number of potential attackers by

- Cluster ID: `rc2_6d7c47aaa7ef3ed6`
- Assertions: 3
- Phrases: increases number of potential attackers by
- Suggested normal forms: increase number of potential attacker by
- Decision: pending (review_status: pending)

## indicates

- Cluster ID: `rc2_4932c716f725df5e`
- Assertions: 3
- Phrases: indicates
- Suggested normal forms: indicate
- Decision: pending (review_status: pending)

## is available to

- Cluster ID: `rc2_c46a55a95503ed3b`
- Assertions: 3
- Phrases: is available to, are available to
- Suggested normal forms: available to
- Decision: pending (review_status: pending)

## is being exploited in

- Cluster ID: `rc2_7be9d1e5a3d43cbd`
- Assertions: 3
- Phrases: is being exploited in, be exploited in
- Suggested normal forms: be exploit in
- Decision: pending (review_status: pending)

## is centralized management software for

- Cluster ID: `rc2_ed162b95a4e3df52`
- Assertions: 3
- Phrases: is centralized management software for
- Suggested normal forms: centraliz management software for
- Decision: pending (review_status: pending)

## is common for

- Cluster ID: `rc2_10d655686e6dda0e`
- Assertions: 3
- Phrases: is common for
- Suggested normal forms: common for
- Decision: accept (review_status: confirmed)

## is considered as

- Cluster ID: `rc2_631d0ad0a29db65d`
- Assertions: 3
- Phrases: is considered as, are considered as
- Suggested normal forms: consider a
- Decision: pending (review_status: pending)

## is deployed at network perimeter to support

- Cluster ID: `rc2_7095ce50ba9252b6`
- Assertions: 3
- Phrases: is deployed at network perimeter to support
- Suggested normal forms: deploy at network perimeter to support
- Decision: pending (review_status: pending)

## is deployed to support

- Cluster ID: `rc2_b86c8adc788b9cc3`
- Assertions: 3
- Phrases: is deployed to support
- Suggested normal forms: deploy to support
- Decision: pending (review_status: pending)

## is due to

- Cluster ID: `rc2_6c9e281b522154b0`
- Assertions: 3
- Phrases: is due to
- Suggested normal forms: due to
- Decision: accept (review_status: confirmed)

## is exposed to

- Cluster ID: `rc2_1ffc052799586542`
- Assertions: 3
- Phrases: is exposed to
- Suggested normal forms: expos to
- Decision: accept (review_status: confirmed)

## is hosting webinar

- Cluster ID: `rc2_a2f19ffe9755fe46`
- Assertions: 3
- Phrases: is hosting webinar
- Suggested normal forms: host webinar
- Decision: pending (review_status: pending)

## is hosting webinar on

- Cluster ID: `rc2_1bfdefd81e529696`
- Assertions: 3
- Phrases: is hosting webinar on
- Suggested normal forms: host webinar on
- Decision: pending (review_status: pending)

## is most

- Cluster ID: `rc2_24ea913efda289dc`
- Assertions: 3
- Phrases: is most, are most
- Suggested normal forms: most
- Decision: pending (review_status: pending)

## is open framework for

- Cluster ID: `rc2_e0a138a966d4f580`
- Assertions: 3
- Phrases: is open framework for
- Suggested normal forms: open framework for
- Decision: accept (review_status: confirmed)

## is open framework for communicating characteristics of

- Cluster ID: `rc2_b909682f1feceeea`
- Assertions: 3
- Phrases: is open framework for communicating characteristics of
- Suggested normal forms: open framework for communicat characteristic of
- Decision: accept (review_status: confirmed)

## is received

- Cluster ID: `rc2_87766353377eb22c`
- Assertions: 3
- Phrases: is received, have received
- Suggested normal forms: receiv
- Decision: pending (review_status: pending)

## is required to use

- Cluster ID: `rc2_e9621bdb52e68d12`
- Assertions: 3
- Phrases: is required to use
- Suggested normal forms: requir to use
- Decision: pending (review_status: pending)

## is subject to

- Cluster ID: `rc2_d8917ae9a95797bf`
- Assertions: 3
- Phrases: is subject to
- Suggested normal forms: subject to
- Decision: pending (review_status: pending)

## is trusted by

- Cluster ID: `rc2_7e7c37e495fbd9d7`
- Assertions: 3
- Phrases: is trusted by, are trusted by
- Suggested normal forms: trust by
- Decision: pending (review_status: pending)

## is unauthorized prior to

- Cluster ID: `rc2_d358362f2eb6a215`
- Assertions: 3
- Phrases: is unauthorized prior to
- Suggested normal forms: unauthoriz prior to
- Decision: accept (review_status: confirmed)

## is used to record CVSS metric information in

- Cluster ID: `rc2_669741e35e97f59f`
- Assertions: 3
- Phrases: is used to record CVSS metric information in
- Suggested normal forms: us to record cvs metric information in
- Decision: accept (review_status: confirmed)

## is violated as result of

- Cluster ID: `rc2_28cbe0cb08167c74`
- Assertions: 3
- Phrases: is violated as result of
- Suggested normal forms: violat a result of
- Decision: accept (review_status: confirmed)

## list

- Cluster ID: `rc2_a330395cc0a53ad1`
- Assertions: 3
- Phrases: list, is listed
- Suggested normal forms: list
- Decision: pending (review_status: pending)

## makes accessible via

- Cluster ID: `rc2_64b9de6536e2f2ba`
- Assertions: 3
- Phrases: makes accessible via
- Suggested normal forms: make accessible via
- Decision: accept (review_status: confirmed)

## makes exploitation of

- Cluster ID: `rc2_4eb40d0b7dddbb62`
- Assertions: 3
- Phrases: makes exploitation of
- Suggested normal forms: make exploitation of
- Decision: pending (review_status: pending)

## manages

- Cluster ID: `rc2_181229424893bb65`
- Assertions: 3
- Phrases: manages
- Suggested normal forms: manage
- Decision: accept (review_status: confirmed)

## measure current state of

- Cluster ID: `rc2_d5c4af354bac7c7f`
- Assertions: 3
- Phrases: measure current state of
- Suggested normal forms: measure current state of
- Decision: accept (review_status: confirmed)

## need to account for

- Cluster ID: `rc2_a65db9eae8b86b88`
- Assertions: 3
- Phrases: need to account for
- Suggested normal forms: ne to account for
- Decision: pending (review_status: pending)

## needed

- Cluster ID: `rc2_be8dff00b0d468b2`
- Assertions: 3
- Phrases: needed
- Suggested normal forms: need
- Decision: accept (review_status: confirmed)

## overlaps consistent with

- Cluster ID: `rc2_eb88e09e142e93b7`
- Assertions: 3
- Phrases: overlaps consistent with
- Suggested normal forms: overlap consistent with
- Decision: accept (review_status: confirmed)

## owns

- Cluster ID: `rc2_5b3975651c3cab92`
- Assertions: 3
- Phrases: owns
- Suggested normal forms: own
- Decision: pending (review_status: pending)

## patches

- Cluster ID: `rc2_413e6ae14bb18485`
- Assertions: 3
- Phrases: patches
- Suggested normal forms: patche
- Decision: pending (review_status: pending)

## pose significant risks to

- Cluster ID: `rc2_cbfa81d920f98bd0`
- Assertions: 3
- Phrases: pose significant risks to, poses significant risks to
- Suggested normal forms: pose significant risk to
- Decision: pending (review_status: pending)

## prevent

- Cluster ID: `rc2_b4d5a180d618df82`
- Assertions: 3
- Phrases: prevent
- Suggested normal forms: prevent
- Decision: pending (review_status: pending)

## progress from

- Cluster ID: `rc2_47910e0144a2a510`
- Assertions: 3
- Phrases: progress from
- Suggested normal forms: progres from
- Decision: accept (review_status: confirmed)

## protect customers through

- Cluster ID: `rc2_254ef5ae3ef2ad67`
- Assertions: 3
- Phrases: protect customers through
- Suggested normal forms: protect customer through
- Decision: accept (review_status: confirmed)

## provide copy of

- Cluster ID: `rc2_14eb1b5a773d15ca`
- Assertions: 3
- Phrases: provide copy of
- Suggested normal forms: provide copy of
- Decision: accept (review_status: confirmed)

## provides PSIRT teams with tools required for

- Cluster ID: `rc2_a618048f9847c3d7`
- Assertions: 3
- Phrases: provides PSIRT teams with tools required for
- Suggested normal forms: provide psirt team with tool requir for
- Decision: accept (review_status: confirmed)

## provides likelihood of exploitation for

- Cluster ID: `rc2_85c7289fb9c0dc1e`
- Assertions: 3
- Phrases: provides likelihood of exploitation for, provides likelihood of exploitation For
- Suggested normal forms: provide likelihood of exploitation for
- Decision: pending (review_status: pending)

## provides product managers with tools required for

- Cluster ID: `rc2_163e178026462a0f`
- Assertions: 3
- Phrases: provides product managers with tools required for
- Suggested normal forms: provide product manager with tool requir for
- Decision: accept (review_status: confirmed)

## provides threat hunters with tools required for

- Cluster ID: `rc2_c959ab471049dfac`
- Assertions: 3
- Phrases: provides threat hunters with tools required for
- Suggested normal forms: provide threat hunter with tool requir for
- Decision: accept (review_status: confirmed)

## publishes

- Cluster ID: `rc2_cbc4e9c802a89b4f`
- Assertions: 3
- Phrases: publishes
- Suggested normal forms: publishe
- Decision: accept (review_status: confirmed)

## reference vulnerabilities by

- Cluster ID: `rc2_4102421a81cfead3`
- Assertions: 3
- Phrases: reference vulnerabilities by
- Suggested normal forms: reference vulnerability by
- Decision: pending (review_status: pending)

## reference vulnerabilities when

- Cluster ID: `rc2_914ade824dffc89b`
- Assertions: 3
- Phrases: reference vulnerabilities when
- Suggested normal forms: reference vulnerability when
- Decision: pending (review_status: pending)

## reflect characteristics of

- Cluster ID: `rc2_e9fe607b59dfa569`
- Assertions: 3
- Phrases: reflect characteristics of, reflects characteristics of
- Suggested normal forms: reflect characteristic of
- Decision: pending (review_status: pending)

## renamed to

- Cluster ID: `rc2_6bbfad64cca432f2`
- Assertions: 3
- Phrases: renamed to
- Suggested normal forms: renam to
- Decision: accept (review_status: confirmed)

## represents direct serious loss of

- Cluster ID: `rc2_a3886a5b4116ace4`
- Assertions: 3
- Phrases: represents direct serious loss of
- Suggested normal forms: represent direct seriou los of
- Decision: pending (review_status: pending)

## represents intrinsic characteristics of

- Cluster ID: `rc2_0dabb5fcedf0e5c4`
- Assertions: 3
- Phrases: represents intrinsic characteristics of
- Suggested normal forms: represent intrinsic characteristic of
- Decision: accept (review_status: confirmed)

## represents intrinsic qualities of

- Cluster ID: `rc2_b4b63e6db1c9894e`
- Assertions: 3
- Phrases: represents intrinsic qualities of
- Suggested normal forms: represent intrinsic quality of
- Decision: accept (review_status: confirmed)

## require affected systems to be taken

- Cluster ID: `rc2_1130023800334014`
- Assertions: 3
- Phrases: require affected systems to be taken
- Suggested normal forms: require affect system to be taken
- Decision: pending (review_status: pending)

## reserves

- Cluster ID: `rc2_6df24c372c044a0f`
- Assertions: 3
- Phrases: reserves
- Suggested normal forms: reserve
- Decision: pending (review_status: pending)

## resides in

- Cluster ID: `rc2_a341c8a72a67e546`
- Assertions: 3
- Phrases: resides in
- Suggested normal forms: reside in
- Decision: accept (review_status: confirmed)

## rule out Nevertheless possibility of

- Cluster ID: `rc2_e54834cc03e19c43`
- Assertions: 3
- Phrases: rule out Nevertheless possibility of, rule out entirely possibility of, rule out possibility of
- Suggested normal forms: rule out entirely possibility of, rule out nevertheles possibility of, rule out possibility of
- Decision: pending (review_status: pending)

## serves

- Cluster ID: `rc2_24c458cfb46d9a45`
- Assertions: 3
- Phrases: serves
- Suggested normal forms: serve
- Decision: accept (review_status: confirmed)

## started

- Cluster ID: `rc2_cced28c6dc3f99c2`
- Assertions: 3
- Phrases: started, starts
- Suggested normal forms: start
- Decision: pending (review_status: pending)

## take a second pass of analysis to determine

- Cluster ID: `rc2_44f47ee0ef6f283f`
- Assertions: 3
- Phrases: take a second pass of analysis to determine
- Suggested normal forms: take a second pas of analysi to determine
- Decision: accept (review_status: confirmed)

## take malicious actions in

- Cluster ID: `rc2_e3a2efcd836eff8f`
- Assertions: 3
- Phrases: take malicious actions in
- Suggested normal forms: take maliciou action in
- Decision: accept (review_status: confirmed)

## upload

- Cluster ID: `rc2_ff4085ad157354dc`
- Assertions: 3
- Phrases: upload
- Suggested normal forms: upload
- Decision: accept (review_status: confirmed)

## warrants

- Cluster ID: `rc2_d9bceb39819ed7a4`
- Assertions: 3
- Phrases: warrants
- Suggested normal forms: warrant
- Decision: accept (review_status: confirmed)

## was presented to CVSS Special Interest Group to incorporate

- Cluster ID: `rc2_1c1b6e4545db1268`
- Assertions: 3
- Phrases: was presented to CVSS Special Interest Group to incorporate
- Suggested normal forms: present to cvs special interest group to incorporate
- Decision: pending (review_status: pending)

## was presented to incorporate

- Cluster ID: `rc2_98deb17b9cd0b6fb`
- Assertions: 3
- Phrases: was presented to incorporate
- Suggested normal forms: present to incorporate
- Decision: pending (review_status: pending)

## we achieved

- Cluster ID: `rc2_bf4b44c9d05a9f5a`
- Assertions: 3
- Phrases: we achieved
- Suggested normal forms: we achiev
- Decision: accept (review_status: confirmed)

## August 21 2026 arrives at

- Cluster ID: `rc2_d2c29a9f1c6ec2e7`
- Assertions: 2
- Phrases: August 21 2026 arrives at, August 21 2026 arrives at moment
- Suggested normal forms: august 21 2026 arrive at, august 21 2026 arrive at moment
- Decision: pending (review_status: pending)

## Is exposed

- Cluster ID: `rc2_3baaa2221eb76e93`
- Assertions: 2
- Phrases: Is exposed, exposed
- Suggested normal forms: expos
- Decision: pending (review_status: pending)

## Is vulnerability as identified by

- Cluster ID: `rc2_164a435969aead7b`
- Assertions: 2
- Phrases: Is vulnerability as identified by
- Suggested normal forms: vulnerability a identifi by
- Decision: accept (review_status: confirmed)

## Updates

- Cluster ID: `rc2_2937013f21818106`
- Assertions: 2
- Phrases: Updates, update
- Suggested normal forms: update
- Decision: pending (review_status: pending)

## access

- Cluster ID: `rc2_448514710f392303`
- Assertions: 2
- Phrases: access
- Suggested normal forms: acces
- Decision: pending (review_status: pending)

## accessed

- Cluster ID: `rc2_a0561fd649cdb6ba`
- Assertions: 2
- Phrases: accessed
- Suggested normal forms: access
- Decision: accept (review_status: confirmed)

## achieve remote code execution without

- Cluster ID: `rc2_6586aff06d4e5e20`
- Assertions: 2
- Phrases: achieve remote code execution without
- Suggested normal forms: achieve remote code execution without
- Decision: accept (review_status: confirmed)

## acknowledges receipt of

- Cluster ID: `rc2_8f42153150244a82`
- Assertions: 2
- Phrases: acknowledges receipt of
- Suggested normal forms: acknowledge receipt of
- Decision: accept (review_status: confirmed)

## acts as critical bridge between

- Cluster ID: `rc2_56e3988287a3b968`
- Assertions: 2
- Phrases: acts as critical bridge between
- Suggested normal forms: act a critical bridge between
- Decision: accept (review_status: confirmed)

## adjusts scores of

- Cluster ID: `rc2_742926538924987d`
- Assertions: 2
- Phrases: adjusts scores of
- Suggested normal forms: adjust score of
- Decision: accept (review_status: confirmed)

## allow attacker to disclose

- Cluster ID: `rc2_f2a570a5ea2d0f4c`
- Assertions: 2
- Phrases: allow attacker to disclose
- Suggested normal forms: allow attacker to disclose
- Decision: accept (review_status: confirmed)

## allows call to

- Cluster ID: `rc2_17f145a83d96b4e0`
- Assertions: 2
- Phrases: allows call to
- Suggested normal forms: allow call to
- Decision: accept (review_status: confirmed)

## allows multiple CVSS Base Scores to be generated for

- Cluster ID: `rc2_3bf9cc3cc40ec70a`
- Assertions: 2
- Phrases: allows multiple CVSS Base Scores to be generated for
- Suggested normal forms: allow multiple cvs base score to be generat for
- Decision: accept (review_status: confirmed)

## allows other processes to impact confidentiality of

- Cluster ID: `rc2_46819aece102ad4e`
- Assertions: 2
- Phrases: allows other processes to impact confidentiality of
- Suggested normal forms: allow other processe to impact confidentiality of
- Decision: pending (review_status: pending)

## allows slightly-more-severe metric strings within

- Cluster ID: `rc2_67618ec1e2742e6a`
- Assertions: 2
- Phrases: allows slightly-more-severe metric strings within
- Suggested normal forms: allow slightly-more-severe metric str within
- Decision: pending (review_status: pending)

## allows users to read

- Cluster ID: `rc2_dd3ddd527f581617`
- Assertions: 2
- Phrases: allows users to read
- Suggested normal forms: allow user to read
- Decision: pending (review_status: pending)

## are accessible from

- Cluster ID: `rc2_c4379fe9309a77ad`
- Assertions: 2
- Phrases: are accessible from, is accessible from
- Suggested normal forms: accessible from
- Decision: pending (review_status: pending)

## are affected by

- Cluster ID: `rc2_16a564459c6cc32d`
- Assertions: 2
- Phrases: are affected by, is affected by
- Suggested normal forms: affect by
- Decision: accept (review_status: confirmed)

## are as

- Cluster ID: `rc2_ca978112ca1bbdca`
- Assertions: 2
- Phrases: are as
- Suggested normal forms: a
- Decision: accept (review_status: confirmed)

## are assigned values by

- Cluster ID: `rc2_155867e9fd6c6a74`
- Assertions: 2
- Phrases: are assigned values by
- Suggested normal forms: assign value by
- Decision: accept (review_status: confirmed)

## are combined with

- Cluster ID: `rc2_20cf15ea25043189`
- Assertions: 2
- Phrases: are combined with
- Suggested normal forms: combin with
- Decision: pending (review_status: pending)

## are considered to have value of

- Cluster ID: `rc2_592520216a93e8ee`
- Assertions: 2
- Phrases: are considered to have value of
- Suggested normal forms: consider to value of
- Decision: accept (review_status: confirmed)

## are defined as documented by

- Cluster ID: `rc2_e2f18f0198bee25f`
- Assertions: 2
- Phrases: are defined as documented by
- Suggested normal forms: defin a document by
- Decision: pending (review_status: pending)

## are defined earlier in

- Cluster ID: `rc2_334967d0bc10584c`
- Assertions: 2
- Phrases: are defined earlier in
- Suggested normal forms: defin earlier in
- Decision: pending (review_status: pending)

## are derived from severity ranking of

- Cluster ID: `rc2_be8d2a3a840404a6`
- Assertions: 2
- Phrases: are derived from severity ranking of
- Suggested normal forms: deriv from severity rank of
- Decision: pending (review_status: pending)

## are direct responsibility of

- Cluster ID: `rc2_139be05393a7501a`
- Assertions: 2
- Phrases: are direct responsibility of
- Suggested normal forms: direct responsibility of
- Decision: accept (review_status: confirmed)

## are exploited in course of single attack to compromise application

- Cluster ID: `rc2_10f6f9c0a532c2fc`
- Assertions: 2
- Phrases: are exploited in course of single attack to compromise application, are exploited in course of single attack to compromise host
- Suggested normal forms: exploit in course of single attack to compromise application, exploit in course of single attack to compromise host
- Decision: pending (review_status: pending)

## are generated by

- Cluster ID: `rc2_2446f0b461a658b6`
- Assertions: 2
- Phrases: are generated by
- Suggested normal forms: generat by
- Decision: accept (review_status: confirmed)

## are how particular kind of

- Cluster ID: `rc2_2983cb3ac06cdac2`
- Assertions: 2
- Phrases: are how particular kind of, describe how particular kind of
- Suggested normal forms: describe how particular kind of, how particular kind of
- Decision: accept (review_status: confirmed)

## are leveraged in

- Cluster ID: `rc2_379cc07fe0b66e35`
- Assertions: 2
- Phrases: are leveraged in
- Suggested normal forms: leverag in
- Decision: accept (review_status: confirmed)

## are modified equivalent of

- Cluster ID: `rc2_ff3003168cfe000a`
- Assertions: 2
- Phrases: are modified equivalent of
- Suggested normal forms: modifi equivalent of
- Decision: pending (review_status: pending)

## are outside

- Cluster ID: `rc2_31207a2065f46a5b`
- Assertions: 2
- Phrases: are outside
- Suggested normal forms: outside
- Decision: accept (review_status: confirmed)

## are provided by

- Cluster ID: `rc2_6f3fb4fd20ba20be`
- Assertions: 2
- Phrases: are provided by
- Suggested normal forms: provid by
- Decision: pending (review_status: pending)

## are relevant to

- Cluster ID: `rc2_10f2514a7e449058`
- Assertions: 2
- Phrases: are relevant to
- Suggested normal forms: relevant to
- Decision: accept (review_status: confirmed)

## are standard ports used by

- Cluster ID: `rc2_07e91f0f417b71ab`
- Assertions: 2
- Phrases: are standard ports used by
- Suggested normal forms: standard port us by
- Decision: pending (review_status: pending)

## are subscribed to Reducing

- Cluster ID: `rc2_834e1e96135f36b3`
- Assertions: 2
- Phrases: are subscribed to Reducing
- Suggested normal forms: subscrib to reduc
- Decision: accept (review_status: confirmed)

## are to define

- Cluster ID: `rc2_a585b1e7d871d437`
- Assertions: 2
- Phrases: are to define, is to define
- Suggested normal forms: to define
- Decision: pending (review_status: pending)

## are used as

- Cluster ID: `rc2_060d63376229bf10`
- Assertions: 2
- Phrases: are used as
- Suggested normal forms: us a
- Decision: accept (review_status: confirmed)

## assume

- Cluster ID: `rc2_82e05dae00a818a3`
- Assertions: 2
- Phrases: assume
- Suggested normal forms: assume
- Decision: accept (review_status: confirmed)

## assumes reasonable worst case impact across

- Cluster ID: `rc2_7a9cdb39beb6c3c6`
- Assertions: 2
- Phrases: assumes reasonable worst case impact across, assumes reasonable worst-case impact across
- Suggested normal forms: assume reasonable worst case impact acros, assume reasonable worst-case impact acros
- Decision: pending (review_status: pending)

## attempt to exploit weakness in

- Cluster ID: `rc2_52a3f9bc104d071e`
- Assertions: 2
- Phrases: attempt to exploit weakness in
- Suggested normal forms: attempt to exploit weaknes in
- Decision: accept (review_status: confirmed)

## automate

- Cluster ID: `rc2_d74a0629c1de34c7`
- Assertions: 2
- Phrases: automate
- Suggested normal forms: automate
- Decision: accept (review_status: confirmed)

## be Recognizing industry-wide necessity for

- Cluster ID: `rc2_06f95ec02413783a`
- Assertions: 2
- Phrases: be Recognizing industry-wide necessity for
- Suggested normal forms: be recogniz industry-wide necessity for
- Decision: pending (review_status: pending)

## be Regarding

- Cluster ID: `rc2_e95b83c5bec3a80d`
- Assertions: 2
- Phrases: be Regarding
- Suggested normal forms: be regard
- Decision: pending (review_status: pending)

## be Steal

- Cluster ID: `rc2_68668cae284f9c09`
- Assertions: 2
- Phrases: be Steal, be steal
- Suggested normal forms: be steal
- Decision: pending (review_status: pending)

## be able

- Cluster ID: `rc2_b70eda7f6bf39f06`
- Assertions: 2
- Phrases: be able
- Suggested normal forms: be able
- Decision: accept (review_status: confirmed)

## be able to

- Cluster ID: `rc2_926de8edc5ac051c`
- Assertions: 2
- Phrases: be able to
- Suggested normal forms: be able to
- Decision: accept (review_status: confirmed)

## be account

- Cluster ID: `rc2_d43ae3160c435875`
- Assertions: 2
- Phrases: be account
- Suggested normal forms: be account
- Decision: pending (review_status: pending)

## be aligned to

- Cluster ID: `rc2_44496d3ace72569f`
- Assertions: 2
- Phrases: be aligned to
- Suggested normal forms: be align to
- Decision: accept (review_status: confirmed)

## be applied

- Cluster ID: `rc2_d5268b336fb1a7d4`
- Assertions: 2
- Phrases: be applied
- Suggested normal forms: be appli
- Decision: accept (review_status: confirmed)

## be apply significant severity to

- Cluster ID: `rc2_76d9815080f68474`
- Assertions: 2
- Phrases: be apply significant severity to
- Suggested normal forms: be apply significant severity to
- Decision: accept (review_status: confirmed)

## be as

- Cluster ID: `rc2_c31de59e22837419`
- Assertions: 2
- Phrases: be as
- Suggested normal forms: be a
- Decision: pending (review_status: pending)

## be associated with exploitation of

- Cluster ID: `rc2_5361bfd2087c7ef7`
- Assertions: 2
- Phrases: be associated with exploitation of
- Suggested normal forms: be associat with exploitation of
- Decision: pending (review_status: pending)

## be based on metric value changes within

- Cluster ID: `rc2_96f7c5d475d937f5`
- Assertions: 2
- Phrases: be based on metric value changes within, be based on metric values within
- Suggested normal forms: be bas on metric value change within, be bas on metric value within
- Decision: pending (review_status: pending)

## be built into

- Cluster ID: `rc2_c063262e327bc1ba`
- Assertions: 2
- Phrases: be built into
- Suggested normal forms: be built into
- Decision: accept (review_status: confirmed)

## be bypass authentication on

- Cluster ID: `rc2_7dcde7e90497ba33`
- Assertions: 2
- Phrases: be bypass authentication on
- Suggested normal forms: be bypas authentication on
- Decision: accept (review_status: confirmed)

## be bypass operations as

- Cluster ID: `rc2_722f56eae2763897`
- Assertions: 2
- Phrases: be bypass operations as
- Suggested normal forms: be bypas operation a
- Decision: accept (review_status: confirmed)

## be calculate order of vectors from

- Cluster ID: `rc2_fbe49290f95d533d`
- Assertions: 2
- Phrases: be calculate order of vectors from
- Suggested normal forms: be calculate order of vector from
- Decision: pending (review_status: pending)

## be calling

- Cluster ID: `rc2_1441af484b734076`
- Assertions: 2
- Phrases: be calling
- Suggested normal forms: be call
- Decision: accept (review_status: confirmed)

## be categorized as

- Cluster ID: `rc2_dfe4d60ba8737fb1`
- Assertions: 2
- Phrases: be categorized as
- Suggested normal forms: be categoriz a
- Decision: accept (review_status: confirmed)

## be certified

- Cluster ID: `rc2_93f9d7da526a82e2`
- Assertions: 2
- Phrases: be certified
- Suggested normal forms: be certifi
- Decision: accept (review_status: confirmed)

## be chained to

- Cluster ID: `rc2_cbedd2cc11f67848`
- Assertions: 2
- Phrases: be chained to
- Suggested normal forms: be chain to
- Decision: accept (review_status: confirmed)

## be classified as

- Cluster ID: `rc2_c33bed508af465a5`
- Assertions: 2
- Phrases: be classified as
- Suggested normal forms: be classifi a
- Decision: pending (review_status: pending)

## be completed

- Cluster ID: `rc2_280e3dc485d26f03`
- Assertions: 2
- Phrases: be completed
- Suggested normal forms: be complet
- Decision: pending (review_status: pending)

## be compromise

- Cluster ID: `rc2_f0bd52a462673b5a`
- Assertions: 2
- Phrases: be compromise
- Suggested normal forms: be compromise
- Decision: pending (review_status: pending)

## be considered Low value for Attack Complexity independent of attacker 's knowledge For

- Cluster ID: `rc2_999521351517d370`
- Assertions: 2
- Phrases: be considered Low value for Attack Complexity independent of attacker 's knowledge For
- Suggested normal forms: be consider low value for attack complexity independent of attacker 's knowledge for
- Decision: pending (review_status: pending)

## be considered Low value for Attack Complexity independent of capabilities For

- Cluster ID: `rc2_d285d02bd479e588`
- Assertions: 2
- Phrases: be considered Low value for Attack Complexity independent of capabilities For
- Suggested normal forms: be consider low value for attack complexity independent of capability for
- Decision: pending (review_status: pending)

## be considered when

- Cluster ID: `rc2_264887c710cd212e`
- Assertions: 2
- Phrases: be considered when
- Suggested normal forms: be consider when
- Decision: accept (review_status: confirmed)

## be containing

- Cluster ID: `rc2_6f1bae1af4db191c`
- Assertions: 2
- Phrases: be containing
- Suggested normal forms: be contain
- Decision: pending (review_status: pending)

## be crash

- Cluster ID: `rc2_59deb2f24c2ad6c2`
- Assertions: 2
- Phrases: be crash
- Suggested normal forms: be crash
- Decision: accept (review_status: confirmed)

## be delivered as payload of network-based worm In

- Cluster ID: `rc2_f690f8a33f63c558`
- Assertions: 2
- Phrases: be delivered as payload of network-based worm In
- Suggested normal forms: be deliver a payload of network-bas worm in
- Decision: pending (review_status: pending)

## be delivered as payload of other automated attack tools In

- Cluster ID: `rc2_74f3bcffcf1199e5`
- Assertions: 2
- Phrases: be delivered as payload of other automated attack tools In
- Suggested normal forms: be deliver a payload of other automat attack tool in
- Decision: pending (review_status: pending)

## be delivered as payload of virus In

- Cluster ID: `rc2_3864d89da833e93b`
- Assertions: 2
- Phrases: be delivered as payload of virus In
- Suggested normal forms: be deliver a payload of viru in
- Decision: pending (review_status: pending)

## be deploy reverse SSH tool for

- Cluster ID: `rc2_082f60e7cdc06dd8`
- Assertions: 2
- Phrases: be deploy reverse SSH tool for
- Suggested normal forms: be deploy reverse ssh tool for
- Decision: accept (review_status: confirmed)

## be derive

- Cluster ID: `rc2_fa6a98acd5df4f18`
- Assertions: 2
- Phrases: be derive
- Suggested normal forms: be derive
- Decision: pending (review_status: pending)

## be described

- Cluster ID: `rc2_f64fbd125af6a1b5`
- Assertions: 2
- Phrases: be described
- Suggested normal forms: be describ
- Decision: accept (review_status: confirmed)

## be described by

- Cluster ID: `rc2_790cf4a985632616`
- Assertions: 2
- Phrases: be described by
- Suggested normal forms: be describ by
- Decision: pending (review_status: pending)

## be described through

- Cluster ID: `rc2_9f3101f88b5e249a`
- Assertions: 2
- Phrases: be described through
- Suggested normal forms: be describ through
- Decision: pending (review_status: pending)

## be determined for

- Cluster ID: `rc2_8379c2333585ffda`
- Assertions: 2
- Phrases: be determined for
- Suggested normal forms: be determin for
- Decision: pending (review_status: pending)

## be discuss

- Cluster ID: `rc2_a3e629097db097c8`
- Assertions: 2
- Phrases: be discuss
- Suggested normal forms: be discus
- Decision: pending (review_status: pending)

## be displayed with

- Cluster ID: `rc2_a3e41bb937ead51e`
- Assertions: 2
- Phrases: be displayed with
- Suggested normal forms: be display with
- Decision: pending (review_status: pending)

## be enforcing

- Cluster ID: `rc2_c8c5d736f263fb0c`
- Assertions: 2
- Phrases: be enforcing
- Suggested normal forms: be enforc
- Decision: accept (review_status: confirmed)

## be enhance

- Cluster ID: `rc2_a7f77df34a06b6e1`
- Assertions: 2
- Phrases: be enhance
- Suggested normal forms: be enhance
- Decision: accept (review_status: confirmed)

## be ensure adherence with

- Cluster ID: `rc2_7ff4e60834dabaf8`
- Assertions: 2
- Phrases: be ensure adherence with
- Suggested normal forms: be ensure adherence with
- Decision: pending (review_status: pending)

## be enumerated as

- Cluster ID: `rc2_9e0a8cc60b8efdca`
- Assertions: 2
- Phrases: be enumerated as
- Suggested normal forms: be enumerat a
- Decision: accept (review_status: confirmed)

## be establish

- Cluster ID: `rc2_8d53136835c78064`
- Assertions: 2
- Phrases: be establish
- Suggested normal forms: be establish
- Decision: accept (review_status: confirmed)

## be evade

- Cluster ID: `rc2_01d56b196b20a3cd`
- Assertions: 2
- Phrases: be evade
- Suggested normal forms: be evade
- Decision: pending (review_status: pending)

## be execute arbitrary code on

- Cluster ID: `rc2_fd5559ec4108c3ee`
- Assertions: 2
- Phrases: be execute arbitrary code on
- Suggested normal forms: be execute arbitrary code on
- Decision: pending (review_status: pending)

## be exploited from across

- Cluster ID: `rc2_e996f519006d3382`
- Assertions: 2
- Phrases: be exploited from across
- Suggested normal forms: be exploit from acros
- Decision: accept (review_status: confirmed)

## be filtering by

- Cluster ID: `rc2_c54208b466c829c4`
- Assertions: 2
- Phrases: be filtering by
- Suggested normal forms: be filter by
- Decision: accept (review_status: confirmed)

## be found

- Cluster ID: `rc2_4242984a6b5f9b37`
- Assertions: 2
- Phrases: be found
- Suggested normal forms: be found
- Decision: accept (review_status: confirmed)

## be found in

- Cluster ID: `rc2_052e8c086e59bf5a`
- Assertions: 2
- Phrases: be found in
- Suggested normal forms: be found in
- Decision: pending (review_status: pending)

## be get

- Cluster ID: `rc2_56709555acf59ce7`
- Assertions: 2
- Phrases: be get
- Suggested normal forms: be get
- Decision: pending (review_status: pending)

## be granted to

- Cluster ID: `rc2_c0992930184f2894`
- Assertions: 2
- Phrases: be granted to
- Suggested normal forms: be grant to
- Decision: accept (review_status: confirmed)

## be identified in

- Cluster ID: `rc2_36a88bd6135dde84`
- Assertions: 2
- Phrases: be identified in
- Suggested normal forms: be identifi in
- Decision: accept (review_status: confirmed)

## be identify

- Cluster ID: `rc2_0f2a706c74c5945e`
- Assertions: 2
- Phrases: be identify
- Suggested normal forms: be identify
- Decision: pending (review_status: pending)

## be identifying cross-agency status in implementation of

- Cluster ID: `rc2_d3966ae647d9ea86`
- Assertions: 2
- Phrases: be identifying cross-agency status in implementation of
- Suggested normal forms: be identify cros-agency statu in implementation of
- Decision: accept (review_status: confirmed)

## be identifying outstanding issues in implementation of

- Cluster ID: `rc2_9f1361fdafe733fb`
- Assertions: 2
- Phrases: be identifying outstanding issues in implementation of
- Suggested normal forms: be identify outstand issue in implementation of
- Decision: accept (review_status: confirmed)

## be included in vector string if

- Cluster ID: `rc2_3f37420413223dde`
- Assertions: 2
- Phrases: be included in vector string if
- Suggested normal forms: be includ in vector str if
- Decision: pending (review_status: pending)

## be incorporate

- Cluster ID: `rc2_3701dfdec8578b81`
- Assertions: 2
- Phrases: be incorporate
- Suggested normal forms: be incorporate
- Decision: accept (review_status: confirmed)

## be increasing

- Cluster ID: `rc2_88cd9f95d4a53d08`
- Assertions: 2
- Phrases: be increasing
- Suggested normal forms: be increas
- Decision: accept (review_status: confirmed)

## be injured as result of

- Cluster ID: `rc2_52287c3d99220e45`
- Assertions: 2
- Phrases: be injured as result of
- Suggested normal forms: be injur a result of
- Decision: pending (review_status: pending)

## be integrated

- Cluster ID: `rc2_6a42bb604ba1eaa8`
- Assertions: 2
- Phrases: be integrated
- Suggested normal forms: be integrat
- Decision: accept (review_status: confirmed)

## be leveraged to generate that

- Cluster ID: `rc2_9a90be9ba762a242`
- Assertions: 2
- Phrases: be leveraged to generate that
- Suggested normal forms: be leverag to generate that
- Decision: pending (review_status: pending)

## be missing

- Cluster ID: `rc2_eb1034d6f6c211bc`
- Assertions: 2
- Phrases: be missing
- Suggested normal forms: be miss
- Decision: pending (review_status: pending)

## be operating under

- Cluster ID: `rc2_38618d5ff822989f`
- Assertions: 2
- Phrases: be operating under
- Suggested normal forms: be operat under
- Decision: pending (review_status: pending)

## be performed for

- Cluster ID: `rc2_26a7befc0f799fb9`
- Assertions: 2
- Phrases: be performed for
- Suggested normal forms: be perform for
- Decision: pending (review_status: pending)

## be performed for attack to be successful For

- Cluster ID: `rc2_4dde1872341f043c`
- Assertions: 2
- Phrases: be performed for attack to be successful For
- Suggested normal forms: be perform for attack to be successful for
- Decision: pending (review_status: pending)

## be populate values of

- Cluster ID: `rc2_eabd66f1f9917288`
- Assertions: 2
- Phrases: be populate values of
- Suggested normal forms: be populate value of
- Decision: pending (review_status: pending)

## be produced by

- Cluster ID: `rc2_ede476f2a85a3446`
- Assertions: 2
- Phrases: be produced by
- Suggested normal forms: be produc by
- Decision: accept (review_status: confirmed)

## be provided for

- Cluster ID: `rc2_7d6cd08302e83a03`
- Assertions: 2
- Phrases: be provided for
- Suggested normal forms: be provid for
- Decision: accept (review_status: confirmed)

## be published at

- Cluster ID: `rc2_3d4b703b7fc4053f`
- Assertions: 2
- Phrases: be published at
- Suggested normal forms: be publish at
- Decision: pending (review_status: pending)

## be raise bar in

- Cluster ID: `rc2_a2df4299157e0d6c`
- Assertions: 2
- Phrases: be raise bar in
- Suggested normal forms: be raise bar in
- Decision: accept (review_status: confirmed)

## be ranking to be

- Cluster ID: `rc2_69839e25c2b7351a`
- Assertions: 2
- Phrases: be ranking to be
- Suggested normal forms: be rank to be
- Decision: pending (review_status: pending)

## be rated at

- Cluster ID: `rc2_e31b0853d36e477b`
- Assertions: 2
- Phrases: be rated at
- Suggested normal forms: be rat at
- Decision: accept (review_status: confirmed)

## be rated at least Medium due strictly to sensitivity of

- Cluster ID: `rc2_80f2106f89bea91a`
- Assertions: 2
- Phrases: be rated at least Medium due strictly to sensitivity of
- Suggested normal forms: be rat at least medium due strictly to sensitivity of
- Decision: accept (review_status: confirmed)

## be reflect more

- Cluster ID: `rc2_1d52445ec097aaae`
- Assertions: 2
- Phrases: be reflect more
- Suggested normal forms: be reflect more
- Decision: accept (review_status: confirmed)

## be reflected

- Cluster ID: `rc2_06087f84e0882d18`
- Assertions: 2
- Phrases: be reflected
- Suggested normal forms: be reflect
- Decision: pending (review_status: pending)

## be reflected e.g. in

- Cluster ID: `rc2_942225824b2675e3`
- Assertions: 2
- Phrases: be reflected e.g. in
- Suggested normal forms: be reflect e.g. in
- Decision: pending (review_status: pending)

## be reflected in

- Cluster ID: `rc2_2e48d4de726d51c9`
- Assertions: 2
- Phrases: be reflected in
- Suggested normal forms: be reflect in
- Decision: pending (review_status: pending)

## be reflected in Environmental metric scoring group

- Cluster ID: `rc2_4097c5dff9d9b7fc`
- Assertions: 2
- Phrases: be reflected in Environmental metric scoring group
- Suggested normal forms: be reflect in environmental metric scor group
- Decision: pending (review_status: pending)

## be reflected via

- Cluster ID: `rc2_cf77c45500654f10`
- Assertions: 2
- Phrases: be reflected via
- Suggested normal forms: be reflect via
- Decision: pending (review_status: pending)

## be remediate

- Cluster ID: `rc2_979afd75731d0ddf`
- Assertions: 2
- Phrases: be remediate
- Suggested normal forms: be remediate
- Decision: accept (review_status: confirmed)

## be reporting through

- Cluster ID: `rc2_f6cafa6828233d85`
- Assertions: 2
- Phrases: be reporting through
- Suggested normal forms: be report through
- Decision: accept (review_status: confirmed)

## be represent

- Cluster ID: `rc2_5be19c5c9ad66bc0`
- Assertions: 2
- Phrases: be represent
- Suggested normal forms: be represent
- Decision: accept (review_status: confirmed)

## be represented in

- Cluster ID: `rc2_179d6160fe0c00f9`
- Assertions: 2
- Phrases: be represented in
- Suggested normal forms: be represent in
- Decision: accept (review_status: confirmed)

## be required into

- Cluster ID: `rc2_6ab2b64e9b5def98`
- Assertions: 2
- Phrases: be required into
- Suggested normal forms: be requir into
- Decision: accept (review_status: confirmed)

## be required to achieve

- Cluster ID: `rc2_31105db2ddc04668`
- Assertions: 2
- Phrases: be required to achieve
- Suggested normal forms: be requir to achieve
- Decision: accept (review_status: confirmed)

## be running

- Cluster ID: `rc2_0ed32fed1d6179f0`
- Assertions: 2
- Phrases: be running
- Suggested normal forms: be runn
- Decision: pending (review_status: pending)

## be running SharePoint in

- Cluster ID: `rc2_38a1a15597dc4b01`
- Assertions: 2
- Phrases: be running SharePoint in
- Suggested normal forms: be runn sharepoint in
- Decision: accept (review_status: confirmed)

## be running with

- Cluster ID: `rc2_33cb9e387c26a43f`
- Assertions: 2
- Phrases: be running with
- Suggested normal forms: be runn with
- Decision: accept (review_status: confirmed)

## be running with reduced privileges in

- Cluster ID: `rc2_6e1e347e4f8265ea`
- Assertions: 2
- Phrases: be running with reduced privileges in
- Suggested normal forms: be runn with reduc privilege in
- Decision: pending (review_status: pending)

## be scored as

- Cluster ID: `rc2_5b4d489610aa62e8`
- Assertions: 2
- Phrases: be scored as
- Suggested normal forms: be scor a
- Decision: pending (review_status: pending)

## be send crafted request to

- Cluster ID: `rc2_d697d33834684c53`
- Assertions: 2
- Phrases: be send crafted request to
- Suggested normal forms: be send craft request to
- Decision: accept (review_status: confirmed)

## be serving as

- Cluster ID: `rc2_391e389fd8132a74`
- Assertions: 2
- Phrases: be serving as
- Suggested normal forms: be serv a
- Decision: accept (review_status: confirmed)

## be set arbitrary properties on

- Cluster ID: `rc2_78d3a80c5194e330`
- Assertions: 2
- Phrases: be set arbitrary properties on
- Suggested normal forms: be set arbitrary property on
- Decision: accept (review_status: confirmed)

## be set to overlap slightly-less-severe metric strings from

- Cluster ID: `rc2_0f372aefae1d4556`
- Assertions: 2
- Phrases: be set to overlap slightly-less-severe metric strings from
- Suggested normal forms: be set to overlap slightly-les-severe metric str from
- Decision: pending (review_status: pending)

## be shared with other components across

- Cluster ID: `rc2_bb9d6b80d1d0ff7c`
- Assertions: 2
- Phrases: be shared with other components across
- Suggested normal forms: be shar with other component acros
- Decision: accept (review_status: confirmed)

## be show

- Cluster ID: `rc2_54b136c974778d09`
- Assertions: 2
- Phrases: be show, be showing
- Suggested normal forms: be show
- Decision: pending (review_status: pending)

## be signed by

- Cluster ID: `rc2_c074326e38350375`
- Assertions: 2
- Phrases: be signed by
- Suggested normal forms: be sign by
- Decision: accept (review_status: confirmed)

## be support ongoing vulnerability remediation based on

- Cluster ID: `rc2_1925e0c822a63392`
- Assertions: 2
- Phrases: be support ongoing vulnerability remediation based on
- Suggested normal forms: be support ongo vulnerability remediation bas on
- Decision: accept (review_status: confirmed)

## be supporting information for

- Cluster ID: `rc2_fa549cfde2dcd255`
- Assertions: 2
- Phrases: be supporting information for
- Suggested normal forms: be support information for
- Decision: accept (review_status: confirmed)

## be taken into

- Cluster ID: `rc2_246bf65731847734`
- Assertions: 2
- Phrases: be taken into
- Suggested normal forms: be taken into
- Decision: pending (review_status: pending)

## be to run

- Cluster ID: `rc2_17a33d15a889b53c`
- Assertions: 2
- Phrases: be to run
- Suggested normal forms: be to run
- Decision: accept (review_status: confirmed)

## be to run listening service with

- Cluster ID: `rc2_c7f0e660074eb800`
- Assertions: 2
- Phrases: be to run listening service with
- Suggested normal forms: be to run listen service with
- Decision: accept (review_status: confirmed)

## be used to calculate

- Cluster ID: `rc2_6954391b295b3e37`
- Assertions: 2
- Phrases: be used to calculate
- Suggested normal forms: be us to calculate
- Decision: accept (review_status: confirmed)

## be used to get

- Cluster ID: `rc2_96515a59bc226064`
- Assertions: 2
- Phrases: be used to get
- Suggested normal forms: be us to get
- Decision: pending (review_status: pending)

## be used to store CVSS information in

- Cluster ID: `rc2_41e51c74a1514f81`
- Assertions: 2
- Phrases: be used to store CVSS information in
- Suggested normal forms: be us to store cvs information in
- Decision: pending (review_status: pending)

## be used to transfer CVSS information in

- Cluster ID: `rc2_bf7a2726baba4f61`
- Assertions: 2
- Phrases: be used to transfer CVSS information in
- Suggested normal forms: be us to transfer cvs information in
- Decision: pending (review_status: pending)

## be useful when

- Cluster ID: `rc2_7baaf953855acba5`
- Assertions: 2
- Phrases: be useful when
- Suggested normal forms: be useful when
- Decision: accept (review_status: confirmed)

## be utilize

- Cluster ID: `rc2_11eeac94424d9c74`
- Assertions: 2
- Phrases: be utilize
- Suggested normal forms: be utilize
- Decision: pending (review_status: pending)

## began five days later

- Cluster ID: `rc2_d372a75b27853852`
- Assertions: 2
- Phrases: began five days later, began five days later on
- Suggested normal forms: began five day later, began five day later on
- Decision: pending (review_status: pending)

## began to see

- Cluster ID: `rc2_f2604aba7ca9ec8e`
- Assertions: 2
- Phrases: began to see
- Suggested normal forms: began to see
- Decision: pending (review_status: pending)

## behavior of software gives threat actor low stochastic opportunity for

- Cluster ID: `rc2_ac2c40f3b10d9b38`
- Assertions: 2
- Phrases: behavior of software gives threat actor low stochastic opportunity for
- Suggested normal forms: behavior of software give threat actor low stochastic opportunity for
- Decision: accept (review_status: confirmed)

## believe

- Cluster ID: `rc2_f078209dfece9535`
- Assertions: 2
- Phrases: believe
- Suggested normal forms: believe
- Decision: accept (review_status: confirmed)

## bound to

- Cluster ID: `rc2_3784683c44619184`
- Assertions: 2
- Phrases: bound to, is bound to
- Suggested normal forms: bound to
- Decision: pending (review_status: pending)

## bypass authentication In

- Cluster ID: `rc2_bef4128f5199e9b9`
- Assertions: 2
- Phrases: bypass authentication In, is authentication bypass in
- Suggested normal forms: authentication bypas in, bypas authentication in
- Decision: pending (review_status: pending)

## cause exploitation events

- Cluster ID: `rc2_6869a9ba613d3a4f`
- Assertions: 2
- Phrases: cause exploitation events
- Suggested normal forms: cause exploitation event
- Decision: accept (review_status: confirmed)

## collaborated to adjust

- Cluster ID: `rc2_5d6a76de5c818f94`
- Assertions: 2
- Phrases: collaborated to adjust
- Suggested normal forms: collaborat to adjust
- Decision: accept (review_status: confirmed)

## collaborated with Deloitte & Touche LLP to adjust

- Cluster ID: `rc2_5946e5cdb401bcf6`
- Assertions: 2
- Phrases: collaborated with Deloitte & Touche LLP to adjust
- Suggested normal forms: collaborat with deloitte & touche llp to adjust
- Decision: accept (review_status: confirmed)

## communicates metrics used in

- Cluster ID: `rc2_835a4fff4c6a1214`
- Assertions: 2
- Phrases: communicates metrics used in
- Suggested normal forms: communicate metric us in
- Decision: pending (review_status: pending)

## conducted searches for

- Cluster ID: `rc2_8ca0127818a852be`
- Assertions: 2
- Phrases: conducted searches for
- Suggested normal forms: conduct searche for
- Decision: pending (review_status: pending)

## conducted zero-day research project against

- Cluster ID: `rc2_8952ea54f8e3d162`
- Assertions: 2
- Phrases: conducted zero-day research project against
- Suggested normal forms: conduct zero-day research project against
- Decision: pending (review_status: pending)

## configured

- Cluster ID: `rc2_82c4604cacfee4bc`
- Assertions: 2
- Phrases: configured
- Suggested normal forms: configur
- Decision: pending (review_status: pending)

## consists of

- Cluster ID: `rc2_5f91503c4d13866b`
- Assertions: 2
- Phrases: consists of
- Suggested normal forms: consist of
- Decision: accept (review_status: confirmed)

## contact

- Cluster ID: `rc2_093e7d5fdbaacfa9`
- Assertions: 2
- Phrases: contact, has contacted
- Suggested normal forms: contact
- Decision: pending (review_status: pending)

## contact QUIRSO GmbH for

- Cluster ID: `rc2_fdf1b23f2d44cef7`
- Assertions: 2
- Phrases: contact QUIRSO GmbH for
- Suggested normal forms: contact quirso gmbh for
- Decision: pending (review_status: pending)

## contained in

- Cluster ID: `rc2_51f2ab03595310df`
- Assertions: 2
- Phrases: contained in
- Suggested normal forms: contain in
- Decision: accept (review_status: confirmed)

## contains scoring rubrics for

- Cluster ID: `rc2_b76292419eb84729`
- Assertions: 2
- Phrases: contains scoring rubrics for
- Suggested normal forms: contain scor rubric for
- Decision: pending (review_status: pending)

## continue to track

- Cluster ID: `rc2_de492903344a2ebc`
- Assertions: 2
- Phrases: continue to track
- Suggested normal forms: continue to track
- Decision: accept (review_status: confirmed)

## continued

- Cluster ID: `rc2_3c66dee1659c632b`
- Assertions: 2
- Phrases: continued
- Suggested normal forms: continu
- Decision: accept (review_status: confirmed)

## contribute to production of

- Cluster ID: `rc2_b2ec12be49c0f576`
- Assertions: 2
- Phrases: contribute to production of
- Suggested normal forms: contribute to production of
- Decision: accept (review_status: confirmed)

## crashes

- Cluster ID: `rc2_17f3c27e3c2a5c91`
- Assertions: 2
- Phrases: crashes
- Suggested normal forms: crashe
- Decision: accept (review_status: confirmed)

## created Stakeholder-Specific Vulnerability Categorization system

- Cluster ID: `rc2_b27bdf370c012599`
- Assertions: 2
- Phrases: created Stakeholder-Specific Vulnerability Categorization system, created Stakeholder-Specific Vulnerability Categorization system in
- Suggested normal forms: creat stakeholder-specific vulnerability categorization system, creat stakeholder-specific vulnerability categorization system in
- Decision: accept (review_status: confirmed)

## created Stakeholder-Specific Vulnerability Categorization system in 2019 prevalence of

- Cluster ID: `rc2_235136902fe42739`
- Assertions: 2
- Phrases: created Stakeholder-Specific Vulnerability Categorization system in 2019 prevalence of, created Stakeholder-Specific Vulnerability Categorization system prevalence of
- Suggested normal forms: creat stakeholder-specific vulnerability categorization system in 2019 prevalence of, creat stakeholder-specific vulnerability categorization system prevalence of
- Decision: pending (review_status: pending)

## deliver high-fidelity insights to market Recognizing industry-wide necessity for

- Cluster ID: `rc2_57081bb5bae16e8d`
- Assertions: 2
- Phrases: deliver high-fidelity insights to market Recognizing industry-wide necessity for
- Suggested normal forms: deliver high-fidelity insight to market recogniz industry-wide necessity for
- Decision: pending (review_status: pending)

## demonstrated operational security awareness having emptied exploit directories after

- Cluster ID: `rc2_8f0358df92808c4b`
- Assertions: 2
- Phrases: demonstrated operational security awareness having emptied exploit directories after
- Suggested normal forms: demonstrat operational security awarenes hav empti exploit directory after
- Decision: accept (review_status: confirmed)

## deny

- Cluster ID: `rc2_3026a0ca485e5831`
- Assertions: 2
- Phrases: deny
- Suggested normal forms: deny
- Decision: accept (review_status: confirmed)

## deployed open-source reverse_ssh framework to establish

- Cluster ID: `rc2_318be4b2f23d9c56`
- Assertions: 2
- Phrases: deployed open-source reverse_ssh framework to establish
- Suggested normal forms: deploy open-source reverse_ssh framework to establish
- Decision: accept (review_status: confirmed)

## describe

- Cluster ID: `rc2_c52028f34e378d1e`
- Assertions: 2
- Phrases: describe, describes
- Suggested normal forms: describe
- Decision: pending (review_status: pending)

## determine

- Cluster ID: `rc2_3d8eefab379df522`
- Assertions: 2
- Phrases: determine, determines
- Suggested normal forms: determine
- Decision: accept (review_status: confirmed)

## developed

- Cluster ID: `rc2_947726dd63187532`
- Assertions: 2
- Phrases: developed
- Suggested normal forms: develop
- Decision: accept (review_status: confirmed)

## did test

- Cluster ID: `rc2_631107a3f9976ac2`
- Assertions: 2
- Phrases: did test
- Suggested normal forms: did test
- Decision: accept (review_status: confirmed)

## die

- Cluster ID: `rc2_a8d79f40ddb79de5`
- Assertions: 2
- Phrases: die
- Suggested normal forms: die
- Decision: accept (review_status: confirmed)

## differ from security-enhancing techniques/technologies

- Cluster ID: `rc2_2893007e93b0d543`
- Assertions: 2
- Phrases: differ from security-enhancing techniques/technologies
- Suggested normal forms: differ from security-enhanc technique/technology
- Decision: accept (review_status: confirmed)

## discover

- Cluster ID: `rc2_5b90071aea261a5b`
- Assertions: 2
- Phrases: discover, discovers
- Suggested normal forms: discover
- Decision: pending (review_status: pending)

## disrupt existing connections

- Cluster ID: `rc2_7d2477b6bf0e99f0`
- Assertions: 2
- Phrases: disrupt existing connections
- Suggested normal forms: disrupt exist connection
- Decision: pending (review_status: pending)

## do need to pass

- Cluster ID: `rc2_15946fb362fde37b`
- Assertions: 2
- Phrases: do need to pass
- Suggested normal forms: ne to pas
- Decision: accept (review_status: confirmed)

## document

- Cluster ID: `rc2_43cc23fa52b87b4c`
- Assertions: 2
- Phrases: document
- Suggested normal forms: document
- Decision: accept (review_status: confirmed)

## does correspond to

- Cluster ID: `rc2_797f3561e93f15f8`
- Assertions: 2
- Phrases: does correspond to
- Suggested normal forms: correspond to
- Decision: accept (review_status: confirmed)

## does impact server-side controls for

- Cluster ID: `rc2_13e9fb89851e7054`
- Assertions: 2
- Phrases: does impact server-side controls for, does server-side controls for
- Suggested normal forms: impact server-side control for, server-side control for
- Decision: pending (review_status: pending)

## does require action at

- Cluster ID: `rc2_83ded92581260a6b`
- Assertions: 2
- Phrases: does require action at
- Suggested normal forms: require action at
- Decision: pending (review_status: pending)

## drops

- Cluster ID: `rc2_d90ee9ccf6bea1d2`
- Assertions: 2
- Phrases: drops
- Suggested normal forms: drop
- Decision: pending (review_status: pending)

## embeds

- Cluster ID: `rc2_e251a7a05ee81b84`
- Assertions: 2
- Phrases: embeds
- Suggested normal forms: emb
- Decision: accept (review_status: confirmed)

## emphasizes

- Cluster ID: `rc2_c21f0c94db79d75f`
- Assertions: 2
- Phrases: emphasizes
- Suggested normal forms: emphasize
- Decision: accept (review_status: confirmed)

## employs

- Cluster ID: `rc2_b0688a56fae3ddb4`
- Assertions: 2
- Phrases: employs
- Suggested normal forms: employ
- Decision: accept (review_status: confirmed)

## employs automated methods to

- Cluster ID: `rc2_7766b68d9e30c349`
- Assertions: 2
- Phrases: employs automated methods to
- Suggested normal forms: employ automat method to
- Decision: accept (review_status: confirmed)

## enable analyst to override

- Cluster ID: `rc2_5af95f20932ad290`
- Assertions: 2
- Phrases: enable analyst to override, enable consumer analyst to override
- Suggested normal forms: enable analyst to override, enable consumer analyst to override
- Decision: pending (review_status: pending)

## enabled them to increase

- Cluster ID: `rc2_76e025d584cb523f`
- Assertions: 2
- Phrases: enabled them to increase
- Suggested normal forms: enabl them to increase
- Decision: accept (review_status: confirmed)

## enabled them to increase dramatically speed of

- Cluster ID: `rc2_979897edbdc84aba`
- Assertions: 2
- Phrases: enabled them to increase dramatically speed of, enabled them to increase speed of
- Suggested normal forms: enabl them to increase dramatically spe of, enabl them to increase spe of
- Decision: accept (review_status: confirmed)

## enrich Base metrics with

- Cluster ID: `rc2_e7d56761544a99b7`
- Assertions: 2
- Phrases: enrich Base metrics with
- Suggested normal forms: enrich base metric with
- Decision: pending (review_status: pending)

## ensure that

- Cluster ID: `rc2_2b99d0a0d2f213b3`
- Assertions: 2
- Phrases: ensure that
- Suggested normal forms: ensure that
- Decision: pending (review_status: pending)

## establishes

- Cluster ID: `rc2_41a5c381f454a5d7`
- Assertions: 2
- Phrases: establishes
- Suggested normal forms: establishe
- Decision: accept (review_status: confirmed)

## execute

- Cluster ID: `rc2_be6bdfe81ec4a456`
- Assertions: 2
- Phrases: execute, executes
- Suggested normal forms: execute
- Decision: pending (review_status: pending)

## executed hundreds of hours of manual targeting analysis in

- Cluster ID: `rc2_cad036410c33f836`
- Assertions: 2
- Phrases: executed hundreds of hours of manual targeting analysis in
- Suggested normal forms: execut hundr of hour of manual target analysi in
- Decision: accept (review_status: confirmed)

## exists

- Cluster ID: `rc2_7d68838bddc6082b`
- Assertions: 2
- Phrases: exists
- Suggested normal forms: exist
- Decision: accept (review_status: confirmed)

## exists in

- Cluster ID: `rc2_595fdc3b57134cdc`
- Assertions: 2
- Phrases: exists in
- Suggested normal forms: exist in
- Decision: pending (review_status: pending)

## expect

- Cluster ID: `rc2_77f2f036726eaa17`
- Assertions: 2
- Phrases: expect
- Suggested normal forms: expect
- Decision: pending (review_status: pending)

## expect repeatable success against

- Cluster ID: `rc2_6f76a77773220789`
- Assertions: 2
- Phrases: expect repeatable success against
- Suggested normal forms: expect repeatable succes against
- Decision: pending (review_status: pending)

## explain

- Cluster ID: `rc2_0818ab2593f5cb6c`
- Assertions: 2
- Phrases: explain, explains
- Suggested normal forms: explain
- Decision: pending (review_status: pending)

## exploit chain to

- Cluster ID: `rc2_eb19af037e7152f1`
- Assertions: 2
- Phrases: exploit chain to
- Suggested normal forms: exploit chain to
- Decision: pending (review_status: pending)

## exploit gives threat actor low stochastic opportunity for

- Cluster ID: `rc2_a5d9798c225fe58e`
- Assertions: 2
- Phrases: exploit gives threat actor low stochastic opportunity for
- Suggested normal forms: exploit give threat actor low stochastic opportunity for
- Decision: accept (review_status: confirmed)

## exploit issue to bypass

- Cluster ID: `rc2_100231277505c1d5`
- Assertions: 2
- Phrases: exploit issue to bypass
- Suggested normal forms: exploit issue to bypas
- Decision: accept (review_status: confirmed)

## exposed OpenSLP on

- Cluster ID: `rc2_ba98e3b9a26629c3`
- Assertions: 2
- Phrases: exposed OpenSLP on
- Suggested normal forms: expos openslp on
- Decision: pending (review_status: pending)

## find

- Cluster ID: `rc2_e6640de835ad09fb`
- Assertions: 2
- Phrases: find, finds
- Suggested normal forms: find
- Decision: pending (review_status: pending)

## follows in

- Cluster ID: `rc2_4e7082f7f40c0409`
- Assertions: 2
- Phrases: follows in
- Suggested normal forms: follow in
- Decision: pending (review_status: pending)

## grant attacker Confidentiality

- Cluster ID: `rc2_e4c54e526f5c76ee`
- Assertions: 2
- Phrases: grant attacker Confidentiality
- Suggested normal forms: grant attacker confidentiality
- Decision: accept (review_status: confirmed)

## grant attacker Confidentiality listening service with

- Cluster ID: `rc2_d1bfc1690b074018`
- Assertions: 2
- Phrases: grant attacker Confidentiality listening service with
- Suggested normal forms: grant attacker confidentiality listen service with
- Decision: accept (review_status: confirmed)

## grant themselves

- Cluster ID: `rc2_ce8c7c07aaf35852`
- Assertions: 2
- Phrases: grant themselves
- Suggested normal forms: grant themselve
- Decision: pending (review_status: pending)

## grant total control of

- Cluster ID: `rc2_8f4b0ccca4a08897`
- Assertions: 2
- Phrases: grant total control of
- Suggested normal forms: grant total control of
- Decision: accept (review_status: confirmed)

## had applied

- Cluster ID: `rc2_4bc968e78749c8a2`
- Assertions: 2
- Phrases: had applied, have applied
- Suggested normal forms: appli
- Decision: pending (review_status: pending)

## had obtained

- Cluster ID: `rc2_cf3c3437a865359b`
- Assertions: 2
- Phrases: had obtained, obtained
- Suggested normal forms: obtain
- Decision: pending (review_status: pending)

## happens after

- Cluster ID: `rc2_b0ff2661f8190545`
- Assertions: 2
- Phrases: happens after
- Suggested normal forms: happen after
- Decision: pending (review_status: pending)

## has MSRC exploitability assessment

- Cluster ID: `rc2_4446ff9c90b46540`
- Assertions: 2
- Phrases: has MSRC exploitability assessment
- Suggested normal forms: msrc exploitability assessment
- Decision: accept (review_status: confirmed)

## has MSRC exploited status

- Cluster ID: `rc2_ab699f5b36a31e88`
- Assertions: 2
- Phrases: has MSRC exploited status
- Suggested normal forms: msrc exploit statu
- Decision: accept (review_status: confirmed)

## has MSRC publicly disclosed status

- Cluster ID: `rc2_07f0b053621b74b9`
- Assertions: 2
- Phrases: has MSRC publicly disclosed status
- Suggested normal forms: msrc publicly disclos statu
- Decision: accept (review_status: confirmed)

## has advanced

- Cluster ID: `rc2_3db970a80ae23ab8`
- Assertions: 2
- Phrases: has advanced
- Suggested normal forms: advanc
- Decision: pending (review_status: pending)

## has advanced knowledge of target system

- Cluster ID: `rc2_114013f4d6641e9b`
- Assertions: 2
- Phrases: has advanced knowledge of target system
- Suggested normal forms: advanc knowledge of target system
- Decision: pending (review_status: pending)

## has allowed CISA to

- Cluster ID: `rc2_0bfc55597b35c95b`
- Assertions: 2
- Phrases: has allowed CISA to
- Suggested normal forms: allow cisa to
- Decision: accept (review_status: confirmed)

## has associated metric value in

- Cluster ID: `rc2_b88cb9765500b8e4`
- Assertions: 2
- Phrases: has associated metric value in
- Suggested normal forms: associat metric value in
- Decision: pending (review_status: pending)

## has been exploited in

- Cluster ID: `rc2_e95cd7f44ecd0f5d`
- Assertions: 2
- Phrases: has been exploited in, have been exploited in
- Suggested normal forms: been exploit in
- Decision: accept (review_status: confirmed)

## has been provided by

- Cluster ID: `rc2_84ebe74cb9c15c39`
- Assertions: 2
- Phrases: has been provided by
- Suggested normal forms: been provid by
- Decision: accept (review_status: confirmed)

## has been updated to allow for

- Cluster ID: `rc2_0123a8959691fffd`
- Assertions: 2
- Phrases: has been updated to allow for
- Suggested normal forms: been updat to allow for
- Decision: pending (review_status: pending)

## has concept of

- Cluster ID: `rc2_0205b96cfded4a4d`
- Assertions: 2
- Phrases: has concept of
- Suggested normal forms: concept of
- Decision: pending (review_status: pending)

## has own security authority

- Cluster ID: `rc2_47d7448b87fb8bd8`
- Assertions: 2
- Phrases: has own security authority
- Suggested normal forms: own security authority
- Decision: pending (review_status: pending)

## has tracked

- Cluster ID: `rc2_2bb8bf7259c4ea0e`
- Assertions: 2
- Phrases: has tracked, is tracking
- Suggested normal forms: track
- Decision: pending (review_status: pending)

## has use of

- Cluster ID: `rc2_fa45c4066a5d5886`
- Assertions: 2
- Phrases: has use of
- Suggested normal forms: use of
- Decision: accept (review_status: confirmed)

## has vulnerability reporting through

- Cluster ID: `rc2_1dc7ad7861ea0e26`
- Assertions: 2
- Phrases: has vulnerability reporting through
- Suggested normal forms: vulnerability report through
- Decision: accept (review_status: confirmed)

## have automated vulnerability reporting through

- Cluster ID: `rc2_6d1923a9fbdaee5a`
- Assertions: 2
- Phrases: have automated vulnerability reporting through
- Suggested normal forms: automat vulnerability report through
- Decision: accept (review_status: confirmed)

## have been published

- Cluster ID: `rc2_2ef789bd92c4855c`
- Assertions: 2
- Phrases: have been published
- Suggested normal forms: been publish
- Decision: pending (review_status: pending)

## have begun

- Cluster ID: `rc2_7bc6220d36ab0e42`
- Assertions: 2
- Phrases: have begun
- Suggested normal forms: begun
- Decision: accept (review_status: confirmed)

## have evidence of

- Cluster ID: `rc2_ef168731079a3499`
- Assertions: 2
- Phrases: have evidence of
- Suggested normal forms: evidence of
- Decision: accept (review_status: confirmed)

## have to be recalled for

- Cluster ID: `rc2_4d0f2c878bd87435`
- Assertions: 2
- Phrases: have to be recalled for
- Suggested normal forms: to be recall for
- Decision: accept (review_status: confirmed)

## having lower impact on embedding implementation assume

- Cluster ID: `rc2_d2fc97cfddd0c566`
- Assertions: 2
- Phrases: having lower impact on embedding implementation assume
- Suggested normal forms: hav lower impact on embedd implementation assume
- Decision: pending (review_status: pending)

## having lower impact on embedding implementation assume high privileges

- Cluster ID: `rc2_e2ef42cb2c1770c5`
- Assertions: 2
- Phrases: having lower impact on embedding implementation assume high privileges
- Suggested normal forms: hav lower impact on embedd implementation assume high privilege
- Decision: pending (review_status: pending)

## identified

- Cluster ID: `rc2_29881e4df0dd60f8`
- Assertions: 2
- Phrases: identified
- Suggested normal forms: identifi
- Decision: pending (review_status: pending)

## impact availability of

- Cluster ID: `rc2_880972606c65e76b`
- Assertions: 2
- Phrases: impact availability of
- Suggested normal forms: impact availability of
- Decision: accept (review_status: confirmed)

## implement token parsing for

- Cluster ID: `rc2_208e3d8ef8b4b368`
- Assertions: 2
- Phrases: implement token parsing for
- Suggested normal forms: implement token pars for
- Decision: accept (review_status: confirmed)

## implements own validation logic

- Cluster ID: `rc2_29f402e04ab34fa9`
- Assertions: 2
- Phrases: implements own validation logic, implements own validation logic in
- Suggested normal forms: implement own validation logic, implement own validation logic in
- Decision: pending (review_status: pending)

## include SQL like

- Cluster ID: `rc2_14fe223b663b055e`
- Assertions: 2
- Phrases: include SQL like
- Suggested normal forms: include sql like
- Decision: accept (review_status: confirmed)

## include presence of

- Cluster ID: `rc2_e6649451b2ae390e`
- Assertions: 2
- Phrases: include presence of
- Suggested normal forms: include presence of
- Decision: pending (review_status: pending)

## include same metric more than

- Cluster ID: `rc2_f981f7afac945784`
- Assertions: 2
- Phrases: include same metric more than
- Suggested normal forms: include same metric more than
- Decision: pending (review_status: pending)

## include standard services like

- Cluster ID: `rc2_1361e9d4a82ff915`
- Assertions: 2
- Phrases: include standard services like
- Suggested normal forms: include standard service like
- Decision: accept (review_status: confirmed)

## includes Claude Code for

- Cluster ID: `rc2_60272963491f6bf8`
- Assertions: 2
- Phrases: includes Claude Code for
- Suggested normal forms: include claude code for
- Decision: accept (review_status: confirmed)

## includes further discussion of CVSS guidelines on scoring

- Cluster ID: `rc2_c5f0263fa73396f3`
- Assertions: 2
- Phrases: includes further discussion of CVSS guidelines on scoring, includes further discussion of CVSS guidelines on scoring rubrics
- Suggested normal forms: include further discussion of cvs guideline on scor, include further discussion of cvs guideline on scor rubric
- Decision: accept (review_status: confirmed)

## includes service accounts embedded into

- Cluster ID: `rc2_1a5eb14885f48427`
- Assertions: 2
- Phrases: includes service accounts embedded into
- Suggested normal forms: include service account embedd into
- Decision: pending (review_status: pending)

## inform

- Cluster ID: `rc2_ea07dcc807ffe0d6`
- Assertions: 2
- Phrases: inform
- Suggested normal forms: inform
- Decision: pending (review_status: pending)

## introduces

- Cluster ID: `rc2_0fee7196f6817d6f`
- Assertions: 2
- Phrases: introduces
- Suggested normal forms: introduce
- Decision: accept (review_status: confirmed)

## is accessible to

- Cluster ID: `rc2_4256f696419fe3ad`
- Assertions: 2
- Phrases: is accessible to
- Suggested normal forms: accessible to
- Decision: accept (review_status: confirmed)

## is applied to

- Cluster ID: `rc2_e3ab29d3bb7f935a`
- Assertions: 2
- Phrases: is applied to
- Suggested normal forms: appli to
- Decision: pending (review_status: pending)

## is associated with

- Cluster ID: `rc2_dddf4df20ea1a265`
- Assertions: 2
- Phrases: is associated with
- Suggested normal forms: associat with
- Decision: pending (review_status: pending)

## is associated with attack

- Cluster ID: `rc2_f20ec81458c7fbea`
- Assertions: 2
- Phrases: is associated with attack
- Suggested normal forms: associat with attack
- Decision: pending (review_status: pending)

## is available as

- Cluster ID: `rc2_2ff5029378ca01a9`
- Assertions: 2
- Phrases: is available as
- Suggested normal forms: available a
- Decision: accept (review_status: confirmed)

## is based upon

- Cluster ID: `rc2_73f001dd4d39fb1d`
- Assertions: 2
- Phrases: is based upon
- Suggested normal forms: bas upon
- Decision: accept (review_status: confirmed)

## is bulletins from

- Cluster ID: `rc2_39bac66319a2fb86`
- Assertions: 2
- Phrases: is bulletins from
- Suggested normal forms: bulletin from
- Decision: pending (review_status: pending)

## is consistent across

- Cluster ID: `rc2_6d80bcd344d5565e`
- Assertions: 2
- Phrases: is consistent across
- Suggested normal forms: consistent acros
- Decision: accept (review_status: confirmed)

## is consistent with

- Cluster ID: `rc2_cdf50b628c891490`
- Assertions: 2
- Phrases: is consistent with
- Suggested normal forms: consistent with
- Decision: pending (review_status: pending)

## is defined as Yes regardless of

- Cluster ID: `rc2_80b7fd608c9ac6bd`
- Assertions: 2
- Phrases: is defined as Yes regardless of
- Suggested normal forms: defin a ye regardles of
- Decision: accept (review_status: confirmed)

## is derived from

- Cluster ID: `rc2_fbaf4b1936f8c872`
- Assertions: 2
- Phrases: is derived from
- Suggested normal forms: deriv from
- Decision: accept (review_status: confirmed)

## is designed to be used by

- Cluster ID: `rc2_e5641b6ac4a3e055`
- Assertions: 2
- Phrases: is designed to be used by, is designed to be used exclusively by
- Suggested normal forms: design to be us by, design to be us exclusively by
- Decision: pending (review_status: pending)

## is efficient than querying API per

- Cluster ID: `rc2_779862889189159b`
- Assertions: 2
- Phrases: is efficient than querying API per
- Suggested normal forms: efficient than query api per
- Decision: accept (review_status: confirmed)

## is encrypted at

- Cluster ID: `rc2_acc165d4a9d95072`
- Assertions: 2
- Phrases: is encrypted at
- Suggested normal forms: encrypt at
- Decision: pending (review_status: pending)

## is existence of

- Cluster ID: `rc2_3fef852f16ebadd2`
- Assertions: 2
- Phrases: is existence of
- Suggested normal forms: existence of
- Decision: pending (review_status: pending)

## is form of

- Cluster ID: `rc2_ad83d7671b99b16c`
- Assertions: 2
- Phrases: is form of
- Suggested normal forms: form of
- Decision: accept (review_status: confirmed)

## is important When

- Cluster ID: `rc2_ee2dfbbee7d1960b`
- Assertions: 2
- Phrases: is important When
- Suggested normal forms: important when
- Decision: accept (review_status: confirmed)

## is internet-exposed without

- Cluster ID: `rc2_e74f8e804bb7499f`
- Assertions: 2
- Phrases: is internet-exposed without
- Suggested normal forms: internet-expos without
- Decision: accept (review_status: confirmed)

## is known by someone other than

- Cluster ID: `rc2_e37224e294272621`
- Assertions: 2
- Phrases: is known by someone other than
- Suggested normal forms: known by someone other than
- Decision: pending (review_status: pending)

## is larger than

- Cluster ID: `rc2_a95aa96f841a1435`
- Assertions: 2
- Phrases: is larger than
- Suggested normal forms: larger than
- Decision: accept (review_status: confirmed)

## is larger than number of

- Cluster ID: `rc2_6b85093874ed059c`
- Assertions: 2
- Phrases: is larger than number of
- Suggested normal forms: larger than number of
- Decision: accept (review_status: confirmed)

## is maintained by

- Cluster ID: `rc2_f552b9bbf9daa241`
- Assertions: 2
- Phrases: is maintained by
- Suggested normal forms: maintain by
- Decision: pending (review_status: pending)

## is maintained by EPSS Special Interest Group at

- Cluster ID: `rc2_a8d68b2fd9f98413`
- Assertions: 2
- Phrases: is maintained by EPSS Special Interest Group at
- Suggested normal forms: maintain by eps special interest group at
- Decision: pending (review_status: pending)

## is notable autonomous process of

- Cluster ID: `rc2_783a8fb98a187703`
- Assertions: 2
- Phrases: is notable autonomous process of
- Suggested normal forms: notable autonomou proces of
- Decision: pending (review_status: pending)

## is notable while managing own autonomous process of

- Cluster ID: `rc2_ab82d2bebfedf1a1`
- Assertions: 2
- Phrases: is notable while managing own autonomous process of
- Suggested normal forms: notable while manag own autonomou proces of
- Decision: pending (review_status: pending)

## is other than

- Cluster ID: `rc2_53dd72d04e71d4a1`
- Assertions: 2
- Phrases: is other than
- Suggested normal forms: other than
- Decision: accept (review_status: confirmed)

## is proportional

- Cluster ID: `rc2_ee6474aa634fa43e`
- Assertions: 2
- Phrases: is proportional
- Suggested normal forms: proportional
- Decision: pending (review_status: pending)

## is proportional to

- Cluster ID: `rc2_f0ebfdc551e4a90e`
- Assertions: 2
- Phrases: is proportional to
- Suggested normal forms: proportional to
- Decision: pending (review_status: pending)

## is recommended to enrich

- Cluster ID: `rc2_d83aff1e98ad6969`
- Assertions: 2
- Phrases: is recommended to enrich
- Suggested normal forms: recommend to enrich
- Decision: accept (review_status: confirmed)

## is recommended to gather

- Cluster ID: `rc2_c5b40c36a66497f7`
- Assertions: 2
- Phrases: is recommended to gather
- Suggested normal forms: recommend to gather
- Decision: accept (review_status: confirmed)

## is resolved to

- Cluster ID: `rc2_ccac0e335163b58a`
- Assertions: 2
- Phrases: is resolved to
- Suggested normal forms: resolv to
- Decision: pending (review_status: pending)

## is resolved to user identity After

- Cluster ID: `rc2_55fd3c7565a1abae`
- Assertions: 2
- Phrases: is resolved to user identity After
- Suggested normal forms: resolv to user identity after
- Decision: pending (review_status: pending)

## is resolved to user identity via

- Cluster ID: `rc2_2a5203b4d69b7100`
- Assertions: 2
- Phrases: is resolved to user identity via
- Suggested normal forms: resolv to user identity via
- Decision: pending (review_status: pending)

## is responsibility

- Cluster ID: `rc2_c5f88e747d24a44c`
- Assertions: 2
- Phrases: is responsibility
- Suggested normal forms: responsibility
- Decision: pending (review_status: pending)

## is restricted On

- Cluster ID: `rc2_9816937728622499`
- Assertions: 2
- Phrases: is restricted On
- Suggested normal forms: restrict on
- Decision: pending (review_status: pending)

## is right mechanism for

- Cluster ID: `rc2_920908ddc64be63d`
- Assertions: 2
- Phrases: is right mechanism for
- Suggested normal forms: right mechanism for
- Decision: pending (review_status: pending)

## is shown in

- Cluster ID: `rc2_1bf1d3f83e0a545b`
- Assertions: 2
- Phrases: is shown in
- Suggested normal forms: shown in
- Decision: pending (review_status: pending)

## is successful in

- Cluster ID: `rc2_9c19b62dba5d1434`
- Assertions: 2
- Phrases: is successful in
- Suggested normal forms: successful in
- Decision: pending (review_status: pending)

## is to enrich value of

- Cluster ID: `rc2_9793b8aa5f598ad1`
- Assertions: 2
- Phrases: is to enrich value of
- Suggested normal forms: to enrich value of
- Decision: pending (review_status: pending)

## is to increase

- Cluster ID: `rc2_6b7014d0e77ab911`
- Assertions: 2
- Phrases: is to increase
- Suggested normal forms: to increase
- Decision: accept (review_status: confirmed)

## is to mitigate

- Cluster ID: `rc2_867b4eb3195305a7`
- Assertions: 2
- Phrases: is to mitigate
- Suggested normal forms: to mitigate
- Decision: accept (review_status: confirmed)

## is updated to reflect

- Cluster ID: `rc2_631d81ce110257ea`
- Assertions: 2
- Phrases: is updated to reflect
- Suggested normal forms: updat to reflect
- Decision: accept (review_status: confirmed)

## is used to record

- Cluster ID: `rc2_dd5999d53a524fea`
- Assertions: 2
- Phrases: is used to record
- Suggested normal forms: us to record
- Decision: accept (review_status: confirmed)

## is validated by

- Cluster ID: `rc2_632ee3648c76ff14`
- Assertions: 2
- Phrases: is validated by
- Suggested normal forms: validat by
- Decision: pending (review_status: pending)

## lack

- Cluster ID: `rc2_e3f315ea36abca8f`
- Assertions: 2
- Phrases: lack
- Suggested normal forms: lack
- Decision: accept (review_status: confirmed)

## lead to heap corruption

- Cluster ID: `rc2_453eda885008936a`
- Assertions: 2
- Phrases: lead to heap corruption
- Suggested normal forms: lead to heap corruption
- Decision: accept (review_status: confirmed)

## lead to unauthenticated remote code execution against vulnerable SharePoint server

- Cluster ID: `rc2_948431980828d395`
- Assertions: 2
- Phrases: lead to unauthenticated remote code execution against vulnerable SharePoint server
- Suggested normal forms: lead to unauthenticat remote code execution against vulnerable sharepoint server
- Decision: accept (review_status: confirmed)

## log out from

- Cluster ID: `rc2_96ffb5097b78bc19`
- Assertions: 2
- Phrases: log out from
- Suggested normal forms: log out from
- Decision: accept (review_status: confirmed)

## maintains gains write access After

- Cluster ID: `rc2_48cab2eaa52dcbcd`
- Assertions: 2
- Phrases: maintains gains write access After
- Suggested normal forms: maintain gain write acces after
- Decision: pending (review_status: pending)

## maintains page to enhance

- Cluster ID: `rc2_2edd926ae1b87a5d`
- Assertions: 2
- Phrases: maintains page to enhance
- Suggested normal forms: maintain page to enhance
- Decision: pending (review_status: pending)

## manage vast repositories of

- Cluster ID: `rc2_ee5aa62fa69e403d`
- Assertions: 2
- Phrases: manage vast repositories of
- Suggested normal forms: manage vast repository of
- Decision: pending (review_status: pending)

## mean from within

- Cluster ID: `rc2_fb854de15413b93a`
- Assertions: 2
- Phrases: mean from within
- Suggested normal forms: mean from within
- Decision: pending (review_status: pending)

## measure

- Cluster ID: `rc2_1501661682797862`
- Assertions: 2
- Phrases: measure, measures
- Suggested normal forms: measure
- Decision: accept (review_status: confirmed)

## meet to determine

- Cluster ID: `rc2_6aa4f0371042637c`
- Assertions: 2
- Phrases: meet to determine
- Suggested normal forms: meet to determine
- Decision: accept (review_status: confirmed)

## need

- Cluster ID: `rc2_cb58e4600bf0142c`
- Assertions: 2
- Phrases: need, needs
- Suggested normal forms: ne
- Decision: pending (review_status: pending)

## occur in

- Cluster ID: `rc2_34c0162587865531`
- Assertions: 2
- Phrases: occur in, occurs / / in
- Suggested normal forms: occur / / in, occur in
- Decision: pending (review_status: pending)

## occurs

- Cluster ID: `rc2_def696de03d9fc35`
- Assertions: 2
- Phrases: occurs
- Suggested normal forms: occur
- Decision: pending (review_status: pending)

## passes through device without

- Cluster ID: `rc2_02a0fa00336f9566`
- Assertions: 2
- Phrases: passes through device without
- Suggested normal forms: passe through device without
- Decision: pending (review_status: pending)

## perform

- Cluster ID: `rc2_fc6d1833bae465ef`
- Assertions: 2
- Phrases: perform, performs
- Suggested normal forms: perform
- Decision: accept (review_status: confirmed)

## perform system critical actions

- Cluster ID: `rc2_f1e64be72a5c9c22`
- Assertions: 2
- Phrases: perform system critical actions, perform system critical actions within
- Suggested normal forms: perform system critical action, perform system critical action within
- Decision: accept (review_status: confirmed)

## populates

- Cluster ID: `rc2_f1010f5da5aa80e2`
- Assertions: 2
- Phrases: populates
- Suggested normal forms: populate
- Decision: pending (review_status: pending)

## presents

- Cluster ID: `rc2_4d4c7eee2e28d03c`
- Assertions: 2
- Phrases: presents
- Suggested normal forms: present
- Decision: pending (review_status: pending)

## probed targets for

- Cluster ID: `rc2_bcf33f3038be1040`
- Assertions: 2
- Phrases: probed targets for
- Suggested normal forms: prob target for
- Decision: pending (review_status: pending)

## produce numeric score within

- Cluster ID: `rc2_362e84d218b605d3`
- Assertions: 2
- Phrases: produce numeric score within
- Suggested normal forms: produce numeric score within
- Decision: pending (review_status: pending)

## protect against post-exploitation activities

- Cluster ID: `rc2_798c8a2016d2fec2`
- Assertions: 2
- Phrases: protect against post-exploitation activities
- Suggested normal forms: protect against post-exploitation activity
- Decision: pending (review_status: pending)

## protect using multi-layer approach In

- Cluster ID: `rc2_9fe2abce006e29ba`
- Assertions: 2
- Phrases: protect using multi-layer approach In
- Suggested normal forms: protect us multi-layer approach in
- Decision: pending (review_status: pending)

## proved

- Cluster ID: `rc2_dd0c2c70261f6204`
- Assertions: 2
- Phrases: proved
- Suggested normal forms: prov
- Decision: pending (review_status: pending)

## provide functionality to

- Cluster ID: `rc2_d5b57e9a0b2f0c80`
- Assertions: 2
- Phrases: provide functionality to, provides functionality to
- Suggested normal forms: provide functionality to
- Decision: pending (review_status: pending)

## provides exploitability assessment for

- Cluster ID: `rc2_120a1466a137fb93`
- Assertions: 2
- Phrases: provides exploitability assessment for
- Suggested normal forms: provide exploitability assessment for
- Decision: pending (review_status: pending)

## provides exploitability assessment for vulnerability at time of

- Cluster ID: `rc2_d54d0dfe0b6256d3`
- Assertions: 2
- Phrases: provides exploitability assessment for vulnerability at time of
- Suggested normal forms: provide exploitability assessment for vulnerability at time of
- Decision: pending (review_status: pending)

## provides minimum information necessary to warn other users without informing attackers about

- Cluster ID: `rc2_9bb39d67835838db`
- Assertions: 2
- Phrases: provides minimum information necessary to warn other users without informing attackers about
- Suggested normal forms: provide minimum information necessary to warn other user without inform attacker about
- Decision: pending (review_status: pending)

## publish Qualitative Severity Ratings from

- Cluster ID: `rc2_977cb8a203af4c23`
- Assertions: 2
- Phrases: publish Qualitative Severity Ratings from
- Suggested normal forms: publish qualitative severity rat from
- Decision: pending (review_status: pending)

## publish Qualitative Severity Ratings in

- Cluster ID: `rc2_f9fdb634e313ea9e`
- Assertions: 2
- Phrases: publish Qualitative Severity Ratings in
- Suggested normal forms: publish qualitative severity rat in
- Decision: pending (review_status: pending)

## published to

- Cluster ID: `rc2_b5bd51d1e8aa8321`
- Assertions: 2
- Phrases: published to
- Suggested normal forms: publish to
- Decision: accept (review_status: confirmed)

## qualify as

- Cluster ID: `rc2_a37073823fd316a9`
- Assertions: 2
- Phrases: qualify as
- Suggested normal forms: qualify a
- Decision: pending (review_status: pending)

## read follow-up publication For

- Cluster ID: `rc2_39b36b15606649b7`
- Assertions: 2
- Phrases: read follow-up publication For
- Suggested normal forms: read follow-up publication for
- Decision: pending (review_status: pending)

## recommends remediating Track vulnerabilities within

- Cluster ID: `rc2_d46639d1f761cbc4`
- Assertions: 2
- Phrases: recommends remediating Track vulnerabilities within
- Suggested normal forms: recommend remediat track vulnerability within
- Decision: accept (review_status: confirmed)

## refers to loss of availability of impacted component itself such as networked service While

- Cluster ID: `rc2_b8a8d372bf8149ed`
- Assertions: 2
- Phrases: refers to loss of availability of impacted component itself such as networked service While, refers to loss of availability of impacted system itself such as networked service While
- Suggested normal forms: refer to los of availability of impact component itself such a network service while, refer to los of availability of impact system itself such a network service while
- Decision: pending (review_status: pending)

## reflect characteristics of thing As

- Cluster ID: `rc2_a1f18ab0b65b1fda`
- Assertions: 2
- Phrases: reflect characteristics of thing As
- Suggested normal forms: reflect characteristic of th a
- Decision: accept (review_status: confirmed)

## remain

- Cluster ID: `rc2_fc2b6c264e75e681`
- Assertions: 2
- Phrases: remain
- Suggested normal forms: remain
- Decision: accept (review_status: confirmed)

## report

- Cluster ID: `rc2_845e91831319e89c`
- Assertions: 2
- Phrases: report, reported
- Suggested normal forms: report
- Decision: pending (review_status: pending)

## require higher For

- Cluster ID: `rc2_1f5b580fec9ec043`
- Assertions: 2
- Phrases: require higher For
- Suggested normal forms: require higher for
- Decision: accept (review_status: confirmed)

## requires read-only permissions prior to being

- Cluster ID: `rc2_7ffc8295ad015863`
- Assertions: 2
- Phrases: requires read-only permissions prior to being
- Suggested normal forms: require read-only permission prior to be
- Decision: accept (review_status: confirmed)

## requires successful completion of prior exploits

- Cluster ID: `rc2_bf23274592c2167c`
- Assertions: 2
- Phrases: requires successful completion of prior exploits
- Suggested normal forms: require successful completion of prior exploit
- Decision: pending (review_status: pending)

## resides

- Cluster ID: `rc2_37dd149a2e88db1f`
- Assertions: 2
- Phrases: resides
- Suggested normal forms: reside
- Decision: accept (review_status: confirmed)

## resolved

- Cluster ID: `rc2_c31df101a9843c03`
- Assertions: 2
- Phrases: resolved
- Suggested normal forms: resolv
- Decision: pending (review_status: pending)

## resolves

- Cluster ID: `rc2_fdf09cdfc26cccf6`
- Assertions: 2
- Phrases: resolves
- Suggested normal forms: resolve
- Decision: accept (review_status: confirmed)

## restart

- Cluster ID: `rc2_3ace60b0a0c1b6c9`
- Assertions: 2
- Phrases: restart
- Suggested normal forms: restart
- Decision: pending (review_status: pending)

## restart events from

- Cluster ID: `rc2_bccbb1ca908fb77c`
- Assertions: 2
- Phrases: restart events from
- Suggested normal forms: restart event from
- Decision: accept (review_status: confirmed)

## result in injuries categorized as

- Cluster ID: `rc2_ba135647e3274735`
- Assertions: 2
- Phrases: result in injuries categorized as
- Suggested normal forms: result in injury categoriz a
- Decision: accept (review_status: confirmed)

## returns

- Cluster ID: `rc2_7187f0675eb38279`
- Assertions: 2
- Phrases: returns
- Suggested normal forms: return
- Decision: pending (review_status: pending)

## review

- Cluster ID: `rc2_c97ace4c8fef2cee`
- Assertions: 2
- Phrases: review, reviewed
- Suggested normal forms: review
- Decision: pending (review_status: pending)

## review Directive to account

- Cluster ID: `rc2_01496018e40f73ac`
- Assertions: 2
- Phrases: review Directive to account, review Directive to account update
- Suggested normal forms: review directive to account, review directive to account update
- Decision: pending (review_status: pending)

## saves starts vulnerable system in case

- Cluster ID: `rc2_b0ead0a77edd8b6d`
- Assertions: 2
- Phrases: saves starts vulnerable system in case
- Suggested normal forms: save start vulnerable system in case
- Decision: pending (review_status: pending)

## saves web browser

- Cluster ID: `rc2_87a5ab8e9970ae1c`
- Assertions: 2
- Phrases: saves web browser
- Suggested normal forms: save web browser
- Decision: pending (review_status: pending)

## send crafted packets to Windows machine with

- Cluster ID: `rc2_c225058f2478141d`
- Assertions: 2
- Phrases: send crafted packets to Windows machine with
- Suggested normal forms: send craft packet to window machine with
- Decision: accept (review_status: confirmed)

## send trivial crafted request to

- Cluster ID: `rc2_887566b7bd907ffe`
- Assertions: 2
- Phrases: send trivial crafted request to
- Suggested normal forms: send trivial craft request to
- Decision: accept (review_status: confirmed)

## sent

- Cluster ID: `rc2_7afbb3347fb7252e`
- Assertions: 2
- Phrases: sent
- Suggested normal forms: sent
- Decision: pending (review_status: pending)

## sent bulletin at

- Cluster ID: `rc2_0b2b82f26f267693`
- Assertions: 2
- Phrases: sent bulletin at
- Suggested normal forms: sent bulletin at
- Decision: pending (review_status: pending)

## sets Base Metric Attack Vector to

- Cluster ID: `rc2_f20db8640ffc51f2`
- Assertions: 2
- Phrases: sets Base Metric Attack Vector to
- Suggested normal forms: set base metric attack vector to
- Decision: pending (review_status: pending)

## showed

- Cluster ID: `rc2_1c6333509debf060`
- Assertions: 2
- Phrases: showed
- Suggested normal forms: show
- Decision: pending (review_status: pending)

## sit at boundary between

- Cluster ID: `rc2_d38382bb424fca7e`
- Assertions: 2
- Phrases: sit at boundary between
- Suggested normal forms: sit at boundary between
- Decision: pending (review_status: pending)

## started HTTP file server

- Cluster ID: `rc2_bcf8eb20e0063255`
- Assertions: 2
- Phrases: started HTTP file server, started HTTP file server from
- Suggested normal forms: start http file server, start http file server from
- Decision: pending (review_status: pending)

## started to connect to attacker-controlled infrastructure

- Cluster ID: `rc2_880e79199e456635`
- Assertions: 2
- Phrases: started to connect to attacker-controlled infrastructure, started to connect to attacker-controlled infrastructure on
- Suggested normal forms: start to connect to attacker-controll infrastructure, start to connect to attacker-controll infrastructure on
- Decision: pending (review_status: pending)

## subvert protections built into

- Cluster ID: `rc2_014f50beb1e2c953`
- Assertions: 2
- Phrases: subvert protections built into
- Suggested normal forms: subvert protection built into
- Decision: accept (review_status: confirmed)

## supplement Base Score with

- Cluster ID: `rc2_08a2a57dc5944876`
- Assertions: 2
- Phrases: supplement Base Score with
- Suggested normal forms: supplement base score with
- Decision: accept (review_status: confirmed)

## supports MEFs

- Cluster ID: `rc2_326ff1b94851d30c`
- Assertions: 2
- Phrases: supports MEFs
- Suggested normal forms: support mef
- Decision: accept (review_status: confirmed)

## supports organisations in

- Cluster ID: `rc2_88fc9c538ed964e4`
- Assertions: 2
- Phrases: supports organisations in
- Suggested normal forms: support organisation in
- Decision: accept (review_status: confirmed)

## sustained over

- Cluster ID: `rc2_bfc167500f5e20f6`
- Assertions: 2
- Phrases: sustained over
- Suggested normal forms: sustain over
- Decision: accept (review_status: confirmed)

## take action

- Cluster ID: `rc2_fbb4485b6366df15`
- Assertions: 2
- Phrases: take action
- Suggested normal forms: take action
- Decision: accept (review_status: confirmed)

## take action to

- Cluster ID: `rc2_6e7b09459d5c5217`
- Assertions: 2
- Phrases: take action to
- Suggested normal forms: take action to
- Decision: accept (review_status: confirmed)

## take precedence

- Cluster ID: `rc2_ae0159569ed25a69`
- Assertions: 2
- Phrases: take precedence
- Suggested normal forms: take precedence
- Decision: accept (review_status: confirmed)

## take precedence CVSS provided by

- Cluster ID: `rc2_ed47fec99f15b265`
- Assertions: 2
- Phrases: take precedence CVSS provided by
- Suggested normal forms: take precedence cvs provid by
- Decision: pending (review_status: pending)

## treat

- Cluster ID: `rc2_a5075550e1f2376f`
- Assertions: 2
- Phrases: treat
- Suggested normal forms: treat
- Decision: accept (review_status: confirmed)

## treat infrastructure component as

- Cluster ID: `rc2_d4e3dc6d65036628`
- Assertions: 2
- Phrases: treat infrastructure component as, treat infrastructure components as
- Suggested normal forms: treat infrastructure component a
- Decision: accept (review_status: confirmed)

## trigger out-of-bounds read

- Cluster ID: `rc2_246619c00b9cde68`
- Assertions: 2
- Phrases: trigger out-of-bounds read
- Suggested normal forms: trigger out-of-bound read
- Decision: pending (review_status: pending)

## undermine

- Cluster ID: `rc2_5d13e04fd93bd7d1`
- Assertions: 2
- Phrases: undermine
- Suggested normal forms: undermine
- Decision: pending (review_status: pending)

## use CVSS information as

- Cluster ID: `rc2_b63665ef18e313cb`
- Assertions: 2
- Phrases: use CVSS information as
- Suggested normal forms: use cvs information a
- Decision: accept (review_status: confirmed)

## use access for

- Cluster ID: `rc2_21df440136e78d99`
- Assertions: 2
- Phrases: use access for
- Suggested normal forms: use acces for
- Decision: accept (review_status: confirmed)

## use forged JWT along with

- Cluster ID: `rc2_c41677a8c4ae8820`
- Assertions: 2
- Phrases: use forged JWT along with
- Suggested normal forms: use forg jwt along with
- Decision: pending (review_status: pending)

## use multiple overlapping systems to determine whether

- Cluster ID: `rc2_e9f5daa145526044`
- Assertions: 2
- Phrases: use multiple overlapping systems to determine whether
- Suggested normal forms: use multiple overlapp system to determine whether
- Decision: pending (review_status: pending)

## use type instantiation to instantiate

- Cluster ID: `rc2_5dcb8d2280b6e5a4`
- Assertions: 2
- Phrases: use type instantiation to instantiate
- Suggested normal forms: use type instantiation to instantiate
- Decision: pending (review_status: pending)

## use type instantiation to instantiate class with

- Cluster ID: `rc2_cf5fef26f245a0bd`
- Assertions: 2
- Phrases: use type instantiation to instantiate class with
- Suggested normal forms: use type instantiation to instantiate clas with
- Decision: pending (review_status: pending)

## used sprint along with different workflows reason across

- Cluster ID: `rc2_d10e1ec005dce545`
- Assertions: 2
- Phrases: used sprint along with different workflows reason across
- Suggested normal forms: us sprint along with different workflow reason acros
- Decision: pending (review_status: pending)

## used sprint reason across

- Cluster ID: `rc2_0408652e01d54707`
- Assertions: 2
- Phrases: used sprint reason across
- Suggested normal forms: us sprint reason acros
- Decision: pending (review_status: pending)

## used sprint to

- Cluster ID: `rc2_ece11527f7688d96`
- Assertions: 2
- Phrases: used sprint to
- Suggested normal forms: us sprint to
- Decision: pending (review_status: pending)

## used sprint to experiment reason across

- Cluster ID: `rc2_bc24ee3ba9e33c72`
- Assertions: 2
- Phrases: used sprint to experiment reason across
- Suggested normal forms: us sprint to experiment reason acros
- Decision: pending (review_status: pending)

## used this for

- Cluster ID: `rc2_1978b9551f69f8a3`
- Assertions: 2
- Phrases: used this for
- Suggested normal forms: us thi for
- Decision: accept (review_status: confirmed)

## warned

- Cluster ID: `rc2_aa63925edf225e26`
- Assertions: 2
- Phrases: warned
- Suggested normal forms: warn
- Decision: pending (review_status: pending)

## warrant further reductions in

- Cluster ID: `rc2_3502380ae4d2db46`
- Assertions: 2
- Phrases: warrant further reductions in
- Suggested normal forms: warrant further reduction in
- Decision: accept (review_status: confirmed)

## was developed as entry for

- Cluster ID: `rc2_ec1992641027d48d`
- Assertions: 2
- Phrases: was developed as entry for
- Suggested normal forms: develop a entry for
- Decision: accept (review_status: confirmed)

## was disclosed by

- Cluster ID: `rc2_62bdacd6ea2173ba`
- Assertions: 2
- Phrases: was disclosed by
- Suggested normal forms: disclos by
- Decision: pending (review_status: pending)

## was discovered by Senior Principal Security Researcher at

- Cluster ID: `rc2_d637d93d976e4e1b`
- Assertions: 2
- Phrases: was discovered by Senior Principal Security Researcher at
- Suggested normal forms: discover by senior principal security researcher at
- Decision: accept (review_status: confirmed)

## were built for For

- Cluster ID: `rc2_73eceb17a27c3c96`
- Assertions: 2
- Phrases: were built for For
- Suggested normal forms: built for for
- Decision: accept (review_status: confirmed)

## with high privileges assume high privileges while assessing vulnerability in

- Cluster ID: `rc2_b7851b373c6c2f89`
- Assertions: 2
- Phrases: with high privileges assume high privileges while assessing vulnerability in
- Suggested normal forms: with high privilege assume high privilege while assess vulnerability in
- Decision: pending (review_status: pending)

## work For

- Cluster ID: `rc2_77cf9d5aee071b56`
- Assertions: 2
- Phrases: work For
- Suggested normal forms: work for
- Decision: pending (review_status: pending)

## worked in 2020 to develop

- Cluster ID: `rc2_66d96e5cd40459d7`
- Assertions: 2
- Phrases: worked in 2020 to develop
- Suggested normal forms: work in 2020 to develop
- Decision: accept (review_status: confirmed)

## worked to develop

- Cluster ID: `rc2_47e6b74ff4c08057`
- Assertions: 2
- Phrases: worked to develop
- Suggested normal forms: work to develop
- Decision: accept (review_status: confirmed)

## worked with SEI to develop

- Cluster ID: `rc2_23c2d2b64feecdfb`
- Assertions: 2
- Phrases: worked with SEI to develop
- Suggested normal forms: work with sei to develop
- Decision: accept (review_status: confirmed)

## wrote

- Cluster ID: `rc2_5a3365e9b3ecf3ea`
- Assertions: 2
- Phrases: wrote
- Suggested normal forms: wrote
- Decision: pending (review_status: pending)

## 's familiar to

- Cluster ID: `rc2_1dac1df50823e29f`
- Assertions: 1
- Phrases: 's familiar to
- Suggested normal forms: 's familiar to
- Decision: accept (review_status: confirmed)

## Are aware of exploited vulnerability included in

- Cluster ID: `rc2_c4778d8ca5bea033`
- Assertions: 1
- Phrases: Are aware of exploited vulnerability included in
- Suggested normal forms: aware of exploit vulnerability includ in
- Decision: accept (review_status: confirmed)

## Based on Risk to support

- Cluster ID: `rc2_dbd845066949c6e0`
- Assertions: 1
- Phrases: Based on Risk to support
- Suggested normal forms: bas on risk to support
- Decision: accept (review_status: confirmed)

## Based on Risk to support agencies in

- Cluster ID: `rc2_548bd6a9f161dbbe`
- Assertions: 1
- Phrases: Based on Risk to support agencies in
- Suggested normal forms: bas on risk to support agency in
- Decision: pending (review_status: pending)

## Based to support

- Cluster ID: `rc2_252389803a84aed6`
- Assertions: 1
- Phrases: Based to support
- Suggested normal forms: bas to support
- Decision: accept (review_status: confirmed)

## Based to support agencies in

- Cluster ID: `rc2_2d311c89f14b0fb3`
- Assertions: 1
- Phrases: Based to support agencies in
- Suggested normal forms: bas to support agency in
- Decision: pending (review_status: pending)

## CISA has added flaw

- Cluster ID: `rc2_a3e779ab09f5bccc`
- Assertions: 1
- Phrases: CISA has added flaw
- Suggested normal forms: cisa add flaw
- Decision: accept (review_status: confirmed)

## CISA has added flaw flag as

- Cluster ID: `rc2_03c5f11eb95d3282`
- Assertions: 1
- Phrases: CISA has added flaw flag as
- Suggested normal forms: cisa add flaw flag a
- Decision: accept (review_status: confirmed)

## CISA has added flaw to catalog of

- Cluster ID: `rc2_ed29e9dbee64485f`
- Assertions: 1
- Phrases: CISA has added flaw to catalog of
- Suggested normal forms: cisa add flaw to catalog of
- Decision: accept (review_status: confirmed)

## Cybersecurity arrives at

- Cluster ID: `rc2_8a449b9c1e510f10`
- Assertions: 1
- Phrases: Cybersecurity arrives at
- Suggested normal forms: cybersecurity arrive at
- Decision: pending (review_status: pending)

## Cybersecurity arrives at moment

- Cluster ID: `rc2_97dffdaaca9eaf38`
- Assertions: 1
- Phrases: Cybersecurity arrives at moment
- Suggested normal forms: cybersecurity arrive at moment
- Decision: accept (review_status: confirmed)

## Fix

- Cluster ID: `rc2_1c6e6c4c02e55178`
- Assertions: 1
- Phrases: Fix
- Suggested normal forms: fix
- Decision: pending (review_status: pending)

## Handles

- Cluster ID: `rc2_c2a116aa910d147b`
- Assertions: 1
- Phrases: Handles
- Suggested normal forms: handle
- Decision: accept (review_status: confirmed)

## Hit

- Cluster ID: `rc2_63d04dee7c50f6fb`
- Assertions: 1
- Phrases: Hit
- Suggested normal forms: hit
- Decision: pending (review_status: pending)

## Is vulnerability on

- Cluster ID: `rc2_8a8d821864d59b8c`
- Assertions: 1
- Phrases: Is vulnerability on
- Suggested normal forms: vulnerability on
- Decision: accept (review_status: confirmed)

## It is which parts of infrastructure have been treated as outside

- Cluster ID: `rc2_429864f2176dc81f`
- Assertions: 1
- Phrases: It is which parts of infrastructure have been treated as outside
- Suggested normal forms: it which part of infrastructure been treat a outside
- Decision: pending (review_status: pending)

## Lets

- Cluster ID: `rc2_5654d4106d7025c2`
- Assertions: 1
- Phrases: Lets
- Suggested normal forms: let
- Decision: accept (review_status: confirmed)

## NET type achieved

- Cluster ID: `rc2_ff88487258ea80cf`
- Assertions: 1
- Phrases: NET type achieved
- Suggested normal forms: net type achiev
- Decision: accept (review_status: confirmed)

## Name

- Cluster ID: `rc2_82a3537ff0dbce7e`
- Assertions: 1
- Phrases: Name
- Suggested normal forms: name
- Decision: accept (review_status: confirmed)

## Print

- Cluster ID: `rc2_ce953a0eb0824661`
- Assertions: 1
- Phrases: Print
- Suggested normal forms: print
- Decision: pending (review_status: pending)

## Text

- Cluster ID: `rc2_982d9e3eb996f559`
- Assertions: 1
- Phrases: Text
- Suggested normal forms: text
- Decision: accept (review_status: confirmed)

## Wanted for

- Cluster ID: `rc2_aa7f1d4d7bca6645`
- Assertions: 1
- Phrases: Wanted for
- Suggested normal forms: want for
- Decision: pending (review_status: pending)

## accept images from

- Cluster ID: `rc2_d887acbe69e8b6bf`
- Assertions: 1
- Phrases: accept images from
- Suggested normal forms: accept image from
- Decision: accept (review_status: confirmed)

## accept images over

- Cluster ID: `rc2_e72ee98a16a0f95f`
- Assertions: 1
- Phrases: accept images over
- Suggested normal forms: accept image over
- Decision: pending (review_status: pending)

## accepts issuer

- Cluster ID: `rc2_18ac0c8e561d692b`
- Assertions: 1
- Phrases: accepts issuer
- Suggested normal forms: accept issuer
- Decision: accept (review_status: confirmed)

## accepts that as

- Cluster ID: `rc2_656e43429ee277d3`
- Assertions: 1
- Phrases: accepts that as
- Suggested normal forms: accept that a
- Decision: accept (review_status: confirmed)

## accepts tokens signed by

- Cluster ID: `rc2_c32f4c973937429c`
- Assertions: 1
- Phrases: accepts tokens signed by
- Suggested normal forms: accept token sign by
- Decision: accept (review_status: confirmed)

## accepts tokens with

- Cluster ID: `rc2_ba2c535fe0da30b8`
- Assertions: 1
- Phrases: accepts tokens with
- Suggested normal forms: accept token with
- Decision: accept (review_status: confirmed)

## access certain restricted objects/resources in

- Cluster ID: `rc2_abd84cf92125b90f`
- Assertions: 1
- Phrases: access certain restricted objects/resources in
- Suggested normal forms: acces certain restrict object/resource in
- Decision: pending (review_status: pending)

## access resources that they be able to access By exploiting vulnerability in

- Cluster ID: `rc2_5cdb8c1c4b0ecb04`
- Assertions: 1
- Phrases: access resources that they be able to access By exploiting vulnerability in
- Suggested normal forms: acces resource that they be able to acces by exploit vulnerability in
- Decision: pending (review_status: pending)

## access resources that they be able to access such as

- Cluster ID: `rc2_196fb3c382a5042f`
- Assertions: 1
- Phrases: access resources that they be able to access such as
- Suggested normal forms: acces resource that they be able to acces such a
- Decision: pending (review_status: pending)

## accessed DeepSeek directly through

- Cluster ID: `rc2_80535af280ab700c`
- Assertions: 1
- Phrases: accessed DeepSeek directly through
- Suggested normal forms: access deepseek directly through
- Decision: pending (review_status: pending)

## accessed Qwen directly through

- Cluster ID: `rc2_07121b82a6e7f75d`
- Assertions: 1
- Phrases: accessed Qwen directly through
- Suggested normal forms: access qwen directly through
- Decision: pending (review_status: pending)

## account for this when

- Cluster ID: `rc2_c2ddd5ec3378a245`
- Assertions: 1
- Phrases: account for this when
- Suggested normal forms: account for thi when
- Decision: pending (review_status: pending)

## achieve

- Cluster ID: `rc2_1c6b6b9e01275af3`
- Assertions: 1
- Phrases: achieve
- Suggested normal forms: achieve
- Decision: accept (review_status: confirmed)

## acts

- Cluster ID: `rc2_f83f07be16e27018`
- Assertions: 1
- Phrases: acts
- Suggested normal forms: act
- Decision: pending (review_status: pending)

## acts as consulting body

- Cluster ID: `rc2_e0ee8167b59ffb3d`
- Assertions: 1
- Phrases: acts as consulting body
- Suggested normal forms: act a consult body
- Decision: pending (review_status: pending)

## add metrics on

- Cluster ID: `rc2_b3a9c8abb3cb2edc`
- Assertions: 1
- Phrases: add metrics on
- Suggested normal forms: add metric on
- Decision: pending (review_status: pending)

## add metrics to

- Cluster ID: `rc2_e447cc1da8627e08`
- Assertions: 1
- Phrases: add metrics to
- Suggested normal forms: add metric to
- Decision: pending (review_status: pending)

## added CVE-2026-55040 with remediation deadline of

- Cluster ID: `rc2_fd3a8a27c4c1e2bd`
- Assertions: 1
- Phrases: added CVE-2026-55040 with remediation deadline of
- Suggested normal forms: add cve-2026-55040 with remediation deadline of
- Decision: accept (review_status: confirmed)

## added CVE-2026-59310 on

- Cluster ID: `rc2_9bc69ebca5e657f3`
- Assertions: 1
- Phrases: added CVE-2026-59310 on
- Suggested normal forms: add cve-2026-59310 on
- Decision: pending (review_status: pending)

## added CVE-2026-59310 to

- Cluster ID: `rc2_133a410ea2074705`
- Assertions: 1
- Phrases: added CVE-2026-59310 to
- Suggested normal forms: add cve-2026-59310 to
- Decision: pending (review_status: pending)

## added CVE-2026-65400 on

- Cluster ID: `rc2_ae31dbf3e0d717d3`
- Assertions: 1
- Phrases: added CVE-2026-65400 on
- Suggested normal forms: add cve-2026-65400 on
- Decision: pending (review_status: pending)

## added CVE-2026-65400 to

- Cluster ID: `rc2_5fde4854260cab02`
- Assertions: 1
- Phrases: added CVE-2026-65400 to
- Suggested normal forms: add cve-2026-65400 to
- Decision: pending (review_status: pending)

## added to IKE Protocol including authentication

- Cluster ID: `rc2_ce8884ff2434fb97`
- Assertions: 1
- Phrases: added to IKE Protocol including authentication
- Suggested normal forms: add to ike protocol includ authentication
- Decision: accept (review_status: confirmed)

## added via easier interoperability with non-Internet Protocol Security

- Cluster ID: `rc2_1907f2ffd8b87401`
- Assertions: 1
- Phrases: added via easier interoperability with non-Internet Protocol Security
- Suggested normal forms: add via easier interoperability with non-internet protocol security
- Decision: accept (review_status: confirmed)

## added via generated addresses

- Cluster ID: `rc2_b1ec61c38d26374d`
- Assertions: 1
- Phrases: added via generated addresses
- Suggested normal forms: add via generat addresse
- Decision: accept (review_status: confirmed)

## added vulnerability to Known Exploited Vulnerabilities catalogue

- Cluster ID: `rc2_e5d31d8db644be31`
- Assertions: 1
- Phrases: added vulnerability to Known Exploited Vulnerabilities catalogue
- Suggested normal forms: add vulnerability to known exploit vulnerability catalogue
- Decision: pending (review_status: pending)

## addressed CVE-2026-33824 in

- Cluster ID: `rc2_772142dd6ca0fb2f`
- Assertions: 1
- Phrases: addressed CVE-2026-33824 in
- Suggested normal forms: address cve-2026-33824 in
- Decision: pending (review_status: pending)

## adjust Base to

- Cluster ID: `rc2_828ccd4e99380099`
- Assertions: 1
- Phrases: adjust Base to
- Suggested normal forms: adjust base to
- Decision: accept (review_status: confirmed)

## adjust Temporal severities to

- Cluster ID: `rc2_4da3e19c701c7e2a`
- Assertions: 1
- Phrases: adjust Temporal severities to
- Suggested normal forms: adjust temporal severity to
- Decision: accept (review_status: confirmed)

## adjusts scores of vectors within

- Cluster ID: `rc2_ea237a933e1913d7`
- Assertions: 1
- Phrases: adjusts scores of vectors within
- Suggested normal forms: adjust score of vector within
- Decision: accept (review_status: confirmed)

## adjusts scores of vectors within qualitatively equivalent set of

- Cluster ID: `rc2_c1add7fb1254539e`
- Assertions: 1
- Phrases: adjusts scores of vectors within qualitatively equivalent set of
- Suggested normal forms: adjust score of vector within qualitatively equivalent set of
- Decision: accept (review_status: confirmed)

## advised

- Cluster ID: `rc2_41ef84ab9a7985e2`
- Assertions: 1
- Phrases: advised
- Suggested normal forms: advis
- Decision: accept (review_status: confirmed)

## af te dwingen en

- Cluster ID: `rc2_603ca12339531b2d`
- Assertions: 1
- Phrases: af te dwingen en
- Suggested normal forms: af te dwingen en
- Decision: pending (review_status: pending)

## affect data used by

- Cluster ID: `rc2_2e1a870b14031374`
- Assertions: 1
- Phrases: affect data used by
- Suggested normal forms: affect data us by
- Decision: pending (review_status: pending)

## affects primary availability of

- Cluster ID: `rc2_04f0b42c21307921`
- Assertions: 1
- Phrases: affects primary availability of
- Suggested normal forms: affect primary availability of
- Decision: accept (review_status: confirmed)

## affects wide range of

- Cluster ID: `rc2_c35feed2505670df`
- Assertions: 1
- Phrases: affects wide range of
- Suggested normal forms: affect wide range of
- Decision: accept (review_status: confirmed)

## affects wide range of supported Windows platforms including Windows Server 2016 through to

- Cluster ID: `rc2_c627114e4bbc1693`
- Assertions: 1
- Phrases: affects wide range of supported Windows platforms including Windows Server 2016 through to
- Suggested normal forms: affect wide range of support window platform includ window server 2016 through to
- Decision: accept (review_status: confirmed)

## agreed upon with

- Cluster ID: `rc2_fccb2c84a03df327`
- Assertions: 1
- Phrases: agreed upon with
- Suggested normal forms: agre upon with
- Decision: accept (review_status: confirmed)

## agreed with

- Cluster ID: `rc2_e3f8e4bf0a9f0879`
- Assertions: 1
- Phrases: agreed with
- Suggested normal forms: agre with
- Decision: pending (review_status: pending)

## align to

- Cluster ID: `rc2_85cc6f4f50715582`
- Assertions: 1
- Phrases: align to
- Suggested normal forms: align to
- Decision: accept (review_status: confirmed)

## allow attacker on network to authenticate to Screen Sharing without

- Cluster ID: `rc2_77b0e42efcfba2d8`
- Assertions: 1
- Phrases: allow attacker on network to authenticate to Screen Sharing without
- Suggested normal forms: allow attacker on network to authenticate to screen shar without
- Decision: pending (review_status: pending)

## allow threat actor with

- Cluster ID: `rc2_30373c9f3d168ae2`
- Assertions: 1
- Phrases: allow threat actor with
- Suggested normal forms: allow threat actor with
- Decision: accept (review_status: confirmed)

## allowed attacker to maintain

- Cluster ID: `rc2_c6707b7683a981b8`
- Assertions: 1
- Phrases: allowed attacker to maintain
- Suggested normal forms: allow attacker to maintain
- Decision: accept (review_status: confirmed)

## allowed attacker to maintain outbound control channel from

- Cluster ID: `rc2_bf93d1008096d6df`
- Assertions: 1
- Phrases: allowed attacker to maintain outbound control channel from
- Suggested normal forms: allow attacker to maintain outbound control channel from
- Decision: accept (review_status: confirmed)

## allows attacker to compromise other files on

- Cluster ID: `rc2_4539dba4cdaa2051`
- Assertions: 1
- Phrases: allows attacker to compromise other files on
- Suggested normal forms: allow attacker to compromise other file on
- Decision: accept (review_status: confirmed)

## allows attacker to execute arbitrary code on

- Cluster ID: `rc2_83899edcb3aab836`
- Assertions: 1
- Phrases: allows attacker to execute arbitrary code on
- Suggested normal forms: allow attacker to execute arbitrary code on
- Decision: pending (review_status: pending)

## allows attackers to affect

- Cluster ID: `rc2_bf14c8e95b262ebc`
- Assertions: 1
- Phrases: allows attackers to affect
- Suggested normal forms: allow attacker to affect
- Decision: pending (review_status: pending)

## allows attackers to affect resources outside

- Cluster ID: `rc2_7eda9b75ff1ecb3e`
- Assertions: 1
- Phrases: allows attackers to affect resources outside
- Suggested normal forms: allow attacker to affect resource outside
- Decision: pending (review_status: pending)

## allows attackers without

- Cluster ID: `rc2_875e29ca7e0e5dea`
- Assertions: 1
- Phrases: allows attackers without
- Suggested normal forms: allow attacker without
- Decision: pending (review_status: pending)

## allows constructing gadget chain Combined with

- Cluster ID: `rc2_bb75650c8a5baadc`
- Assertions: 1
- Phrases: allows constructing gadget chain Combined with
- Suggested normal forms: allow construct gadget chain combin with
- Decision: pending (review_status: pending)

## allows for unauthenticated RCE against

- Cluster ID: `rc2_fc1f66b0b3a8cb6a`
- Assertions: 1
- Phrases: allows for unauthenticated RCE against
- Suggested normal forms: allow for unauthenticat rce against
- Decision: pending (review_status: pending)

## allows other processes to impact availability in

- Cluster ID: `rc2_8203bf0f249e47fa`
- Assertions: 1
- Phrases: allows other processes to impact availability in
- Suggested normal forms: allow other processe to impact availability in
- Decision: pending (review_status: pending)

## allows other processes to impact integrity in

- Cluster ID: `rc2_8ed7ed974b266e88`
- Assertions: 1
- Phrases: allows other processes to impact integrity in
- Suggested normal forms: allow other processe to impact integrity in
- Decision: pending (review_status: pending)

## allows users

- Cluster ID: `rc2_96205b20835adda0`
- Assertions: 1
- Phrases: allows users
- Suggested normal forms: allow user
- Decision: pending (review_status: pending)

## allows users to

- Cluster ID: `rc2_7d8c8320bf9c2482`
- Assertions: 1
- Phrases: allows users to
- Suggested normal forms: allow user to
- Decision: pending (review_status: pending)

## allows users to export

- Cluster ID: `rc2_3ded4b6bda469302`
- Assertions: 1
- Phrases: allows users to export
- Suggested normal forms: allow user to export
- Decision: accept (review_status: confirmed)

## allows users to read files only under

- Cluster ID: `rc2_8a4a51d9ffd88222`
- Assertions: 1
- Phrases: allows users to read files only under
- Suggested normal forms: allow user to read file only under
- Decision: pending (review_status: pending)

## allows users to read web pages only under

- Cluster ID: `rc2_8a52d1956e208025`
- Assertions: 1
- Phrases: allows users to read web pages only under
- Suggested normal forms: allow user to read web page only under
- Decision: pending (review_status: pending)

## appeared to be working at

- Cluster ID: `rc2_af87faeb3b1748cc`
- Assertions: 1
- Phrases: appeared to be working at
- Suggested normal forms: appear to be work at
- Decision: pending (review_status: pending)

## appeared to be working at first When

- Cluster ID: `rc2_3429236532ad803b`
- Assertions: 1
- Phrases: appeared to be working at first When
- Suggested normal forms: appear to be work at first when
- Decision: pending (review_status: pending)

## applies additional validation Starting with

- Cluster ID: `rc2_fcbe9e5975449073`
- Assertions: 1
- Phrases: applies additional validation Starting with
- Suggested normal forms: apply additional validation start with
- Decision: accept (review_status: confirmed)

## applies as Federal Civilian Executive Branch systems

- Cluster ID: `rc2_603e342710cf0077`
- Assertions: 1
- Phrases: applies as Federal Civilian Executive Branch systems
- Suggested normal forms: apply a federal civilian executive branch system
- Decision: accept (review_status: confirmed)

## applies to court in

- Cluster ID: `rc2_fb12d6e50d2078a9`
- Assertions: 1
- Phrases: applies to court in
- Suggested normal forms: apply to court in
- Decision: accept (review_status: confirmed)

## approved by

- Cluster ID: `rc2_7033f273285337fd`
- Assertions: 1
- Phrases: approved by
- Suggested normal forms: approv by
- Decision: accept (review_status: confirmed)

## approved by CVE Board as scope of

- Cluster ID: `rc2_8bfd1aa6919a6539`
- Assertions: 1
- Phrases: approved by CVE Board as scope of
- Suggested normal forms: approv by cve board a scope of
- Decision: pending (review_status: pending)

## are Subsequent Systems

- Cluster ID: `rc2_c5c878601afbd67c`
- Assertions: 1
- Phrases: are Subsequent Systems
- Suggested normal forms: subsequent system
- Decision: pending (review_status: pending)

## are advisories from

- Cluster ID: `rc2_0f60228541dfa742`
- Assertions: 1
- Phrases: are advisories from
- Suggested normal forms: advisory from
- Decision: pending (review_status: pending)

## are aid to scoring

- Cluster ID: `rc2_f56bcc9a21754c22`
- Assertions: 1
- Phrases: are aid to scoring
- Suggested normal forms: aid to scor
- Decision: accept (review_status: confirmed)

## are available back to

- Cluster ID: `rc2_0ad262f48de4e42c`
- Assertions: 1
- Phrases: are available back to
- Suggested normal forms: available back to
- Decision: pending (review_status: pending)

## are available for Cortex XSIAM/XDR/Cloud customers with

- Cluster ID: `rc2_13354a1e62e1fd75`
- Assertions: 1
- Phrases: are available for Cortex XSIAM/XDR/Cloud customers with
- Suggested normal forms: available for cortex xsiam/xdr/cloud customer with
- Decision: pending (review_status: pending)

## are blocked to provide additional protection against

- Cluster ID: `rc2_127d978468d3602e`
- Assertions: 1
- Phrases: are blocked to provide additional protection against
- Suggested normal forms: block to provide additional protection against
- Decision: accept (review_status: confirmed)

## are building

- Cluster ID: `rc2_44575cf5b28512d7`
- Assertions: 1
- Phrases: are building
- Suggested normal forms: build
- Decision: accept (review_status: confirmed)

## are captured in

- Cluster ID: `rc2_8c365bbfa0b97b3d`
- Assertions: 1
- Phrases: are captured in
- Suggested normal forms: captur in
- Decision: pending (review_status: pending)

## are combined which to form

- Cluster ID: `rc2_380554f8043114d1`
- Assertions: 1
- Phrases: are combined which to form
- Suggested normal forms: combin which to form
- Decision: accept (review_status: confirmed)

## are competing in

- Cluster ID: `rc2_d82f4501ba7fdd63`
- Assertions: 1
- Phrases: are competing in
- Suggested normal forms: compet in
- Decision: pending (review_status: pending)

## are considered as system of interest for scoring

- Cluster ID: `rc2_5b42c13dc0edb1d0`
- Assertions: 1
- Phrases: are considered as system of interest for scoring
- Suggested normal forms: consider a system of interest for scor
- Decision: pending (review_status: pending)

## are considered constituent elements of

- Cluster ID: `rc2_7b53c6fa82f8a37e`
- Assertions: 1
- Phrases: are considered constituent elements of
- Suggested normal forms: consider constituent element of
- Decision: pending (review_status: pending)

## are constructing

- Cluster ID: `rc2_b252d4eb5acf5aea`
- Assertions: 1
- Phrases: are constructing
- Suggested normal forms: construct
- Decision: accept (review_status: confirmed)

## are constructing persistent AI offensive infrastructure Rather than using AI tools in

- Cluster ID: `rc2_0aca014425756d82`
- Assertions: 1
- Phrases: are constructing persistent AI offensive infrastructure Rather than using AI tools in
- Suggested normal forms: construct persistent ai offensive infrastructure rather than us ai tool in
- Decision: accept (review_status: confirmed)

## are critical first steps mitigate risk of

- Cluster ID: `rc2_efe70ae657956920`
- Assertions: 1
- Phrases: are critical first steps mitigate risk of
- Suggested normal forms: critical first step mitigate risk of
- Decision: pending (review_status: pending)

## are critical first steps to

- Cluster ID: `rc2_b846e7a63f8c152f`
- Assertions: 1
- Phrases: are critical first steps to
- Suggested normal forms: critical first step to
- Decision: pending (review_status: pending)

## are designed to measure severity of

- Cluster ID: `rc2_ca9188bd527c348a`
- Assertions: 1
- Phrases: are designed to measure severity of
- Suggested normal forms: design to measure severity of
- Decision: accept (review_status: confirmed)

## are direct responsibility rather than

- Cluster ID: `rc2_a8883716ff5e78b5`
- Assertions: 1
- Phrases: are direct responsibility rather than
- Suggested normal forms: direct responsibility rather than
- Decision: accept (review_status: confirmed)

## are direct responsibility than

- Cluster ID: `rc2_aa50c851fbe73487`
- Assertions: 1
- Phrases: are direct responsibility than
- Suggested normal forms: direct responsibility than
- Decision: pending (review_status: pending)

## are example reasons provided for

- Cluster ID: `rc2_f59707d0c8bc2f0e`
- Assertions: 1
- Phrases: are example reasons provided for
- Suggested normal forms: example reason provid for
- Decision: pending (review_status: pending)

## are exhaustive list of

- Cluster ID: `rc2_994f50129c23cd8b`
- Assertions: 1
- Phrases: are exhaustive list of
- Suggested normal forms: exhaustive list of
- Decision: pending (review_status: pending)

## are exploiting critical-severity remote code execution flaw in

- Cluster ID: `rc2_bb586888bb7ebca2`
- Assertions: 1
- Phrases: are exploiting critical-severity remote code execution flaw in
- Suggested normal forms: exploit critical-severity remote code execution flaw in
- Decision: pending (review_status: pending)

## are facing

- Cluster ID: `rc2_002af3c45720e7dd`
- Assertions: 1
- Phrases: are facing
- Suggested normal forms: fac
- Decision: accept (review_status: confirmed)

## are frequent attack vector for malicious cyber actors including those backed by

- Cluster ID: `rc2_a548f91403a44084`
- Assertions: 1
- Phrases: are frequent attack vector for malicious cyber actors including those backed by
- Suggested normal forms: frequent attack vector for maliciou cyber actor includ those back by
- Decision: accept (review_status: confirmed)

## are handled in Rapid7 PoC for

- Cluster ID: `rc2_4eddb8454b6c21d1`
- Assertions: 1
- Phrases: are handled in Rapid7 PoC for
- Suggested normal forms: handl in rapid7 poc for
- Decision: pending (review_status: pending)

## are handled through

- Cluster ID: `rc2_1d961c7be2fa6832`
- Assertions: 1
- Phrases: are handled through
- Suggested normal forms: handl through
- Decision: pending (review_status: pending)

## are how particular kind of buffer overflow to

- Cluster ID: `rc2_af87ddb7a1cc3590`
- Assertions: 1
- Phrases: are how particular kind of buffer overflow to
- Suggested normal forms: how particular kind of buffer overflow to
- Decision: accept (review_status: confirmed)

## are in place for

- Cluster ID: `rc2_1d6f9a6444224e10`
- Assertions: 1
- Phrases: are in place for
- Suggested normal forms: in place for
- Decision: pending (review_status: pending)

## are known to

- Cluster ID: `rc2_6fdaf5143c1eb2f9`
- Assertions: 1
- Phrases: are known to
- Suggested normal forms: known to
- Decision: pending (review_status: pending)

## are limited to

- Cluster ID: `rc2_b7eb6994fb4a70ef`
- Assertions: 1
- Phrases: are limited to
- Suggested normal forms: limit to
- Decision: pending (review_status: pending)

## are limited to settings owned by

- Cluster ID: `rc2_315334f1bb96314e`
- Assertions: 1
- Phrases: are limited to settings owned by
- Suggested normal forms: limit to sett own by
- Decision: pending (review_status: pending)

## are met such as

- Cluster ID: `rc2_4d3fe717d5f43953`
- Assertions: 1
- Phrases: are met such as
- Suggested normal forms: met such a
- Decision: accept (review_status: confirmed)

## are number of recommendations for

- Cluster ID: `rc2_cc94e3097dfbe62a`
- Assertions: 1
- Phrases: are number of recommendations for
- Suggested normal forms: number of recommendation for
- Decision: accept (review_status: confirmed)

## are precursors to

- Cluster ID: `rc2_8f2663bc3a48c89e`
- Assertions: 1
- Phrases: are precursors to
- Suggested normal forms: precursor to
- Decision: accept (review_status: confirmed)

## are preferred / in

- Cluster ID: `rc2_d7c71218860fbee0`
- Assertions: 1
- Phrases: are preferred / in
- Suggested normal forms: preferr / in
- Decision: pending (review_status: pending)

## are preferred / in certain contexts From

- Cluster ID: `rc2_02718cd9f74b04ab`
- Assertions: 1
- Phrases: are preferred / in certain contexts From
- Suggested normal forms: preferr / in certain context from
- Decision: pending (review_status: pending)

## are present in

- Cluster ID: `rc2_1635348974a40efa`
- Assertions: 1
- Phrases: are present in
- Suggested normal forms: present in
- Decision: accept (review_status: confirmed)

## are produced by

- Cluster ID: `rc2_e54c1834c30f3601`
- Assertions: 1
- Phrases: are produced by
- Suggested normal forms: produc by
- Decision: accept (review_status: confirmed)

## are protected better from

- Cluster ID: `rc2_821a3dccea778c6c`
- Assertions: 1
- Phrases: are protected better from
- Suggested normal forms: protect better from
- Decision: pending (review_status: pending)

## are protected from

- Cluster ID: `rc2_054f0f86bd7fc852`
- Assertions: 1
- Phrases: are protected from
- Suggested normal forms: protect from
- Decision: pending (review_status: pending)

## are provided along

- Cluster ID: `rc2_dad372ec55ee9ca5`
- Assertions: 1
- Phrases: are provided along
- Suggested normal forms: provid along
- Decision: pending (review_status: pending)

## are provided as

- Cluster ID: `rc2_976a9024d11e51e3`
- Assertions: 1
- Phrases: are provided as
- Suggested normal forms: provid a
- Decision: pending (review_status: pending)

## are provided as LOB systems in

- Cluster ID: `rc2_3c0bb19a59a867fc`
- Assertions: 1
- Phrases: are provided as LOB systems in
- Suggested normal forms: provid a lob system in
- Decision: pending (review_status: pending)

## are published by

- Cluster ID: `rc2_63166feba25324ba`
- Assertions: 1
- Phrases: are published by
- Suggested normal forms: publish by
- Decision: accept (review_status: confirmed)

## are published starting from

- Cluster ID: `rc2_09b66182374d6d0f`
- Assertions: 1
- Phrases: are published starting from
- Suggested normal forms: publish start from
- Decision: pending (review_status: pending)

## are publishing technical analysis of

- Cluster ID: `rc2_894bda97ffb5a330`
- Assertions: 1
- Phrases: are publishing technical analysis of
- Suggested normal forms: publish technical analysi of
- Decision: pending (review_status: pending)

## are publishing technical analysis of CVE-2026-63520

- Cluster ID: `rc2_1c789ef1bf34a1b7`
- Assertions: 1
- Phrases: are publishing technical analysis of CVE-2026-63520
- Suggested normal forms: publish technical analysi of cve-2026-63520
- Decision: pending (review_status: pending)

## are publishing technical analysis of vulnerability along with accompanying proof-of-concept script

- Cluster ID: `rc2_1a03820913cf5980`
- Assertions: 1
- Phrases: are publishing technical analysis of vulnerability along with accompanying proof-of-concept script
- Suggested normal forms: publish technical analysi of vulnerability along with accompany proof-of-concept script
- Decision: pending (review_status: pending)

## are rated with

- Cluster ID: `rc2_b9dae677ee051856`
- Assertions: 1
- Phrases: are rated with
- Suggested normal forms: rat with
- Decision: accept (review_status: confirmed)

## are required to comply with

- Cluster ID: `rc2_94b23d17cd61b506`
- Assertions: 1
- Phrases: are required to comply with
- Suggested normal forms: requir to comply with
- Decision: pending (review_status: pending)

## are required to have

- Cluster ID: `rc2_effde594a383c02e`
- Assertions: 1
- Phrases: are required to have
- Suggested normal forms: requir to
- Decision: accept (review_status: confirmed)

## are required to have rapid response times for

- Cluster ID: `rc2_3ec0914c95019eb8`
- Assertions: 1
- Phrases: are required to have rapid response times for
- Suggested normal forms: requir to rapid response time for
- Decision: accept (review_status: confirmed)

## are salient to

- Cluster ID: `rc2_d71a83e35216b36d`
- Assertions: 1
- Phrases: are salient to
- Suggested normal forms: salient to
- Decision: accept (review_status: confirmed)

## are series of

- Cluster ID: `rc2_e35263d434fbf520`
- Assertions: 1
- Phrases: are series of
- Suggested normal forms: sery of
- Decision: pending (review_status: pending)

## are set to default value of Defined reasonable worst case of

- Cluster ID: `rc2_5b532bab3c669a7d`
- Assertions: 1
- Phrases: are set to default value of Defined reasonable worst case of
- Suggested normal forms: set to default value of defin reasonable worst case of
- Decision: accept (review_status: confirmed)

## are shared between

- Cluster ID: `rc2_a213c6b5b4853f13`
- Assertions: 1
- Phrases: are shared between
- Suggested normal forms: shar between
- Decision: accept (review_status: confirmed)

## are simplified to illustrate

- Cluster ID: `rc2_79a41a53feb0f0f5`
- Assertions: 1
- Phrases: are simplified to illustrate
- Suggested normal forms: simplifi to illustrate
- Decision: accept (review_status: confirmed)

## are suggestive examples of when to select Concentrated metric values for

- Cluster ID: `rc2_6a73ac482fbeab28`
- Assertions: 1
- Phrases: are suggestive examples of when to select Concentrated metric values for
- Suggested normal forms: suggestive example of when to select concentrat metric value for
- Decision: pending (review_status: pending)

## are suggestive examples of when to select Diffuse for

- Cluster ID: `rc2_99fb1962b6e8bafd`
- Assertions: 1
- Phrases: are suggestive examples of when to select Diffuse for
- Suggested normal forms: suggestive example of when to select diffuse for
- Decision: pending (review_status: pending)

## are under full control of

- Cluster ID: `rc2_e21c1600cc89479b`
- Assertions: 1
- Phrases: are under full control of
- Suggested normal forms: under full control of
- Decision: pending (review_status: pending)

## are withholding

- Cluster ID: `rc2_d2454c4d8a166f48`
- Assertions: 1
- Phrases: are withholding
- Suggested normal forms: withhold
- Decision: pending (review_status: pending)

## arises from

- Cluster ID: `rc2_fddc1f6bb83fc401`
- Assertions: 1
- Phrases: arises from
- Suggested normal forms: arise from
- Decision: accept (review_status: confirmed)

## ask

- Cluster ID: `rc2_2f2fc7f2e9ce13b0`
- Assertions: 1
- Phrases: ask
- Suggested normal forms: ask
- Decision: accept (review_status: confirmed)

## ask about score

- Cluster ID: `rc2_dd2293c5f13e62cc`
- Assertions: 1
- Phrases: ask about score
- Suggested normal forms: ask about score
- Decision: accept (review_status: confirmed)

## ask most

- Cluster ID: `rc2_d68b5da5c2b30a62`
- Assertions: 1
- Phrases: ask most
- Suggested normal forms: ask most
- Decision: accept (review_status: confirmed)

## assessed

- Cluster ID: `rc2_14b9005e4f90ef7e`
- Assertions: 1
- Phrases: assessed
- Suggested normal forms: assess
- Decision: pending (review_status: pending)

## assessed entire product as

- Cluster ID: `rc2_015a04fda43e86e0`
- Assertions: 1
- Phrases: assessed entire product as
- Suggested normal forms: assess entire product a
- Decision: pending (review_status: pending)

## assist in

- Cluster ID: `rc2_a37d53fee23894da`
- Assertions: 1
- Phrases: assist in
- Suggested normal forms: assist in
- Decision: pending (review_status: pending)

## assume Attack Vector of

- Cluster ID: `rc2_f0d8ac1f818ac357`
- Assertions: 1
- Phrases: assume Attack Vector of
- Suggested normal forms: assume attack vector of
- Decision: accept (review_status: confirmed)

## assume Attack Vector of Network As

- Cluster ID: `rc2_6dfa05c252cef0b2`
- Assertions: 1
- Phrases: assume Attack Vector of Network As
- Suggested normal forms: assume attack vector of network a
- Decision: accept (review_status: confirmed)

## attach

- Cluster ID: `rc2_a919007637abd504`
- Assertions: 1
- Phrases: attach
- Suggested normal forms: attach
- Decision: pending (review_status: pending)

## attempted to use

- Cluster ID: `rc2_779a3126d1cb2fac`
- Assertions: 1
- Phrases: attempted to use
- Suggested normal forms: attempt to use
- Decision: pending (review_status: pending)

## augmented

- Cluster ID: `rc2_5d69825fe9a39338`
- Assertions: 1
- Phrases: augmented
- Suggested normal forms: augment
- Decision: accept (review_status: confirmed)

## augmented agentic work with

- Cluster ID: `rc2_38759e2f7856c5a9`
- Assertions: 1
- Phrases: augmented agentic work with
- Suggested normal forms: augment agentic work with
- Decision: accept (review_status: confirmed)

## augments information in

- Cluster ID: `rc2_6eb153113a67c013`
- Assertions: 1
- Phrases: augments information in
- Suggested normal forms: augment information in
- Decision: pending (review_status: pending)

## authenticate as

- Cluster ID: `rc2_e89eb4cc639b4097`
- Assertions: 1
- Phrases: authenticate as
- Suggested normal forms: authenticate a
- Decision: accept (review_status: confirmed)

## automate exploitation events for vulnerability across

- Cluster ID: `rc2_26e1028599c33b41`
- Assertions: 1
- Phrases: automate exploitation events for vulnerability across
- Suggested normal forms: automate exploitation event for vulnerability acros
- Decision: accept (review_status: confirmed)

## base64

- Cluster ID: `rc2_371a286d5872a373`
- Assertions: 1
- Phrases: base64
- Suggested normal forms: base64
- Decision: accept (review_status: confirmed)

## be Constructing

- Cluster ID: `rc2_6939b49c02d496f4`
- Assertions: 1
- Phrases: be Constructing
- Suggested normal forms: be construct
- Decision: accept (review_status: confirmed)

## be Inspecting

- Cluster ID: `rc2_37381f88641812cd`
- Assertions: 1
- Phrases: be Inspecting
- Suggested normal forms: be inspect
- Decision: pending (review_status: pending)

## be Returning to

- Cluster ID: `rc2_f9776e26bd47012c`
- Assertions: 1
- Phrases: be Returning to
- Suggested normal forms: be return to
- Decision: pending (review_status: pending)

## be Returning to MethodInstance from

- Cluster ID: `rc2_dfa993cbc99dedd8`
- Assertions: 1
- Phrases: be Returning to MethodInstance from
- Suggested normal forms: be return to methodinstance from
- Decision: pending (review_status: pending)

## be Starting with

- Cluster ID: `rc2_2d4a2ab009d778a7`
- Assertions: 1
- Phrases: be Starting with
- Suggested normal forms: be start with
- Decision: accept (review_status: confirmed)

## be Taken

- Cluster ID: `rc2_a1f36f7646009bbc`
- Assertions: 1
- Phrases: be Taken
- Suggested normal forms: be taken
- Decision: accept (review_status: confirmed)

## be accompanied by

- Cluster ID: `rc2_db766f46f7a98e79`
- Assertions: 1
- Phrases: be accompanied by
- Suggested normal forms: be accompani by
- Decision: accept (review_status: confirmed)

## be account for changes in

- Cluster ID: `rc2_82a266fc550c1293`
- Assertions: 1
- Phrases: be account for changes in
- Suggested normal forms: be account for change in
- Decision: pending (review_status: pending)

## be achieved

- Cluster ID: `rc2_c3768dd73e843822`
- Assertions: 1
- Phrases: be achieved
- Suggested normal forms: be achiev
- Decision: pending (review_status: pending)

## be added in

- Cluster ID: `rc2_f7097bd62881321c`
- Assertions: 1
- Phrases: be added in
- Suggested normal forms: be add in
- Decision: pending (review_status: pending)

## be added to

- Cluster ID: `rc2_c2b24e6fa1590ead`
- Assertions: 1
- Phrases: be added to
- Suggested normal forms: be add to
- Decision: pending (review_status: pending)

## be added to existing

- Cluster ID: `rc2_3251b0e6a5ea38c6`
- Assertions: 1
- Phrases: be added to existing
- Suggested normal forms: be add to exist
- Decision: pending (review_status: pending)

## be allow inbound traffic on UDP ports only from

- Cluster ID: `rc2_4b5f4118883bf3e7`
- Assertions: 1
- Phrases: be allow inbound traffic on UDP ports only from
- Suggested normal forms: be allow inbound traffic on udp port only from
- Decision: accept (review_status: confirmed)

## be allow inbound traffic only from

- Cluster ID: `rc2_d2b927d93f7d0bde`
- Assertions: 1
- Phrases: be allow inbound traffic only from
- Suggested normal forms: be allow inbound traffic only from
- Decision: accept (review_status: confirmed)

## be allowing malicious user to

- Cluster ID: `rc2_1494a693ab846f7f`
- Assertions: 1
- Phrases: be allowing malicious user to
- Suggested normal forms: be allow maliciou user to
- Decision: pending (review_status: pending)

## be assess lumpiness of

- Cluster ID: `rc2_1a40f9995b1f364c`
- Assertions: 1
- Phrases: be assess lumpiness of
- Suggested normal forms: be asses lumpines of
- Decision: pending (review_status: pending)

## be assessed as

- Cluster ID: `rc2_82796410eedaee88`
- Assertions: 1
- Phrases: be assessed as
- Suggested normal forms: be assess a
- Decision: pending (review_status: pending)

## be assessed as having impact to Subsequent System

- Cluster ID: `rc2_93fe477849c2d47e`
- Assertions: 1
- Phrases: be assessed as having impact to Subsequent System
- Suggested normal forms: be assess a hav impact to subsequent system
- Decision: pending (review_status: pending)

## be assessing

- Cluster ID: `rc2_91fd0d96a1098658`
- Assertions: 1
- Phrases: be assessing
- Suggested normal forms: be assess
- Decision: pending (review_status: pending)

## be assessing vulnerability in

- Cluster ID: `rc2_c9a0078aa3d56bee`
- Assertions: 1
- Phrases: be assessing vulnerability in
- Suggested normal forms: be assess vulnerability in
- Decision: accept (review_status: confirmed)

## be associated with

- Cluster ID: `rc2_332845a89a9a908c`
- Assertions: 1
- Phrases: be associated with
- Suggested normal forms: be associat with
- Decision: accept (review_status: confirmed)

## be assume

- Cluster ID: `rc2_bd07a3d3ac9963b7`
- Assertions: 1
- Phrases: be assume
- Suggested normal forms: be assume
- Decision: accept (review_status: confirmed)

## be assume identity of

- Cluster ID: `rc2_37380a5862a1ed4e`
- Assertions: 1
- Phrases: be assume identity of
- Suggested normal forms: be assume identity of
- Decision: pending (review_status: pending)

## be attached to

- Cluster ID: `rc2_86ec244f64d5bb70`
- Assertions: 1
- Phrases: be attached to
- Suggested normal forms: be attach to
- Decision: accept (review_status: confirmed)

## be attack

- Cluster ID: `rc2_399a7d862e864300`
- Assertions: 1
- Phrases: be attack
- Suggested normal forms: be attack
- Decision: pending (review_status: pending)

## be attributed to

- Cluster ID: `rc2_e09a9772626f9ecc`
- Assertions: 1
- Phrases: be attributed to
- Suggested normal forms: be attribut to
- Decision: pending (review_status: pending)

## be avoid types of

- Cluster ID: `rc2_16ce16f97b9a0fdb`
- Assertions: 1
- Phrases: be avoid types of
- Suggested normal forms: be avoid type of
- Decision: pending (review_status: pending)

## be backed by

- Cluster ID: `rc2_ee5a1427a9d84f73`
- Assertions: 1
- Phrases: be backed by
- Suggested normal forms: be back by
- Decision: accept (review_status: confirmed)

## be based on adjusting CVSS-BTE scores as

- Cluster ID: `rc2_4fa1835d4dd6053f`
- Assertions: 1
- Phrases: be based on adjusting CVSS-BTE scores as
- Suggested normal forms: be bas on adjust cvs-bte score a
- Decision: pending (review_status: pending)

## be based on applications hosted by

- Cluster ID: `rc2_56c4e7c4b56a725f`
- Assertions: 1
- Phrases: be based on applications hosted by
- Suggested normal forms: be bas on application host by
- Decision: pending (review_status: pending)

## be based on component placement within

- Cluster ID: `rc2_5d0c1d16f28a6e3a`
- Assertions: 1
- Phrases: be based on component placement within
- Suggested normal forms: be bas on component placement within
- Decision: pending (review_status: pending)

## be based on information regarding availability of

- Cluster ID: `rc2_df8e0da19125ba5b`
- Assertions: 1
- Phrases: be based on information regarding availability of
- Suggested normal forms: be bas on information regard availability of
- Decision: pending (review_status: pending)

## be based on system placement within

- Cluster ID: `rc2_d85dda78068a1b1a`
- Assertions: 1
- Phrases: be based on system placement within
- Suggested normal forms: be bas on system placement within
- Decision: pending (review_status: pending)

## be based on uptime requirements of

- Cluster ID: `rc2_158b8416a0c16816`
- Assertions: 1
- Phrases: be based on uptime requirements of
- Suggested normal forms: be bas on uptime requirement of
- Decision: pending (review_status: pending)

## be block

- Cluster ID: `rc2_22b52f7d5ab462a9`
- Assertions: 1
- Phrases: be block
- Suggested normal forms: be block
- Decision: pending (review_status: pending)

## be bypassed by

- Cluster ID: `rc2_e8b19b5dfa08d2f1`
- Assertions: 1
- Phrases: be bypassed by
- Suggested normal forms: be bypass by
- Decision: pending (review_status: pending)

## be calculated

- Cluster ID: `rc2_bdbd021ac21fc4a9`
- Assertions: 1
- Phrases: be calculated
- Suggested normal forms: be calculat
- Decision: pending (review_status: pending)

## be calculated as if Base Attack Vector was set to Physical

- Cluster ID: `rc2_1b3edb62dca4c8a8`
- Assertions: 1
- Phrases: be calculated as if Base Attack Vector was set to Physical
- Suggested normal forms: be calculat a if base attack vector set to physical
- Decision: pending (review_status: pending)

## be chaining when

- Cluster ID: `rc2_31b9e0296d676056`
- Assertions: 1
- Phrases: be chaining when
- Suggested normal forms: be chain when
- Decision: pending (review_status: pending)

## be checking version via

- Cluster ID: `rc2_e9b1edcd95074708`
- Assertions: 1
- Phrases: be checking version via
- Suggested normal forms: be check version via
- Decision: accept (review_status: confirmed)

## be classified at

- Cluster ID: `rc2_99d010046ca541e1`
- Assertions: 1
- Phrases: be classified at
- Suggested normal forms: be classifi at
- Decision: pending (review_status: pending)

## be collected during

- Cluster ID: `rc2_b47ec305b1c8ab9d`
- Assertions: 1
- Phrases: be collected during
- Suggested normal forms: be collect dur
- Decision: accept (review_status: confirmed)

## be communicated within

- Cluster ID: `rc2_ba4f8956df4e2097`
- Assertions: 1
- Phrases: be communicated within
- Suggested normal forms: be communicat within
- Decision: accept (review_status: confirmed)

## be communicated within vulnerability disclosure notice For

- Cluster ID: `rc2_ae6917baf99b3562`
- Assertions: 1
- Phrases: be communicated within vulnerability disclosure notice For
- Suggested normal forms: be communicat within vulnerability disclosure notice for
- Decision: accept (review_status: confirmed)

## be compressed

- Cluster ID: `rc2_f51e782210edda28`
- Assertions: 1
- Phrases: be compressed
- Suggested normal forms: be compress
- Decision: accept (review_status: confirmed)

## be compressed in definition of

- Cluster ID: `rc2_18b29354da6a575a`
- Assertions: 1
- Phrases: be compressed in definition of
- Suggested normal forms: be compress in definition of
- Decision: accept (review_status: confirmed)

## be compute

- Cluster ID: `rc2_8426bd0eedf8d147`
- Assertions: 1
- Phrases: be compute
- Suggested normal forms: be compute
- Decision: accept (review_status: confirmed)

## be concerning

- Cluster ID: `rc2_74e6d088d0c6d2de`
- Assertions: 1
- Phrases: be concerning
- Suggested normal forms: be concern
- Decision: pending (review_status: pending)

## be concluded with

- Cluster ID: `rc2_93cc67eaab014421`
- Assertions: 1
- Phrases: be concluded with
- Suggested normal forms: be conclud with
- Decision: pending (review_status: pending)

## be concluded with successful discovery of

- Cluster ID: `rc2_0082a7b1b7363a15`
- Assertions: 1
- Phrases: be concluded with successful discovery of
- Suggested normal forms: be conclud with successful discovery of
- Decision: pending (review_status: pending)

## be confirmed through acknowledgment by

- Cluster ID: `rc2_d45d1fc3bb674394`
- Assertions: 1
- Phrases: be confirmed through acknowledgment by
- Suggested normal forms: be confirm through acknowledgment by
- Decision: pending (review_status: pending)

## be confirmed through acknowledgment by author of

- Cluster ID: `rc2_795bde4a0b0b60f8`
- Assertions: 1
- Phrases: be confirmed through acknowledgment by author of
- Suggested normal forms: be confirm through acknowledgment by author of
- Decision: pending (review_status: pending)

## be considered Since

- Cluster ID: `rc2_cabfcd65d91b13e6`
- Assertions: 1
- Phrases: be considered Since
- Suggested normal forms: be consider since
- Decision: pending (review_status: pending)

## be considered as

- Cluster ID: `rc2_6e7add09f375fcdc`
- Assertions: 1
- Phrases: be considered as
- Suggested normal forms: be consider a
- Decision: accept (review_status: confirmed)

## be contacting target SharePoint servers domain controller over

- Cluster ID: `rc2_01c68eddd7a6b631`
- Assertions: 1
- Phrases: be contacting target SharePoint servers domain controller over
- Suggested normal forms: be contact target sharepoint server domain controller over
- Decision: pending (review_status: pending)

## be create

- Cluster ID: `rc2_b364613436aaf96d`
- Assertions: 1
- Phrases: be create
- Suggested normal forms: be create
- Decision: accept (review_status: confirmed)

## be decide what vector group in ordering of

- Cluster ID: `rc2_b958183b5cc94093`
- Assertions: 1
- Phrases: be decide what vector group in ordering of
- Suggested normal forms: be decide what vector group in order of
- Decision: pending (review_status: pending)

## be decoding it

- Cluster ID: `rc2_157a1f6ed73dd472`
- Assertions: 1
- Phrases: be decoding it
- Suggested normal forms: be decod it
- Decision: pending (review_status: pending)

## be defined as

- Cluster ID: `rc2_64241f4ed876077c`
- Assertions: 1
- Phrases: be defined as
- Suggested normal forms: be defin a
- Decision: accept (review_status: confirmed)

## be defined for System of

- Cluster ID: `rc2_2fd40cd38d158e64`
- Assertions: 1
- Phrases: be defined for System of
- Suggested normal forms: be defin for system of
- Decision: accept (review_status: confirmed)

## be deleted by

- Cluster ID: `rc2_4829995b319534d9`
- Assertions: 1
- Phrases: be deleted by
- Suggested normal forms: be delet by
- Decision: accept (review_status: confirmed)

## be describe

- Cluster ID: `rc2_12b8d8dcb06add1c`
- Assertions: 1
- Phrases: be describe
- Suggested normal forms: be describe
- Decision: pending (review_status: pending)

## be described as chain of

- Cluster ID: `rc2_e617edfd13e001c3`
- Assertions: 1
- Phrases: be described as chain of
- Suggested normal forms: be describ a chain of
- Decision: pending (review_status: pending)

## be described consistent with

- Cluster ID: `rc2_0baa01161f1776fb`
- Assertions: 1
- Phrases: be described consistent with
- Suggested normal forms: be describ consistent with
- Decision: accept (review_status: confirmed)

## be described in

- Cluster ID: `rc2_b08b05a253f5b557`
- Assertions: 1
- Phrases: be described in
- Suggested normal forms: be describ in
- Decision: accept (review_status: confirmed)

## be deserialization gadget in

- Cluster ID: `rc2_2935faa3621cfb48`
- Assertions: 1
- Phrases: be deserialization gadget in
- Suggested normal forms: be deserialization gadget in
- Decision: accept (review_status: confirmed)

## be deserializing it via

- Cluster ID: `rc2_85dc4f536fadda24`
- Assertions: 1
- Phrases: be deserializing it via
- Suggested normal forms: be deserializ it via
- Decision: accept (review_status: confirmed)

## be designed

- Cluster ID: `rc2_1f2fa2ad0913b5d0`
- Assertions: 1
- Phrases: be designed
- Suggested normal forms: be design
- Decision: accept (review_status: confirmed)

## be designed to be deployed as part of

- Cluster ID: `rc2_2e060c7acc788592`
- Assertions: 1
- Phrases: be designed to be deployed as part of
- Suggested normal forms: be design to be deploy a part of
- Decision: accept (review_status: confirmed)

## be designed to prevent

- Cluster ID: `rc2_99b57590a775604f`
- Assertions: 1
- Phrases: be designed to prevent
- Suggested normal forms: be design to prevent
- Decision: accept (review_status: confirmed)

## be designed to retain

- Cluster ID: `rc2_1191bba8aff889d1`
- Assertions: 1
- Phrases: be designed to retain
- Suggested normal forms: be design to retain
- Decision: pending (review_status: pending)

## be designed to retain successful procedures across

- Cluster ID: `rc2_1b07ef8f4d8d0903`
- Assertions: 1
- Phrases: be designed to retain successful procedures across
- Suggested normal forms: be design to retain successful procedure acros
- Decision: accept (review_status: confirmed)

## be disclosed by

- Cluster ID: `rc2_44858e4caa6f765d`
- Assertions: 1
- Phrases: be disclosed by
- Suggested normal forms: be disclos by
- Decision: pending (review_status: pending)

## be disclosed by Broadcom on

- Cluster ID: `rc2_720a2ec58f02bd8b`
- Assertions: 1
- Phrases: be disclosed by Broadcom on
- Suggested normal forms: be disclos by broadcom on
- Decision: pending (review_status: pending)

## be disclosed in

- Cluster ID: `rc2_5164076c9fdae520`
- Assertions: 1
- Phrases: be disclosed in
- Suggested normal forms: be disclos in
- Decision: pending (review_status: pending)

## be discussed

- Cluster ID: `rc2_7ca3b40b78476cde`
- Assertions: 1
- Phrases: be discussed
- Suggested normal forms: be discuss
- Decision: pending (review_status: pending)

## be discussed above through

- Cluster ID: `rc2_ce547793ee5804c0`
- Assertions: 1
- Phrases: be discussed above through
- Suggested normal forms: be discuss above through
- Decision: pending (review_status: pending)

## be employed

- Cluster ID: `rc2_f91ad0384165009b`
- Assertions: 1
- Phrases: be employed
- Suggested normal forms: be employ
- Decision: pending (review_status: pending)

## be enabled by

- Cluster ID: `rc2_29e93587cff13fa7`
- Assertions: 1
- Phrases: be enabled by
- Suggested normal forms: be enabl by
- Decision: accept (review_status: confirmed)

## be encoding that

- Cluster ID: `rc2_b0938fee50fd2228`
- Assertions: 1
- Phrases: be encoding that
- Suggested normal forms: be encod that
- Decision: pending (review_status: pending)

## be enrich

- Cluster ID: `rc2_dcff18c2201069bb`
- Assertions: 1
- Phrases: be enrich
- Suggested normal forms: be enrich
- Decision: pending (review_status: pending)

## be enumerated

- Cluster ID: `rc2_1be9d9ca8ec5afe1`
- Assertions: 1
- Phrases: be enumerated
- Suggested normal forms: be enumerat
- Decision: pending (review_status: pending)

## be execute code as

- Cluster ID: `rc2_9d814015f5f7d0dc`
- Assertions: 1
- Phrases: be execute code as
- Suggested normal forms: be execute code a
- Decision: accept (review_status: confirmed)

## be exfiltrated through

- Cluster ID: `rc2_0a9cc7aa48d7a1f3`
- Assertions: 1
- Phrases: be exfiltrated through
- Suggested normal forms: be exfiltrat through
- Decision: accept (review_status: confirmed)

## be expected in

- Cluster ID: `rc2_e04cf911134eaa93`
- Assertions: 1
- Phrases: be expected in
- Suggested normal forms: be expect in
- Decision: pending (review_status: pending)

## be exploited by

- Cluster ID: `rc2_faa250e471c3754e`
- Assertions: 1
- Phrases: be exploited by
- Suggested normal forms: be exploit by
- Decision: accept (review_status: confirmed)

## be feeding

- Cluster ID: `rc2_a7947e66bfcb5ede`
- Assertions: 1
- Phrases: be feeding
- Suggested normal forms: be feed
- Decision: accept (review_status: confirmed)

## be flagged as exploited in

- Cluster ID: `rc2_90ddca390101e967`
- Assertions: 1
- Phrases: be flagged as exploited in
- Suggested normal forms: be flagg a exploit in
- Decision: pending (review_status: pending)

## be focused on

- Cluster ID: `rc2_2119cf99e7af5918`
- Assertions: 1
- Phrases: be focused on
- Suggested normal forms: be focus on
- Decision: pending (review_status: pending)

## be followed by deployment of

- Cluster ID: `rc2_b8ff535c4a3b6f97`
- Assertions: 1
- Phrases: be followed by deployment of
- Suggested normal forms: be follow by deployment of
- Decision: accept (review_status: confirmed)

## be fortify more

- Cluster ID: `rc2_48b3b694aea8b4ec`
- Assertions: 1
- Phrases: be fortify more
- Suggested normal forms: be fortify more
- Decision: pending (review_status: pending)

## be fortify risk of

- Cluster ID: `rc2_c673a9de7d70c019`
- Assertions: 1
- Phrases: be fortify risk of
- Suggested normal forms: be fortify risk of
- Decision: pending (review_status: pending)

## be found inside

- Cluster ID: `rc2_613100e739ad1b36`
- Assertions: 1
- Phrases: be found inside
- Suggested normal forms: be found inside
- Decision: accept (review_status: confirmed)

## be frustrated by

- Cluster ID: `rc2_f9afe24ea6978fd1`
- Assertions: 1
- Phrases: be frustrated by
- Suggested normal forms: be frustrat by
- Decision: pending (review_status: pending)

## be gain code execution by

- Cluster ID: `rc2_f36ddb630715cb70`
- Assertions: 1
- Phrases: be gain code execution by
- Suggested normal forms: be gain code execution by
- Decision: pending (review_status: pending)

## be gathered during

- Cluster ID: `rc2_7f144b0539b82636`
- Assertions: 1
- Phrases: be gathered during
- Suggested normal forms: be gather dur
- Decision: accept (review_status: confirmed)

## be get Vulnerability A to perform

- Cluster ID: `rc2_ea43d48cf46f8a3b`
- Assertions: 1
- Phrases: be get Vulnerability A to perform
- Suggested normal forms: be get vulnerability a to perform
- Decision: pending (review_status: pending)

## be get into

- Cluster ID: `rc2_a746dbb72650f0e8`
- Assertions: 1
- Phrases: be get into
- Suggested normal forms: be get into
- Decision: pending (review_status: pending)

## be governed by

- Cluster ID: `rc2_c66a0d8cde94b0aa`
- Assertions: 1
- Phrases: be governed by
- Suggested normal forms: be govern by
- Decision: pending (review_status: pending)

## be granted by

- Cluster ID: `rc2_849f626aedde08e6`
- Assertions: 1
- Phrases: be granted by
- Suggested normal forms: be grant by
- Decision: accept (review_status: confirmed)

## be granted by default in

- Cluster ID: `rc2_10e3f999df454abd`
- Assertions: 1
- Phrases: be granted by default in
- Suggested normal forms: be grant by default in
- Decision: accept (review_status: confirmed)

## be granted by default without

- Cluster ID: `rc2_bbb6d5845ec25cca`
- Assertions: 1
- Phrases: be granted by default without
- Suggested normal forms: be grant by default without
- Decision: accept (review_status: confirmed)

## be guided by

- Cluster ID: `rc2_540caa6c4a5372b5`
- Assertions: 1
- Phrases: be guided by
- Suggested normal forms: be guid by
- Decision: pending (review_status: pending)

## be harden

- Cluster ID: `rc2_094b8ab8b8810143`
- Assertions: 1
- Phrases: be harden
- Suggested normal forms: be harden
- Decision: pending (review_status: pending)

## be harden cybersecurity practices including policies for

- Cluster ID: `rc2_20e67961e9d7fd92`
- Assertions: 1
- Phrases: be harden cybersecurity practices including policies for
- Suggested normal forms: be harden cybersecurity practice includ policy for
- Decision: pending (review_status: pending)

## be having entry in

- Cluster ID: `rc2_9b64f7ead429c053`
- Assertions: 1
- Phrases: be having entry in
- Suggested normal forms: be hav entry in
- Decision: pending (review_status: pending)

## be held by

- Cluster ID: `rc2_1a9aa8606198adb3`
- Assertions: 1
- Phrases: be held by
- Suggested normal forms: be held by
- Decision: accept (review_status: confirmed)

## be hit

- Cluster ID: `rc2_6386c449711363a6`
- Assertions: 1
- Phrases: be hit
- Suggested normal forms: be hit
- Decision: accept (review_status: confirmed)

## be hit System.Object visible in

- Cluster ID: `rc2_d43b2cbfad256415`
- Assertions: 1
- Phrases: be hit System.Object visible in
- Suggested normal forms: be hit system.object visible in
- Decision: pending (review_status: pending)

## be hosted by

- Cluster ID: `rc2_058071cf102d50b7`
- Assertions: 1
- Phrases: be hosted by
- Suggested normal forms: be host by
- Decision: accept (review_status: confirmed)

## be hosted in

- Cluster ID: `rc2_7afe0cb2b97860df`
- Assertions: 1
- Phrases: be hosted in
- Suggested normal forms: be host in
- Decision: accept (review_status: confirmed)

## be hosting

- Cluster ID: `rc2_a2ab32c9a233208b`
- Assertions: 1
- Phrases: be hosting
- Suggested normal forms: be host
- Decision: accept (review_status: confirmed)

## be impacted by

- Cluster ID: `rc2_b9fb590143909e7e`
- Assertions: 1
- Phrases: be impacted by
- Suggested normal forms: be impact by
- Decision: pending (review_status: pending)

## be imported within

- Cluster ID: `rc2_5ee48b1629e70107`
- Assertions: 1
- Phrases: be imported within
- Suggested normal forms: be import within
- Decision: accept (review_status: confirmed)

## be in to use

- Cluster ID: `rc2_d6c9a2aa1e0ab89e`
- Assertions: 1
- Phrases: be in to use
- Suggested normal forms: be in to use
- Decision: accept (review_status: confirmed)

## be include vulnerability in

- Cluster ID: `rc2_c5fdbf26b97bfb5e`
- Assertions: 1
- Phrases: be include vulnerability in
- Suggested normal forms: be include vulnerability in
- Decision: pending (review_status: pending)

## be increasing severity of

- Cluster ID: `rc2_529ba2838c25a565`
- Assertions: 1
- Phrases: be increasing severity of
- Suggested normal forms: be increas severity of
- Decision: pending (review_status: pending)

## be inferred from

- Cluster ID: `rc2_7df06840dfd49bb4`
- Assertions: 1
- Phrases: be inferred from
- Suggested normal forms: be inferr from
- Decision: accept (review_status: confirmed)

## be informed by analysis of

- Cluster ID: `rc2_b15879e9bed5653c`
- Assertions: 1
- Phrases: be informed by analysis of
- Suggested normal forms: be inform by analysi of
- Decision: accept (review_status: confirmed)

## be installed on

- Cluster ID: `rc2_c34b8d262167cbc5`
- Assertions: 1
- Phrases: be installed on
- Suggested normal forms: be install on
- Decision: accept (review_status: confirmed)

## be instructing DeepSeek to use

- Cluster ID: `rc2_ae6febb90d3f5214`
- Assertions: 1
- Phrases: be instructing DeepSeek to use
- Suggested normal forms: be instruct deepseek to use
- Decision: accept (review_status: confirmed)

## be instructing DeepSeek to use actor 's fofoapi.py script for

- Cluster ID: `rc2_c46610814c4fa3c6`
- Assertions: 1
- Phrases: be instructing DeepSeek to use actor 's fofoapi.py script for
- Suggested normal forms: be instruct deepseek to use actor 's fofoapi.py script for
- Decision: pending (review_status: pending)

## be integrated in

- Cluster ID: `rc2_8cce7b9ec8973b67`
- Assertions: 1
- Phrases: be integrated in
- Suggested normal forms: be integrat in
- Decision: pending (review_status: pending)

## be integrated with

- Cluster ID: `rc2_8b5aa60c33878aec`
- Assertions: 1
- Phrases: be integrated with
- Suggested normal forms: be integrat with
- Decision: accept (review_status: confirmed)

## be interact with external content of

- Cluster ID: `rc2_ecf223b16efb6abe`
- Assertions: 1
- Phrases: be interact with external content of
- Suggested normal forms: be interact with external content of
- Decision: pending (review_status: pending)

## be interact with external content of type DotNetAssembly with

- Cluster ID: `rc2_b2c90f880a01ee66`
- Assertions: 1
- Phrases: be interact with external content of type DotNetAssembly with
- Suggested normal forms: be interact with external content of type dotnetassembly with
- Decision: pending (review_status: pending)

## be invoked during

- Cluster ID: `rc2_edd7c2b2c923bbbd`
- Assertions: 1
- Phrases: be invoked during
- Suggested normal forms: be invok dur
- Decision: pending (review_status: pending)

## be issued during

- Cluster ID: `rc2_1baa337c9c8d3c03`
- Assertions: 1
- Phrases: be issued during
- Suggested normal forms: be issu dur
- Decision: accept (review_status: confirmed)

## be issued during April 2026 Patch

- Cluster ID: `rc2_e8d2d2f09c0b5365`
- Assertions: 1
- Phrases: be issued during April 2026 Patch
- Suggested normal forms: be issu dur april 2026 patch
- Decision: accept (review_status: confirmed)

## be joining against

- Cluster ID: `rc2_245face5db5479c2`
- Assertions: 1
- Phrases: be joining against
- Suggested normal forms: be join against
- Decision: accept (review_status: confirmed)

## be know in advance

- Cluster ID: `rc2_b5d080f266e6d273`
- Assertions: 1
- Phrases: be know in advance
- Suggested normal forms: be know in advance
- Decision: accept (review_status: confirmed)

## be known

- Cluster ID: `rc2_f635873a6727352e`
- Assertions: 1
- Phrases: be known
- Suggested normal forms: be known
- Decision: pending (review_status: pending)

## be known as

- Cluster ID: `rc2_87d7faf584cc70e0`
- Assertions: 1
- Phrases: be known as
- Suggested normal forms: be known a
- Decision: pending (review_status: pending)

## be labeled

- Cluster ID: `rc2_4e7df6df64a1ca5d`
- Assertions: 1
- Phrases: be labeled
- Suggested normal forms: be label
- Decision: accept (review_status: confirmed)

## be leading

- Cluster ID: `rc2_ca1d35739469d9d4`
- Assertions: 1
- Phrases: be leading
- Suggested normal forms: be lead
- Decision: pending (review_status: pending)

## be learning

- Cluster ID: `rc2_b68bb55ef1a5f6df`
- Assertions: 1
- Phrases: be learning
- Suggested normal forms: be learn
- Decision: pending (review_status: pending)

## be leveraged to pivot into

- Cluster ID: `rc2_d7bd08634a00f278`
- Assertions: 1
- Phrases: be leveraged to pivot into
- Suggested normal forms: be leverag to pivot into
- Decision: accept (review_status: confirmed)

## be leveraging unique dataset to support

- Cluster ID: `rc2_b5e952b91e27f480`
- Assertions: 1
- Phrases: be leveraging unique dataset to support
- Suggested normal forms: be leverag unique dataset to support
- Decision: pending (review_status: pending)

## be limit

- Cluster ID: `rc2_55cbb566d63e167e`
- Assertions: 1
- Phrases: be limit
- Suggested normal forms: be limit
- Decision: accept (review_status: confirmed)

## be listed in alphabetical order by

- Cluster ID: `rc2_9c7977e31f9318e3`
- Assertions: 1
- Phrases: be listed in alphabetical order by
- Suggested normal forms: be list in alphabetical order by
- Decision: accept (review_status: confirmed)

## be listed on

- Cluster ID: `rc2_82ac6704095e9634`
- Assertions: 1
- Phrases: be listed on
- Suggested normal forms: be list on
- Decision: pending (review_status: pending)

## be listed on first.org website

- Cluster ID: `rc2_1cdd3da251507cd1`
- Assertions: 1
- Phrases: be listed on first.org website
- Suggested normal forms: be list on first.org website
- Decision: pending (review_status: pending)

## be locate

- Cluster ID: `rc2_3895d4e87dba72b2`
- Assertions: 1
- Phrases: be locate
- Suggested normal forms: be locate
- Decision: accept (review_status: confirmed)

## be looking

- Cluster ID: `rc2_9bb8ea1603602961`
- Assertions: 1
- Phrases: be looking
- Suggested normal forms: be look
- Decision: accept (review_status: confirmed)

## be looking at

- Cluster ID: `rc2_9f72e42f132bd19a`
- Assertions: 1
- Phrases: be looking at
- Suggested normal forms: be look at
- Decision: accept (review_status: confirmed)

## be made from

- Cluster ID: `rc2_95cc9a8c9533e987`
- Assertions: 1
- Phrases: be made from
- Suggested normal forms: be made from
- Decision: accept (review_status: confirmed)

## be made to

- Cluster ID: `rc2_bb8ae217b8835d21`
- Assertions: 1
- Phrases: be made to
- Suggested normal forms: be made to
- Decision: pending (review_status: pending)

## be make

- Cluster ID: `rc2_db48156c804cb150`
- Assertions: 1
- Phrases: be make
- Suggested normal forms: be make
- Decision: accept (review_status: confirmed)

## be matched against

- Cluster ID: `rc2_bc3eb0997b3de006`
- Assertions: 1
- Phrases: be matched against
- Suggested normal forms: be match against
- Decision: pending (review_status: pending)

## be mgmt

- Cluster ID: `rc2_9ab8fe48c296ac02`
- Assertions: 1
- Phrases: be mgmt
- Suggested normal forms: be mgmt
- Decision: pending (review_status: pending)

## be missing CPE information for

- Cluster ID: `rc2_a9039d0837999f7d`
- Assertions: 1
- Phrases: be missing CPE information for
- Suggested normal forms: be miss cpe information for
- Decision: pending (review_status: pending)

## be mitigate vulnerability in

- Cluster ID: `rc2_9ecc429be43e18ef`
- Assertions: 1
- Phrases: be mitigate vulnerability in
- Suggested normal forms: be mitigate vulnerability in
- Decision: pending (review_status: pending)

## be more

- Cluster ID: `rc2_5fe476826df1f1e6`
- Assertions: 1
- Phrases: be more
- Suggested normal forms: be more
- Decision: pending (review_status: pending)

## be named

- Cluster ID: `rc2_717b095e3df5a1eb`
- Assertions: 1
- Phrases: be named
- Suggested normal forms: be nam
- Decision: pending (review_status: pending)

## be needed to

- Cluster ID: `rc2_863a1f1f6c3c627e`
- Assertions: 1
- Phrases: be needed to
- Suggested normal forms: be need to
- Decision: accept (review_status: confirmed)

## be needed to break

- Cluster ID: `rc2_db0737043f647c63`
- Assertions: 1
- Phrases: be needed to break
- Suggested normal forms: be need to break
- Decision: pending (review_status: pending)

## be needed to break crypto channel

- Cluster ID: `rc2_6167715048900b91`
- Assertions: 1
- Phrases: be needed to break crypto channel
- Suggested normal forms: be need to break crypto channel
- Decision: pending (review_status: pending)

## be noting removals made from

- Cluster ID: `rc2_8494abe2e8609571`
- Assertions: 1
- Phrases: be noting removals made from
- Suggested normal forms: be not removal made from
- Decision: accept (review_status: confirmed)

## be observed by

- Cluster ID: `rc2_112b2b35205d7598`
- Assertions: 1
- Phrases: be observed by
- Suggested normal forms: be observ by
- Decision: pending (review_status: pending)

## be observed during

- Cluster ID: `rc2_f2d316082b116909`
- Assertions: 1
- Phrases: be observed during
- Suggested normal forms: be observ dur
- Decision: accept (review_status: confirmed)

## be observed to execute via tool like

- Cluster ID: `rc2_77b09b2e8430a620`
- Assertions: 1
- Phrases: be observed to execute via tool like
- Suggested normal forms: be observ to execute via tool like
- Decision: accept (review_status: confirmed)

## be operated by

- Cluster ID: `rc2_622e4a037bafe2c0`
- Assertions: 1
- Phrases: be operated by
- Suggested normal forms: be operat by
- Decision: accept (review_status: confirmed)

## be operated by Department of

- Cluster ID: `rc2_66a2c4661949f475`
- Assertions: 1
- Phrases: be operated by Department of
- Suggested normal forms: be operat by department of
- Decision: accept (review_status: confirmed)

## be operating systems as

- Cluster ID: `rc2_a8dd746b6d70ed28`
- Assertions: 1
- Phrases: be operating systems as
- Suggested normal forms: be operat system a
- Decision: accept (review_status: confirmed)

## be operating through

- Cluster ID: `rc2_748b9ac7024ebfe8`
- Assertions: 1
- Phrases: be operating through
- Suggested normal forms: be operat through
- Decision: accept (review_status: confirmed)

## be ordering of

- Cluster ID: `rc2_435c68ac22685455`
- Assertions: 1
- Phrases: be ordering of
- Suggested normal forms: be order of
- Decision: pending (review_status: pending)

## be outlined in

- Cluster ID: `rc2_5f764e27c7ef25f5`
- Assertions: 1
- Phrases: be outlined in
- Suggested normal forms: be outlin in
- Decision: accept (review_status: confirmed)

## be où

- Cluster ID: `rc2_a68150f3d98f1eb8`
- Assertions: 1
- Phrases: be où
- Suggested normal forms: be où
- Decision: accept (review_status: confirmed)

## be patched by

- Cluster ID: `rc2_5adaa9729a3ed287`
- Assertions: 1
- Phrases: be patched by
- Suggested normal forms: be patch by
- Decision: accept (review_status: confirmed)

## be patched by Microsoft for

- Cluster ID: `rc2_7be34a2f62cc642f`
- Assertions: 1
- Phrases: be patched by Microsoft for
- Suggested normal forms: be patch by microsoft for
- Decision: pending (review_status: pending)

## be patched by Microsoft in

- Cluster ID: `rc2_a88d894b03643cad`
- Assertions: 1
- Phrases: be patched by Microsoft in
- Suggested normal forms: be patch by microsoft in
- Decision: pending (review_status: pending)

## be patched in

- Cluster ID: `rc2_219e89097d1e314c`
- Assertions: 1
- Phrases: be patched in
- Suggested normal forms: be patch in
- Decision: pending (review_status: pending)

## be perform conscious interactions with

- Cluster ID: `rc2_9b4a229b3c370f28`
- Assertions: 1
- Phrases: be perform conscious interactions with
- Suggested normal forms: be perform consciou interaction with
- Decision: accept (review_status: confirmed)

## be pertaining to

- Cluster ID: `rc2_06718323c6ef15ad`
- Assertions: 1
- Phrases: be pertaining to
- Suggested normal forms: be pertain to
- Decision: accept (review_status: confirmed)

## be pour

- Cluster ID: `rc2_e922c5f5e798435b`
- Assertions: 1
- Phrases: be pour
- Suggested normal forms: be pour
- Decision: accept (review_status: confirmed)

## be preferred over those with

- Cluster ID: `rc2_f7446700a9cb6380`
- Assertions: 1
- Phrases: be preferred over those with
- Suggested normal forms: be preferr over those with
- Decision: accept (review_status: confirmed)

## be process

- Cluster ID: `rc2_62065174b9480383`
- Assertions: 1
- Phrases: be process
- Suggested normal forms: be proces
- Decision: accept (review_status: confirmed)

## be produce severity more accurate for

- Cluster ID: `rc2_3df4050df9843d6b`
- Assertions: 1
- Phrases: be produce severity more accurate for
- Suggested normal forms: be produce severity more accurate for
- Decision: accept (review_status: confirmed)

## be producing

- Cluster ID: `rc2_8a262897c0f12313`
- Assertions: 1
- Phrases: be producing
- Suggested normal forms: be produc
- Decision: accept (review_status: confirmed)

## be protect against

- Cluster ID: `rc2_6ebf1d53ab0ceebb`
- Assertions: 1
- Phrases: be protect against
- Suggested normal forms: be protect against
- Decision: accept (review_status: confirmed)

## be protect against campaigns by

- Cluster ID: `rc2_318ff262f56cc335`
- Assertions: 1
- Phrases: be protect against campaigns by
- Suggested normal forms: be protect against campaign by
- Decision: accept (review_status: confirmed)

## be provide

- Cluster ID: `rc2_fd020a25e295e7a3`
- Assertions: 1
- Phrases: be provide
- Suggested normal forms: be provide
- Decision: accept (review_status: confirmed)

## be provide additional CVE information for

- Cluster ID: `rc2_a5107232925f287e`
- Assertions: 1
- Phrases: be provide additional CVE information for
- Suggested normal forms: be provide additional cve information for
- Decision: pending (review_status: pending)

## be provide cyber community

- Cluster ID: `rc2_6be4f0dca33408f5`
- Assertions: 1
- Phrases: be provide cyber community
- Suggested normal forms: be provide cyber community
- Decision: accept (review_status: confirmed)

## be provide to

- Cluster ID: `rc2_81f8376eff91df12`
- Assertions: 1
- Phrases: be provide to
- Suggested normal forms: be provide to
- Decision: pending (review_status: pending)

## be provided by CVE Program for

- Cluster ID: `rc2_585f6a6c5aa72312`
- Assertions: 1
- Phrases: be provided by CVE Program for
- Suggested normal forms: be provid by cve program for
- Decision: accept (review_status: confirmed)

## be provided by Microsoft on

- Cluster ID: `rc2_b1a672de6814b4af`
- Assertions: 1
- Phrases: be provided by Microsoft on
- Suggested normal forms: be provid by microsoft on
- Decision: accept (review_status: confirmed)

## be providing authentication services to components in

- Cluster ID: `rc2_a443baa9d8c6b3f2`
- Assertions: 1
- Phrases: be providing authentication services to components in
- Suggested normal forms: be provid authentication service to component in
- Decision: accept (review_status: confirmed)

## be providing connectivity to components in

- Cluster ID: `rc2_ab8b99c78031e0db`
- Assertions: 1
- Phrases: be providing connectivity to components in
- Suggested normal forms: be provid connectivity to component in
- Decision: accept (review_status: confirmed)

## be providing protection to components in

- Cluster ID: `rc2_1dde4547fca94b5d`
- Assertions: 1
- Phrases: be providing protection to components in
- Suggested normal forms: be provid protection to component in
- Decision: accept (review_status: confirmed)

## be published by CVE Numbering Authority with

- Cluster ID: `rc2_839fa23c753fb4bf`
- Assertions: 1
- Phrases: be published by CVE Numbering Authority with
- Suggested normal forms: be publish by cve number authority with
- Decision: accept (review_status: confirmed)

## be published through

- Cluster ID: `rc2_977b3a9d5c2e1199`
- Assertions: 1
- Phrases: be published through
- Suggested normal forms: be publish through
- Decision: pending (review_status: pending)

## be query

- Cluster ID: `rc2_a16ba248871ed86e`
- Assertions: 1
- Phrases: be query
- Suggested normal forms: be query
- Decision: pending (review_status: pending)

## be rank chess players from

- Cluster ID: `rc2_9b0383a94e8e20ad`
- Assertions: 1
- Phrases: be rank chess players from
- Suggested normal forms: be rank ches player from
- Decision: pending (review_status: pending)

## be rated as more severe

- Cluster ID: `rc2_3bd11ed0507124c7`
- Assertions: 1
- Phrases: be rated as more severe
- Suggested normal forms: be rat a more severe
- Decision: pending (review_status: pending)

## be rated at minimum of

- Cluster ID: `rc2_bcdc09d87f65e643`
- Assertions: 1
- Phrases: be rated at minimum of
- Suggested normal forms: be rat at minimum of
- Decision: pending (review_status: pending)

## be re-assessed for

- Cluster ID: `rc2_c6f89926b4786771`
- Assertions: 1
- Phrases: be re-assessed for
- Suggested normal forms: be re-assess for
- Decision: pending (review_status: pending)

## be re-assessed for specific implementation When assessing vulnerability in

- Cluster ID: `rc2_62cc33e8219ef9cb`
- Assertions: 1
- Phrases: be re-assessed for specific implementation When assessing vulnerability in
- Suggested normal forms: be re-assess for specific implementation when assess vulnerability in
- Decision: pending (review_status: pending)

## be reach CISA 's Known Exploited Vulnerabilities catalogue in

- Cluster ID: `rc2_778b169693b4dc81`
- Assertions: 1
- Phrases: be reach CISA 's Known Exploited Vulnerabilities catalogue in
- Suggested normal forms: be reach cisa 's known exploit vulnerability catalogue in
- Decision: pending (review_status: pending)

## be reduce

- Cluster ID: `rc2_862ce3619bfe63bb`
- Assertions: 1
- Phrases: be reduce
- Suggested normal forms: be reduce
- Decision: accept (review_status: confirmed)

## be reduced to

- Cluster ID: `rc2_e47dd5cef84376cf`
- Assertions: 1
- Phrases: be reduced to
- Suggested normal forms: be reduc to
- Decision: pending (review_status: pending)

## be reduced wherever

- Cluster ID: `rc2_adf852779b143565`
- Assertions: 1
- Phrases: be reduced wherever
- Suggested normal forms: be reduc wherever
- Decision: accept (review_status: confirmed)

## be reduced • After

- Cluster ID: `rc2_5d6850fd1b670943`
- Assertions: 1
- Phrases: be reduced • After
- Suggested normal forms: be reduc • after
- Decision: pending (review_status: pending)

## be referred to as

- Cluster ID: `rc2_f0cf0d192686af1b`
- Assertions: 1
- Phrases: be referred to as
- Suggested normal forms: be referr to a
- Decision: pending (review_status: pending)

## be referred to throughout

- Cluster ID: `rc2_845d241e67fcb3af`
- Assertions: 1
- Phrases: be referred to throughout
- Suggested normal forms: be referr to throughout
- Decision: pending (review_status: pending)

## be remove

- Cluster ID: `rc2_4390bc4e74538739`
- Assertions: 1
- Phrases: be remove
- Suggested normal forms: be remove
- Decision: pending (review_status: pending)

## be renamed to Exploit

- Cluster ID: `rc2_49d953724b43643a`
- Assertions: 1
- Phrases: be renamed to Exploit
- Suggested normal forms: be renam to exploit
- Decision: pending (review_status: pending)

## be renamed to Exploit Maturity with

- Cluster ID: `rc2_337d5881ac581328`
- Assertions: 1
- Phrases: be renamed to Exploit Maturity with
- Suggested normal forms: be renam to exploit maturity with
- Decision: pending (review_status: pending)

## be requested by

- Cluster ID: `rc2_fcd62263ac6eebf5`
- Assertions: 1
- Phrases: be requested by
- Suggested normal forms: be request by
- Decision: pending (review_status: pending)

## be requested by victim

- Cluster ID: `rc2_e374fc1df5fa7f55`
- Assertions: 1
- Phrases: be requested by victim
- Suggested normal forms: be request by victim
- Decision: pending (review_status: pending)

## be requested by victim in to

- Cluster ID: `rc2_fa8e07873c4139af`
- Assertions: 1
- Phrases: be requested by victim in to
- Suggested normal forms: be request by victim in to
- Decision: pending (review_status: pending)

## be required to enable

- Cluster ID: `rc2_6ca81f697bd95d9f`
- Assertions: 1
- Phrases: be required to enable
- Suggested normal forms: be requir to enable
- Decision: accept (review_status: confirmed)

## be requiring unauthenticated form with

- Cluster ID: `rc2_ab85ad20d1ff3b1c`
- Assertions: 1
- Phrases: be requiring unauthenticated form with
- Suggested normal forms: be requir unauthenticat form with
- Decision: accept (review_status: confirmed)

## be responding to

- Cluster ID: `rc2_b19f55c15dbdc14e`
- Assertions: 1
- Phrases: be responding to
- Suggested normal forms: be respond to
- Decision: accept (review_status: confirmed)

## be restrict

- Cluster ID: `rc2_e0f7e42c8b55f4e8`
- Assertions: 1
- Phrases: be restrict
- Suggested normal forms: be restrict
- Decision: accept (review_status: confirmed)

## be restrict MLflow interface to

- Cluster ID: `rc2_768886505669c9fc`
- Assertions: 1
- Phrases: be restrict MLflow interface to
- Suggested normal forms: be restrict mlflow interface to
- Decision: pending (review_status: pending)

## be risk

- Cluster ID: `rc2_38d7329a1478d6a1`
- Assertions: 1
- Phrases: be risk
- Suggested normal forms: be risk
- Decision: pending (review_status: pending)

## be run it for

- Cluster ID: `rc2_ddc8989b13180e5a`
- Assertions: 1
- Phrases: be run it for
- Suggested normal forms: be run it for
- Decision: accept (review_status: confirmed)

## be run method with

- Cluster ID: `rc2_6ac76144d83380ec`
- Assertions: 1
- Phrases: be run method with
- Suggested normal forms: be run method with
- Decision: accept (review_status: confirmed)

## be running in

- Cluster ID: `rc2_0cfb350c550e82d2`
- Assertions: 1
- Phrases: be running in
- Suggested normal forms: be runn in
- Decision: accept (review_status: confirmed)

## be scored as Network In

- Cluster ID: `rc2_829ff26ca5583d57`
- Assertions: 1
- Phrases: be scored as Network In
- Suggested normal forms: be scor a network in
- Decision: pending (review_status: pending)

## be scored as Total

- Cluster ID: `rc2_aac1e2c6f3a22025`
- Assertions: 1
- Phrases: be scored as Total
- Suggested normal forms: be scor a total
- Decision: pending (review_status: pending)

## be scored if those

- Cluster ID: `rc2_40f7088fb5ca4597`
- Assertions: 1
- Phrases: be scored if those
- Suggested normal forms: be scor if those
- Decision: pending (review_status: pending)

## be scoring on

- Cluster ID: `rc2_3f246c03ed4c81f1`
- Assertions: 1
- Phrases: be scoring on
- Suggested normal forms: be scor on
- Decision: pending (review_status: pending)

## be selected of

- Cluster ID: `rc2_8bdde03eb4de4f33`
- Assertions: 1
- Phrases: be selected of
- Suggested normal forms: be select of
- Decision: accept (review_status: confirmed)

## be send crafted IKE traffic to

- Cluster ID: `rc2_44e454c7de0649e1`
- Assertions: 1
- Phrases: be send crafted IKE traffic to
- Suggested normal forms: be send craft ike traffic to
- Decision: accept (review_status: confirmed)

## be set

- Cluster ID: `rc2_13bffd2d87f5216b`
- Assertions: 1
- Phrases: be set
- Suggested normal forms: be set
- Decision: accept (review_status: confirmed)

## be set How

- Cluster ID: `rc2_7005f703ef19a971`
- Assertions: 1
- Phrases: be set How
- Suggested normal forms: be set how
- Decision: accept (review_status: confirmed)

## be set as

- Cluster ID: `rc2_23e83cc5873572ca`
- Assertions: 1
- Phrases: be set as
- Suggested normal forms: be set a
- Decision: pending (review_status: pending)

## be set by

- Cluster ID: `rc2_074b381f9d13965b`
- Assertions: 1
- Phrases: be set by
- Suggested normal forms: be set by
- Decision: accept (review_status: confirmed)

## be set to additional special value of

- Cluster ID: `rc2_54ee3df18ce9d959`
- Assertions: 1
- Phrases: be set to additional special value of
- Suggested normal forms: be set to additional special value of
- Decision: pending (review_status: pending)

## be set to new instance of

- Cluster ID: `rc2_70e2d91588725119`
- Assertions: 1
- Phrases: be set to new instance of
- Suggested normal forms: be set to new instance of
- Decision: pending (review_status: pending)

## be set to overlap

- Cluster ID: `rc2_41b9d3d9a0e90ea8`
- Assertions: 1
- Phrases: be set to overlap
- Suggested normal forms: be set to overlap
- Decision: pending (review_status: pending)

## be shared by

- Cluster ID: `rc2_1f8ad3232aa67143`
- Assertions: 1
- Phrases: be shared by
- Suggested normal forms: be shar by
- Decision: pending (review_status: pending)

## be sharing with

- Cluster ID: `rc2_24814df97186db9f`
- Assertions: 1
- Phrases: be sharing with
- Suggested normal forms: be shar with
- Decision: accept (review_status: confirmed)

## be sorted by

- Cluster ID: `rc2_e398bb9afc0059a0`
- Assertions: 1
- Phrases: be sorted by
- Suggested normal forms: be sort by
- Decision: pending (review_status: pending)

## be spanning

- Cluster ID: `rc2_d936e3a6881cacb2`
- Assertions: 1
- Phrases: be spanning
- Suggested normal forms: be spann
- Decision: accept (review_status: confirmed)

## be successful

- Cluster ID: `rc2_f1d817e30e4eabce`
- Assertions: 1
- Phrases: be successful
- Suggested normal forms: be successful
- Decision: pending (review_status: pending)

## be supplemented with analysis of

- Cluster ID: `rc2_23f122a1837641aa`
- Assertions: 1
- Phrases: be supplemented with analysis of
- Suggested normal forms: be supplement with analysi of
- Decision: accept (review_status: confirmed)

## be taken in context of

- Cluster ID: `rc2_82faba3521b5a418`
- Assertions: 1
- Phrases: be taken in context of
- Suggested normal forms: be taken in context of
- Decision: pending (review_status: pending)

## be taken into consideration for

- Cluster ID: `rc2_de40c7bf0eea25bf`
- Assertions: 1
- Phrases: be taken into consideration for
- Suggested normal forms: be taken into consideration for
- Decision: pending (review_status: pending)

## be taken into consideration when

- Cluster ID: `rc2_bfe621a1a86bc694`
- Assertions: 1
- Phrases: be taken into consideration when
- Suggested normal forms: be taken into consideration when
- Decision: pending (review_status: pending)

## be talk about

- Cluster ID: `rc2_77ec95cde1f87d4c`
- Assertions: 1
- Phrases: be talk about
- Suggested normal forms: be talk about
- Decision: accept (review_status: confirmed)

## be to run Availability impacts For

- Cluster ID: `rc2_844881993c2259fe`
- Assertions: 1
- Phrases: be to run Availability impacts For
- Suggested normal forms: be to run availability impact for
- Decision: accept (review_status: confirmed)

## be to run listening service with administrator privileges For

- Cluster ID: `rc2_75bd70d2884e0847`
- Assertions: 1
- Phrases: be to run listening service with administrator privileges For
- Suggested normal forms: be to run listen service with administrator privilege for
- Decision: accept (review_status: confirmed)

## be traverse directories beyond

- Cluster ID: `rc2_2f9dba91fb5905a2`
- Assertions: 1
- Phrases: be traverse directories beyond
- Suggested normal forms: be traverse directory beyond
- Decision: accept (review_status: confirmed)

## be treated

- Cluster ID: `rc2_e917bbe508800aab`
- Assertions: 1
- Phrases: be treated
- Suggested normal forms: be treat
- Decision: pending (review_status: pending)

## be treated as

- Cluster ID: `rc2_6e20e7a8a661795e`
- Assertions: 1
- Phrases: be treated as
- Suggested normal forms: be treat a
- Decision: accept (review_status: confirmed)

## be treated as proof of

- Cluster ID: `rc2_cb3c729d45adc20e`
- Assertions: 1
- Phrases: be treated as proof of
- Suggested normal forms: be treat a proof of
- Decision: pending (review_status: pending)

## be treated as proof of malicious activity by

- Cluster ID: `rc2_967ad12e5cc1885b`
- Assertions: 1
- Phrases: be treated as proof of malicious activity by
- Suggested normal forms: be treat a proof of maliciou activity by
- Decision: pending (review_status: pending)

## be treated to

- Cluster ID: `rc2_fb4027ca011d8df3`
- Assertions: 1
- Phrases: be treated to
- Suggested normal forms: be treat to
- Decision: pending (review_status: pending)

## be understood by

- Cluster ID: `rc2_9344b2a7b1ae03f6`
- Assertions: 1
- Phrases: be understood by
- Suggested normal forms: be understood by
- Decision: pending (review_status: pending)

## be updated

- Cluster ID: `rc2_7c4ce622b7742d1e`
- Assertions: 1
- Phrases: be updated
- Suggested normal forms: be updat
- Decision: pending (review_status: pending)

## be updated by

- Cluster ID: `rc2_14bfafbbdba851e6`
- Assertions: 1
- Phrases: be updated by
- Suggested normal forms: be updat by
- Decision: pending (review_status: pending)

## be use as

- Cluster ID: `rc2_5f698d148a26f6e6`
- Assertions: 1
- Phrases: be use as
- Suggested normal forms: be use a
- Decision: accept (review_status: confirmed)

## be use in

- Cluster ID: `rc2_6e1c86e5e02f330c`
- Assertions: 1
- Phrases: be use in
- Suggested normal forms: be use in
- Decision: accept (review_status: confirmed)

## be used by programs For

- Cluster ID: `rc2_6d99bd037f8600ba`
- Assertions: 1
- Phrases: be used by programs For
- Suggested normal forms: be us by program for
- Decision: pending (review_status: pending)

## be used for calculation of

- Cluster ID: `rc2_ec8b0592b246a301`
- Assertions: 1
- Phrases: be used for calculation of
- Suggested normal forms: be us for calculation of
- Decision: pending (review_status: pending)

## be used for calculation of score In

- Cluster ID: `rc2_9ebb1096a3f4210f`
- Assertions: 1
- Phrases: be used for calculation of score In
- Suggested normal forms: be us for calculation of score in
- Decision: pending (review_status: pending)

## be used in equations with

- Cluster ID: `rc2_8245fb9506f1f16d`
- Assertions: 1
- Phrases: be used in equations with
- Suggested normal forms: be us in equation with
- Decision: pending (review_status: pending)

## be used to align with

- Cluster ID: `rc2_4ba94640f66596e7`
- Assertions: 1
- Phrases: be used to align with
- Suggested normal forms: be us to align with
- Decision: pending (review_status: pending)

## be used to demonstrate existence of

- Cluster ID: `rc2_92b9ae47e8eba3ba`
- Assertions: 1
- Phrases: be used to demonstrate existence of
- Suggested normal forms: be us to demonstrate existence of
- Decision: accept (review_status: confirmed)

## be used to derive quantitative score for

- Cluster ID: `rc2_2a6f242457a4f9e7`
- Assertions: 1
- Phrases: be used to derive quantitative score for
- Suggested normal forms: be us to derive quantitative score for
- Decision: pending (review_status: pending)

## be used to enrich

- Cluster ID: `rc2_bd3a85533e74d79d`
- Assertions: 1
- Phrases: be used to enrich
- Suggested normal forms: be us to enrich
- Decision: pending (review_status: pending)

## be used to represent small change in

- Cluster ID: `rc2_1a1b3c0f47167c81`
- Assertions: 1
- Phrases: be used to represent small change in
- Suggested normal forms: be us to represent small change in
- Decision: pending (review_status: pending)

## be used to score

- Cluster ID: `rc2_dc095b4c98a7a76d`
- Assertions: 1
- Phrases: be used to score
- Suggested normal forms: be us to score
- Decision: pending (review_status: pending)

## be used to take

- Cluster ID: `rc2_351c52276c685edf`
- Assertions: 1
- Phrases: be used to take
- Suggested normal forms: be us to take
- Decision: pending (review_status: pending)

## be used to turn

- Cluster ID: `rc2_b85d27753ec68416`
- Assertions: 1
- Phrases: be used to turn
- Suggested normal forms: be us to turn
- Decision: pending (review_status: pending)

## be used to turn expert comparisons into

- Cluster ID: `rc2_45db4e382967d227`
- Assertions: 1
- Phrases: be used to turn expert comparisons into
- Suggested normal forms: be us to turn expert comparison into
- Decision: pending (review_status: pending)

## be using conventional workflows with

- Cluster ID: `rc2_b69c9a7a24f9eb94`
- Assertions: 1
- Phrases: be using conventional workflows with
- Suggested normal forms: be us conventional workflow with
- Decision: accept (review_status: confirmed)

## be using more time from

- Cluster ID: `rc2_067d6787afd63c5b`
- Assertions: 1
- Phrases: be using more time from
- Suggested normal forms: be us more time from
- Decision: pending (review_status: pending)

## be utilize Environmental Metric Group to improve quality of

- Cluster ID: `rc2_8a1a2fbe2c06e3b1`
- Assertions: 1
- Phrases: be utilize Environmental Metric Group to improve quality of
- Suggested normal forms: be utilize environmental metric group to improve quality of
- Decision: accept (review_status: confirmed)

## be viewed in incident view of

- Cluster ID: `rc2_7f34144252688de8`
- Assertions: 1
- Phrases: be viewed in incident view of
- Suggested normal forms: be view in incident view of
- Decision: pending (review_status: pending)

## be win

- Cluster ID: `rc2_18075323cfc27666`
- Assertions: 1
- Phrases: be win
- Suggested normal forms: be win
- Decision: accept (review_status: confirmed)

## be wrapping that

- Cluster ID: `rc2_2dd607dc0745a607`
- Assertions: 1
- Phrases: be wrapping that
- Suggested normal forms: be wrapp that
- Decision: pending (review_status: pending)

## began

- Cluster ID: `rc2_b3cebf40b6c091af`
- Assertions: 1
- Phrases: began
- Suggested normal forms: began
- Decision: accept (review_status: confirmed)

## began around

- Cluster ID: `rc2_279d6b1f2e16a228`
- Assertions: 1
- Phrases: began around
- Suggested normal forms: began around
- Decision: pending (review_status: pending)

## began reporting exploitation in

- Cluster ID: `rc2_51c5980e42551a32`
- Assertions: 1
- Phrases: began reporting exploitation in
- Suggested normal forms: began report exploitation in
- Decision: pending (review_status: pending)

## begin to

- Cluster ID: `rc2_36f1602a6ba4f085`
- Assertions: 1
- Phrases: begin to
- Suggested normal forms: begin to
- Decision: pending (review_status: pending)

## begin to construct

- Cluster ID: `rc2_7d91fbd7d158cf33`
- Assertions: 1
- Phrases: begin to construct
- Suggested normal forms: begin to construct
- Decision: accept (review_status: confirmed)

## begins in

- Cluster ID: `rc2_81797050ab567772`
- Assertions: 1
- Phrases: begins in
- Suggested normal forms: begin in
- Decision: pending (review_status: pending)

## belongs to

- Cluster ID: `rc2_36b5ac4e2e79a653`
- Assertions: 1
- Phrases: belongs to
- Suggested normal forms: belong to
- Decision: pending (review_status: pending)

## break secure measures

- Cluster ID: `rc2_a0152b705050b04e`
- Assertions: 1
- Phrases: break secure measures
- Suggested normal forms: break secure measure
- Decision: pending (review_status: pending)

## calculates

- Cluster ID: `rc2_edca249d8d1f9a5b`
- Assertions: 1
- Phrases: calculates
- Suggested normal forms: calculate
- Decision: pending (review_status: pending)

## call Deserialize with base64-encoded string as

- Cluster ID: `rc2_a567d4e1ab44ac92`
- Assertions: 1
- Phrases: call Deserialize with base64-encoded string as
- Suggested normal forms: call deserialize with base64-encod str a
- Decision: accept (review_status: confirmed)

## calls to fetch

- Cluster ID: `rc2_cc24e541fbc458c0`
- Assertions: 1
- Phrases: calls to fetch
- Suggested normal forms: call to fetch
- Decision: accept (review_status: confirmed)

## capture effects of

- Cluster ID: `rc2_75ce9c0f65a6de60`
- Assertions: 1
- Phrases: capture effects of
- Suggested normal forms: capture effect of
- Decision: accept (review_status: confirmed)

## captures answer to

- Cluster ID: `rc2_33d4a4352d33ace0`
- Assertions: 1
- Phrases: captures answer to
- Suggested normal forms: capture answer to
- Decision: accept (review_status: confirmed)

## captures variables of

- Cluster ID: `rc2_7eaf7a4db0be92b0`
- Assertions: 1
- Phrases: captures variables of
- Suggested normal forms: capture variable of
- Decision: pending (review_status: pending)

## captures wider repercussions adversary control of

- Cluster ID: `rc2_f18d64637f24b032`
- Assertions: 1
- Phrases: captures wider repercussions adversary control of
- Suggested normal forms: capture wider repercussion adversary control of
- Decision: pending (review_status: pending)

## carried out by

- Cluster ID: `rc2_a7b021b134184526`
- Assertions: 1
- Phrases: carried out by
- Suggested normal forms: carri out by
- Decision: pending (review_status: pending)

## carry

- Cluster ID: `rc2_6ef49cacb4c39f8f`
- Assertions: 1
- Phrases: carry
- Suggested normal forms: carry
- Decision: pending (review_status: pending)

## caused

- Cluster ID: `rc2_d98221bdeb3aab99`
- Assertions: 1
- Phrases: caused
- Suggested normal forms: caus
- Decision: pending (review_status: pending)

## caused exposure of

- Cluster ID: `rc2_fb5b15aff089ff90`
- Assertions: 1
- Phrases: caused exposure of
- Suggested normal forms: caus exposure of
- Decision: accept (review_status: confirmed)

## caused exposure of operation

- Cluster ID: `rc2_8448eed202b429dc`
- Assertions: 1
- Phrases: caused exposure of operation
- Suggested normal forms: caus exposure of operation
- Decision: accept (review_status: confirmed)

## causes MLflow server to query cloud provider metadata endpoint without

- Cluster ID: `rc2_0f5f245b0b5a8e44`
- Assertions: 1
- Phrases: causes MLflow server to query cloud provider metadata endpoint without
- Suggested normal forms: cause mlflow server to query cloud provider metadata endpoint without
- Decision: pending (review_status: pending)

## causes it to disclose plaintext password of

- Cluster ID: `rc2_561b1d8337585753`
- Assertions: 1
- Phrases: causes it to disclose plaintext password of
- Suggested normal forms: cause it to disclose plaintext password of
- Decision: accept (review_status: confirmed)

## causes unauthorized modification of

- Cluster ID: `rc2_eef96d8a4fc2f55c`
- Assertions: 1
- Phrases: causes unauthorized modification of
- Suggested normal forms: cause unauthoriz modification of
- Decision: pending (review_status: pending)

## causes web server to disclose plaintext password of

- Cluster ID: `rc2_01e6d287402d3359`
- Assertions: 1
- Phrases: causes web server to disclose plaintext password of
- Suggested normal forms: cause web server to disclose plaintext password of
- Decision: accept (review_status: confirmed)

## cette même page de

- Cluster ID: `rc2_997279ed55af63d0`
- Assertions: 1
- Phrases: cette même page de
- Suggested normal forms: cette même page de
- Decision: pending (review_status: pending)

## change Attack Complexity to

- Cluster ID: `rc2_a160e94eee96fee9`
- Assertions: 1
- Phrases: change Attack Complexity to
- Suggested normal forms: change attack complexity to
- Decision: accept (review_status: confirmed)

## change across

- Cluster ID: `rc2_86e55cbbc1bfb303`
- Assertions: 1
- Phrases: change across
- Suggested normal forms: change acros
- Decision: pending (review_status: pending)

## chose to bind

- Cluster ID: `rc2_764f472f3319c350`
- Assertions: 1
- Phrases: chose to bind
- Suggested normal forms: chose to bind
- Decision: accept (review_status: confirmed)

## cloned public repository for

- Cluster ID: `rc2_8f3eeac0f1d075c8`
- Assertions: 1
- Phrases: cloned public repository for
- Suggested normal forms: clon public repository for
- Decision: pending (review_status: pending)

## code

- Cluster ID: `rc2_5694d08a2e53ffca`
- Assertions: 1
- Phrases: code
- Suggested normal forms: code
- Decision: accept (review_status: confirmed)

## collect

- Cluster ID: `rc2_81824c90f8a5276b`
- Assertions: 1
- Phrases: collect
- Suggested normal forms: collect
- Decision: pending (review_status: pending)

## collect from expert analysts

- Cluster ID: `rc2_e476ad048d370ead`
- Assertions: 1
- Phrases: collect from expert analysts
- Suggested normal forms: collect from expert analyst
- Decision: pending (review_status: pending)

## compares to

- Cluster ID: `rc2_1b014f4e46071337`
- Assertions: 1
- Phrases: compares to
- Suggested normal forms: compare to
- Decision: accept (review_status: confirmed)

## compute

- Cluster ID: `rc2_b04a12f6483ea24a`
- Assertions: 1
- Phrases: compute
- Suggested normal forms: compute
- Decision: accept (review_status: confirmed)

## conducted

- Cluster ID: `rc2_85ca6d6d291c070d`
- Assertions: 1
- Phrases: conducted
- Suggested normal forms: conduct
- Decision: pending (review_status: pending)

## conducted autonomous research After

- Cluster ID: `rc2_6fb2c37f0d94282a`
- Assertions: 1
- Phrases: conducted autonomous research After
- Suggested normal forms: conduct autonomou research after
- Decision: pending (review_status: pending)

## conducted autonomous research to identify

- Cluster ID: `rc2_69f98f0d185a3150`
- Assertions: 1
- Phrases: conducted autonomous research to identify
- Suggested normal forms: conduct autonomou research to identify
- Decision: pending (review_status: pending)

## conducted autonomous vulnerability enumeration

- Cluster ID: `rc2_b280c2c3bdb01ff4`
- Assertions: 1
- Phrases: conducted autonomous vulnerability enumeration
- Suggested normal forms: conduct autonomou vulnerability enumeration
- Decision: accept (review_status: confirmed)

## conducted autonomous vulnerability enumeration downloaded attempted exploits against

- Cluster ID: `rc2_3149b15b5efbc73e`
- Assertions: 1
- Phrases: conducted autonomous vulnerability enumeration downloaded attempted exploits against
- Suggested normal forms: conduct autonomou vulnerability enumeration download attempt exploit against
- Decision: pending (review_status: pending)

## conducted autonomous vulnerability enumeration downloaded public exploits against

- Cluster ID: `rc2_7ae5deec0375dcf2`
- Assertions: 1
- Phrases: conducted autonomous vulnerability enumeration downloaded public exploits against
- Suggested normal forms: conduct autonomou vulnerability enumeration download public exploit against
- Decision: pending (review_status: pending)

## configured Claude Code

- Cluster ID: `rc2_a13003fc082ddeff`
- Assertions: 1
- Phrases: configured Claude Code
- Suggested normal forms: configur claude code
- Decision: pending (review_status: pending)

## configured Claude Code with

- Cluster ID: `rc2_bb897e4eec384bc1`
- Assertions: 1
- Phrases: configured Claude Code with
- Suggested normal forms: configur claude code with
- Decision: pending (review_status: pending)

## configured multiple large language models In

- Cluster ID: `rc2_29401d5a721d221c`
- Assertions: 1
- Phrases: configured multiple large language models In
- Suggested normal forms: configur multiple large language model in
- Decision: accept (review_status: confirmed)

## configured multiple large language models consistent with

- Cluster ID: `rc2_9e59613073e418d6`
- Assertions: 1
- Phrases: configured multiple large language models consistent with
- Suggested normal forms: configur multiple large language model consistent with
- Decision: pending (review_status: pending)

## configured system to limit

- Cluster ID: `rc2_40bc47598b6a1f40`
- Assertions: 1
- Phrases: configured system to limit
- Suggested normal forms: configur system to limit
- Decision: accept (review_status: confirmed)

## confirmed active exploitation of

- Cluster ID: `rc2_368f72f6a5ec8a20`
- Assertions: 1
- Phrases: confirmed active exploitation of
- Suggested normal forms: confirm active exploitation of
- Decision: pending (review_status: pending)

## confirmed active exploitation of CVE-2026-20349 on

- Cluster ID: `rc2_51fbbca64ef351bd`
- Assertions: 1
- Phrases: confirmed active exploitation of CVE-2026-20349 on
- Suggested normal forms: confirm active exploitation of cve-2026-20349 on
- Decision: pending (review_status: pending)

## confirmed n8n as

- Cluster ID: `rc2_6534e4cc8a8ddcd1`
- Assertions: 1
- Phrases: confirmed n8n as
- Suggested normal forms: confirm n8n a
- Decision: pending (review_status: pending)

## consolidated remote access onto Cisco ASA during

- Cluster ID: `rc2_6ba482088fe1a414`
- Assertions: 1
- Phrases: consolidated remote access onto Cisco ASA during
- Suggested normal forms: consolidat remote acces onto cisco asa dur
- Decision: accept (review_status: confirmed)

## consolidated remote access onto FTD hardware during

- Cluster ID: `rc2_b5853994cc59f3f9`
- Assertions: 1
- Phrases: consolidated remote access onto FTD hardware during
- Suggested normal forms: consolidat remote acces onto ftd hardware dur
- Decision: accept (review_status: confirmed)

## constrain impacts When

- Cluster ID: `rc2_e403dcb94de3b633`
- Assertions: 1
- Phrases: constrain impacts When
- Suggested normal forms: constrain impact when
- Decision: pending (review_status: pending)

## consult

- Cluster ID: `rc2_89fc0f6aa4921aac`
- Assertions: 1
- Phrases: consult
- Suggested normal forms: consult
- Decision: pending (review_status: pending)

## contains SharePoint 's own STS certificate thumbprint

- Cluster ID: `rc2_c1008df02bf1482d`
- Assertions: 1
- Phrases: contains SharePoint 's own STS certificate thumbprint
- Suggested normal forms: contain sharepoint 's own st certificate thumbprint
- Decision: pending (review_status: pending)

## contains authentication bypass vulnerability in

- Cluster ID: `rc2_c04c0ac5eee201df`
- Assertions: 1
- Phrases: contains authentication bypass vulnerability in
- Suggested normal forms: contain authentication bypas vulnerability in
- Decision: accept (review_status: confirmed)

## contains functionality

- Cluster ID: `rc2_f2d7dfc5ab5e1066`
- Assertions: 1
- Phrases: contains functionality
- Suggested normal forms: contain functionality
- Decision: pending (review_status: pending)

## contains out-of-bounds write vulnerability in

- Cluster ID: `rc2_b07c49de20ab7680`
- Assertions: 1
- Phrases: contains out-of-bounds write vulnerability in
- Suggested normal forms: contain out-of-bound write vulnerability in
- Decision: pending (review_status: pending)

## contains web-friendly version of

- Cluster ID: `rc2_da07550753f81971`
- Assertions: 1
- Phrases: contains web-friendly version of
- Suggested normal forms: contain web-friendly version of
- Decision: pending (review_status: pending)

## continued investigating activity As announced in

- Cluster ID: `rc2_8d2b852834e2cc12`
- Assertions: 1
- Phrases: continued investigating activity As announced in
- Suggested normal forms: continu investigat activity a announc in
- Decision: pending (review_status: pending)

## continued investigating infrastructure associated with exploitation of CVE-2026 As announced in

- Cluster ID: `rc2_8dabee9b7e3a86d0`
- Assertions: 1
- Phrases: continued investigating infrastructure associated with exploitation of CVE-2026 As announced in
- Suggested normal forms: continu investigat infrastructure associat with exploitation of cve-2026 a announc in
- Decision: pending (review_status: pending)

## continues to

- Cluster ID: `rc2_509a7aea82f74921`
- Assertions: 1
- Phrases: continues to
- Suggested normal forms: continue to
- Decision: pending (review_status: pending)

## convert

- Cluster ID: `rc2_c47579671ec3e9f3`
- Assertions: 1
- Phrases: convert
- Suggested normal forms: convert
- Decision: pending (review_status: pending)

## convert it to

- Cluster ID: `rc2_16ecc67c5b55b486`
- Assertions: 1
- Phrases: convert it to
- Suggested normal forms: convert it to
- Decision: pending (review_status: pending)

## correlated to other signs of

- Cluster ID: `rc2_e3f79cab45959df6`
- Assertions: 1
- Phrases: correlated to other signs of
- Suggested normal forms: correlat to other sign of
- Decision: pending (review_status: pending)

## craft

- Cluster ID: `rc2_355543f790a3b210`
- Assertions: 1
- Phrases: craft
- Suggested normal forms: craft
- Decision: pending (review_status: pending)

## create

- Cluster ID: `rc2_fa8847b0c3318327`
- Assertions: 1
- Phrases: create
- Suggested normal forms: create
- Decision: pending (review_status: pending)

## created Stakeholder-Specific Vulnerability Categorization system to provide

- Cluster ID: `rc2_94d5388202c42d3f`
- Assertions: 1
- Phrases: created Stakeholder-Specific Vulnerability Categorization system to provide
- Suggested normal forms: creat stakeholder-specific vulnerability categorization system to provide
- Decision: accept (review_status: confirmed)

## dans coin supérieur gauche de

- Cluster ID: `rc2_5e19a5bf9d4a6a41`
- Assertions: 1
- Phrases: dans coin supérieur gauche de
- Suggested normal forms: dan coin supérieur gauche de
- Decision: accept (review_status: confirmed)

## decide on vulnerability response actions consistent with

- Cluster ID: `rc2_04986d338f175bd5`
- Assertions: 1
- Phrases: decide on vulnerability response actions consistent with
- Suggested normal forms: decide on vulnerability response action consistent with
- Decision: accept (review_status: confirmed)

## decide which metric-group-based vector sets define qualitative severity To do

- Cluster ID: `rc2_9e412281b051060a`
- Assertions: 1
- Phrases: decide which metric-group-based vector sets define qualitative severity To do
- Suggested normal forms: decide which metric-group-bas vector set define qualitative severity to
- Decision: pending (review_status: pending)

## decided to go

- Cluster ID: `rc2_03d055a3bae9cca2`
- Assertions: 1
- Phrases: decided to go
- Suggested normal forms: decid to go
- Decision: accept (review_status: confirmed)

## decided to go different route After failing with

- Cluster ID: `rc2_c42fdefe22b2ce03`
- Assertions: 1
- Phrases: decided to go different route After failing with
- Suggested normal forms: decid to go different route after fail with
- Decision: pending (review_status: pending)

## decrease

- Cluster ID: `rc2_b2dc971f4895ca1f`
- Assertions: 1
- Phrases: decrease
- Suggested normal forms: decrease
- Decision: pending (review_status: pending)

## default to

- Cluster ID: `rc2_77d4bf8f382a7fae`
- Assertions: 1
- Phrases: default to
- Suggested normal forms: default to
- Decision: pending (review_status: pending)

## defer

- Cluster ID: `rc2_8f106893acee44fa`
- Assertions: 1
- Phrases: defer
- Suggested normal forms: defer
- Decision: accept (review_status: confirmed)

## defer applying critical vCenter patch how

- Cluster ID: `rc2_c95f91a08d9a1321`
- Assertions: 1
- Phrases: defer applying critical vCenter patch how
- Suggested normal forms: defer apply critical vcenter patch how
- Decision: accept (review_status: confirmed)

## defer applying critical vCenter patch without

- Cluster ID: `rc2_f9197fc537668771`
- Assertions: 1
- Phrases: defer applying critical vCenter patch without
- Suggested normal forms: defer apply critical vcenter patch without
- Decision: accept (review_status: confirmed)

## defer applying critical vCenter patch without accepting active exploitation risk how

- Cluster ID: `rc2_c2a513e52313423b`
- Assertions: 1
- Phrases: defer applying critical vCenter patch without accepting active exploitation risk how
- Suggested normal forms: defer apply critical vcenter patch without accept active exploitation risk how
- Decision: accept (review_status: confirmed)

## define DefaultValues for

- Cluster ID: `rc2_149f9583bc54d6ee`
- Assertions: 1
- Phrases: define DefaultValues for
- Suggested normal forms: define defaultvalue for
- Decision: accept (review_status: confirmed)

## define in model to do something

- Cluster ID: `rc2_9cedb9e7cddc422a`
- Assertions: 1
- Phrases: define in model to do something
- Suggested normal forms: define in model to someth
- Decision: accept (review_status: confirmed)

## defined MethodInstance

- Cluster ID: `rc2_3bf1f7f749e57b36`
- Assertions: 1
- Phrases: defined MethodInstance
- Suggested normal forms: defin methodinstance
- Decision: pending (review_status: pending)

## defined MethodInstance as

- Cluster ID: `rc2_98784e3e09777f25`
- Assertions: 1
- Phrases: defined MethodInstance as
- Suggested normal forms: defin methodinstance a
- Decision: accept (review_status: confirmed)

## defines arbitrary process to

- Cluster ID: `rc2_5f81b36f05309df7`
- Assertions: 1
- Phrases: defines arbitrary process to
- Suggested normal forms: define arbitrary proces to
- Decision: pending (review_status: pending)

## defines argument for

- Cluster ID: `rc2_d193f831fbc3301a`
- Assertions: 1
- Phrases: defines argument for
- Suggested normal forms: define argument for
- Decision: accept (review_status: confirmed)

## deliver

- Cluster ID: `rc2_fa2dcc238152c873`
- Assertions: 1
- Phrases: deliver
- Suggested normal forms: deliver
- Decision: pending (review_status: pending)

## demonstrates impact to

- Cluster ID: `rc2_441b509bcb73c935`
- Assertions: 1
- Phrases: demonstrates impact to
- Suggested normal forms: demonstrate impact to
- Decision: accept (review_status: confirmed)

## depends on

- Cluster ID: `rc2_60cd72f34aebea1e`
- Assertions: 1
- Phrases: depends on
- Suggested normal forms: depend on
- Decision: accept (review_status: confirmed)

## depends on conditions beyond

- Cluster ID: `rc2_a9a1d0a2c09e56cb`
- Assertions: 1
- Phrases: depends on conditions beyond
- Suggested normal forms: depend on condition beyond
- Decision: pending (review_status: pending)

## deployed open-source reverse_ssh framework After

- Cluster ID: `rc2_a3e8fcbfb6f7f004`
- Assertions: 1
- Phrases: deployed open-source reverse_ssh framework After
- Suggested normal forms: deploy open-source reverse_ssh framework after
- Decision: pending (review_status: pending)

## describe how

- Cluster ID: `rc2_86d6fd4370bc4a97`
- Assertions: 1
- Phrases: describe how
- Suggested normal forms: describe how
- Decision: pending (review_status: pending)

## describe same targeting logic

- Cluster ID: `rc2_64b5ba6490d8999d`
- Assertions: 1
- Phrases: describe same targeting logic
- Suggested normal forms: describe same target logic
- Decision: pending (review_status: pending)

## described

- Cluster ID: `rc2_c61b6446c46a45fc`
- Assertions: 1
- Phrases: described
- Suggested normal forms: describ
- Decision: pending (review_status: pending)

## described it as critical directory traversal vulnerability in

- Cluster ID: `rc2_31e4315fdf87d0ff`
- Assertions: 1
- Phrases: described it as critical directory traversal vulnerability in
- Suggested normal forms: describ it a critical directory traversal vulnerability in
- Decision: pending (review_status: pending)

## describes issue as

- Cluster ID: `rc2_f6cf2274ae8e2c4a`
- Assertions: 1
- Phrases: describes issue as
- Suggested normal forms: describe issue a
- Decision: accept (review_status: confirmed)

## deserialize

- Cluster ID: `rc2_3ef7bf7f4c1cd006`
- Assertions: 1
- Phrases: deserialize
- Suggested normal forms: deserialize
- Decision: accept (review_status: confirmed)

## detects

- Cluster ID: `rc2_cfacfd3ec33b9608`
- Assertions: 1
- Phrases: detects
- Suggested normal forms: detect
- Decision: accept (review_status: confirmed)

## determined following preliminary metrics subgroups

- Cluster ID: `rc2_ce0ae8033faf74d6`
- Assertions: 1
- Phrases: determined following preliminary metrics subgroups
- Suggested normal forms: determin follow preliminary metric subgroup
- Decision: accept (review_status: confirmed)

## developed for offensive use

- Cluster ID: `rc2_02e570372036f464`
- Assertions: 1
- Phrases: developed for offensive use
- Suggested normal forms: develop for offensive use
- Decision: accept (review_status: confirmed)

## deviate from

- Cluster ID: `rc2_c2428955ff9d773f`
- Assertions: 1
- Phrases: deviate from
- Suggested normal forms: deviate from
- Decision: pending (review_status: pending)

## did achieve

- Cluster ID: `rc2_8520825114d70f2c`
- Assertions: 1
- Phrases: did achieve
- Suggested normal forms: did achieve
- Decision: pending (review_status: pending)

## did do anything beyond

- Cluster ID: `rc2_f77e641e7949eed2`
- Assertions: 1
- Phrases: did do anything beyond
- Suggested normal forms: did anyth beyond
- Decision: pending (review_status: pending)

## did encompass more traditional vulnerability research such as

- Cluster ID: `rc2_298837a82483022b`
- Assertions: 1
- Phrases: did encompass more traditional vulnerability research such as
- Suggested normal forms: did encompas more traditional vulnerability research such a
- Decision: accept (review_status: confirmed)

## did include requests for

- Cluster ID: `rc2_330214926bc2fed0`
- Assertions: 1
- Phrases: did include requests for
- Suggested normal forms: did include request for
- Decision: pending (review_status: pending)

## differ from

- Cluster ID: `rc2_bccbc876f5399e37`
- Assertions: 1
- Phrases: differ from
- Suggested normal forms: differ from
- Decision: pending (review_status: pending)

## differ on cause of

- Cluster ID: `rc2_84f4827b98be05d1`
- Assertions: 1
- Phrases: differ on cause of
- Suggested normal forms: differ on cause of
- Decision: accept (review_status: confirmed)

## digest

- Cluster ID: `rc2_0bf474896363505e`
- Assertions: 1
- Phrases: digest
- Suggested normal forms: digest
- Decision: accept (review_status: confirmed)

## direct how

- Cluster ID: `rc2_2e91dba18e6faf22`
- Assertions: 1
- Phrases: direct how
- Suggested normal forms: direct how
- Decision: pending (review_status: pending)

## directed agencies to

- Cluster ID: `rc2_bfaa75233febcb80`
- Assertions: 1
- Phrases: directed agencies to
- Suggested normal forms: direct agency to
- Decision: accept (review_status: confirmed)

## directed agencies to remediate

- Cluster ID: `rc2_f537310e67c43175`
- Assertions: 1
- Phrases: directed agencies to remediate
- Suggested normal forms: direct agency to remediate
- Decision: accept (review_status: confirmed)

## disables

- Cluster ID: `rc2_e9d8992f348162fd`
- Assertions: 1
- Phrases: disables
- Suggested normal forms: disable
- Decision: pending (review_status: pending)

## disclosed CVE-2026-59310 on

- Cluster ID: `rc2_ac2cc3c6deb605c0`
- Assertions: 1
- Phrases: disclosed CVE-2026-59310 on
- Suggested normal forms: disclos cve-2026-59310 on
- Decision: accept (review_status: confirmed)

## discloses

- Cluster ID: `rc2_99d79cff2cb32aac`
- Assertions: 1
- Phrases: discloses
- Suggested normal forms: disclose
- Decision: accept (review_status: confirmed)

## discover target to use by

- Cluster ID: `rc2_8d7795a5ad2afa6a`
- Assertions: 1
- Phrases: discover target to use by
- Suggested normal forms: discover target to use by
- Decision: pending (review_status: pending)

## discover target to use by first contacting target SharePoint servers domain controller over

- Cluster ID: `rc2_5e659c0d5c8f9599`
- Assertions: 1
- Phrases: discover target to use by first contacting target SharePoint servers domain controller over
- Suggested normal forms: discover target to use by first contact target sharepoint server domain controller over
- Decision: pending (review_status: pending)

## discovers potential SharePoint users via

- Cluster ID: `rc2_c384df13c7341ef1`
- Assertions: 1
- Phrases: discovers potential SharePoint users via
- Suggested normal forms: discover potential sharepoint user via
- Decision: pending (review_status: pending)

## discussed

- Cluster ID: `rc2_d6a919ef536282bf`
- Assertions: 1
- Phrases: discussed
- Suggested normal forms: discuss
- Decision: pending (review_status: pending)

## discussed to

- Cluster ID: `rc2_7d98f98395f43d0e`
- Assertions: 1
- Phrases: discussed to
- Suggested normal forms: discuss to
- Decision: pending (review_status: pending)

## discusses leveraging BDC models for

- Cluster ID: `rc2_96ea9797feed6b5f`
- Assertions: 1
- Phrases: discusses leveraging BDC models for
- Suggested normal forms: discusse leverag bdc model for
- Decision: accept (review_status: confirmed)

## do align with

- Cluster ID: `rc2_beb65ca95f912346`
- Assertions: 1
- Phrases: do align with
- Suggested normal forms: align with
- Decision: accept (review_status: confirmed)

## do apply to certain systems operated by

- Cluster ID: `rc2_f6f5fcd8ae17c3fd`
- Assertions: 1
- Phrases: do apply to certain systems operated by
- Suggested normal forms: apply to certain system operat by
- Decision: pending (review_status: pending)

## do constitute

- Cluster ID: `rc2_5c097b19679a817e`
- Assertions: 1
- Phrases: do constitute
- Suggested normal forms: constitute
- Decision: pending (review_status: pending)

## do replace

- Cluster ID: `rc2_7ab3778776cde4fa`
- Assertions: 1
- Phrases: do replace
- Suggested normal forms: replace
- Decision: accept (review_status: confirmed)

## do use to configure

- Cluster ID: `rc2_99164ac005889196`
- Assertions: 1
- Phrases: do use to configure
- Suggested normal forms: use to configure
- Decision: accept (review_status: confirmed)

## document BDCM schema in

- Cluster ID: `rc2_f079a3d39e618272`
- Assertions: 1
- Phrases: document BDCM schema in
- Suggested normal forms: document bdcm schema in
- Decision: accept (review_status: confirmed)

## does apply to contractors Unless directed by

- Cluster ID: `rc2_4054558482a12408`
- Assertions: 1
- Phrases: does apply to contractors Unless directed by
- Suggested normal forms: apply to contractor unles direct by
- Decision: pending (review_status: pending)

## does approve

- Cluster ID: `rc2_74e21680eac7385c`
- Assertions: 1
- Phrases: does approve
- Suggested normal forms: approve
- Decision: pending (review_status: pending)

## does change priority of

- Cluster ID: `rc2_da551cffe2b3edff`
- Assertions: 1
- Phrases: does change priority of
- Suggested normal forms: change priority of
- Decision: accept (review_status: confirmed)

## does change priority of SSVC decision Based on

- Cluster ID: `rc2_4c9edfb697ee1d7f`
- Assertions: 1
- Phrases: does change priority of SSVC decision Based on
- Suggested normal forms: change priority of ssvc decision bas on
- Decision: pending (review_status: pending)

## does have open connectivity to

- Cluster ID: `rc2_d9492a15ef33a8b3`
- Assertions: 1
- Phrases: does have open connectivity to
- Suggested normal forms: open connectivity to
- Decision: accept (review_status: confirmed)

## does impact retention of

- Cluster ID: `rc2_9a0e02ab51274bb9`
- Assertions: 1
- Phrases: does impact retention of
- Suggested normal forms: impact retention of
- Decision: accept (review_status: confirmed)

## does predict

- Cluster ID: `rc2_8e9afe9d1df3927e`
- Assertions: 1
- Phrases: does predict
- Suggested normal forms: predict
- Decision: pending (review_status: pending)

## does take action to overcome

- Cluster ID: `rc2_a08d23292a8606df`
- Assertions: 1
- Phrases: does take action to overcome
- Suggested normal forms: take action to overcome
- Decision: accept (review_status: confirmed)

## doing

- Cluster ID: `rc2_ac0b52a2ae6ef999`
- Assertions: 1
- Phrases: doing
- Suggested normal forms: do
- Decision: accept (review_status: confirmed)

## downloaded

- Cluster ID: `rc2_68ff63fb82e0e5df`
- Assertions: 1
- Phrases: downloaded
- Suggested normal forms: download
- Decision: accept (review_status: confirmed)

## downloaded it from

- Cluster ID: `rc2_47d4083ea0f09378`
- Assertions: 1
- Phrases: downloaded it from
- Suggested normal forms: download it from
- Decision: accept (review_status: confirmed)

## egress to

- Cluster ID: `rc2_ae2efbb6bc81870d`
- Assertions: 1
- Phrases: egress to
- Suggested normal forms: egres to
- Decision: accept (review_status: confirmed)

## embraces

- Cluster ID: `rc2_3962ce683c81e928`
- Assertions: 1
- Phrases: embraces
- Suggested normal forms: embrace
- Decision: pending (review_status: pending)

## emerge

- Cluster ID: `rc2_15275743f9d38346`
- Assertions: 1
- Phrases: emerge
- Suggested normal forms: emerge
- Decision: accept (review_status: confirmed)

## emerge as

- Cluster ID: `rc2_e2ece150bf4b0bba`
- Assertions: 1
- Phrases: emerge as
- Suggested normal forms: emerge a
- Decision: accept (review_status: confirmed)

## emerge as consequence of

- Cluster ID: `rc2_cb3aee0343380ef3`
- Assertions: 1
- Phrases: emerge as consequence of
- Suggested normal forms: emerge a consequence of
- Decision: accept (review_status: confirmed)

## emerging trends

- Cluster ID: `rc2_65dd1734337264fe`
- Assertions: 1
- Phrases: emerging trends
- Suggested normal forms: emerg trend
- Decision: accept (review_status: confirmed)

## employs Endpoint Protection Modules To combat

- Cluster ID: `rc2_e7e84cb8ea2ba6d4`
- Assertions: 1
- Phrases: employs Endpoint Protection Modules To combat
- Suggested normal forms: employ endpoint protection module to combat
- Decision: pending (review_status: pending)

## empowers organizations to transcend challenges of

- Cluster ID: `rc2_8a75f2132e8f0991`
- Assertions: 1
- Phrases: empowers organizations to transcend challenges of
- Suggested normal forms: empower organization to transcend challenge of
- Decision: accept (review_status: confirmed)

## enabled anti-attribution settings on

- Cluster ID: `rc2_f86134284052c8f6`
- Assertions: 1
- Phrases: enabled anti-attribution settings on
- Suggested normal forms: enabl anti-attribution sett on
- Decision: accept (review_status: confirmed)

## enabled us to understand

- Cluster ID: `rc2_9b6df13c4cff5b1a`
- Assertions: 1
- Phrases: enabled us to understand
- Suggested normal forms: enabl u to understand
- Decision: pending (review_status: pending)

## enables attacker

- Cluster ID: `rc2_843d670abe785c0f`
- Assertions: 1
- Phrases: enables attacker
- Suggested normal forms: enable attacker
- Decision: accept (review_status: confirmed)

## enables attacker to read files on

- Cluster ID: `rc2_866c806f7ffd0eb6`
- Assertions: 1
- Phrases: enables attacker to read files on
- Suggested normal forms: enable attacker to read file on
- Decision: accept (review_status: confirmed)

## enables authorized organization to enrich content of

- Cluster ID: `rc2_858d83d7ee8de0a2`
- Assertions: 1
- Phrases: enables authorized organization to enrich content of
- Suggested normal forms: enable authoriz organization to enrich content of
- Decision: accept (review_status: confirmed)

## enables qualified organization to enrich content of

- Cluster ID: `rc2_49704faee91ca85b`
- Assertions: 1
- Phrases: enables qualified organization to enrich content of
- Suggested normal forms: enable qualifi organization to enrich content of
- Decision: accept (review_status: confirmed)

## encompasses

- Cluster ID: `rc2_0de068736aa1c144`
- Assertions: 1
- Phrases: encompasses
- Suggested normal forms: encompasse
- Decision: pending (review_status: pending)

## ends at

- Cluster ID: `rc2_1f2ca552f13ad6d8`
- Assertions: 1
- Phrases: ends at
- Suggested normal forms: end at
- Decision: accept (review_status: confirmed)

## enforces

- Cluster ID: `rc2_c1f1005e99318bf6`
- Assertions: 1
- Phrases: enforces
- Suggested normal forms: enforce
- Decision: pending (review_status: pending)

## evolves upon

- Cluster ID: `rc2_19b576176d3af627`
- Assertions: 1
- Phrases: evolves upon
- Suggested normal forms: evolve upon
- Decision: accept (review_status: confirmed)

## evolves upon CISA 's KEV Catalog while deferring action against

- Cluster ID: `rc2_636820ab8cb12dff`
- Assertions: 1
- Phrases: evolves upon CISA 's KEV Catalog while deferring action against
- Suggested normal forms: evolve upon cisa 's kev catalog while deferr action against
- Decision: pending (review_status: pending)

## examine post-exploitation activity observed during

- Cluster ID: `rc2_17abbb2e429182fe`
- Assertions: 1
- Phrases: examine post-exploitation activity observed during
- Suggested normal forms: examine post-exploitation activity observ dur
- Decision: pending (review_status: pending)

## executed hundreds of hours of manual targeting analysis while

- Cluster ID: `rc2_729f6c18dbae7046`
- Assertions: 1
- Phrases: executed hundreds of hours of manual targeting analysis while
- Suggested normal forms: execut hundr of hour of manual target analysi while
- Decision: pending (review_status: pending)

## executes calc process on

- Cluster ID: `rc2_918c8eec55f02609`
- Assertions: 1
- Phrases: executes calc process on
- Suggested normal forms: execute calc proces on
- Decision: accept (review_status: confirmed)

## executes in

- Cluster ID: `rc2_95ce7649ec47c435`
- Assertions: 1
- Phrases: executes in
- Suggested normal forms: execute in
- Decision: accept (review_status: confirmed)

## executes in environment with

- Cluster ID: `rc2_295935833f464d85`
- Assertions: 1
- Phrases: executes in environment with
- Suggested normal forms: execute in environment with
- Decision: accept (review_status: confirmed)

## exist to leverage core foundation of CVSS for

- Cluster ID: `rc2_00b18c8e41ebd7e6`
- Assertions: 1
- Phrases: exist to leverage core foundation of CVSS for
- Suggested normal forms: exist to leverage core foundation of cvs for
- Decision: pending (review_status: pending)

## exists in more components of

- Cluster ID: `rc2_543167e6f28e3e64`
- Assertions: 1
- Phrases: exists in more components of
- Suggested normal forms: exist in more component of
- Decision: pending (review_status: pending)

## expanded

- Cluster ID: `rc2_d78de925a8786731`
- Assertions: 1
- Phrases: expanded
- Suggested normal forms: expand
- Decision: pending (review_status: pending)

## expands beyond

- Cluster ID: `rc2_5359eea5301159cb`
- Assertions: 1
- Phrases: expands beyond
- Suggested normal forms: expand beyond
- Decision: accept (review_status: confirmed)

## expect method to use to perform

- Cluster ID: `rc2_8d38af2c1276ff1f`
- Assertions: 1
- Phrases: expect method to use to perform
- Suggested normal forms: expect method to use to perform
- Decision: accept (review_status: confirmed)

## expects Finder methods to return

- Cluster ID: `rc2_27c606de4e5282bf`
- Assertions: 1
- Phrases: expects Finder methods to return
- Suggested normal forms: expect finder method to return
- Decision: pending (review_status: pending)

## exploit edge network infrastructure

- Cluster ID: `rc2_726b5e543db95974`
- Assertions: 1
- Phrases: exploit edge network infrastructure
- Suggested normal forms: exploit edge network infrastructure
- Decision: pending (review_status: pending)

## exploit for CVE-2026-55040

- Cluster ID: `rc2_d943f47397713fc1`
- Assertions: 1
- Phrases: exploit for CVE-2026-55040
- Suggested normal forms: exploit for cve-2026-55040
- Decision: pending (review_status: pending)

## exploit from

- Cluster ID: `rc2_3b4f6a6a9d3a75fe`
- Assertions: 1
- Phrases: exploit from
- Suggested normal forms: exploit from
- Decision: accept (review_status: confirmed)

## exploit issue to execute code on

- Cluster ID: `rc2_6df684ee5fce84fe`
- Assertions: 1
- Phrases: exploit issue to execute code on
- Suggested normal forms: exploit issue to execute code on
- Decision: pending (review_status: pending)

## exploit related appliances

- Cluster ID: `rc2_46faf573f1d48b6b`
- Assertions: 1
- Phrases: exploit related appliances
- Suggested normal forms: exploit relat appliance
- Decision: pending (review_status: pending)

## exploit removes capabilities with

- Cluster ID: `rc2_060588cda195d4b7`
- Assertions: 1
- Phrases: exploit removes capabilities with
- Suggested normal forms: exploit remove capability with
- Decision: pending (review_status: pending)

## exploit vulnerability from inside

- Cluster ID: `rc2_c7966baa174f1fea`
- Assertions: 1
- Phrases: exploit vulnerability from inside
- Suggested normal forms: exploit vulnerability from inside
- Decision: pending (review_status: pending)

## exploit was made available On

- Cluster ID: `rc2_bd3f5533fdb61fb6`
- Assertions: 1
- Phrases: exploit was made available On
- Suggested normal forms: exploit made available on
- Decision: pending (review_status: pending)

## exploited it over multiple days with

- Cluster ID: `rc2_92e07c5d3f190b44`
- Assertions: 1
- Phrases: exploited it over multiple days with
- Suggested normal forms: exploit it over multiple day with
- Decision: accept (review_status: confirmed)

## expose

- Cluster ID: `rc2_f3b96e66bb86f375`
- Assertions: 1
- Phrases: expose
- Suggested normal forms: expose
- Decision: pending (review_status: pending)

## expose IKE services to

- Cluster ID: `rc2_65831e9eaf70d0ab`
- Assertions: 1
- Phrases: expose IKE services to
- Suggested normal forms: expose ike service to
- Decision: accept (review_status: confirmed)

## exposed infrastructure by starting file server in

- Cluster ID: `rc2_edf3cd7d5ac00714`
- Assertions: 1
- Phrases: exposed infrastructure by starting file server in
- Suggested normal forms: expos infrastructure by start file server in
- Decision: pending (review_status: pending)

## extends beyond

- Cluster ID: `rc2_efa984d58e1bf190`
- Assertions: 1
- Phrases: extends beyond
- Suggested normal forms: extend beyond
- Decision: pending (review_status: pending)

## extracts / /

- Cluster ID: `rc2_83c3851f7224331c`
- Assertions: 1
- Phrases: extracts / /
- Suggested normal forms: extract / /
- Decision: pending (review_status: pending)

## extracts / / directly

- Cluster ID: `rc2_da81942951b2764c`
- Assertions: 1
- Phrases: extracts / / directly
- Suggested normal forms: extract / / directly
- Decision: pending (review_status: pending)

## extracts / / x5t value from

- Cluster ID: `rc2_e93639d7d81b2560`
- Assertions: 1
- Phrases: extracts / / x5t value from
- Suggested normal forms: extract / / x5t value from
- Decision: pending (review_status: pending)

## extracts Bearer token from

- Cluster ID: `rc2_d220f8a3161c6de3`
- Assertions: 1
- Phrases: extracts Bearer token from
- Suggested normal forms: extract bearer token from
- Decision: accept (review_status: confirmed)

## faces

- Cluster ID: `rc2_0282d9b79f42c74c`
- Assertions: 1
- Phrases: faces
- Suggested normal forms: face
- Decision: accept (review_status: confirmed)

## facilitating

- Cluster ID: `rc2_3372c8eeeb84e926`
- Assertions: 1
- Phrases: facilitating
- Suggested normal forms: facilitat
- Decision: accept (review_status: confirmed)

## failed

- Cluster ID: `rc2_51280dabfbc880cd`
- Assertions: 1
- Phrases: failed
- Suggested normal forms: fail
- Decision: accept (review_status: confirmed)

## falls through to

- Cluster ID: `rc2_e8d93821e0927228`
- Assertions: 1
- Phrases: falls through to
- Suggested normal forms: fall through to
- Decision: pending (review_status: pending)

## files

- Cluster ID: `rc2_3b9c358f36f0a31b`
- Assertions: 1
- Phrases: files
- Suggested normal forms: file
- Decision: pending (review_status: pending)

## fires

- Cluster ID: `rc2_dc9f28b12dd1818e`
- Assertions: 1
- Phrases: fires
- Suggested normal forms: fire
- Decision: accept (review_status: confirmed)

## focus

- Cluster ID: `rc2_bcd77267eb729b62`
- Assertions: 1
- Phrases: focus
- Suggested normal forms: focu
- Decision: accept (review_status: confirmed)

## follow path of

- Cluster ID: `rc2_b9a7daee43f0b0a6`
- Assertions: 1
- Phrases: follow path of
- Suggested normal forms: follow path of
- Decision: accept (review_status: confirmed)

## follow path of least resistance For

- Cluster ID: `rc2_9ea08ea975fe1e0a`
- Assertions: 1
- Phrases: follow path of least resistance For
- Suggested normal forms: follow path of least resistance for
- Decision: accept (review_status: confirmed)

## followed within

- Cluster ID: `rc2_28dc547c13b0ecef`
- Assertions: 1
- Phrases: followed within
- Suggested normal forms: follow within
- Decision: accept (review_status: confirmed)

## force default credential to be

- Cluster ID: `rc2_afcd940bbe46875f`
- Assertions: 1
- Phrases: force default credential to be
- Suggested normal forms: force default credential to be
- Decision: pending (review_status: pending)

## found

- Cluster ID: `rc2_bcc649cfdb8cc557`
- Assertions: 1
- Phrases: found
- Suggested normal forms: found
- Decision: accept (review_status: confirmed)

## found attempted to exploit them automatically

- Cluster ID: `rc2_13b99b015e3b9b17`
- Assertions: 1
- Phrases: found attempted to exploit them automatically
- Suggested normal forms: found attempt to exploit them automatically
- Decision: pending (review_status: pending)

## found was GetEntityObject function in

- Cluster ID: `rc2_8b6c13c602033b65`
- Assertions: 1
- Phrases: found was GetEntityObject function in
- Suggested normal forms: found getentityobject function in
- Decision: pending (review_status: pending)

## framed

- Cluster ID: `rc2_0187489c04b9357c`
- Assertions: 1
- Phrases: framed
- Suggested normal forms: fram
- Decision: accept (review_status: confirmed)

## framed lookup table by

- Cluster ID: `rc2_5ab0cee8b3f87a0e`
- Assertions: 1
- Phrases: framed lookup table by
- Suggested normal forms: fram lookup table by
- Decision: accept (review_status: confirmed)

## framed lookup table to

- Cluster ID: `rc2_4e1b136057fd7308`
- Assertions: 1
- Phrases: framed lookup table to
- Suggested normal forms: fram lookup table to
- Decision: accept (review_status: confirmed)

## gain

- Cluster ID: `rc2_66dd231befc8120d`
- Assertions: 1
- Phrases: gain
- Suggested normal forms: gain
- Decision: accept (review_status: confirmed)

## gain complete control of

- Cluster ID: `rc2_08f87ebdda519e67`
- Assertions: 1
- Phrases: gain complete control of
- Suggested normal forms: gain complete control of
- Decision: accept (review_status: confirmed)

## gain control over with

- Cluster ID: `rc2_2cf492c1fd24d5ab`
- Assertions: 1
- Phrases: gain control over with
- Suggested normal forms: gain control over with
- Decision: accept (review_status: confirmed)

## gained unique insights into

- Cluster ID: `rc2_8ae47ebd7bda8dad`
- Assertions: 1
- Phrases: gained unique insights into
- Suggested normal forms: gain unique insight into
- Decision: pending (review_status: pending)

## gave us peek into

- Cluster ID: `rc2_945e6708cdbd8cf8`
- Assertions: 1
- Phrases: gave us peek into
- Suggested normal forms: gave u peek into
- Decision: pending (review_status: pending)

## get smart input about

- Cluster ID: `rc2_6cc92df91345fa48`
- Assertions: 1
- Phrases: get smart input about
- Suggested normal forms: get smart input about
- Decision: pending (review_status: pending)

## gets SharePoint to run

- Cluster ID: `rc2_5122cdaa77acb30a`
- Assertions: 1
- Phrases: gets SharePoint to run
- Suggested normal forms: get sharepoint to run
- Decision: accept (review_status: confirmed)

## gets SharePoint to run it for

- Cluster ID: `rc2_0e29d7ee631b985b`
- Assertions: 1
- Phrases: gets SharePoint to run it for
- Suggested normal forms: get sharepoint to run it for
- Decision: accept (review_status: confirmed)

## gets patched

- Cluster ID: `rc2_61c3601cb5ae4971`
- Assertions: 1
- Phrases: gets patched
- Suggested normal forms: get patch
- Decision: accept (review_status: confirmed)

## gets patched for

- Cluster ID: `rc2_ace1815d06a8a4eb`
- Assertions: 1
- Phrases: gets patched for
- Suggested normal forms: get patch for
- Decision: accept (review_status: confirmed)

## goes

- Cluster ID: `rc2_be09e4a3db0fc7be`
- Assertions: 1
- Phrases: goes
- Suggested normal forms: goe
- Decision: pending (review_status: pending)

## grows in order faster than

- Cluster ID: `rc2_168916bba9e922fc`
- Assertions: 1
- Phrases: grows in order faster than
- Suggested normal forms: grow in order faster than
- Decision: pending (review_status: pending)

## had accessible

- Cluster ID: `rc2_89c683ba0c58f547`
- Assertions: 1
- Phrases: had accessible
- Suggested normal forms: accessible
- Decision: pending (review_status: pending)

## had accessible publicly

- Cluster ID: `rc2_8dd857f4cbb49369`
- Assertions: 1
- Phrases: had accessible publicly
- Suggested normal forms: accessible publicly
- Decision: pending (review_status: pending)

## had limited

- Cluster ID: `rc2_55ea09e5715d0a8d`
- Assertions: 1
- Phrases: had limited
- Suggested normal forms: limit
- Decision: accept (review_status: confirmed)

## had moved to newer release of

- Cluster ID: `rc2_890c51599667add8`
- Assertions: 1
- Phrases: had moved to newer release of
- Suggested normal forms: mov to newer release of
- Decision: pending (review_status: pending)

## had moved to newer release of chosen model By

- Cluster ID: `rc2_fd0550bb30e67c34`
- Assertions: 1
- Phrases: had moved to newer release of chosen model By
- Suggested normal forms: mov to newer release of chosen model by
- Decision: pending (review_status: pending)

## had moved to newer release of chosen model that

- Cluster ID: `rc2_383adf4df1cc1307`
- Assertions: 1
- Phrases: had moved to newer release of chosen model that
- Suggested normal forms: mov to newer release of chosen model that
- Decision: pending (review_status: pending)

## has advanced knowledge of

- Cluster ID: `rc2_27d74e38f09269e1`
- Assertions: 1
- Phrases: has advanced knowledge of
- Suggested normal forms: advanc knowledge of
- Decision: accept (review_status: confirmed)

## has assessment by

- Cluster ID: `rc2_ceae88d236ada8f6`
- Assertions: 1
- Phrases: has assessment by
- Suggested normal forms: assessment by
- Decision: pending (review_status: pending)

## has been abused in

- Cluster ID: `rc2_3986f766ba6154cf`
- Assertions: 1
- Phrases: has been abused in
- Suggested normal forms: been abus in
- Decision: pending (review_status: pending)

## has been achieved

- Cluster ID: `rc2_add31bd0c9e45a00`
- Assertions: 1
- Phrases: has been achieved
- Suggested normal forms: been achiev
- Decision: pending (review_status: pending)

## has been added to identify combinations of

- Cluster ID: `rc2_8551474934febf17`
- Assertions: 1
- Phrases: has been added to identify combinations of
- Suggested normal forms: been add to identify combination of
- Decision: pending (review_status: pending)

## has been disclosed to

- Cluster ID: `rc2_598d689b944b7acc`
- Assertions: 1
- Phrases: has been disclosed to
- Suggested normal forms: been disclos to
- Decision: pending (review_status: pending)

## has been documented

- Cluster ID: `rc2_382d115bd3702e61`
- Assertions: 1
- Phrases: has been documented
- Suggested normal forms: been document
- Decision: accept (review_status: confirmed)

## has been expedited as third party has published details of

- Cluster ID: `rc2_0241fbf229526feb`
- Assertions: 1
- Phrases: has been expedited as third party has published details of
- Suggested normal forms: been expedit a third party publish detail of
- Decision: pending (review_status: pending)

## has been exploited in wild even as

- Cluster ID: `rc2_16c5730a88409c3c`
- Assertions: 1
- Phrases: has been exploited in wild even as
- Suggested normal forms: been exploit in wild even a
- Decision: pending (review_status: pending)

## has been replaced

- Cluster ID: `rc2_b49c4a3d1abbc6ca`
- Assertions: 1
- Phrases: has been replaced
- Suggested normal forms: been replac
- Decision: pending (review_status: pending)

## has been replaced capturing impacts from

- Cluster ID: `rc2_219e426b0d73ed18`
- Assertions: 1
- Phrases: has been replaced capturing impacts from
- Suggested normal forms: been replac captur impact from
- Decision: pending (review_status: pending)

## has been replaced with concepts of vulnerable system

- Cluster ID: `rc2_8f84d0f646ece474`
- Assertions: 1
- Phrases: has been replaced with concepts of vulnerable system
- Suggested normal forms: been replac with concept of vulnerable system
- Decision: pending (review_status: pending)

## has been replaced with concepts of vulnerable system capturing impacts from

- Cluster ID: `rc2_5821af064afd7b64`
- Assertions: 1
- Phrases: has been replaced with concepts of vulnerable system capturing impacts from
- Suggested normal forms: been replac with concept of vulnerable system captur impact from
- Decision: pending (review_status: pending)

## has been replaced with subsequent system

- Cluster ID: `rc2_52cc5991ee53050f`
- Assertions: 1
- Phrases: has been replaced with subsequent system
- Suggested normal forms: been replac with subsequent system
- Decision: pending (review_status: pending)

## has been replaced with subsequent system capturing impacts from

- Cluster ID: `rc2_2786232a42454137`
- Assertions: 1
- Phrases: has been replaced with subsequent system capturing impacts from
- Suggested normal forms: been replac with subsequent system captur impact from
- Decision: pending (review_status: pending)

## has been tested by anyone other than

- Cluster ID: `rc2_897a2da039c49d96`
- Assertions: 1
- Phrases: has been tested by anyone other than
- Suggested normal forms: been test by anyone other than
- Decision: pending (review_status: pending)

## has been updated

- Cluster ID: `rc2_07231655ae00200e`
- Assertions: 1
- Phrases: has been updated
- Suggested normal forms: been updat
- Decision: accept (review_status: confirmed)

## has been updated to reflect

- Cluster ID: `rc2_15ca58c9c7edfe80`
- Assertions: 1
- Phrases: has been updated to reflect
- Suggested normal forms: been updat to reflect
- Decision: accept (review_status: confirmed)

## has best understanding of

- Cluster ID: `rc2_44e2c11c88739721`
- Assertions: 1
- Phrases: has best understanding of
- Suggested normal forms: best understand of
- Decision: accept (review_status: confirmed)

## has broad control over

- Cluster ID: `rc2_7efa9e9de886cf84`
- Assertions: 1
- Phrases: has broad control over
- Suggested normal forms: broad control over
- Decision: pending (review_status: pending)

## has catalog of

- Cluster ID: `rc2_c703990dc49bd26a`
- Assertions: 1
- Phrases: has catalog of
- Suggested normal forms: catalog of
- Decision: accept (review_status: confirmed)

## has chained

- Cluster ID: `rc2_9414886b1ebf025d`
- Assertions: 1
- Phrases: has chained
- Suggested normal forms: chain
- Decision: pending (review_status: pending)

## has chained authentication bypass CVE-2026-55040 with separate RCE vulnerability for

- Cluster ID: `rc2_e1f84ddd9221167a`
- Assertions: 1
- Phrases: has chained authentication bypass CVE-2026-55040 with separate RCE vulnerability for
- Suggested normal forms: chain authentication bypas cve-2026-55040 with separate rce vulnerability for
- Decision: pending (review_status: pending)

## has choosing over

- Cluster ID: `rc2_cd4b5cf510fa1aff`
- Assertions: 1
- Phrases: has choosing over
- Suggested normal forms: choos over
- Decision: accept (review_status: confirmed)

## has colleagues at

- Cluster ID: `rc2_bef5555afea5032f`
- Assertions: 1
- Phrases: has colleagues at
- Suggested normal forms: colleague at
- Decision: accept (review_status: confirmed)

## has contacted Broadcom for statement on

- Cluster ID: `rc2_0a4989ab06be65cd`
- Assertions: 1
- Phrases: has contacted Broadcom for statement on
- Suggested normal forms: contact broadcom for statement on
- Decision: pending (review_status: pending)

## has cybersecurity practices including policies for

- Cluster ID: `rc2_c38f64ee1154f78f`
- Assertions: 1
- Phrases: has cybersecurity practices including policies for
- Suggested normal forms: cybersecurity practice includ policy for
- Decision: pending (review_status: pending)

## has decreased

- Cluster ID: `rc2_595d0bd30fdc1ca5`
- Assertions: 1
- Phrases: has decreased
- Suggested normal forms: decreas
- Decision: pending (review_status: pending)

## has developed generic YARA rule for

- Cluster ID: `rc2_341c7371dedb83ca`
- Assertions: 1
- Phrases: has developed generic YARA rule for
- Suggested normal forms: develop generic yara rule for
- Decision: pending (review_status: pending)

## has developed generic YARA rule for identifying reverse_ssh builds To support

- Cluster ID: `rc2_4d4355dd01043d11`
- Assertions: 1
- Phrases: has developed generic YARA rule for identifying reverse_ssh builds To support
- Suggested normal forms: develop generic yara rule for identify reverse_ssh build to support
- Decision: pending (review_status: pending)

## has disclosure for

- Cluster ID: `rc2_1e012b2f85a08058`
- Assertions: 1
- Phrases: has disclosure for
- Suggested normal forms: disclosure for
- Decision: accept (review_status: confirmed)

## has earlier experimentation with

- Cluster ID: `rc2_c64d1ecd6c464983`
- Assertions: 1
- Phrases: has earlier experimentation with
- Suggested normal forms: earlier experimentation with
- Decision: pending (review_status: pending)

## has effectiveness for

- Cluster ID: `rc2_537dffa66d81ebb1`
- Assertions: 1
- Phrases: has effectiveness for
- Suggested normal forms: effectivenes for
- Decision: pending (review_status: pending)

## has first sprint in

- Cluster ID: `rc2_dba5a4929112e7fa`
- Assertions: 1
- Phrases: has first sprint in
- Suggested normal forms: first sprint in
- Decision: pending (review_status: pending)

## has increased

- Cluster ID: `rc2_fc69963f3b1f5991`
- Assertions: 1
- Phrases: has increased
- Suggested normal forms: increas
- Decision: pending (review_status: pending)

## has increased weight For

- Cluster ID: `rc2_5cc90aed35b5e0a0`
- Assertions: 1
- Phrases: has increased weight For
- Suggested normal forms: increas weight for
- Decision: pending (review_status: pending)

## has intelligence sharing with

- Cluster ID: `rc2_f7b5e88a90f32c5d`
- Assertions: 1
- Phrases: has intelligence sharing with
- Suggested normal forms: intelligence shar with
- Decision: accept (review_status: confirmed)

## has later testing of

- Cluster ID: `rc2_c45f163f7dd4d523`
- Assertions: 1
- Phrases: has later testing of
- Suggested normal forms: later test of
- Decision: pending (review_status: pending)

## has lower complexity than

- Cluster ID: `rc2_b0777f862fd6633e`
- Assertions: 1
- Phrases: has lower complexity than
- Suggested normal forms: lower complexity than
- Decision: pending (review_status: pending)

## has maintenance of

- Cluster ID: `rc2_1febcde8f4b40109`
- Assertions: 1
- Phrases: has maintenance of
- Suggested normal forms: maintenance of
- Decision: accept (review_status: confirmed)

## has mapped

- Cluster ID: `rc2_3a69487cf2846f13`
- Assertions: 1
- Phrases: has mapped
- Suggested normal forms: mapp
- Decision: accept (review_status: confirmed)

## has membership in

- Cluster ID: `rc2_3876e0d5aafe56f2`
- Assertions: 1
- Phrases: has membership in
- Suggested normal forms: membership in
- Decision: pending (review_status: pending)

## has moved in

- Cluster ID: `rc2_da47847d346a41fb`
- Assertions: 1
- Phrases: has moved in
- Suggested normal forms: mov in
- Decision: pending (review_status: pending)

## has parameterless constructor with

- Cluster ID: `rc2_fca671e600b24410`
- Assertions: 1
- Phrases: has parameterless constructor with
- Suggested normal forms: parameterles constructor with
- Decision: accept (review_status: confirmed)

## has perfect knowledge of

- Cluster ID: `rc2_66b4be3ef711f5ea`
- Assertions: 1
- Phrases: has perfect knowledge of
- Suggested normal forms: perfect knowledge of
- Decision: accept (review_status: confirmed)

## has policies for

- Cluster ID: `rc2_cc21dcedf5072368`
- Assertions: 1
- Phrases: has policies for
- Suggested normal forms: policy for
- Decision: pending (review_status: pending)

## has published full technical details for

- Cluster ID: `rc2_55e4ca42ea49b671`
- Assertions: 1
- Phrases: has published full technical details for
- Suggested normal forms: publish full technical detail for
- Decision: accept (review_status: confirmed)

## has published in CNA container

- Cluster ID: `rc2_16c9a31460f2d02b`
- Assertions: 1
- Phrases: has published in CNA container
- Suggested normal forms: publish in cna container
- Decision: accept (review_status: confirmed)

## has published in-depth technical analysis of flaw accompanied by proof-of-concept

- Cluster ID: `rc2_770d4f3c635699ba`
- Assertions: 1
- Phrases: has published in-depth technical analysis of flaw accompanied by proof-of-concept
- Suggested normal forms: publish in-depth technical analysi of flaw accompani by proof-of-concept
- Decision: accept (review_status: confirmed)

## has script for

- Cluster ID: `rc2_9f4e53bd3e456742`
- Assertions: 1
- Phrases: has script for
- Suggested normal forms: script for
- Decision: accept (review_status: confirmed)

## has shared

- Cluster ID: `rc2_8bb596034beab707`
- Assertions: 1
- Phrases: has shared
- Suggested normal forms: shar
- Decision: pending (review_status: pending)

## has shared findings with

- Cluster ID: `rc2_fa6e252912bfd926`
- Assertions: 1
- Phrases: has shared findings with
- Suggested normal forms: shar find with
- Decision: pending (review_status: pending)

## has status on

- Cluster ID: `rc2_618ccd545db24938`
- Assertions: 1
- Phrases: has status on
- Suggested normal forms: statu on
- Decision: pending (review_status: pending)

## has suite of

- Cluster ID: `rc2_bab6ebda8450a0cb`
- Assertions: 1
- Phrases: has suite of
- Suggested normal forms: suite of
- Decision: accept (review_status: confirmed)

## has to return

- Cluster ID: `rc2_cd877cffb4033ce8`
- Assertions: 1
- Phrases: has to return
- Suggested normal forms: to return
- Decision: accept (review_status: confirmed)

## has to return collection by

- Cluster ID: `rc2_7932cadc00b91742`
- Assertions: 1
- Phrases: has to return collection by
- Suggested normal forms: to return collection by
- Decision: accept (review_status: confirmed)

## has to update

- Cluster ID: `rc2_bc24f747995f0941`
- Assertions: 1
- Phrases: has to update
- Suggested normal forms: to update
- Decision: accept (review_status: confirmed)

## has tracked same systematic methodology throughout

- Cluster ID: `rc2_36b6843f1b2fa5fc`
- Assertions: 1
- Phrases: has tracked same systematic methodology throughout
- Suggested normal forms: track same systematic methodology throughout
- Decision: accept (review_status: confirmed)

## has vendor advisory

- Cluster ID: `rc2_4766b8fa7cd0954d`
- Assertions: 1
- Phrases: has vendor advisory
- Suggested normal forms: vendor advisory
- Decision: accept (review_status: confirmed)

## have attribute rated as

- Cluster ID: `rc2_156ce974c9568bf4`
- Assertions: 1
- Phrases: have attribute rated as
- Suggested normal forms: attribute rat a
- Decision: pending (review_status: pending)

## have attribute rated as High

- Cluster ID: `rc2_8dec257a8648c680`
- Assertions: 1
- Phrases: have attribute rated as High
- Suggested normal forms: attribute rat a high
- Decision: pending (review_status: pending)

## have attribute rated as Low

- Cluster ID: `rc2_6ada8841d9d86a95`
- Assertions: 1
- Phrases: have attribute rated as Low
- Suggested normal forms: attribute rat a low
- Decision: pending (review_status: pending)

## have available on

- Cluster ID: `rc2_6712e25cf763eb1c`
- Assertions: 1
- Phrases: have available on
- Suggested normal forms: available on
- Decision: pending (review_status: pending)

## have been compromised

- Cluster ID: `rc2_c4506041ab912941`
- Assertions: 1
- Phrases: have been compromised
- Suggested normal forms: been compromis
- Decision: pending (review_status: pending)

## have been exploited which in

- Cluster ID: `rc2_a0a6fbc949c40006`
- Assertions: 1
- Phrases: have been exploited which in
- Suggested normal forms: been exploit which in
- Decision: accept (review_status: confirmed)

## have been generated via script for

- Cluster ID: `rc2_8ee314e62e7e5d08`
- Assertions: 1
- Phrases: have been generated via script for
- Suggested normal forms: been generat via script for
- Decision: accept (review_status: confirmed)

## have begun exploiting critical Microsoft SharePoint flaw following release of

- Cluster ID: `rc2_3da62117829546e8`
- Assertions: 1
- Phrases: have begun exploiting critical Microsoft SharePoint flaw following release of
- Suggested normal forms: begun exploit critical microsoft sharepoint flaw follow release of
- Decision: pending (review_status: pending)

## have begun using Microsoft SharePoint RCE vulnerability in

- Cluster ID: `rc2_c057eee58df12495`
- Assertions: 1
- Phrases: have begun using Microsoft SharePoint RCE vulnerability in
- Suggested normal forms: begun us microsoft sharepoint rce vulnerability in
- Decision: pending (review_status: pending)

## have concentrated

- Cluster ID: `rc2_f54c4438ccb3b913`
- Assertions: 1
- Phrases: have concentrated
- Suggested normal forms: concentrat
- Decision: accept (review_status: confirmed)

## have concentrated value For

- Cluster ID: `rc2_a1b31a6674c5f916`
- Assertions: 1
- Phrases: have concentrated value For
- Suggested normal forms: concentrat value for
- Decision: pending (review_status: pending)

## have disproportionate security impact particularly in

- Cluster ID: `rc2_85b69ccbc7ffc1c3`
- Assertions: 1
- Phrases: have disproportionate security impact particularly in
- Suggested normal forms: disproportionate security impact particularly in
- Decision: pending (review_status: pending)

## have established macOS patch cycle at

- Cluster ID: `rc2_ca24726939643ada`
- Assertions: 1
- Phrases: have established macOS patch cycle at
- Suggested normal forms: establish maco patch cycle at
- Decision: pending (review_status: pending)

## have established macOS patch cycle with

- Cluster ID: `rc2_d4250535cdf0495b`
- Assertions: 1
- Phrases: have established macOS patch cycle with
- Suggested normal forms: establish maco patch cycle with
- Decision: pending (review_status: pending)

## have existed under

- Cluster ID: `rc2_ac1610ee432a6605`
- Assertions: 1
- Phrases: have existed under
- Suggested normal forms: exist under
- Decision: pending (review_status: pending)

## have had prior knowledge of

- Cluster ID: `rc2_319bd7ca4c505978`
- Assertions: 1
- Phrases: have had prior knowledge of
- Suggested normal forms: prior knowledge of
- Decision: accept (review_status: confirmed)

## have header

- Cluster ID: `rc2_1e0584a25d9f43bf`
- Assertions: 1
- Phrases: have header
- Suggested normal forms: header
- Decision: accept (review_status: confirmed)

## have impact on

- Cluster ID: `rc2_73c2ee88385afcb9`
- Assertions: 1
- Phrases: have impact on
- Suggested normal forms: impact on
- Decision: pending (review_status: pending)

## have more information

- Cluster ID: `rc2_a1260fe992b39a4b`
- Assertions: 1
- Phrases: have more information
- Suggested normal forms: more information
- Decision: pending (review_status: pending)

## have more information at

- Cluster ID: `rc2_5279b349fdbb9895`
- Assertions: 1
- Phrases: have more information at
- Suggested normal forms: more information at
- Decision: pending (review_status: pending)

## have processed

- Cluster ID: `rc2_19ed40bf62c399b8`
- Assertions: 1
- Phrases: have processed
- Suggested normal forms: process
- Decision: accept (review_status: confirmed)

## have received response by

- Cluster ID: `rc2_25b480d92450da65`
- Assertions: 1
- Phrases: have received response by
- Suggested normal forms: receiv response by
- Decision: pending (review_status: pending)

## have significant impact on

- Cluster ID: `rc2_1ad29f7ee16b1d9c`
- Assertions: 1
- Phrases: have significant impact on
- Suggested normal forms: significant impact on
- Decision: accept (review_status: confirmed)

## have smallest difference between

- Cluster ID: `rc2_7fbd78dd686cba9f`
- Assertions: 1
- Phrases: have smallest difference between
- Suggested normal forms: smallest difference between
- Decision: pending (review_status: pending)

## have targeted

- Cluster ID: `rc2_34a04005bcaf206e`
- Assertions: 1
- Phrases: have targeted
- Suggested normal forms: target
- Decision: accept (review_status: confirmed)

## have targeted material throughout

- Cluster ID: `rc2_7827623b72506718`
- Assertions: 1
- Phrases: have targeted material throughout
- Suggested normal forms: target material throughout
- Decision: accept (review_status: confirmed)

## have to be

- Cluster ID: `rc2_0af1207eeabd1586`
- Assertions: 1
- Phrases: have to be
- Suggested normal forms: to be
- Decision: pending (review_status: pending)

## have to react between

- Cluster ID: `rc2_7daa09efd9edba94`
- Assertions: 1
- Phrases: have to react between
- Suggested normal forms: to react between
- Decision: accept (review_status: confirmed)

## heeft

- Cluster ID: `rc2_5ad594e331da7016`
- Assertions: 1
- Phrases: heeft
- Suggested normal forms: heeft
- Decision: accept (review_status: confirmed)

## help block attacks with

- Cluster ID: `rc2_e0c5e3585efbb71f`
- Assertions: 1
- Phrases: help block attacks with
- Suggested normal forms: help block attack with
- Decision: pending (review_status: pending)

## helps satisfy couple of

- Cluster ID: `rc2_f52da565997c6817`
- Assertions: 1
- Phrases: helps satisfy couple of
- Suggested normal forms: help satisfy couple of
- Decision: pending (review_status: pending)

## het

- Cluster ID: `rc2_68419b272cd4eb1b`
- Assertions: 1
- Phrases: het
- Suggested normal forms: het
- Decision: pending (review_status: pending)

## highlights

- Cluster ID: `rc2_dc2c5be187f6f31e`
- Assertions: 1
- Phrases: highlights
- Suggested normal forms: highlight
- Decision: pending (review_status: pending)

## holds credentials for

- Cluster ID: `rc2_5ae1e9395c131cb7`
- Assertions: 1
- Phrases: holds credentials for
- Suggested normal forms: hold credential for
- Decision: accept (review_status: confirmed)

## hone autonomous attack processes retarget without

- Cluster ID: `rc2_b890fe0a882829fa`
- Assertions: 1
- Phrases: hone autonomous attack processes retarget without
- Suggested normal forms: hone autonomou attack processe retarget without
- Decision: accept (review_status: confirmed)

## hôtes

- Cluster ID: `rc2_275684fd7c4a5b7d`
- Assertions: 1
- Phrases: hôtes
- Suggested normal forms: hôtes
- Decision: pending (review_status: pending)

## identified attempted exploitation through

- Cluster ID: `rc2_45268163eea65ada`
- Assertions: 1
- Phrases: identified attempted exploitation through
- Suggested normal forms: identifi attempt exploitation through
- Decision: accept (review_status: confirmed)

## identified testing of

- Cluster ID: `rc2_aa55d1b548b27f2c`
- Assertions: 1
- Phrases: identified testing of
- Suggested normal forms: identifi test of
- Decision: accept (review_status: confirmed)

## identified that for

- Cluster ID: `rc2_2eac07191cc5fb32`
- Assertions: 1
- Phrases: identified that for
- Suggested normal forms: identifi that for
- Decision: pending (review_status: pending)

## identified that for useful gadget from

- Cluster ID: `rc2_f239b722fc814189`
- Assertions: 1
- Phrases: identified that for useful gadget from
- Suggested normal forms: identifi that for useful gadget from
- Decision: pending (review_status: pending)

## identifies cybersecurity vulnerability by

- Cluster ID: `rc2_b64de804e1bc85d0`
- Assertions: 1
- Phrases: identifies cybersecurity vulnerability by
- Suggested normal forms: identify cybersecurity vulnerability by
- Decision: pending (review_status: pending)

## identifies new KEVs

- Cluster ID: `rc2_1e82301f48bcc31c`
- Assertions: 1
- Phrases: identifies new KEVs
- Suggested normal forms: identify new kev
- Decision: accept (review_status: confirmed)

## identifies value Instead of declaring decision point as

- Cluster ID: `rc2_a3e3a1445cd639d5`
- Assertions: 1
- Phrases: identifies value Instead of declaring decision point as
- Suggested normal forms: identify value instead of declar decision point a
- Decision: accept (review_status: confirmed)

## identifies vulnerabilities as

- Cluster ID: `rc2_d22c5d2b1fbf6e14`
- Assertions: 1
- Phrases: identifies vulnerabilities as
- Suggested normal forms: identify vulnerability a
- Decision: accept (review_status: confirmed)

## identifies vulnerabilities through inclusion in

- Cluster ID: `rc2_85191e5eddfa728a`
- Assertions: 1
- Phrases: identifies vulnerabilities through inclusion in
- Suggested normal forms: identify vulnerability through inclusion in
- Decision: accept (review_status: confirmed)

## identify applicable fixed version in

- Cluster ID: `rc2_c3305b6c145c7815`
- Assertions: 1
- Phrases: identify applicable fixed version in
- Suggested normal forms: identify applicable fix version in
- Decision: pending (review_status: pending)

## identify complete list of

- Cluster ID: `rc2_6b7dd853b4a86945`
- Assertions: 1
- Phrases: identify complete list of
- Suggested normal forms: identify complete list of
- Decision: pending (review_status: pending)

## identify in example

- Cluster ID: `rc2_f67411f0496edc4a`
- Assertions: 1
- Phrases: identify in example
- Suggested normal forms: identify in example
- Decision: accept (review_status: confirmed)

## impacts Integrity of

- Cluster ID: `rc2_1ea2d8b6825ddbd8`
- Assertions: 1
- Phrases: impacts Integrity of
- Suggested normal forms: impact integrity of
- Decision: accept (review_status: confirmed)

## impacts Integrity of system along with

- Cluster ID: `rc2_55848c693a2e00ea`
- Assertions: 1
- Phrases: impacts Integrity of system along with
- Suggested normal forms: impact integrity of system along with
- Decision: accept (review_status: confirmed)

## improve

- Cluster ID: `rc2_2b35ed6944dd2e8f`
- Assertions: 1
- Phrases: improve
- Suggested normal forms: improve
- Decision: pending (review_status: pending)

## improve compatibility with

- Cluster ID: `rc2_d5966c6ef135d445`
- Assertions: 1
- Phrases: improve compatibility with
- Suggested normal forms: improve compatibility with
- Decision: pending (review_status: pending)

## include IKEv2 Remote Access VPN with

- Cluster ID: `rc2_11ec629743a17259`
- Assertions: 1
- Phrases: include IKEv2 Remote Access VPN with
- Suggested normal forms: include ikev2 remote acces vpn with
- Decision: accept (review_status: confirmed)

## include for example

- Cluster ID: `rc2_74f05228d83735a9`
- Assertions: 1
- Phrases: include for example
- Suggested normal forms: include for example
- Decision: pending (review_status: pending)

## include impacts to humans When assessed in

- Cluster ID: `rc2_0d69f486c27b2846`
- Assertions: 1
- Phrases: include impacts to humans When assessed in
- Suggested normal forms: include impact to human when assess in
- Decision: pending (review_status: pending)

## include impacts to humans in

- Cluster ID: `rc2_5c1b98263d587b11`
- Assertions: 1
- Phrases: include impacts to humans in
- Suggested normal forms: include impact to human in
- Decision: pending (review_status: pending)

## include requesting assistance about

- Cluster ID: `rc2_4e41f623cc2a99b5`
- Assertions: 1
- Phrases: include requesting assistance about
- Suggested normal forms: include request assistance about
- Decision: pending (review_status: pending)

## included in example

- Cluster ID: `rc2_8ee31392b3376e15`
- Assertions: 1
- Phrases: included in example
- Suggested normal forms: includ in example
- Decision: pending (review_status: pending)

## includes fix for

- Cluster ID: `rc2_fae2e146f56d2413`
- Assertions: 1
- Phrases: includes fix for
- Suggested normal forms: include fix for
- Decision: accept (review_status: confirmed)

## includes further discussion of

- Cluster ID: `rc2_d2544840ff250fa3`
- Assertions: 1
- Phrases: includes further discussion of
- Suggested normal forms: include further discussion of
- Decision: pending (review_status: pending)

## includes further discussion of CVSS guidelines on glossary of terms used in User Guide documents

- Cluster ID: `rc2_683d8cc1ef64d65f`
- Assertions: 1
- Phrases: includes further discussion of CVSS guidelines on glossary of terms used in User Guide documents
- Suggested normal forms: include further discussion of cvs guideline on glossary of term us in user guide document
- Decision: pending (review_status: pending)

## increases mission readiness across

- Cluster ID: `rc2_24aae38976fe4092`
- Assertions: 1
- Phrases: increases mission readiness across
- Suggested normal forms: increase mission readines acros
- Decision: accept (review_status: confirmed)

## increases mission readiness across federal government by prioritizing high-risk vulnerabilities for

- Cluster ID: `rc2_baa63f844684b8ee`
- Assertions: 1
- Phrases: increases mission readiness across federal government by prioritizing high-risk vulnerabilities for
- Suggested normal forms: increase mission readines acros federal government by prioritiz high-risk vulnerability for
- Decision: accept (review_status: confirmed)

## increases number of potential attackers increasing severity of

- Cluster ID: `rc2_53976aff63bab196`
- Assertions: 1
- Phrases: increases number of potential attackers increasing severity of
- Suggested normal forms: increase number of potential attacker increas severity of
- Decision: pending (review_status: pending)

## inherits from

- Cluster ID: `rc2_a3f041e6f68d6ced`
- Assertions: 1
- Phrases: inherits from
- Suggested normal forms: inherit from
- Decision: accept (review_status: confirmed)

## instructs

- Cluster ID: `rc2_c1c58eabfe7be897`
- Assertions: 1
- Phrases: instructs
- Suggested normal forms: instruct
- Decision: pending (review_status: pending)

## instructs analysts on

- Cluster ID: `rc2_e2bafd409279fe14`
- Assertions: 1
- Phrases: instructs analysts on
- Suggested normal forms: instruct analyst on
- Decision: pending (review_status: pending)

## integrate

- Cluster ID: `rc2_ad9b338ab555c072`
- Assertions: 1
- Phrases: integrate
- Suggested normal forms: integrate
- Decision: pending (review_status: pending)

## integrate prior work into

- Cluster ID: `rc2_a1670a10bf2bae93`
- Assertions: 1
- Phrases: integrate prior work into
- Suggested normal forms: integrate prior work into
- Decision: pending (review_status: pending)

## interacts to complete

- Cluster ID: `rc2_51944054b099fff1`
- Assertions: 1
- Phrases: interacts to complete
- Suggested normal forms: interact to complete
- Decision: pending (review_status: pending)

## introduces novel operational security risks for

- Cluster ID: `rc2_4c112b167f7fe0e0`
- Assertions: 1
- Phrases: introduces novel operational security risks for
- Suggested normal forms: introduce novel operational security risk for
- Decision: pending (review_status: pending)

## introduces pathway In

- Cluster ID: `rc2_bf62b6452a637004`
- Assertions: 1
- Phrases: introduces pathway In
- Suggested normal forms: introduce pathway in
- Decision: pending (review_status: pending)

## introduces pathway to

- Cluster ID: `rc2_ca7950cfb2c69c86`
- Assertions: 1
- Phrases: introduces pathway to
- Suggested normal forms: introduce pathway to
- Decision: pending (review_status: pending)

## involve Exploitation for

- Cluster ID: `rc2_0921c7f603f66937`
- Assertions: 1
- Phrases: involve Exploitation for
- Suggested normal forms: involve exploitation for
- Decision: pending (review_status: pending)

## involved

- Cluster ID: `rc2_b07922b686f7c4e8`
- Assertions: 1
- Phrases: involved
- Suggested normal forms: involv
- Decision: pending (review_status: pending)

## is Assembly Qualified Type string of

- Cluster ID: `rc2_e54e3e86a04c16f1`
- Assertions: 1
- Phrases: is Assembly Qualified Type string of
- Suggested normal forms: assembly qualifi type str of
- Decision: pending (review_status: pending)

## is CI/CD pipelines into

- Cluster ID: `rc2_96cf98725f26a920`
- Assertions: 1
- Phrases: is CI/CD pipelines into
- Suggested normal forms: ci/cd pipeline into
- Decision: pending (review_status: pending)

## is Line of

- Cluster ID: `rc2_8cead051f2c68312`
- Assertions: 1
- Phrases: is Line of
- Suggested normal forms: line of
- Decision: pending (review_status: pending)

## is On

- Cluster ID: `rc2_b8d31e852725afb1`
- Assertions: 1
- Phrases: is On
- Suggested normal forms: on
- Decision: pending (review_status: pending)

## is On VPN deployments for

- Cluster ID: `rc2_21a4f86989ec4d84`
- Assertions: 1
- Phrases: is On VPN deployments for
- Suggested normal forms: on vpn deployment for
- Decision: pending (review_status: pending)

## is SecurityKeyIdentifierClause keyIdentifierClause out

- Cluster ID: `rc2_639aa73231c00e0e`
- Assertions: 1
- Phrases: is SecurityKeyIdentifierClause keyIdentifierClause out
- Suggested normal forms: securitykeyidentifierclause keyidentifierclause out
- Decision: accept (review_status: confirmed)

## is System.Web.HttpApplication httpApplication out

- Cluster ID: `rc2_155f017cf6497aa2`
- Assertions: 1
- Phrases: is System.Web.HttpApplication httpApplication out
- Suggested normal forms: system.web.httpapplication httpapplication out
- Decision: accept (review_status: confirmed)

## is accelerating

- Cluster ID: `rc2_9a938eacd89673cf`
- Assertions: 1
- Phrases: is accelerating
- Suggested normal forms: accelerat
- Decision: pending (review_status: pending)

## is accessible via public networks such as

- Cluster ID: `rc2_1d807cd6432841db`
- Assertions: 1
- Phrases: is accessible via public networks such as
- Suggested normal forms: accessible via public network such a
- Decision: accept (review_status: confirmed)

## is acting under usual capabilities of

- Cluster ID: `rc2_f6e89951ed614fef`
- Assertions: 1
- Phrases: is acting under usual capabilities of
- Suggested normal forms: act under usual capability of
- Decision: accept (review_status: confirmed)

## is adapted from

- Cluster ID: `rc2_e702f04389de8cb1`
- Assertions: 1
- Phrases: is adapted from
- Suggested normal forms: adapt from
- Decision: pending (review_status: pending)

## is administrative control plane for

- Cluster ID: `rc2_1bfa2aa77feae465`
- Assertions: 1
- Phrases: is administrative control plane for
- Suggested normal forms: administrative control plane for
- Decision: accept (review_status: confirmed)

## is analyzed as

- Cluster ID: `rc2_cf01f5d4b2832889`
- Assertions: 1
- Phrases: is analyzed as
- Suggested normal forms: analyz a
- Decision: accept (review_status: confirmed)

## is applicable For

- Cluster ID: `rc2_2201cf4f09e03e27`
- Assertions: 1
- Phrases: is applicable For
- Suggested normal forms: applicable for
- Decision: pending (review_status: pending)

## is applicable to multiple operating systems produced by

- Cluster ID: `rc2_51625d49208074a7`
- Assertions: 1
- Phrases: is applicable to multiple operating systems produced by
- Suggested normal forms: applicable to multiple operat system produc by
- Decision: pending (review_status: pending)

## is assessed with Attack Vector of

- Cluster ID: `rc2_d2bfffb0ed20f119`
- Assertions: 1
- Phrases: is assessed with Attack Vector of
- Suggested normal forms: assess with attack vector of
- Decision: pending (review_status: pending)

## is assigned score of

- Cluster ID: `rc2_ae7e0dc44606984f`
- Assertions: 1
- Phrases: is assigned score of
- Suggested normal forms: assign score of
- Decision: accept (review_status: confirmed)

## is assigned score of MacroVector from

- Cluster ID: `rc2_f8ea1d6b16564766`
- Assertions: 1
- Phrases: is assigned score of MacroVector from
- Suggested normal forms: assign score of macrovector from
- Decision: accept (review_status: confirmed)

## is assigned to

- Cluster ID: `rc2_ec6493fed2fd117f`
- Assertions: 1
- Phrases: is assigned to
- Suggested normal forms: assign to
- Decision: pending (review_status: pending)

## is attacker know in

- Cluster ID: `rc2_11be9f84bf375482`
- Assertions: 1
- Phrases: is attacker know in
- Suggested normal forms: attacker know in
- Decision: accept (review_status: confirmed)

## is available because

- Cluster ID: `rc2_b2beaf568d52998c`
- Assertions: 1
- Phrases: is available because
- Suggested normal forms: available because
- Decision: pending (review_status: pending)

## is available on CISA ADP website on

- Cluster ID: `rc2_7d7693bc3eb75f44`
- Assertions: 1
- Phrases: is available on CISA ADP website on
- Suggested normal forms: available on cisa adp website on
- Decision: pending (review_status: pending)

## is available through

- Cluster ID: `rc2_9cabe27780244dfe`
- Assertions: 1
- Phrases: is available through
- Suggested normal forms: available through
- Decision: accept (review_status: confirmed)

## is available to actors with

- Cluster ID: `rc2_981c9fd25006962c`
- Assertions: 1
- Phrases: is available to actors with
- Suggested normal forms: available to actor with
- Decision: accept (review_status: confirmed)

## is based in

- Cluster ID: `rc2_6bedd7f9a045fe24`
- Assertions: 1
- Phrases: is based in
- Suggested normal forms: bas in
- Decision: pending (review_status: pending)

## is because

- Cluster ID: `rc2_a511aeeeb8a11993`
- Assertions: 1
- Phrases: is because
- Suggested normal forms: because
- Decision: pending (review_status: pending)

## is behavior of

- Cluster ID: `rc2_7f9d91504979c15d`
- Assertions: 1
- Phrases: is behavior of
- Suggested normal forms: behavior of
- Decision: pending (review_status: pending)

## is behind

- Cluster ID: `rc2_b1b886ce5f5750a0`
- Assertions: 1
- Phrases: is behind
- Suggested normal forms: behind
- Decision: pending (review_status: pending)

## is behind exploitation activity

- Cluster ID: `rc2_d733c6009f70e80f`
- Assertions: 1
- Phrases: is behind exploitation activity
- Suggested normal forms: behind exploitation activity
- Decision: pending (review_status: pending)

## is being abused in

- Cluster ID: `rc2_86ff21e930d2db61`
- Assertions: 1
- Phrases: is being abused in
- Suggested normal forms: be abus in
- Decision: pending (review_status: pending)

## is being coordinated to avoid interfering with

- Cluster ID: `rc2_435a3349a0f7f5b1`
- Assertions: 1
- Phrases: is being coordinated to avoid interfering with
- Suggested normal forms: be coordinat to avoid interfer with
- Decision: pending (review_status: pending)

## is being coordinated with law-enforcement partners to avoid interfering with

- Cluster ID: `rc2_1ec0a40d8737a921`
- Assertions: 1
- Phrases: is being coordinated with law-enforcement partners to avoid interfering with
- Suggested normal forms: be coordinat with law-enforcement partner to avoid interfer with
- Decision: pending (review_status: pending)

## is buffer overflow vulnerability in

- Cluster ID: `rc2_f24c43a7d6873a96`
- Assertions: 1
- Phrases: is buffer overflow vulnerability in
- Suggested normal forms: buffer overflow vulnerability in
- Decision: accept (review_status: confirmed)

## is built to find

- Cluster ID: `rc2_f6c180a92fd68417`
- Assertions: 1
- Phrases: is built to find
- Suggested normal forms: built to find
- Decision: pending (review_status: pending)

## is called during

- Cluster ID: `rc2_b4e7a4a7c9b07c2c`
- Assertions: 1
- Phrases: is called during
- Suggested normal forms: call dur
- Decision: accept (review_status: confirmed)

## is captured by

- Cluster ID: `rc2_d714a4f37761aafa`
- Assertions: 1
- Phrases: is captured by
- Suggested normal forms: captur by
- Decision: pending (review_status: pending)

## is car c'est

- Cluster ID: `rc2_5e8b387a96a41b14`
- Assertions: 1
- Phrases: is car c'est
- Suggested normal forms: car c'est
- Decision: pending (review_status: pending)

## is caused by memory management error within

- Cluster ID: `rc2_6af5f70395035b20`
- Assertions: 1
- Phrases: is caused by memory management error within
- Suggested normal forms: caus by memory management error within
- Decision: pending (review_status: pending)

## is centralized management software

- Cluster ID: `rc2_1da2df10e39dd29b`
- Assertions: 1
- Phrases: is centralized management software
- Suggested normal forms: centraliz management software
- Decision: pending (review_status: pending)

## is change in

- Cluster ID: `rc2_9dbb0fb4bb20a52a`
- Assertions: 1
- Phrases: is change in
- Suggested normal forms: change in
- Decision: accept (review_status: confirmed)

## is class For German organizations under

- Cluster ID: `rc2_315a4bc620427437`
- Assertions: 1
- Phrases: is class For German organizations under
- Suggested normal forms: clas for german organization under
- Decision: accept (review_status: confirmed)

## is class of

- Cluster ID: `rc2_0043751870e3f674`
- Assertions: 1
- Phrases: is class of
- Suggested normal forms: clas of
- Decision: accept (review_status: confirmed)

## is cloud deployments into

- Cluster ID: `rc2_47f187a3d1855398`
- Assertions: 1
- Phrases: is cloud deployments into
- Suggested normal forms: cloud deployment into
- Decision: accept (review_status: confirmed)

## is code injection RCE vulnerability disclosed in

- Cluster ID: `rc2_07c5f7ddaad5fb57`
- Assertions: 1
- Phrases: is code injection RCE vulnerability disclosed in
- Suggested normal forms: code injection rce vulnerability disclos in
- Decision: pending (review_status: pending)

## is code injection-to-BDC-deserialization vulnerability from

- Cluster ID: `rc2_72f71040ddaa1dd9`
- Assertions: 1
- Phrases: is code injection-to-BDC-deserialization vulnerability from
- Suggested normal forms: code injection-to-bdc-deserialization vulnerability from
- Decision: pending (review_status: pending)

## is conditioned on

- Cluster ID: `rc2_421a05393aecaef6`
- Assertions: 1
- Phrases: is conditioned on
- Suggested normal forms: condition on
- Decision: pending (review_status: pending)

## is connected

- Cluster ID: `rc2_5a638a128ca67348`
- Assertions: 1
- Phrases: is connected
- Suggested normal forms: connect
- Decision: accept (review_status: confirmed)

## is connected to Active Directory Federation Services

- Cluster ID: `rc2_06b9d8f6911bbace`
- Assertions: 1
- Phrases: is connected to Active Directory Federation Services
- Suggested normal forms: connect to active directory federation service
- Decision: accept (review_status: confirmed)

## is consequential in

- Cluster ID: `rc2_0d925d49f3b77449`
- Assertions: 1
- Phrases: is consequential in
- Suggested normal forms: consequential in
- Decision: accept (review_status: confirmed)

## is considered part of

- Cluster ID: `rc2_d0c19a56b58b7d55`
- Assertions: 1
- Phrases: is considered part of
- Suggested normal forms: consider part of
- Decision: pending (review_status: pending)

## is considered part of smart speaker system For

- Cluster ID: `rc2_e84978ed93f11e69`
- Assertions: 1
- Phrases: is considered part of smart speaker system For
- Suggested normal forms: consider part of smart speaker system for
- Decision: pending (review_status: pending)

## is consistent for

- Cluster ID: `rc2_2a80dca3bf9cb078`
- Assertions: 1
- Phrases: is consistent for
- Suggested normal forms: consistent for
- Decision: pending (review_status: pending)

## is continuing to analyze

- Cluster ID: `rc2_b2e90eba5f8ad057`
- Assertions: 1
- Phrases: is continuing to analyze
- Suggested normal forms: continu to analyze
- Decision: pending (review_status: pending)

## is defined as

- Cluster ID: `rc2_e12893b7677d5179`
- Assertions: 1
- Phrases: is defined as
- Suggested normal forms: defin a
- Decision: accept (review_status: confirmed)

## is defined as set of

- Cluster ID: `rc2_4b09237d0677efb9`
- Assertions: 1
- Phrases: is defined as set of
- Suggested normal forms: defin a set of
- Decision: accept (review_status: confirmed)

## is defined by

- Cluster ID: `rc2_187acf5b9f037e33`
- Assertions: 1
- Phrases: is defined by
- Suggested normal forms: defin by
- Decision: pending (review_status: pending)

## is defined more than

- Cluster ID: `rc2_4e6240436d6ba4fe`
- Assertions: 1
- Phrases: is defined more than
- Suggested normal forms: defin more than
- Decision: pending (review_status: pending)

## is deployed by

- Cluster ID: `rc2_124b7ab43c6643e0`
- Assertions: 1
- Phrases: is deployed by
- Suggested normal forms: deploy by
- Decision: accept (review_status: confirmed)

## is deployed by data science teams independently of

- Cluster ID: `rc2_4af632c26884de7b`
- Assertions: 1
- Phrases: is deployed by data science teams independently of
- Suggested normal forms: deploy by data science team independently of
- Decision: accept (review_status: confirmed)

## is deployed on secure network unavailable from

- Cluster ID: `rc2_4cf973285aa52621`
- Assertions: 1
- Phrases: is deployed on secure network unavailable from
- Suggested normal forms: deploy on secure network unavailable from
- Decision: pending (review_status: pending)

## is designed for lookup

- Cluster ID: `rc2_ab846ae837782f92`
- Assertions: 1
- Phrases: is designed for lookup
- Suggested normal forms: design for lookup
- Decision: pending (review_status: pending)

## is designed to

- Cluster ID: `rc2_ce37b787032d9681`
- Assertions: 1
- Phrases: is designed to
- Suggested normal forms: design to
- Decision: pending (review_status: pending)

## is designed to exploit

- Cluster ID: `rc2_e04b410fbf7614c3`
- Assertions: 1
- Phrases: is designed to exploit
- Suggested normal forms: design to exploit
- Decision: pending (review_status: pending)

## is determined as difference between

- Cluster ID: `rc2_8e804d38ef9cbc6f`
- Assertions: 1
- Phrases: is determined as difference between
- Suggested normal forms: determin a difference between
- Decision: pending (review_status: pending)

## is determined by corresponding Base metrics as

- Cluster ID: `rc2_7d036f222abffad9`
- Assertions: 1
- Phrases: is determined by corresponding Base metrics as
- Suggested normal forms: determin by correspond base metric a
- Decision: pending (review_status: pending)

## is determined in

- Cluster ID: `rc2_c672aca766ca233b`
- Assertions: 1
- Phrases: is determined in
- Suggested normal forms: determin in
- Decision: pending (review_status: pending)

## is endpoint incident in

- Cluster ID: `rc2_91bf82c47150e919`
- Assertions: 1
- Phrases: is endpoint incident in
- Suggested normal forms: endpoint incident in
- Decision: pending (review_status: pending)

## is enumerable on

- Cluster ID: `rc2_2ee5d9d155e089f8`
- Assertions: 1
- Phrases: is enumerable on
- Suggested normal forms: enumerable on
- Decision: pending (review_status: pending)

## is equal higher than

- Cluster ID: `rc2_a010e79ff56c6f98`
- Assertions: 1
- Phrases: is equal higher than
- Suggested normal forms: equal higher than
- Decision: pending (review_status: pending)

## is equivalent to metric value of

- Cluster ID: `rc2_cd2c0a15b44d374d`
- Assertions: 1
- Phrases: is equivalent to metric value of
- Suggested normal forms: equivalent to metric value of
- Decision: pending (review_status: pending)

## is example

- Cluster ID: `rc2_50d858e0985ecc7f`
- Assertions: 1
- Phrases: is example
- Suggested normal forms: example
- Decision: pending (review_status: pending)

## is example of

- Cluster ID: `rc2_c0c0e126aae41153`
- Assertions: 1
- Phrases: is example of
- Suggested normal forms: example of
- Decision: accept (review_status: confirmed)

## is executed with permission of Windows service

- Cluster ID: `rc2_a800f896edc378b1`
- Assertions: 1
- Phrases: is executed with permission of Windows service
- Suggested normal forms: execut with permission of window service
- Decision: accept (review_status: confirmed)

## is exposed to internet by

- Cluster ID: `rc2_f87eb418bff59b9a`
- Assertions: 1
- Phrases: is exposed to internet by
- Suggested normal forms: expos to internet by
- Decision: accept (review_status: confirmed)

## is exposed to processes unauthenticated traffic As

- Cluster ID: `rc2_a9f58dc3af99047f`
- Assertions: 1
- Phrases: is exposed to processes unauthenticated traffic As
- Suggested normal forms: expos to processe unauthenticat traffic a
- Decision: pending (review_status: pending)

## is exposed to processes unauthenticated traffic as part of

- Cluster ID: `rc2_aea505d084d5fe25`
- Assertions: 1
- Phrases: is exposed to processes unauthenticated traffic as part of
- Suggested normal forms: expos to processe unauthenticat traffic a part of
- Decision: pending (review_status: pending)

## is exposed to untrusted networks As

- Cluster ID: `rc2_524be121a99c0609`
- Assertions: 1
- Phrases: is exposed to untrusted networks As
- Suggested normal forms: expos to untrust network a
- Decision: pending (review_status: pending)

## is exposed to untrusted networks as part of

- Cluster ID: `rc2_df650042c7909f54`
- Assertions: 1
- Phrases: is exposed to untrusted networks as part of
- Suggested normal forms: expos to untrust network a part of
- Decision: pending (review_status: pending)

## is first pass of

- Cluster ID: `rc2_9738b1c5c1aeec2f`
- Assertions: 1
- Phrases: is first pass of
- Suggested normal forms: first pas of
- Decision: pending (review_status: pending)

## is followed during

- Cluster ID: `rc2_6153e209384e7800`
- Assertions: 1
- Phrases: is followed during
- Suggested normal forms: follow dur
- Decision: pending (review_status: pending)

## is force multiplier model guidance from

- Cluster ID: `rc2_320d2878d0a36aac`
- Assertions: 1
- Phrases: is force multiplier model guidance from
- Suggested normal forms: force multiplier model guidance from
- Decision: pending (review_status: pending)

## is form over behavior of

- Cluster ID: `rc2_a3d8dccab34fc8b9`
- Assertions: 1
- Phrases: is form over behavior of
- Suggested normal forms: form over behavior of
- Decision: accept (review_status: confirmed)

## is frequent target for broad control over

- Cluster ID: `rc2_8fee001316243b48`
- Assertions: 1
- Phrases: is frequent target for broad control over
- Suggested normal forms: frequent target for broad control over
- Decision: pending (review_status: pending)

## is from

- Cluster ID: `rc2_75857a45899985be`
- Assertions: 1
- Phrases: is from
- Suggested normal forms: from
- Decision: pending (review_status: pending)

## is greatest for

- Cluster ID: `rc2_3a068e69c6043787`
- Assertions: 1
- Phrases: is greatest for
- Suggested normal forms: greatest for
- Decision: pending (review_status: pending)

## is high-priority indicator

- Cluster ID: `rc2_549c4896847d436c`
- Assertions: 1
- Phrases: is high-priority indicator
- Suggested normal forms: high-priority indicator
- Decision: pending (review_status: pending)

## is high-priority indicator execution on

- Cluster ID: `rc2_1fbfccd48c40abcf`
- Assertions: 1
- Phrases: is high-priority indicator execution on
- Suggested normal forms: high-priority indicator execution on
- Decision: pending (review_status: pending)

## is high-priority indicator requiring investigation execution on

- Cluster ID: `rc2_48b45217bade7d05`
- Assertions: 1
- Phrases: is high-priority indicator requiring investigation execution on
- Suggested normal forms: high-priority indicator requir investigation execution on
- Decision: pending (review_status: pending)

## is ideal vulnerability From

- Cluster ID: `rc2_149f6788398f61a5`
- Assertions: 1
- Phrases: is ideal vulnerability From
- Suggested normal forms: ideal vulnerability from
- Decision: pending (review_status: pending)

## is important variable in

- Cluster ID: `rc2_390a36e227113ac0`
- Assertions: 1
- Phrases: is important variable in
- Suggested normal forms: important variable in
- Decision: pending (review_status: pending)

## is in TrustedSecurityTokenServices

- Cluster ID: `rc2_b4b169c44dce590b`
- Assertions: 1
- Phrases: is in TrustedSecurityTokenServices
- Suggested normal forms: in trustedsecuritytokenservice
- Decision: pending (review_status: pending)

## is initiated outbound by

- Cluster ID: `rc2_0f8d8f5f323f9f1e`
- Assertions: 1
- Phrases: is initiated outbound by
- Suggested normal forms: initiat outbound by
- Decision: accept (review_status: confirmed)

## is integrated

- Cluster ID: `rc2_b482ab1ecae01d10`
- Assertions: 1
- Phrases: is integrated
- Suggested normal forms: integrat
- Decision: pending (review_status: pending)

## is interesting Type attribute in

- Cluster ID: `rc2_fa2d0c31fad0e250`
- Assertions: 1
- Phrases: is interesting Type attribute in
- Suggested normal forms: interest type attribute in
- Decision: pending (review_status: pending)

## is kept in

- Cluster ID: `rc2_ea0340b85ff89412`
- Assertions: 1
- Phrases: is kept in
- Suggested normal forms: kept in
- Decision: pending (review_status: pending)

## is kept up to

- Cluster ID: `rc2_fbf7310841a883c9`
- Assertions: 1
- Phrases: is kept up to
- Suggested normal forms: kept up to
- Decision: accept (review_status: confirmed)

## is known XML element of

- Cluster ID: `rc2_962f016ae7e7f40b`
- Assertions: 1
- Phrases: is known XML element of
- Suggested normal forms: known xml element of
- Decision: pending (review_status: pending)

## is known as

- Cluster ID: `rc2_6c2298a8b1b731b0`
- Assertions: 1
- Phrases: is known as
- Suggested normal forms: known a
- Decision: pending (review_status: pending)

## is less

- Cluster ID: `rc2_7b5454f75089acf2`
- Assertions: 1
- Phrases: is less
- Suggested normal forms: les
- Decision: pending (review_status: pending)

## is limited to service provided by

- Cluster ID: `rc2_0fc3ba6d451aa156`
- Assertions: 1
- Phrases: is limited to service provided by
- Suggested normal forms: limit to service provid by
- Decision: accept (review_status: confirmed)

## is linked to

- Cluster ID: `rc2_bc000fbc2178075d`
- Assertions: 1
- Phrases: is linked to
- Suggested normal forms: link to
- Decision: accept (review_status: confirmed)

## is linked to campaign prior to intelligence sharing with

- Cluster ID: `rc2_f2192c1e35575328`
- Assertions: 1
- Phrases: is linked to campaign prior to intelligence sharing with
- Suggested normal forms: link to campaign prior to intelligence shar with
- Decision: pending (review_status: pending)

## is local.LocalLoginProvider out

- Cluster ID: `rc2_d74fadc60a164f85`
- Assertions: 1
- Phrases: is local.LocalLoginProvider out
- Suggested normal forms: local.localloginprovider out
- Decision: accept (review_status: confirmed)

## is made of

- Cluster ID: `rc2_60aaca356cb99d2d`
- Assertions: 1
- Phrases: is made of
- Suggested normal forms: made of
- Decision: pending (review_status: pending)

## is management plane for

- Cluster ID: `rc2_f825728f86ddfabd`
- Assertions: 1
- Phrases: is management plane for
- Suggested normal forms: management plane for
- Decision: accept (review_status: confirmed)

## is maximum severity distance between highest severity vector and lowest severity vector of

- Cluster ID: `rc2_d747c65f5bd75e33`
- Assertions: 1
- Phrases: is maximum severity distance between highest severity vector and lowest severity vector of
- Suggested normal forms: maximum severity distance between highest severity vector and lowest severity vector of
- Decision: pending (review_status: pending)

## is more severe vulnerability From

- Cluster ID: `rc2_95b85467cc9c9ae5`
- Assertions: 1
- Phrases: is more severe vulnerability From
- Suggested normal forms: more severe vulnerability from
- Decision: pending (review_status: pending)

## is multiplied by proportion of

- Cluster ID: `rc2_1a6b8e7d3d7ccb64`
- Assertions: 1
- Phrases: is multiplied by proportion of
- Suggested normal forms: multipli by proportion of
- Decision: accept (review_status: confirmed)

## is non-functional with

- Cluster ID: `rc2_c69d699a877c3d03`
- Assertions: 1
- Phrases: is non-functional with
- Suggested normal forms: non-functional with
- Decision: pending (review_status: pending)

## is not used

- Cluster ID: `rc2_675def73084bb012`
- Assertions: 1
- Phrases: is not used
- Suggested normal forms: not us
- Decision: pending (review_status: pending)

## is notable as

- Cluster ID: `rc2_a0089650fd10bbb5`
- Assertions: 1
- Phrases: is notable as
- Suggested normal forms: notable a
- Decision: pending (review_status: pending)

## is notable through to

- Cluster ID: `rc2_029a4b529f60c9c8`
- Assertions: 1
- Phrases: is notable through to
- Suggested normal forms: notable through to
- Decision: pending (review_status: pending)

## is object obj out

- Cluster ID: `rc2_5ea0a89f61689c10`
- Assertions: 1
- Phrases: is object obj out
- Suggested normal forms: object obj out
- Decision: accept (review_status: confirmed)

## is object target out

- Cluster ID: `rc2_41fe614852ccd746`
- Assertions: 1
- Phrases: is object target out
- Suggested normal forms: object target out
- Decision: pending (review_status: pending)

## is observed payload for

- Cluster ID: `rc2_e9fbdedce18b1723`
- Assertions: 1
- Phrases: is observed payload for
- Suggested normal forms: observ payload for
- Decision: pending (review_status: pending)

## is obtained by

- Cluster ID: `rc2_26b6947618395259`
- Assertions: 1
- Phrases: is obtained by
- Suggested normal forms: obtain by
- Decision: pending (review_status: pending)

## is of

- Cluster ID: `rc2_28391d3bc64ec15c`
- Assertions: 1
- Phrases: is of
- Suggested normal forms: of
- Decision: pending (review_status: pending)

## is opportunistic with

- Cluster ID: `rc2_c8731f8bf159fa79`
- Assertions: 1
- Phrases: is opportunistic with
- Suggested normal forms: opportunistic with
- Decision: pending (review_status: pending)

## is overload being selected instead of

- Cluster ID: `rc2_ffa8ced164b6748a`
- Assertions: 1
- Phrases: is overload being selected instead of
- Suggested normal forms: overload be select instead of
- Decision: pending (review_status: pending)

## is parsing type from

- Cluster ID: `rc2_41ab7672c5bec6ff`
- Assertions: 1
- Phrases: is parsing type from
- Suggested normal forms: pars type from
- Decision: pending (review_status: pending)

## is position in

- Cluster ID: `rc2_90f7671e0220f59c`
- Assertions: 1
- Phrases: is position in
- Suggested normal forms: position in
- Decision: accept (review_status: confirmed)

## is potential entry point into

- Cluster ID: `rc2_6c421c7e776e9645`
- Assertions: 1
- Phrases: is potential entry point into
- Suggested normal forms: potential entry point into
- Decision: accept (review_status: confirmed)

## is practitioner community

- Cluster ID: `rc2_4869611048761f5b`
- Assertions: 1
- Phrases: is practitioner community
- Suggested normal forms: practitioner community
- Decision: pending (review_status: pending)

## is proposed to adopt optional pass-through Supplemental Metric called Provider Urgency To facilitate

- Cluster ID: `rc2_65d75354db840b5c`
- Assertions: 1
- Phrases: is proposed to adopt optional pass-through Supplemental Metric called Provider Urgency To facilitate
- Suggested normal forms: propos to adopt optional pas-through supplemental metric call provider urgency to facilitate
- Decision: pending (review_status: pending)

## is provisioned by

- Cluster ID: `rc2_06f2b439a96dc01f`
- Assertions: 1
- Phrases: is provisioned by
- Suggested normal forms: provision by
- Decision: pending (review_status: pending)

## is querying

- Cluster ID: `rc2_a8b771920b8319e4`
- Assertions: 1
- Phrases: is querying
- Suggested normal forms: query
- Decision: pending (review_status: pending)

## is querying current score for

- Cluster ID: `rc2_d1cb607dfd9165be`
- Assertions: 1
- Phrases: is querying current score for
- Suggested normal forms: query current score for
- Decision: pending (review_status: pending)

## is reachable from

- Cluster ID: `rc2_ea74f7acc4f310b5`
- Assertions: 1
- Phrases: is reachable from
- Suggested normal forms: reachable from
- Decision: accept (review_status: confirmed)

## is reachable from outside

- Cluster ID: `rc2_9aa9bfb9b4094d9c`
- Assertions: 1
- Phrases: is reachable from outside
- Suggested normal forms: reachable from outside
- Decision: pending (review_status: pending)

## is reachable via

- Cluster ID: `rc2_abc655d8ef81c8e7`
- Assertions: 1
- Phrases: is reachable via
- Suggested normal forms: reachable via
- Decision: accept (review_status: confirmed)

## is reachable without

- Cluster ID: `rc2_1629073bb007be46`
- Assertions: 1
- Phrases: is reachable without
- Suggested normal forms: reachable without
- Decision: pending (review_status: pending)

## is received over network

- Cluster ID: `rc2_bb1c781684595ea6`
- Assertions: 1
- Phrases: is received over network
- Suggested normal forms: receiv over network
- Decision: accept (review_status: confirmed)

## is recommended to use multiple sources of

- Cluster ID: `rc2_1af211cb9ebc9864`
- Assertions: 1
- Phrases: is recommended to use multiple sources of
- Suggested normal forms: recommend to use multiple source of
- Decision: pending (review_status: pending)

## is reference to

- Cluster ID: `rc2_f7dc676341fcd6ea`
- Assertions: 1
- Phrases: is reference to
- Suggested normal forms: reference to
- Decision: accept (review_status: confirmed)

## is released during processing of crafted IKE packets

- Cluster ID: `rc2_438b1d357051e124`
- Assertions: 1
- Phrases: is released during processing of crafted IKE packets
- Suggested normal forms: releas dur process of craft ike packet
- Decision: accept (review_status: confirmed)

## is released more than once

- Cluster ID: `rc2_ab32d9099b8bae1c`
- Assertions: 1
- Phrases: is released more than once
- Suggested normal forms: releas more than once
- Decision: accept (review_status: confirmed)

## is reliable

- Cluster ID: `rc2_20475dfea3a2deb7`
- Assertions: 1
- Phrases: is reliable
- Suggested normal forms: reliable
- Decision: accept (review_status: confirmed)

## is reliable in

- Cluster ID: `rc2_6188a7ef7c21e3d6`
- Assertions: 1
- Phrases: is reliable in
- Suggested normal forms: reliable in
- Decision: pending (review_status: pending)

## is represented as

- Cluster ID: `rc2_bc4b0ac029f17f5e`
- Assertions: 1
- Phrases: is represented as
- Suggested normal forms: represent a
- Decision: pending (review_status: pending)

## is required to be on

- Cluster ID: `rc2_d2e3cbaea2d3c3cd`
- Assertions: 1
- Phrases: is required to be on
- Suggested normal forms: requir to be on
- Decision: pending (review_status: pending)

## is required to be to exploit

- Cluster ID: `rc2_b5cb08ba45cd45cd`
- Assertions: 1
- Phrases: is required to be to exploit
- Suggested normal forms: requir to be to exploit
- Decision: pending (review_status: pending)

## is required to gather

- Cluster ID: `rc2_4ba95c471fb394e0`
- Assertions: 1
- Phrases: is required to gather
- Suggested normal forms: requir to gather
- Decision: accept (review_status: confirmed)

## is responsibility When assessing chain of

- Cluster ID: `rc2_c1579797d5e7a1aa`
- Assertions: 1
- Phrases: is responsibility When assessing chain of
- Suggested normal forms: responsibility when assess chain of
- Decision: pending (review_status: pending)

## is responsibility to populate values of

- Cluster ID: `rc2_f4e6783df3afebbb`
- Assertions: 1
- Phrases: is responsibility to populate values of
- Suggested normal forms: responsibility to populate value of
- Decision: pending (review_status: pending)

## is responsible for

- Cluster ID: `rc2_23a21e0ce351ca46`
- Assertions: 1
- Phrases: is responsible for
- Suggested normal forms: responsible for
- Decision: accept (review_status: confirmed)

## is responsible for proper operation of

- Cluster ID: `rc2_5d9ce7d89e5f643d`
- Assertions: 1
- Phrases: is responsible for proper operation of
- Suggested normal forms: responsible for proper operation of
- Decision: accept (review_status: confirmed)

## is restricted to

- Cluster ID: `rc2_8fce4ec605427bb6`
- Assertions: 1
- Phrases: is restricted to
- Suggested normal forms: restrict to
- Decision: pending (review_status: pending)

## is result of

- Cluster ID: `rc2_6d6641fe18e4b49c`
- Assertions: 1
- Phrases: is result of
- Suggested normal forms: result of
- Decision: pending (review_status: pending)

## is same as

- Cluster ID: `rc2_2ced99838a9a5622`
- Assertions: 1
- Phrases: is same as
- Suggested normal forms: same a
- Decision: pending (review_status: pending)

## is same as issuer of

- Cluster ID: `rc2_bdbae8e611b6981e`
- Assertions: 1
- Phrases: is same as issuer of
- Suggested normal forms: same a issuer of
- Decision: pending (review_status: pending)

## is score of

- Cluster ID: `rc2_0ea2164487a7419c`
- Assertions: 1
- Phrases: is score of
- Suggested normal forms: score of
- Decision: accept (review_status: confirmed)

## is score of MacroVector i.e. score of

- Cluster ID: `rc2_d0386cfaf521dd44`
- Assertions: 1
- Phrases: is score of MacroVector i.e. score of
- Suggested normal forms: score of macrovector i.e. score of
- Decision: accept (review_status: confirmed)

## is scored with

- Cluster ID: `rc2_0c431200fe4f4ef2`
- Assertions: 1
- Phrases: is scored with
- Suggested normal forms: scor with
- Decision: accept (review_status: confirmed)

## is searchable on

- Cluster ID: `rc2_b28e772676024002`
- Assertions: 1
- Phrases: is searchable on
- Suggested normal forms: searchable on
- Decision: pending (review_status: pending)

## is secure VPN within

- Cluster ID: `rc2_b9fa0b79042ef704`
- Assertions: 1
- Phrases: is secure VPN within
- Suggested normal forms: secure vpn within
- Decision: accept (review_status: confirmed)

## is set known as

- Cluster ID: `rc2_3ab5a5118eeafc34`
- Assertions: 1
- Phrases: is set known as
- Suggested normal forms: set known a
- Decision: pending (review_status: pending)

## is set of

- Cluster ID: `rc2_1db12a3d180a728f`
- Assertions: 1
- Phrases: is set of
- Suggested normal forms: set of
- Decision: accept (review_status: confirmed)

## is shown below For

- Cluster ID: `rc2_5f7ab6b6717791c2`
- Assertions: 1
- Phrases: is shown below For
- Suggested normal forms: shown below for
- Decision: pending (review_status: pending)

## is significant amount of

- Cluster ID: `rc2_3b204635c1d65085`
- Assertions: 1
- Phrases: is significant amount of
- Suggested normal forms: significant amount of
- Decision: accept (review_status: confirmed)

## is significant because of

- Cluster ID: `rc2_9ba8cd9378365518`
- Assertions: 1
- Phrases: is significant because of
- Suggested normal forms: significant because of
- Decision: pending (review_status: pending)

## is significant for

- Cluster ID: `rc2_573f085e4a1b3385`
- Assertions: 1
- Phrases: is significant for
- Suggested normal forms: significant for
- Decision: accept (review_status: confirmed)

## is significant than

- Cluster ID: `rc2_6131f6f46517def6`
- Assertions: 1
- Phrases: is significant than
- Suggested normal forms: significant than
- Decision: accept (review_status: confirmed)

## is similar to

- Cluster ID: `rc2_0afcc552ab813e3d`
- Assertions: 1
- Phrases: is similar to
- Suggested normal forms: similar to
- Decision: pending (review_status: pending)

## is something like get specific value from

- Cluster ID: `rc2_6d2d02e92c73dfa2`
- Assertions: 1
- Phrases: is something like get specific value from
- Suggested normal forms: someth like get specific value from
- Decision: pending (review_status: pending)

## is staged for

- Cluster ID: `rc2_a6a3f16b8e174536`
- Assertions: 1
- Phrases: is staged for
- Suggested normal forms: stag for
- Decision: accept (review_status: confirmed)

## is subject to floating

- Cluster ID: `rc2_5924f81357f89ad8`
- Assertions: 1
- Phrases: is subject to floating
- Suggested normal forms: subject to float
- Decision: pending (review_status: pending)

## is supported by

- Cluster ID: `rc2_d499e1984d4d1220`
- Assertions: 1
- Phrases: is supported by
- Suggested normal forms: support by
- Decision: accept (review_status: confirmed)

## is supported by actor 's GitHub activity specifically maintenance of

- Cluster ID: `rc2_4fc95f86e5372af1`
- Assertions: 1
- Phrases: is supported by actor 's GitHub activity specifically maintenance of
- Suggested normal forms: support by actor 's github activity specifically maintenance of
- Decision: pending (review_status: pending)

## is that

- Cluster ID: `rc2_8e7fc0236af43df9`
- Assertions: 1
- Phrases: is that
- Suggested normal forms: that
- Decision: pending (review_status: pending)

## is to define mitigations in

- Cluster ID: `rc2_5a95964a12d2eb7b`
- Assertions: 1
- Phrases: is to define mitigations in
- Suggested normal forms: to define mitigation in
- Decision: pending (review_status: pending)

## is typical for

- Cluster ID: `rc2_9df3021869361fa8`
- Assertions: 1
- Phrases: is typical for
- Suggested normal forms: typical for
- Decision: accept (review_status: confirmed)

## is unauthenticated RCE against

- Cluster ID: `rc2_b7a5195f19780212`
- Assertions: 1
- Phrases: is unauthenticated RCE against
- Suggested normal forms: unauthenticat rce against
- Decision: pending (review_status: pending)

## is unusual in

- Cluster ID: `rc2_98d332a7b98cb6d3`
- Assertions: 1
- Phrases: is unusual in
- Suggested normal forms: unusual in
- Decision: pending (review_status: pending)

## is updated by originating CNA to provide

- Cluster ID: `rc2_9b6978d24f2e5089`
- Assertions: 1
- Phrases: is updated by originating CNA to provide
- Suggested normal forms: updat by originat cna to provide
- Decision: accept (review_status: confirmed)

## is updated to provide

- Cluster ID: `rc2_e50cf98c798bc246`
- Assertions: 1
- Phrases: is updated to provide
- Suggested normal forms: updat to provide
- Decision: accept (review_status: confirmed)

## is used in

- Cluster ID: `rc2_830f3121f36ea520`
- Assertions: 1
- Phrases: is used in
- Suggested normal forms: us in
- Decision: accept (review_status: confirmed)

## is used to provide

- Cluster ID: `rc2_521b384bfd7da16d`
- Assertions: 1
- Phrases: is used to provide
- Suggested normal forms: us to provide
- Decision: pending (review_status: pending)

## is useful to

- Cluster ID: `rc2_294e785057e65bf5`
- Assertions: 1
- Phrases: is useful to
- Suggested normal forms: useful to
- Decision: pending (review_status: pending)

## is useful when

- Cluster ID: `rc2_a7487e9167ee1d9d`
- Assertions: 1
- Phrases: is useful when
- Suggested normal forms: useful when
- Decision: pending (review_status: pending)

## is validated by other reputable sources

- Cluster ID: `rc2_476ddc9c612ad23a`
- Assertions: 1
- Phrases: is validated by other reputable sources
- Suggested normal forms: validat by other reputable source
- Decision: accept (review_status: confirmed)

## is validated by vendor

- Cluster ID: `rc2_087f5e67c76a4ca8`
- Assertions: 1
- Phrases: is validated by vendor
- Suggested normal forms: validat by vendor
- Decision: accept (review_status: confirmed)

## is valuable to

- Cluster ID: `rc2_700dc53dab65c2a1`
- Assertions: 1
- Phrases: is valuable to
- Suggested normal forms: valuable to
- Decision: accept (review_status: confirmed)

## is which parts of

- Cluster ID: `rc2_40a90e8ce38bfc79`
- Assertions: 1
- Phrases: is which parts of
- Suggested normal forms: which part of
- Decision: pending (review_status: pending)

## is worse than

- Cluster ID: `rc2_a8aa0712c2f4e45e`
- Assertions: 1
- Phrases: is worse than
- Suggested normal forms: worse than
- Decision: accept (review_status: confirmed)

## is x5t out

- Cluster ID: `rc2_8291c0697998051b`
- Assertions: 1
- Phrases: is x5t out
- Suggested normal forms: x5t out
- Decision: accept (review_status: confirmed)

## issue

- Cluster ID: `rc2_4a502846d070e208`
- Assertions: 1
- Phrases: issue
- Suggested normal forms: issue
- Decision: accept (review_status: confirmed)

## issue commands as

- Cluster ID: `rc2_d365f4d24c26d6d8`
- Assertions: 1
- Phrases: issue commands as
- Suggested normal forms: issue command a
- Decision: accept (review_status: confirmed)

## it has added flaw

- Cluster ID: `rc2_fe85f63c6919a253`
- Assertions: 1
- Phrases: it has added flaw
- Suggested normal forms: it add flaw
- Decision: accept (review_status: confirmed)

## it has added flaw flag as

- Cluster ID: `rc2_903486b2e5ad635b`
- Assertions: 1
- Phrases: it has added flaw flag as
- Suggested normal forms: it add flaw flag a
- Decision: accept (review_status: confirmed)

## it has added flaw to catalog of

- Cluster ID: `rc2_60d9b91274aa6794`
- Assertions: 1
- Phrases: it has added flaw to catalog of
- Suggested normal forms: it add flaw to catalog of
- Decision: accept (review_status: confirmed)

## know

- Cluster ID: `rc2_cd1bb3012bcfaa0c`
- Assertions: 1
- Phrases: know
- Suggested normal forms: know
- Decision: accept (review_status: confirmed)

## know similar structure to CVE-2026-63520 from

- Cluster ID: `rc2_1802ba799a0b13cd`
- Assertions: 1
- Phrases: know similar structure to CVE-2026-63520 from
- Suggested normal forms: know similar structure to cve-2026-63520 from
- Decision: accept (review_status: confirmed)

## knows from

- Cluster ID: `rc2_7efbe2c7e534df9f`
- Assertions: 1
- Phrases: knows from
- Suggested normal forms: know from
- Decision: accept (review_status: confirmed)

## launched

- Cluster ID: `rc2_abfc412ce6e530df`
- Assertions: 1
- Phrases: launched
- Suggested normal forms: launch
- Decision: pending (review_status: pending)

## launched parallel scanning across

- Cluster ID: `rc2_6654fa5df8b6893f`
- Assertions: 1
- Phrases: launched parallel scanning across
- Suggested normal forms: launch parallel scann acros
- Decision: pending (review_status: pending)

## lead to exploitation of

- Cluster ID: `rc2_7821454d4d131b45`
- Assertions: 1
- Phrases: lead to exploitation of
- Suggested normal forms: lead to exploitation of
- Decision: accept (review_status: confirmed)

## lead to major loss of

- Cluster ID: `rc2_60fdc3ac300a01a1`
- Assertions: 1
- Phrases: lead to major loss of
- Suggested normal forms: lead to major los of
- Decision: accept (review_status: confirmed)

## leads to malfunction of

- Cluster ID: `rc2_76d510b128b79cee`
- Assertions: 1
- Phrases: leads to malfunction of
- Suggested normal forms: lead to malfunction of
- Decision: pending (review_status: pending)

## leaned on earlier experimentation with

- Cluster ID: `rc2_d516c4ed4435407f`
- Assertions: 1
- Phrases: leaned on earlier experimentation with
- Suggested normal forms: lean on earlier experimentation with
- Decision: pending (review_status: pending)

## learn

- Cluster ID: `rc2_6a8da52e920664ef`
- Assertions: 1
- Phrases: learn
- Suggested normal forms: learn
- Decision: pending (review_status: pending)

## led actor to select most permissive model for

- Cluster ID: `rc2_9788a3e34b1e7399`
- Assertions: 1
- Phrases: led actor to select most permissive model for
- Suggested normal forms: l actor to select most permissive model for
- Decision: pending (review_status: pending)

## led safety systems to

- Cluster ID: `rc2_6f5e27de85e48fa7`
- Assertions: 1
- Phrases: led safety systems to
- Suggested normal forms: l safety system to
- Decision: accept (review_status: confirmed)

## leveraged

- Cluster ID: `rc2_1ada63f0bdface52`
- Assertions: 1
- Phrases: leveraged
- Suggested normal forms: leverag
- Decision: pending (review_status: pending)

## leveraged following tools in

- Cluster ID: `rc2_2223df3fa1e9edc2`
- Assertions: 1
- Phrases: leveraged following tools in
- Suggested normal forms: leverag follow tool in
- Decision: pending (review_status: pending)

## lies in

- Cluster ID: `rc2_a2515dc1fc7f2d12`
- Assertions: 1
- Phrases: lies in
- Suggested normal forms: ly in
- Decision: pending (review_status: pending)

## like to thank Abigail Palacios for

- Cluster ID: `rc2_b735ddb12118d7d8`
- Assertions: 1
- Phrases: like to thank Abigail Palacios for
- Suggested normal forms: like to thank abigail palacio for
- Decision: accept (review_status: confirmed)

## like to thank Abigail Palacios from

- Cluster ID: `rc2_e47ec89f2010c474`
- Assertions: 1
- Phrases: like to thank Abigail Palacios from
- Suggested normal forms: like to thank abigail palacio from
- Decision: accept (review_status: confirmed)

## like to thank Grace Staley from

- Cluster ID: `rc2_cce1571f239959a1`
- Assertions: 1
- Phrases: like to thank Grace Staley from
- Suggested normal forms: like to thank grace staley from
- Decision: accept (review_status: confirmed)

## like to thank Ian Barton of

- Cluster ID: `rc2_c2f14ecc7c1503ff`
- Assertions: 1
- Phrases: like to thank Ian Barton of
- Suggested normal forms: like to thank ian barton of
- Decision: accept (review_status: confirmed)

## like to thank Vivian Smith for

- Cluster ID: `rc2_49926b94c616b62b`
- Assertions: 1
- Phrases: like to thank Vivian Smith for
- Suggested normal forms: like to thank vivian smith for
- Decision: accept (review_status: confirmed)

## like to thank Vivian Smith from

- Cluster ID: `rc2_265953c6810fe696`
- Assertions: 1
- Phrases: like to thank Vivian Smith from
- Suggested normal forms: like to thank vivian smith from
- Decision: accept (review_status: confirmed)

## limited effectiveness for

- Cluster ID: `rc2_18dc46582667f6c8`
- Assertions: 1
- Phrases: limited effectiveness for
- Suggested normal forms: limit effectivenes for
- Decision: pending (review_status: pending)

## linked

- Cluster ID: `rc2_b1b1bdb480c61d07`
- Assertions: 1
- Phrases: linked
- Suggested normal forms: link
- Decision: pending (review_status: pending)

## linked method to

- Cluster ID: `rc2_8e405a06fdd312da`
- Assertions: 1
- Phrases: linked method to
- Suggested normal forms: link method to
- Decision: pending (review_status: pending)

## list distinct vulnerabilities along with

- Cluster ID: `rc2_f5649ca6d51ac3e9`
- Assertions: 1
- Phrases: list distinct vulnerabilities along with
- Suggested normal forms: list distinct vulnerability along with
- Decision: pending (review_status: pending)

## list resulting score along with

- Cluster ID: `rc2_3739c8821381cbab`
- Assertions: 1
- Phrases: list resulting score along with
- Suggested normal forms: list result score along with
- Decision: pending (review_status: pending)

## live during

- Cluster ID: `rc2_a5f9d901c6686069`
- Assertions: 1
- Phrases: live during
- Suggested normal forms: live dur
- Decision: accept (review_status: confirmed)

## log in as

- Cluster ID: `rc2_69c5f3520e13da3e`
- Assertions: 1
- Phrases: log in as
- Suggested normal forms: log in a
- Decision: pending (review_status: pending)

## looked at

- Cluster ID: `rc2_2cc56642d9a6a072`
- Assertions: 1
- Phrases: looked at
- Suggested normal forms: look at
- Decision: pending (review_status: pending)

## looked like

- Cluster ID: `rc2_2b30614115847ba7`
- Assertions: 1
- Phrases: looked like
- Suggested normal forms: look like
- Decision: pending (review_status: pending)

## looked like right path towards

- Cluster ID: `rc2_cb8ca3f93988839e`
- Assertions: 1
- Phrases: looked like right path towards
- Suggested normal forms: look like right path toward
- Decision: pending (review_status: pending)

## maintains authoritative source of

- Cluster ID: `rc2_d9982e33dde5caf3`
- Assertions: 1
- Phrases: maintains authoritative source of
- Suggested normal forms: maintain authoritative source of
- Decision: accept (review_status: confirmed)

## make structured use of

- Cluster ID: `rc2_8ac768a8e66d4fa2`
- Assertions: 1
- Phrases: make structured use of
- Suggested normal forms: make structur use of
- Decision: pending (review_status: pending)

## managed to get

- Cluster ID: `rc2_cb093e8575851cee`
- Assertions: 1
- Phrases: managed to get
- Suggested normal forms: manag to get
- Decision: pending (review_status: pending)

## managed to get valid BDCM model instantiate System.Object visible in

- Cluster ID: `rc2_a4abb3e504db0be1`
- Assertions: 1
- Phrases: managed to get valid BDCM model instantiate System.Object visible in
- Suggested normal forms: manag to get valid bdcm model instantiate system.object visible in
- Decision: pending (review_status: pending)

## manages virtualisation for

- Cluster ID: `rc2_ce0483e4139535af`
- Assertions: 1
- Phrases: manages virtualisation for
- Suggested normal forms: manage virtualisation for
- Decision: accept (review_status: confirmed)

## matches

- Cluster ID: `rc2_4a0d9299dcb1e696`
- Assertions: 1
- Phrases: matches
- Suggested normal forms: matche
- Decision: accept (review_status: confirmed)

## means that

- Cluster ID: `rc2_c0303e3beba02afd`
- Assertions: 1
- Phrases: means that
- Suggested normal forms: mean that
- Decision: pending (review_status: pending)

## means that attacker reasonably In

- Cluster ID: `rc2_c3e6419002b08720`
- Assertions: 1
- Phrases: means that attacker reasonably In
- Suggested normal forms: mean that attacker reasonably in
- Decision: pending (review_status: pending)

## measure additional extrinsic attributes of

- Cluster ID: `rc2_779e34e0df7134ec`
- Assertions: 1
- Phrases: measure additional extrinsic attributes of
- Suggested normal forms: measure additional extrinsic attribute of
- Decision: accept (review_status: confirmed)

## measures degree of

- Cluster ID: `rc2_85055f2f467194c3`
- Assertions: 1
- Phrases: measures degree of
- Suggested normal forms: measure degree of
- Decision: pending (review_status: pending)

## measures degree of difficulty to mitigate vulnerability in

- Cluster ID: `rc2_3f3603a007ce42f0`
- Assertions: 1
- Phrases: measures degree of difficulty to mitigate vulnerability in
- Suggested normal forms: measure degree of difficulty to mitigate vulnerability in
- Decision: pending (review_status: pending)

## method achieved

- Cluster ID: `rc2_a889bd9628acf52a`
- Assertions: 1
- Phrases: method achieved
- Suggested normal forms: method achiev
- Decision: accept (review_status: confirmed)

## modify Environmental Score prior to applying

- Cluster ID: `rc2_808f58eb7e3a0f79`
- Assertions: 1
- Phrases: modify Environmental Score prior to applying
- Suggested normal forms: modify environmental score prior to apply
- Decision: pending (review_status: pending)

## move

- Cluster ID: `rc2_683a62ce15fbabb1`
- Assertions: 1
- Phrases: move
- Suggested normal forms: move
- Decision: pending (review_status: pending)

## move into other parts of

- Cluster ID: `rc2_0e67b88d26729b5a`
- Assertions: 1
- Phrases: move into other parts of
- Suggested normal forms: move into other part of
- Decision: pending (review_status: pending)

## named

- Cluster ID: `rc2_592372bb39bc1c65`
- Assertions: 1
- Phrases: named
- Suggested normal forms: nam
- Decision: pending (review_status: pending)

## narrow

- Cluster ID: `rc2_5eda958e9ddee772`
- Assertions: 1
- Phrases: narrow
- Suggested normal forms: narrow
- Decision: accept (review_status: confirmed)

## navigate through

- Cluster ID: `rc2_a0854bd01fa2569c`
- Assertions: 1
- Phrases: navigate through
- Suggested normal forms: navigate through
- Decision: accept (review_status: confirmed)

## navigate through CISA SSVC tree model to final overall decision for

- Cluster ID: `rc2_094be535fdada0df`
- Assertions: 1
- Phrases: navigate through CISA SSVC tree model to final overall decision for
- Suggested normal forms: navigate through cisa ssvc tree model to final overall decision for
- Decision: pending (review_status: pending)

## need to account for impacts When identifying values for

- Cluster ID: `rc2_c4c3434542b13730`
- Assertions: 1
- Phrases: need to account for impacts When identifying values for
- Suggested normal forms: ne to account for impact when identify value for
- Decision: pending (review_status: pending)

## need to account for impacts to impacts outside of Vulnerable System When identifying values for

- Cluster ID: `rc2_ab5c9eb66a183c87`
- Assertions: 1
- Phrases: need to account for impacts to impacts outside of Vulnerable System When identifying values for
- Suggested normal forms: ne to account for impact to impact outside of vulnerable system when identify value for
- Decision: pending (review_status: pending)

## need to be launched

- Cluster ID: `rc2_248e3021fe01ce5e`
- Assertions: 1
- Phrases: need to be launched
- Suggested normal forms: ne to be launch
- Decision: pending (review_status: pending)

## need to be launched multiple times against

- Cluster ID: `rc2_7029ed3b4afb6efe`
- Assertions: 1
- Phrases: need to be launched multiple times against
- Suggested normal forms: ne to be launch multiple time against
- Decision: pending (review_status: pending)

## need to be launched multiple times before

- Cluster ID: `rc2_b4354f474fbb0b37`
- Assertions: 1
- Phrases: need to be launched multiple times before
- Suggested normal forms: ne to be launch multiple time before
- Decision: pending (review_status: pending)

## need to evaluate effect of

- Cluster ID: `rc2_48bcea37460cf852`
- Assertions: 1
- Phrases: need to evaluate effect of
- Suggested normal forms: ne to evaluate effect of
- Decision: accept (review_status: confirmed)

## need to write

- Cluster ID: `rc2_b3340a43b0b9ef06`
- Assertions: 1
- Phrases: need to write
- Suggested normal forms: ne to write
- Decision: accept (review_status: confirmed)

## needed to make

- Cluster ID: `rc2_fa5a7a12176655d7`
- Assertions: 1
- Phrases: needed to make
- Suggested normal forms: need to make
- Decision: pending (review_status: pending)

## needed to make request to process model As

- Cluster ID: `rc2_1d2e0b8932a639a9`
- Assertions: 1
- Phrases: needed to make request to process model As
- Suggested normal forms: need to make request to proces model a
- Decision: pending (review_status: pending)

## needs to

- Cluster ID: `rc2_61ee47d132b04d2d`
- Assertions: 1
- Phrases: needs to
- Suggested normal forms: ne to
- Decision: pending (review_status: pending)

## obtains privileged credentials

- Cluster ID: `rc2_25e31df7005ca411`
- Assertions: 1
- Phrases: obtains privileged credentials
- Suggested normal forms: obtain privileg credential
- Decision: accept (review_status: confirmed)

## obtains privileged credentials prior to

- Cluster ID: `rc2_c356439bf28ff472`
- Assertions: 1
- Phrases: obtains privileged credentials prior to
- Suggested normal forms: obtain privileg credential prior to
- Decision: accept (review_status: confirmed)

## occur when

- Cluster ID: `rc2_c7634049c595286e`
- Assertions: 1
- Phrases: occur when
- Suggested normal forms: occur when
- Decision: pending (review_status: pending)

## opens

- Cluster ID: `rc2_2348f99874421257`
- Assertions: 1
- Phrases: opens
- Suggested normal forms: open
- Decision: accept (review_status: confirmed)

## opens outbound SSH tunnel from

- Cluster ID: `rc2_394a83e1e1ac27f2`
- Assertions: 1
- Phrases: opens outbound SSH tunnel from
- Suggested normal forms: open outbound ssh tunnel from
- Decision: accept (review_status: confirmed)

## opens outbound SSH tunnel to

- Cluster ID: `rc2_c734570db8f29558`
- Assertions: 1
- Phrases: opens outbound SSH tunnel to
- Suggested normal forms: open outbound ssh tunnel to
- Decision: accept (review_status: confirmed)

## operate

- Cluster ID: `rc2_2c29d39181de8f85`
- Assertions: 1
- Phrases: operate
- Suggested normal forms: operate
- Decision: pending (review_status: pending)

## operates as

- Cluster ID: `rc2_3c12f56c63b34cbd`
- Assertions: 1
- Phrases: operates as
- Suggested normal forms: operate a
- Decision: pending (review_status: pending)

## orchestrated

- Cluster ID: `rc2_5185fe7745278bd5`
- Assertions: 1
- Phrases: orchestrated
- Suggested normal forms: orchestrat
- Decision: pending (review_status: pending)

## orchestrated multiple AI platforms

- Cluster ID: `rc2_00456f8e0053ee18`
- Assertions: 1
- Phrases: orchestrated multiple AI platforms
- Suggested normal forms: orchestrat multiple ai platform
- Decision: pending (review_status: pending)

## orchestrated operator via Telegram for

- Cluster ID: `rc2_ca64d58f5322463d`
- Assertions: 1
- Phrases: orchestrated operator via Telegram for
- Suggested normal forms: orchestrat operator via telegram for
- Decision: pending (review_status: pending)

## ordered

- Cluster ID: `rc2_3eeb7e96e59ce40f`
- Assertions: 1
- Phrases: ordered
- Suggested normal forms: order
- Decision: pending (review_status: pending)

## owns right in

- Cluster ID: `rc2_be97260cc56371f9`
- Assertions: 1
- Phrases: owns right in
- Suggested normal forms: own right in
- Decision: pending (review_status: pending)

## pairing with CVE-2026-55040 authentication bypass achieved

- Cluster ID: `rc2_5a2993786ff0c735`
- Assertions: 1
- Phrases: pairing with CVE-2026-55040 authentication bypass achieved
- Suggested normal forms: pair with cve-2026-55040 authentication bypas achiev
- Decision: accept (review_status: confirmed)

## parses

- Cluster ID: `rc2_30c471f6aafbca70`
- Assertions: 1
- Phrases: parses
- Suggested normal forms: parse
- Decision: pending (review_status: pending)

## pass

- Cluster ID: `rc2_7f1f073d8bb9b2e3`
- Assertions: 1
- Phrases: pass
- Suggested normal forms: pas
- Decision: pending (review_status: pending)

## pass them In

- Cluster ID: `rc2_850182e3d66d232c`
- Assertions: 1
- Phrases: pass them In
- Suggested normal forms: pas them in
- Decision: pending (review_status: pending)

## pass them to

- Cluster ID: `rc2_a74d6e5b8e9baa30`
- Assertions: 1
- Phrases: pass them to
- Suggested normal forms: pas them to
- Decision: pending (review_status: pending)

## pass them without checking validity of

- Cluster ID: `rc2_65d01559a2ebc67d`
- Assertions: 1
- Phrases: pass them without checking validity of
- Suggested normal forms: pas them without check validity of
- Decision: pending (review_status: pending)

## passed to separate system with

- Cluster ID: `rc2_5b1f3363998cd67f`
- Assertions: 1
- Phrases: passed to separate system with
- Suggested normal forms: pass to separate system with
- Decision: pending (review_status: pending)

## passes through

- Cluster ID: `rc2_859737fd0dae3ac4`
- Assertions: 1
- Phrases: passes through
- Suggested normal forms: passe through
- Decision: pending (review_status: pending)

## patched CVE-2026-65400 on

- Cluster ID: `rc2_ed6c5ea32b18ccdd`
- Assertions: 1
- Phrases: patched CVE-2026-65400 on
- Suggested normal forms: patch cve-2026-65400 on
- Decision: accept (review_status: confirmed)

## patched vCenter 's Syslog server on

- Cluster ID: `rc2_2e112adbe9bf8867`
- Assertions: 1
- Phrases: patched vCenter 's Syslog server on
- Suggested normal forms: patch vcenter 's syslog server on
- Decision: accept (review_status: confirmed)

## pause

- Cluster ID: `rc2_6210c0bf05396716`
- Assertions: 1
- Phrases: pause
- Suggested normal forms: pause
- Decision: pending (review_status: pending)

## pause for a minute to talk about concept

- Cluster ID: `rc2_bc314644a25e7bc1`
- Assertions: 1
- Phrases: pause for a minute to talk about concept
- Suggested normal forms: pause for a minute to talk about concept
- Decision: pending (review_status: pending)

## perform In

- Cluster ID: `rc2_41581ce0357408c6`
- Assertions: 1
- Phrases: perform In
- Suggested normal forms: perform in
- Decision: accept (review_status: confirmed)

## perform additional attacks

- Cluster ID: `rc2_59297751cb7488dc`
- Assertions: 1
- Phrases: perform additional attacks
- Suggested normal forms: perform additional attack
- Decision: pending (review_status: pending)

## perform arbitrary operations such as

- Cluster ID: `rc2_9ccdb43fdf1ebdb2`
- Assertions: 1
- Phrases: perform arbitrary operations such as
- Suggested normal forms: perform arbitrary operation such a
- Decision: accept (review_status: confirmed)

## perform during

- Cluster ID: `rc2_9eaf65d93242ab8d`
- Assertions: 1
- Phrases: perform during
- Suggested normal forms: perform dur
- Decision: accept (review_status: confirmed)

## perform operations against

- Cluster ID: `rc2_af39c447357bc7ff`
- Assertions: 1
- Phrases: perform operations against
- Suggested normal forms: perform operation against
- Decision: pending (review_status: pending)

## perform operations as

- Cluster ID: `rc2_d6c60e8ec0ac7897`
- Assertions: 1
- Phrases: perform operations as
- Suggested normal forms: perform operation a
- Decision: accept (review_status: confirmed)

## permits attacker to exhaust shared system resource such as

- Cluster ID: `rc2_5a2dc42a636ca560`
- Assertions: 1
- Phrases: permits attacker to exhaust shared system resource such as
- Suggested normal forms: permit attacker to exhaust shar system resource such a
- Decision: accept (review_status: confirmed)

## pin

- Cluster ID: `rc2_64f46a7526a186d2`
- Assertions: 1
- Phrases: pin
- Suggested normal forms: pin
- Decision: pending (review_status: pending)

## pin request to

- Cluster ID: `rc2_394bff20dff94062`
- Assertions: 1
- Phrases: pin request to
- Suggested normal forms: pin request to
- Decision: pending (review_status: pending)

## plans

- Cluster ID: `rc2_64879f7d6b960a01`
- Assertions: 1
- Phrases: plans
- Suggested normal forms: plan
- Decision: pending (review_status: pending)

## points to

- Cluster ID: `rc2_2f2b81e22d39ecfa`
- Assertions: 1
- Phrases: points to
- Suggested normal forms: point to
- Decision: pending (review_status: pending)

## possess to exploiting vulnerability

- Cluster ID: `rc2_1532bd1a7dc2efeb`
- Assertions: 1
- Phrases: possess to exploiting vulnerability
- Suggested normal forms: posses to exploit vulnerability
- Decision: accept (review_status: confirmed)

## pour

- Cluster ID: `rc2_ed29bcecc78d7ffb`
- Assertions: 1
- Phrases: pour
- Suggested normal forms: pour
- Decision: pending (review_status: pending)

## pour fonctionner de manière cohérente sur toutes les versions

- Cluster ID: `rc2_460f5371dae95cc7`
- Assertions: 1
- Phrases: pour fonctionner de manière cohérente sur toutes les versions
- Suggested normal forms: pour fonctionner de manière cohérente sur toute le version
- Decision: accept (review_status: confirmed)

## pour l' éteindre

- Cluster ID: `rc2_22d5280868819c5a`
- Assertions: 1
- Phrases: pour l' éteindre
- Suggested normal forms: pour l' éteindre
- Decision: pending (review_status: pending)

## prefer

- Cluster ID: `rc2_472dc7749c49f123`
- Assertions: 1
- Phrases: prefer
- Suggested normal forms: prefer
- Decision: accept (review_status: confirmed)

## prevents vulnerability from

- Cluster ID: `rc2_5f819b82874157d2`
- Assertions: 1
- Phrases: prevents vulnerability from
- Suggested normal forms: prevent vulnerability from
- Decision: accept (review_status: confirmed)

## prioritise

- Cluster ID: `rc2_e370499df49ab1e8`
- Assertions: 1
- Phrases: prioritise
- Suggested normal forms: prioritise
- Decision: pending (review_status: pending)

## proceeds to call

- Cluster ID: `rc2_6ab0163c2f2181a6`
- Assertions: 1
- Phrases: proceeds to call
- Suggested normal forms: proce to call
- Decision: pending (review_status: pending)

## provide copy of policies If requested by

- Cluster ID: `rc2_230324d7a0066a8e`
- Assertions: 1
- Phrases: provide copy of policies If requested by
- Suggested normal forms: provide copy of policy if request by
- Decision: accept (review_status: confirmed)

## provide copy of procedures If requested by

- Cluster ID: `rc2_44070ed240720d41`
- Assertions: 1
- Phrases: provide copy of procedures If requested by
- Suggested normal forms: provide copy of procedure if request by
- Decision: pending (review_status: pending)

## provide copy of updated vulnerability management policies if requested by

- Cluster ID: `rc2_e44dca129f2645eb`
- Assertions: 1
- Phrases: provide copy of updated vulnerability management policies if requested by
- Suggested normal forms: provide copy of updat vulnerability management policy if request by
- Decision: pending (review_status: pending)

## provide direct access into

- Cluster ID: `rc2_f120357db0da0b5a`
- Assertions: 1
- Phrases: provide direct access into
- Suggested normal forms: provide direct acces into
- Decision: accept (review_status: confirmed)

## provide procedures if requested by

- Cluster ID: `rc2_27a65fb00de2322c`
- Assertions: 1
- Phrases: provide procedures if requested by
- Suggested normal forms: provide procedure if request by
- Decision: pending (review_status: pending)

## provide public reporting of

- Cluster ID: `rc2_3930ab244c052211`
- Assertions: 1
- Phrases: provide public reporting of
- Suggested normal forms: provide public report of
- Decision: accept (review_status: confirmed)

## provides guidance on

- Cluster ID: `rc2_90032ec6b918f451`
- Assertions: 1
- Phrases: provides guidance on
- Suggested normal forms: provide guidance on
- Decision: pending (review_status: pending)

## provides likelihood of

- Cluster ID: `rc2_6053c85453965f06`
- Assertions: 1
- Phrases: provides likelihood of
- Suggested normal forms: provide likelihood of
- Decision: accept (review_status: confirmed)

## provides two-pass enrichment for

- Cluster ID: `rc2_e581167bd604dcae`
- Assertions: 1
- Phrases: provides two-pass enrichment for
- Suggested normal forms: provide two-pas enrichment for
- Decision: pending (review_status: pending)

## publish updates at

- Cluster ID: `rc2_b30b78de1692efeb`
- Assertions: 1
- Phrases: publish updates at
- Suggested normal forms: publish update at
- Decision: accept (review_status: confirmed)

## published PoC for

- Cluster ID: `rc2_724d80516418f36d`
- Assertions: 1
- Phrases: published PoC for
- Suggested normal forms: publish poc for
- Decision: accept (review_status: confirmed)

## published PoC for CVE-2026-55040 on

- Cluster ID: `rc2_66bcc6f89d6d27d8`
- Assertions: 1
- Phrases: published PoC for CVE-2026-55040 on
- Suggested normal forms: publish poc for cve-2026-55040 on
- Decision: accept (review_status: confirmed)

## publishes technical details for

- Cluster ID: `rc2_f06c8728c0c80ec1`
- Assertions: 1
- Phrases: publishes technical details for
- Suggested normal forms: publishe technical detail for
- Decision: accept (review_status: confirmed)

## pulls from

- Cluster ID: `rc2_92cabd979184cd1b`
- Assertions: 1
- Phrases: pulls from
- Suggested normal forms: pull from
- Decision: pending (review_status: pending)

## pulls from Class property in

- Cluster ID: `rc2_d437655e2aa1031b`
- Assertions: 1
- Phrases: pulls from Class property in
- Suggested normal forms: pull from clas property in
- Decision: pending (review_status: pending)

## qualify

- Cluster ID: `rc2_e48cfe4f6f37ec01`
- Assertions: 1
- Phrases: qualify
- Suggested normal forms: qualify
- Decision: pending (review_status: pending)

## ran

- Cluster ID: `rc2_c8fc6bf296faa18d`
- Assertions: 1
- Phrases: ran
- Suggested normal forms: ran
- Decision: pending (review_status: pending)

## ranges to identify

- Cluster ID: `rc2_003ebe46ac223924`
- Assertions: 1
- Phrases: ranges to identify
- Suggested normal forms: range to identify
- Decision: accept (review_status: confirmed)

## rate higher-scored vector set as more severe certain percentage of

- Cluster ID: `rc2_920d91fda87fffdd`
- Assertions: 1
- Phrases: rate higher-scored vector set as more severe certain percentage of
- Suggested normal forms: rate higher-scor vector set a more severe certain percentage of
- Decision: pending (review_status: pending)

## reach

- Cluster ID: `rc2_ed4561f685f13353`
- Assertions: 1
- Phrases: reach
- Suggested normal forms: reach
- Decision: accept (review_status: confirmed)

## reaches

- Cluster ID: `rc2_f61028db9a6c6e1b`
- Assertions: 1
- Phrases: reaches
- Suggested normal forms: reache
- Decision: pending (review_status: pending)

## read from

- Cluster ID: `rc2_e6540d43a27a853a`
- Assertions: 1
- Phrases: read from
- Suggested normal forms: read from
- Decision: accept (review_status: confirmed)

## receives

- Cluster ID: `rc2_95100519be034221`
- Assertions: 1
- Phrases: receives
- Suggested normal forms: receive
- Decision: pending (review_status: pending)

## recommends remediating Act vulnerabilities

- Cluster ID: `rc2_83bac6565b5f7956`
- Assertions: 1
- Phrases: recommends remediating Act vulnerabilities
- Suggested normal forms: recommend remediat act vulnerability
- Decision: pending (review_status: pending)

## recommends remediating Act vulnerabilities as soon as

- Cluster ID: `rc2_f4ec6c6233c07c57`
- Assertions: 1
- Phrases: recommends remediating Act vulnerabilities as soon as
- Suggested normal forms: recommend remediat act vulnerability a soon a
- Decision: pending (review_status: pending)

## recovered

- Cluster ID: `rc2_ec3915f542e0f8cb`
- Assertions: 1
- Phrases: recovered
- Suggested normal forms: recover
- Decision: pending (review_status: pending)

## recovered following sequence from

- Cluster ID: `rc2_d365ddf74a5aa4d5`
- Assertions: 1
- Phrases: recovered following sequence from
- Suggested normal forms: recover follow sequence from
- Decision: pending (review_status: pending)

## recurses into

- Cluster ID: `rc2_fe06f68665a1525e`
- Assertions: 1
- Phrases: recurses into
- Suggested normal forms: recurse into
- Decision: pending (review_status: pending)

## reduces expert effort into

- Cluster ID: `rc2_c2f6e68cc47382fc`
- Assertions: 1
- Phrases: reduces expert effort into
- Suggested normal forms: reduce expert effort into
- Decision: pending (review_status: pending)

## refers to operation of

- Cluster ID: `rc2_ccc2543a8db45609`
- Assertions: 1
- Phrases: refers to operation of
- Suggested normal forms: refer to operation of
- Decision: pending (review_status: pending)

## refine

- Cluster ID: `rc2_7baef513d86be18f`
- Assertions: 1
- Phrases: refine
- Suggested normal forms: refine
- Decision: pending (review_status: pending)

## refine further

- Cluster ID: `rc2_e52710ca4080041a`
- Assertions: 1
- Phrases: refine further
- Suggested normal forms: refine further
- Decision: pending (review_status: pending)

## refine resulting severity score to

- Cluster ID: `rc2_1f6f25fb1b0211c3`
- Assertions: 1
- Phrases: refine resulting severity score to
- Suggested normal forms: refine result severity score to
- Decision: pending (review_status: pending)

## reflects change in

- Cluster ID: `rc2_09ffbf0ccf9cf581`
- Assertions: 1
- Phrases: reflects change in
- Suggested normal forms: reflect change in
- Decision: pending (review_status: pending)

## reflects characteristics of vulnerability intrinsic qualities of

- Cluster ID: `rc2_976a378ddbfc3142`
- Assertions: 1
- Phrases: reflects characteristics of vulnerability intrinsic qualities of
- Suggested normal forms: reflect characteristic of vulnerability intrinsic quality of
- Decision: pending (review_status: pending)

## refused

- Cluster ID: `rc2_e370290e6d9ee7da`
- Assertions: 1
- Phrases: refused
- Suggested normal forms: refus
- Decision: accept (review_status: confirmed)

## relates to

- Cluster ID: `rc2_dca2a31ec44d0f85`
- Assertions: 1
- Phrases: relates to
- Suggested normal forms: relate to
- Decision: accept (review_status: confirmed)

## released patches for

- Cluster ID: `rc2_bf4a53a021bc6910`
- Assertions: 1
- Phrases: released patches for
- Suggested normal forms: releas patche for
- Decision: pending (review_status: pending)

## released security updates for

- Cluster ID: `rc2_ca342ca25898e25d`
- Assertions: 1
- Phrases: released security updates for
- Suggested normal forms: releas security update for
- Decision: accept (review_status: confirmed)

## released security updates for CVE-2026-33824 on

- Cluster ID: `rc2_e837de55347add0a`
- Assertions: 1
- Phrases: released security updates for CVE-2026-33824 on
- Suggested normal forms: releas security update for cve-2026-33824 on
- Decision: pending (review_status: pending)

## rely on helper functions defined as

- Cluster ID: `rc2_a8202b72de68d295`
- Assertions: 1
- Phrases: rely on helper functions defined as
- Suggested normal forms: rely on helper function defin a
- Decision: pending (review_status: pending)

## remediates

- Cluster ID: `rc2_06b9c7fc60671c97`
- Assertions: 1
- Phrases: remediates
- Suggested normal forms: remediate
- Decision: accept (review_status: confirmed)

## remove assessed metrics for specific elements from updated CVE Record CVE Record with

- Cluster ID: `rc2_407a04c3a0bdf1d5`
- Assertions: 1
- Phrases: remove assessed metrics for specific elements from updated CVE Record CVE Record with
- Suggested normal forms: remove assess metric for specific element from updat cve record cve record with
- Decision: pending (review_status: pending)

## renamed

- Cluster ID: `rc2_b70a4b4f8181ea98`
- Assertions: 1
- Phrases: renamed
- Suggested normal forms: renam
- Decision: accept (review_status: confirmed)

## report information

- Cluster ID: `rc2_fe64766ada7eb59d`
- Assertions: 1
- Phrases: report information
- Suggested normal forms: report information
- Decision: pending (review_status: pending)

## report information to

- Cluster ID: `rc2_9dfd17e25a352156`
- Assertions: 1
- Phrases: report information to
- Suggested normal forms: report information to
- Decision: pending (review_status: pending)

## report status on

- Cluster ID: `rc2_f19cbb420d62494d`
- Assertions: 1
- Phrases: report status on
- Suggested normal forms: report statu on
- Decision: pending (review_status: pending)

## reported on August 12

- Cluster ID: `rc2_03cee0bf3a591c63`
- Assertions: 1
- Phrases: reported on August 12
- Suggested normal forms: report on august 12
- Decision: pending (review_status: pending)

## repudiate

- Cluster ID: `rc2_fafc53924a741d47`
- Assertions: 1
- Phrases: repudiate
- Suggested normal forms: repudiate
- Decision: pending (review_status: pending)

## require attacker to For

- Cluster ID: `rc2_ea6b5acb77a757f4`
- Assertions: 1
- Phrases: require attacker to For
- Suggested normal forms: require attacker to for
- Decision: pending (review_status: pending)

## require closer monitoring for

- Cluster ID: `rc2_d97e477e66a17763`
- Assertions: 1
- Phrases: require closer monitoring for
- Suggested normal forms: require closer monitor for
- Decision: accept (review_status: confirmed)

## requires attacker capability

- Cluster ID: `rc2_15fc4ed7a6ab78d9`
- Assertions: 1
- Phrases: requires attacker capability
- Suggested normal forms: require attacker capability
- Decision: accept (review_status: confirmed)

## requires local low-privileged user in to

- Cluster ID: `rc2_0230a833b7fef90d`
- Assertions: 1
- Phrases: requires local low-privileged user in to
- Suggested normal forms: require local low-privileg user in to
- Decision: pending (review_status: pending)

## requires target-specific circumvention to exploit

- Cluster ID: `rc2_7663a58299e91380`
- Assertions: 1
- Phrases: requires target-specific circumvention to exploit
- Suggested normal forms: require target-specific circumvention to exploit
- Decision: pending (review_status: pending)

## resembles

- Cluster ID: `rc2_d5393b48316f7414`
- Assertions: 1
- Phrases: resembles
- Suggested normal forms: resemble
- Decision: pending (review_status: pending)

## resolves arbitrary assembly-qualified type names from

- Cluster ID: `rc2_09c739f174c2b0ac`
- Assertions: 1
- Phrases: resolves arbitrary assembly-qualified type names from
- Suggested normal forms: resolve arbitrary assembly-qualifi type name from
- Decision: accept (review_status: confirmed)

## resolves arbitrary assembly-qualified type names without

- Cluster ID: `rc2_8e2bdfab0c7a38ca`
- Assertions: 1
- Phrases: resolves arbitrary assembly-qualified type names without
- Suggested normal forms: resolve arbitrary assembly-qualifi type name without
- Decision: accept (review_status: confirmed)

## resolves key from

- Cluster ID: `rc2_8e5601c56e7de9c2`
- Assertions: 1
- Phrases: resolves key from
- Suggested normal forms: resolve key from
- Decision: pending (review_status: pending)

## retrieve x509 certificate of

- Cluster ID: `rc2_2613d3517327b6ff`
- Assertions: 1
- Phrases: retrieve x509 certificate of
- Suggested normal forms: retrieve x509 certificate of
- Decision: pending (review_status: pending)

## retrieve x509 certificate of STS signing certificate In to know

- Cluster ID: `rc2_411a8aae24b76dbb`
- Assertions: 1
- Phrases: retrieve x509 certificate of STS signing certificate In to know
- Suggested normal forms: retrieve x509 certificate of st sign certificate in to know
- Decision: pending (review_status: pending)

## retrieve x509 certificate of STS signing certificate from

- Cluster ID: `rc2_8dafe1cbcf3c3ab9`
- Assertions: 1
- Phrases: retrieve x509 certificate of STS signing certificate from
- Suggested normal forms: retrieve x509 certificate of st sign certificate from
- Decision: pending (review_status: pending)

## retrieved

- Cluster ID: `rc2_22d127eb0b9dc5e0`
- Assertions: 1
- Phrases: retrieved
- Suggested normal forms: retriev
- Decision: pending (review_status: pending)

## retrieved tooling during

- Cluster ID: `rc2_b74e3135458d812f`
- Assertions: 1
- Phrases: retrieved tooling during
- Suggested normal forms: retriev tool dur
- Decision: pending (review_status: pending)

## retrieved tooling via

- Cluster ID: `rc2_70852331183c4b8b`
- Assertions: 1
- Phrases: retrieved tooling via
- Suggested normal forms: retriev tool via
- Decision: pending (review_status: pending)

## returned with

- Cluster ID: `rc2_126ab1202ff3d0b5`
- Assertions: 1
- Phrases: returned with
- Suggested normal forms: return with
- Decision: pending (review_status: pending)

## returned with proxy anonymization on

- Cluster ID: `rc2_5103726ff6410293`
- Assertions: 1
- Phrases: returned with proxy anonymization on
- Suggested normal forms: return with proxy anonymization on
- Decision: pending (review_status: pending)

## returns STS signing certificate as part of

- Cluster ID: `rc2_5492bb16e1595fa5`
- Assertions: 1
- Phrases: returns STS signing certificate as part of
- Suggested normal forms: return st sign certificate a part of
- Decision: pending (review_status: pending)

## returns X509SecurityToken wrapping that

- Cluster ID: `rc2_31f40941cd1b42c6`
- Assertions: 1
- Phrases: returns X509SecurityToken wrapping that
- Suggested normal forms: return x509securitytoken wrapp that
- Decision: pending (review_status: pending)

## revealed

- Cluster ID: `rc2_419a636ccc2aa55c`
- Assertions: 1
- Phrases: revealed
- Suggested normal forms: reveal
- Decision: pending (review_status: pending)

## revealed full operational environment to

- Cluster ID: `rc2_16db70d7f20e41f8`
- Assertions: 1
- Phrases: revealed full operational environment to
- Suggested normal forms: reveal full operational environment to
- Decision: pending (review_status: pending)

## reverse

- Cluster ID: `rc2_b2d7f24e833051d5`
- Assertions: 1
- Phrases: reverse
- Suggested normal forms: reverse
- Decision: accept (review_status: confirmed)

## reverse engineering

- Cluster ID: `rc2_11108fa8a883da89`
- Assertions: 1
- Phrases: reverse engineering
- Suggested normal forms: reverse engineer
- Decision: pending (review_status: pending)

## reverse engineering to provide

- Cluster ID: `rc2_5a2c56b268b29422`
- Assertions: 1
- Phrases: reverse engineering to provide
- Suggested normal forms: reverse engineer to provide
- Decision: accept (review_status: confirmed)

## review Directive following issuance of

- Cluster ID: `rc2_f6ccd047b6c28c5c`
- Assertions: 1
- Phrases: review Directive following issuance of
- Suggested normal forms: review directive follow issuance of
- Decision: pending (review_status: pending)

## review Directive to account for changes in

- Cluster ID: `rc2_349b82ecdda11326`
- Assertions: 1
- Phrases: review Directive to account for changes in
- Suggested normal forms: review directive to account for change in
- Decision: pending (review_status: pending)

## root

- Cluster ID: `rc2_4813494d137e1631`
- Assertions: 1
- Phrases: root
- Suggested normal forms: root
- Decision: pending (review_status: pending)

## run with

- Cluster ID: `rc2_de67a1d043f6c558`
- Assertions: 1
- Phrases: run with
- Suggested normal forms: run with
- Decision: accept (review_status: confirmed)

## runs macOS Screen

- Cluster ID: `rc2_220772357155a3c5`
- Assertions: 1
- Phrases: runs macOS Screen
- Suggested normal forms: run maco screen
- Decision: accept (review_status: confirmed)

## s introduire sur ce réseau

- Cluster ID: `rc2_5d2b9b54798070db`
- Assertions: 1
- Phrases: s introduire sur ce réseau
- Suggested normal forms: s introduire sur ce réseau
- Decision: pending (review_status: pending)

## satisfy

- Cluster ID: `rc2_7688bd7c427206cb`
- Assertions: 1
- Phrases: satisfy
- Suggested normal forms: satisfy
- Decision: accept (review_status: confirmed)

## scan

- Cluster ID: `rc2_59ad1b2fc74287de`
- Assertions: 1
- Phrases: scan
- Suggested normal forms: scan
- Decision: pending (review_status: pending)

## scan Conduct including development environments outside

- Cluster ID: `rc2_695799cad2fff777`
- Assertions: 1
- Phrases: scan Conduct including development environments outside
- Suggested normal forms: scan conduct includ development environment outside
- Decision: pending (review_status: pending)

## scan Conduct including experimentation environments outside

- Cluster ID: `rc2_4fb200258899215d`
- Assertions: 1
- Phrases: scan Conduct including experimentation environments outside
- Suggested normal forms: scan conduct includ experimentation environment outside
- Decision: pending (review_status: pending)

## searched

- Cluster ID: `rc2_2419329067823cab`
- Assertions: 1
- Phrases: searched
- Suggested normal forms: search
- Decision: pending (review_status: pending)

## searched GitHub for trending 2026 CVE PoC repositories sorted by

- Cluster ID: `rc2_1fea7405407a0c2f`
- Assertions: 1
- Phrases: searched GitHub for trending 2026 CVE PoC repositories sorted by
- Suggested normal forms: search github for trend 2026 cve poc repository sort by
- Decision: pending (review_status: pending)

## searched exfiltrated data for

- Cluster ID: `rc2_a182cf6dd85ed802`
- Assertions: 1
- Phrases: searched exfiltrated data for
- Suggested normal forms: search exfiltrat data for
- Decision: pending (review_status: pending)

## searches

- Cluster ID: `rc2_2decc9ec9a691815`
- Assertions: 1
- Phrases: searches
- Suggested normal forms: searche
- Decision: pending (review_status: pending)

## searches TrustedSecurityTokenServices collection for

- Cluster ID: `rc2_cc4c11ef0e22c7a9`
- Assertions: 1
- Phrases: searches TrustedSecurityTokenServices collection for
- Suggested normal forms: searche trustedsecuritytokenservice collection for
- Decision: pending (review_status: pending)

## see Sorting algorithm in

- Cluster ID: `rc2_c15dc6c83a627cff`
- Assertions: 1
- Phrases: see Sorting algorithm in
- Suggested normal forms: see sort algorithm in
- Decision: pending (review_status: pending)

## see concrete example of RCE in action by

- Cluster ID: `rc2_f8d61e4febfbf92e`
- Assertions: 1
- Phrases: see concrete example of RCE in action by
- Suggested normal forms: see concrete example of rce in action by
- Decision: pending (review_status: pending)

## see concrete example of bypass in action by

- Cluster ID: `rc2_20c819f30ce0debc`
- Assertions: 1
- Phrases: see concrete example of bypass in action by
- Suggested normal forms: see concrete example of bypas in action by
- Decision: pending (review_status: pending)

## see in Mittelstand environments

- Cluster ID: `rc2_af80fd3c9dca24ca`
- Assertions: 1
- Phrases: see in Mittelstand environments
- Suggested normal forms: see in mittelstand environment
- Decision: accept (review_status: confirmed)

## sends JWT with

- Cluster ID: `rc2_a162fd7bcc9ea268`
- Assertions: 1
- Phrases: sends JWT with
- Suggested normal forms: send jwt with
- Decision: accept (review_status: confirmed)

## sends crafted HTTP/S input to

- Cluster ID: `rc2_61464cdb419d3c63`
- Assertions: 1
- Phrases: sends crafted HTTP/S input to
- Suggested normal forms: send craft http/s input to
- Decision: accept (review_status: confirmed)

## served as

- Cluster ID: `rc2_2213b551d4785318`
- Assertions: 1
- Phrases: served as
- Suggested normal forms: serv a
- Decision: pending (review_status: pending)

## served as reasoning engine for

- Cluster ID: `rc2_f72b82adf13259d9`
- Assertions: 1
- Phrases: served as reasoning engine for
- Suggested normal forms: serv a reason engine for
- Decision: accept (review_status: confirmed)

## serves as guide for

- Cluster ID: `rc2_3992352c911131cc`
- Assertions: 1
- Phrases: serves as guide for
- Suggested normal forms: serve a guide for
- Decision: pending (review_status: pending)

## serves as identity hub

- Cluster ID: `rc2_cc0b5998576971a1`
- Assertions: 1
- Phrases: serves as identity hub
- Suggested normal forms: serve a identity hub
- Decision: accept (review_status: confirmed)

## serves purpose from

- Cluster ID: `rc2_86e97aef799d0115`
- Assertions: 1
- Phrases: serves purpose from
- Suggested normal forms: serve purpose from
- Decision: accept (review_status: confirmed)

## set CreateNoWindow to

- Cluster ID: `rc2_d6e216cf9f7b0f7b`
- Assertions: 1
- Phrases: set CreateNoWindow to
- Suggested normal forms: set createnowindow to
- Decision: accept (review_status: confirmed)

## set in

- Cluster ID: `rc2_8a3408554120ca37`
- Assertions: 1
- Phrases: set in
- Suggested normal forms: set in
- Decision: accept (review_status: confirmed)

## sets actor token 's x5t header to thumbprint of

- Cluster ID: `rc2_c75a3226d46325ca`
- Assertions: 1
- Phrases: sets actor token 's x5t header to thumbprint of
- Suggested normal forms: set actor token 's x5t header to thumbprint of
- Decision: accept (review_status: confirmed)

## sets from

- Cluster ID: `rc2_88c3f4239c0b997f`
- Assertions: 1
- Phrases: sets from
- Suggested normal forms: set from
- Decision: pending (review_status: pending)

## share

- Cluster ID: `rc2_c3bc45ac352fe43f`
- Assertions: 1
- Phrases: share
- Suggested normal forms: share
- Decision: accept (review_status: confirmed)

## shift

- Cluster ID: `rc2_ecd3fad7a4d35d71`
- Assertions: 1
- Phrases: shift
- Suggested normal forms: shift
- Decision: accept (review_status: confirmed)

## shift required timeline for

- Cluster ID: `rc2_6ca45a760cc98a70`
- Assertions: 1
- Phrases: shift required timeline for
- Suggested normal forms: shift requir timeline for
- Decision: accept (review_status: confirmed)

## shift required timeline such as

- Cluster ID: `rc2_78b6c2dba645e99b`
- Assertions: 1
- Phrases: shift required timeline such as
- Suggested normal forms: shift requir timeline such a
- Decision: accept (review_status: confirmed)

## show differing counts of SharePoint servers on

- Cluster ID: `rc2_9e621d880e7e6dcb`
- Assertions: 1
- Phrases: show differing counts of SharePoint servers on
- Suggested normal forms: show differ count of sharepoint server on
- Decision: pending (review_status: pending)

## stack

- Cluster ID: `rc2_6ee08e6eb3bc6f45`
- Assertions: 1
- Phrases: stack
- Suggested normal forms: stack
- Decision: accept (review_status: confirmed)

## stack at

- Cluster ID: `rc2_41c4f8a14d38f4b8`
- Assertions: 1
- Phrases: stack at
- Suggested normal forms: stack at
- Decision: pending (review_status: pending)

## stack at time of calling ValidateToken

- Cluster ID: `rc2_6a4d52596a8d49f8`
- Assertions: 1
- Phrases: stack at time of calling ValidateToken
- Suggested normal forms: stack at time of call validatetoken
- Decision: pending (review_status: pending)

## stack below

- Cluster ID: `rc2_53fed8556532b6d9`
- Assertions: 1
- Phrases: stack below
- Suggested normal forms: stack below
- Decision: pending (review_status: pending)

## stack have been treated as outside

- Cluster ID: `rc2_7f1b4b54df143114`
- Assertions: 1
- Phrases: stack have been treated as outside
- Suggested normal forms: stack been treat a outside
- Decision: pending (review_status: pending)

## started to connect to

- Cluster ID: `rc2_5ab00ec13a3d9c71`
- Assertions: 1
- Phrases: started to connect to
- Suggested normal forms: start to connect to
- Decision: pending (review_status: pending)

## started to connect to attacker-controlled infrastructure on August 3

- Cluster ID: `rc2_e081a29e727fcdfb`
- Assertions: 1
- Phrases: started to connect to attacker-controlled infrastructure on August 3
- Suggested normal forms: start to connect to attacker-controll infrastructure on august 3
- Decision: pending (review_status: pending)

## starts vulnerable system in

- Cluster ID: `rc2_0563703b4204296b`
- Assertions: 1
- Phrases: starts vulnerable system in
- Suggested normal forms: start vulnerable system in
- Decision: pending (review_status: pending)

## starts with partial access to restricted information For

- Cluster ID: `rc2_f2079c34d047524c`
- Assertions: 1
- Phrases: starts with partial access to restricted information For
- Suggested normal forms: start with partial acces to restrict information for
- Decision: pending (review_status: pending)

## starts with partial access to successful exploitation of vulnerability For

- Cluster ID: `rc2_62f9e3016d1a4820`
- Assertions: 1
- Phrases: starts with partial access to successful exploitation of vulnerability For
- Suggested normal forms: start with partial acces to successful exploitation of vulnerability for
- Decision: pending (review_status: pending)

## stop

- Cluster ID: `rc2_6c45cb72a36e63d5`
- Assertions: 1
- Phrases: stop
- Suggested normal forms: stop
- Decision: pending (review_status: pending)

## succeed

- Cluster ID: `rc2_9076524bf5f0c804`
- Assertions: 1
- Phrases: succeed
- Suggested normal forms: succe
- Decision: pending (review_status: pending)

## suffers

- Cluster ID: `rc2_4cf14180a81b04a1`
- Assertions: 1
- Phrases: suffers
- Suggested normal forms: suffer
- Decision: pending (review_status: pending)

## supplement

- Cluster ID: `rc2_03dd65bf2241cb43`
- Assertions: 1
- Phrases: supplement
- Suggested normal forms: supplement
- Decision: accept (review_status: confirmed)

## supply machine-level asset tagging information

- Cluster ID: `rc2_4532f34314bd3118`
- Assertions: 1
- Phrases: supply machine-level asset tagging information
- Suggested normal forms: supply machine-level asset tagg information
- Decision: pending (review_status: pending)

## support success of

- Cluster ID: `rc2_1304960fc3b33fa5`
- Assertions: 1
- Phrases: support success of
- Suggested normal forms: support succes of
- Decision: pending (review_status: pending)

## supported Windows Server releases Tracked as

- Cluster ID: `rc2_40f19a53996b432f`
- Assertions: 1
- Phrases: supported Windows Server releases Tracked as
- Suggested normal forms: support window server release track a
- Decision: pending (review_status: pending)

## supports MEFs for

- Cluster ID: `rc2_5a94754c1d6f485c`
- Assertions: 1
- Phrases: supports MEFs for
- Suggested normal forms: support mef for
- Decision: accept (review_status: confirmed)

## surveyed

- Cluster ID: `rc2_811f2a14b9850c9d`
- Assertions: 1
- Phrases: surveyed
- Suggested normal forms: survey
- Decision: pending (review_status: pending)

## surveyed deployment counts via

- Cluster ID: `rc2_e2f36fde3a1586bf`
- Assertions: 1
- Phrases: surveyed deployment counts via
- Suggested normal forms: survey deployment count via
- Decision: pending (review_status: pending)

## survives

- Cluster ID: `rc2_0fb542ca67334617`
- Assertions: 1
- Phrases: survives
- Suggested normal forms: survive
- Decision: pending (review_status: pending)

## systèmes

- Cluster ID: `rc2_26700a1f57a629b5`
- Assertions: 1
- Phrases: systèmes
- Suggested normal forms: systèmes
- Decision: accept (review_status: confirmed)

## take

- Cluster ID: `rc2_d1905cf90af29a5a`
- Assertions: 1
- Phrases: take
- Suggested normal forms: take
- Decision: pending (review_status: pending)

## take immediate action

- Cluster ID: `rc2_fc0b7bd9e85f770a`
- Assertions: 1
- Phrases: take immediate action
- Suggested normal forms: take immediate action
- Decision: pending (review_status: pending)

## take immediate action ensure cybersecurity practices including policies for

- Cluster ID: `rc2_2ee402b3fe8be10f`
- Assertions: 1
- Phrases: take immediate action ensure cybersecurity practices including policies for
- Suggested normal forms: take immediate action ensure cybersecurity practice includ policy for
- Decision: pending (review_status: pending)

## take immediate action to harden

- Cluster ID: `rc2_6d28ec3ce32e1b36`
- Assertions: 1
- Phrases: take immediate action to harden
- Suggested normal forms: take immediate action to harden
- Decision: pending (review_status: pending)

## take immediate action to harden American networks As

- Cluster ID: `rc2_19985b053ca97ebf`
- Assertions: 1
- Phrases: take immediate action to harden American networks As
- Suggested normal forms: take immediate action to harden american network a
- Decision: pending (review_status: pending)

## take steps to avoid types of

- Cluster ID: `rc2_aac26bfe21e35fd3`
- Assertions: 1
- Phrases: take steps to avoid types of
- Suggested normal forms: take step to avoid type of
- Decision: pending (review_status: pending)

## take values If

- Cluster ID: `rc2_5e55342044a363b6`
- Assertions: 1
- Phrases: take values If
- Suggested normal forms: take value if
- Decision: pending (review_status: pending)

## takes advantage of software exploits

- Cluster ID: `rc2_1cad87053bbdf630`
- Assertions: 1
- Phrases: takes advantage of software exploits
- Suggested normal forms: take advantage of software exploit
- Decision: pending (review_status: pending)

## takes advantage of vulnerabilities

- Cluster ID: `rc2_d66550a8d4b24359`
- Assertions: 1
- Phrases: takes advantage of vulnerabilities
- Suggested normal forms: take advantage of vulnerability
- Decision: pending (review_status: pending)

## takes environmental factors into

- Cluster ID: `rc2_f106b57cd1b441f9`
- Assertions: 1
- Phrases: takes environmental factors into
- Suggested normal forms: take environmental factor into
- Decision: accept (review_status: confirmed)

## targeted government entity in

- Cluster ID: `rc2_7f70e26f048fae7f`
- Assertions: 1
- Phrases: targeted government entity in
- Suggested normal forms: target government entity in
- Decision: accept (review_status: confirmed)

## tend to be

- Cluster ID: `rc2_8b3f277ef37bfc0d`
- Assertions: 1
- Phrases: tend to be
- Suggested normal forms: tend to be
- Decision: pending (review_status: pending)

## there have

- Cluster ID: `rc2_e244f187f696561d`
- Assertions: 1
- Phrases: there have
- Suggested normal forms: there
- Decision: pending (review_status: pending)

## think

- Cluster ID: `rc2_dc2fc19d8fce376c`
- Assertions: 1
- Phrases: think
- Suggested normal forms: think
- Decision: pending (review_status: pending)

## threat actor retrieved

- Cluster ID: `rc2_1c153281ff2120ba`
- Assertions: 1
- Phrases: threat actor retrieved
- Suggested normal forms: threat actor retriev
- Decision: pending (review_status: pending)

## threat actor retrieved manually

- Cluster ID: `rc2_3e3fdb162f34992e`
- Assertions: 1
- Phrases: threat actor retrieved manually
- Suggested normal forms: threat actor retriev manually
- Decision: pending (review_status: pending)

## threat actor retrieved tooling during

- Cluster ID: `rc2_026578a435b47769`
- Assertions: 1
- Phrases: threat actor retrieved tooling during
- Suggested normal forms: threat actor retriev tool dur
- Decision: pending (review_status: pending)

## threat actor retrieved tooling via

- Cluster ID: `rc2_be70c842d602c7eb`
- Assertions: 1
- Phrases: threat actor retrieved tooling via
- Suggested normal forms: threat actor retriev tool via
- Decision: pending (review_status: pending)

## to bind

- Cluster ID: `rc2_b39accc9bb67c680`
- Assertions: 1
- Phrases: to bind
- Suggested normal forms: to bind
- Decision: accept (review_status: confirmed)

## to bind together

- Cluster ID: `rc2_6a7172822f444970`
- Assertions: 1
- Phrases: to bind together
- Suggested normal forms: to bind together
- Decision: accept (review_status: confirmed)

## to compute

- Cluster ID: `rc2_b2305d5d10db3178`
- Assertions: 1
- Phrases: to compute
- Suggested normal forms: to compute
- Decision: accept (review_status: confirmed)

## to convey additional extrinsic attributes of

- Cluster ID: `rc2_8200e5f11334ae20`
- Assertions: 1
- Phrases: to convey additional extrinsic attributes of
- Suggested normal forms: to convey additional extrinsic attribute of
- Decision: pending (review_status: pending)

## to interact beyond

- Cluster ID: `rc2_fb454fce2e0f61f3`
- Assertions: 1
- Phrases: to interact beyond
- Suggested normal forms: to interact beyond
- Decision: pending (review_status: pending)

## told

- Cluster ID: `rc2_1fcc08c7733965bc`
- Assertions: 1
- Phrases: told
- Suggested normal forms: told
- Decision: accept (review_status: confirmed)

## trigger ObjectDataProvider chain in

- Cluster ID: `rc2_91f63f979864f8e1`
- Assertions: 1
- Phrases: trigger ObjectDataProvider chain in
- Suggested normal forms: trigger objectdataprovider chain in
- Decision: pending (review_status: pending)

## triggers gadget chain

- Cluster ID: `rc2_fbffdd9f9578cb6b`
- Assertions: 1
- Phrases: triggers gadget chain
- Suggested normal forms: trigger gadget chain
- Decision: pending (review_status: pending)

## trust

- Cluster ID: `rc2_f796e2f28ae58117`
- Assertions: 1
- Phrases: trust
- Suggested normal forms: trust
- Decision: pending (review_status: pending)

## understand

- Cluster ID: `rc2_f9dc689e6d50ad6f`
- Assertions: 1
- Phrases: understand
- Suggested normal forms: understand
- Decision: pending (review_status: pending)

## understand capabilities of

- Cluster ID: `rc2_144816b1a7ae501b`
- Assertions: 1
- Phrases: understand capabilities of
- Suggested normal forms: understand capability of
- Decision: pending (review_status: pending)

## understand capabilities of publicly available LLMs For

- Cluster ID: `rc2_1e57f226f55d9bfd`
- Assertions: 1
- Phrases: understand capabilities of publicly available LLMs For
- Suggested normal forms: understand capability of publicly available llm for
- Decision: pending (review_status: pending)

## understand limits For

- Cluster ID: `rc2_d934800a04bbedaa`
- Assertions: 1
- Phrases: understand limits For
- Suggested normal forms: understand limit for
- Decision: pending (review_status: pending)

## update without

- Cluster ID: `rc2_841b108abd3d48dd`
- Assertions: 1
- Phrases: update without
- Suggested normal forms: update without
- Decision: pending (review_status: pending)

## use KEV catalog as

- Cluster ID: `rc2_236f7ba2ae586d6c`
- Assertions: 1
- Phrases: use KEV catalog as
- Suggested normal forms: use kev catalog a
- Decision: pending (review_status: pending)

## use SMB NULL session to query learn

- Cluster ID: `rc2_268a7cb4fdb6031d`
- Assertions: 1
- Phrases: use SMB NULL session to query learn
- Suggested normal forms: use smb null session to query learn
- Decision: pending (review_status: pending)

## use conceptual model of system of interest When establishing boundaries for

- Cluster ID: `rc2_5d01ecf3b7c7d917`
- Assertions: 1
- Phrases: use conceptual model of system of interest When establishing boundaries for
- Suggested normal forms: use conceptual model of system of interest when establish boundary for
- Decision: accept (review_status: confirmed)

## use standard definitions for

- Cluster ID: `rc2_7238362e0d3edda3`
- Assertions: 1
- Phrases: use standard definitions for
- Suggested normal forms: use standard definition for
- Decision: pending (review_status: pending)

## use target realm in

- Cluster ID: `rc2_5a106619d58db5bf`
- Assertions: 1
- Phrases: use target realm in
- Suggested normal forms: use target realm in
- Decision: pending (review_status: pending)

## use vulnerability as

- Cluster ID: `rc2_252493d00f859c54`
- Assertions: 1
- Phrases: use vulnerability as
- Suggested normal forms: use vulnerability a
- Decision: pending (review_status: pending)

## used Hermes Agent with DeepSeek for attack phase of

- Cluster ID: `rc2_e9afa523050bf580`
- Assertions: 1
- Phrases: used Hermes Agent with DeepSeek for attack phase of
- Suggested normal forms: us herme agent with deepseek for attack phase of
- Decision: accept (review_status: confirmed)

## used sprint along with

- Cluster ID: `rc2_062e60171b2ab0ef`
- Assertions: 1
- Phrases: used sprint along with
- Suggested normal forms: us sprint along with
- Decision: pending (review_status: pending)

## uses ADP container to provide additional CVE information for

- Cluster ID: `rc2_d914c0078f213883`
- Assertions: 1
- Phrases: uses ADP container to provide additional CVE information for
- Suggested normal forms: use adp container to provide additional cve information for
- Decision: pending (review_status: pending)

## uses DbTypeReflector For

- Cluster ID: `rc2_3e1a7f96130496e0`
- Assertions: 1
- Phrases: uses DbTypeReflector For
- Suggested normal forms: use dbtypereflector for
- Decision: pending (review_status: pending)

## uses Exploitability to describe

- Cluster ID: `rc2_b4f0b55b20678611`
- Assertions: 1
- Phrases: uses Exploitability to describe
- Suggested normal forms: use exploitability to describe
- Decision: accept (review_status: confirmed)

## uses Impact assessment to describe

- Cluster ID: `rc2_68ed402e56166505`
- Assertions: 1
- Phrases: uses Impact assessment to describe
- Suggested normal forms: use impact assessment to describe
- Decision: accept (review_status: confirmed)

## uses following decision points for

- Cluster ID: `rc2_12a378ae667bf581`
- Assertions: 1
- Phrases: uses following decision points for
- Suggested normal forms: use follow decision point for
- Decision: accept (review_status: confirmed)

## uses type reflectors to

- Cluster ID: `rc2_e65a2cf5beb838ca`
- Assertions: 1
- Phrases: uses type reflectors to
- Suggested normal forms: use type reflector to
- Decision: accept (review_status: confirmed)

## validates emerging threat posed by

- Cluster ID: `rc2_26f3516e36931c13`
- Assertions: 1
- Phrases: validates emerging threat posed by
- Suggested normal forms: validate emerg threat pos by
- Decision: pending (review_status: pending)

## venture

- Cluster ID: `rc2_352c00e4c6860a34`
- Assertions: 1
- Phrases: venture
- Suggested normal forms: venture
- Decision: pending (review_status: pending)

## venture such guess In

- Cluster ID: `rc2_d7d8846fa755aa4d`
- Assertions: 1
- Phrases: venture such guess In
- Suggested normal forms: venture such gues in
- Decision: pending (review_status: pending)

## verify

- Cluster ID: `rc2_a12dd3a7fd3203a4`
- Assertions: 1
- Phrases: verify
- Suggested normal forms: verify
- Decision: accept (review_status: confirmed)

## view

- Cluster ID: `rc2_2bcb43cbc8f6b7ef`
- Assertions: 1
- Phrases: view
- Suggested normal forms: view
- Decision: pending (review_status: pending)

## view gadget chain as

- Cluster ID: `rc2_96e88a1672ea207e`
- Assertions: 1
- Phrases: view gadget chain as
- Suggested normal forms: view gadget chain a
- Decision: pending (review_status: pending)

## views associated External List

- Cluster ID: `rc2_bf640f7154e7f8b9`
- Assertions: 1
- Phrases: views associated External List
- Suggested normal forms: view associat external list
- Decision: accept (review_status: confirmed)

## violated

- Cluster ID: `rc2_f47dedb977ea4264`
- Assertions: 1
- Phrases: violated
- Suggested normal forms: violat
- Decision: pending (review_status: pending)

## violates security policy of information system

- Cluster ID: `rc2_254b63061b861a02`
- Assertions: 1
- Phrases: violates security policy of information system
- Suggested normal forms: violate security policy of information system
- Decision: pending (review_status: pending)

## voor

- Cluster ID: `rc2_a6f105e2b9902600`
- Assertions: 1
- Phrases: voor
- Suggested normal forms: voor
- Decision: accept (review_status: confirmed)

## was added to

- Cluster ID: `rc2_f0b513d80e4caecc`
- Assertions: 1
- Phrases: was added to
- Suggested normal forms: add to
- Decision: accept (review_status: confirmed)

## was added to VulnCheck KEV before

- Cluster ID: `rc2_4bf3e1b1da1f2e79`
- Assertions: 1
- Phrases: was added to VulnCheck KEV before
- Suggested normal forms: add to vulncheck kev before
- Decision: accept (review_status: confirmed)

## was added to VulnCheck KEV on

- Cluster ID: `rc2_415dbfa3b931aa60`
- Assertions: 1
- Phrases: was added to VulnCheck KEV on
- Suggested normal forms: add to vulncheck kev on
- Decision: accept (review_status: confirmed)

## was addressed Tuesday release Tracked as

- Cluster ID: `rc2_018781e49b91594d`
- Assertions: 1
- Phrases: was addressed Tuesday release Tracked as
- Suggested normal forms: address tuesday release track a
- Decision: pending (review_status: pending)

## was addressed as part of Microsoft 's April 2026 Patch

- Cluster ID: `rc2_677893c5dcf9d5af`
- Assertions: 1
- Phrases: was addressed as part of Microsoft 's April 2026 Patch
- Suggested normal forms: address a part of microsoft 's april 2026 patch
- Decision: pending (review_status: pending)

## was created for

- Cluster ID: `rc2_219b73351c3c338d`
- Assertions: 1
- Phrases: was created for
- Suggested normal forms: creat for
- Decision: accept (review_status: confirmed)

## was determined by soliciting input from

- Cluster ID: `rc2_8139f2e150d4a8ff`
- Assertions: 1
- Phrases: was determined by soliciting input from
- Suggested normal forms: determin by solicit input from
- Decision: pending (review_status: pending)

## was disclosed by Microsoft

- Cluster ID: `rc2_e9d58e60cd08991b`
- Assertions: 1
- Phrases: was disclosed by Microsoft
- Suggested normal forms: disclos by microsoft
- Decision: pending (review_status: pending)

## was disclosed by Rapid7

- Cluster ID: `rc2_af4e778e2a87a693`
- Assertions: 1
- Phrases: was disclosed by Rapid7
- Suggested normal forms: disclos by rapid7
- Decision: pending (review_status: pending)

## was helpful when

- Cluster ID: `rc2_737d76a1d08dcbea`
- Assertions: 1
- Phrases: was helpful when
- Suggested normal forms: helpful when
- Decision: accept (review_status: confirmed)

## was improved by

- Cluster ID: `rc2_e33ca972603a290b`
- Assertions: 1
- Phrases: was improved by
- Suggested normal forms: improv by
- Decision: pending (review_status: pending)

## was improved by clarifying definitions of

- Cluster ID: `rc2_27dfeca124e8c125`
- Assertions: 1
- Phrases: was improved by clarifying definitions of
- Suggested normal forms: improv by clarify definition of
- Decision: pending (review_status: pending)

## was new function found inside

- Cluster ID: `rc2_a4b1fffdf565985a`
- Assertions: 1
- Phrases: was new function found inside
- Suggested normal forms: new function found inside
- Decision: pending (review_status: pending)

## was passed to

- Cluster ID: `rc2_503da479595e93ef`
- Assertions: 1
- Phrases: was passed to
- Suggested normal forms: pass to
- Decision: pending (review_status: pending)

## was patched by

- Cluster ID: `rc2_4be65cbfb68a1f04`
- Assertions: 1
- Phrases: was patched by
- Suggested normal forms: patch by
- Decision: pending (review_status: pending)

## was patched by Microsoft

- Cluster ID: `rc2_a50f41e909746c36`
- Assertions: 1
- Phrases: was patched by Microsoft
- Suggested normal forms: patch by microsoft
- Decision: pending (review_status: pending)

## was patched by Microsoft Tracked as

- Cluster ID: `rc2_1342f3a4e66dbf0f`
- Assertions: 1
- Phrases: was patched by Microsoft Tracked as
- Suggested normal forms: patch by microsoft track a
- Decision: pending (review_status: pending)

## was patched by Microsoft as part of

- Cluster ID: `rc2_17e7dcfeefe27e21`
- Assertions: 1
- Phrases: was patched by Microsoft as part of
- Suggested normal forms: patch by microsoft a part of
- Decision: pending (review_status: pending)

## was presented to CVSS Special Interest Group to incorporate privacy into

- Cluster ID: `rc2_ecdc6732f3e4fa52`
- Assertions: 1
- Phrases: was presented to CVSS Special Interest Group to incorporate privacy into
- Suggested normal forms: present to cvs special interest group to incorporate privacy into
- Decision: pending (review_status: pending)

## was presented to incorporate privacy For

- Cluster ID: `rc2_2f72bf3d17978d20`
- Assertions: 1
- Phrases: was presented to incorporate privacy For
- Suggested normal forms: present to incorporate privacy for
- Decision: pending (review_status: pending)

## was presented to incorporate privacy into

- Cluster ID: `rc2_ca61029cfc45b729`
- Assertions: 1
- Phrases: was presented to incorporate privacy into
- Suggested normal forms: present to incorporate privacy into
- Decision: pending (review_status: pending)

## was presented to incorporate privacy into CVSS For

- Cluster ID: `rc2_7df8aeb5396b15b5`
- Assertions: 1
- Phrases: was presented to incorporate privacy into CVSS For
- Suggested normal forms: present to incorporate privacy into cvs for
- Decision: pending (review_status: pending)

## was prevented by

- Cluster ID: `rc2_ad84b8bfcf1a1114`
- Assertions: 1
- Phrases: was prevented by
- Suggested normal forms: prevent by
- Decision: accept (review_status: confirmed)

## was promising

- Cluster ID: `rc2_154981fc05aa2ee3`
- Assertions: 1
- Phrases: was promising
- Suggested normal forms: promis
- Decision: pending (review_status: pending)

## was to hit

- Cluster ID: `rc2_53f03225ce09c219`
- Assertions: 1
- Phrases: was to hit
- Suggested normal forms: to hit
- Decision: pending (review_status: pending)

## was undertaken through

- Cluster ID: `rc2_82261aef4c30a9d3`
- Assertions: 1
- Phrases: was undertaken through
- Suggested normal forms: undertaken through
- Decision: accept (review_status: confirmed)

## was unsuccessful on the day of

- Cluster ID: `rc2_59993d36f8a9461a`
- Assertions: 1
- Phrases: was unsuccessful on the day of
- Suggested normal forms: unsuccessful on the day of
- Decision: pending (review_status: pending)

## was uploaded in

- Cluster ID: `rc2_4aa974904926b49b`
- Assertions: 1
- Phrases: was uploaded in
- Suggested normal forms: upload in
- Decision: accept (review_status: confirmed)

## was used to sort big-picture ordering of

- Cluster ID: `rc2_73a6d6f6d4f9d5ca`
- Assertions: 1
- Phrases: was used to sort big-picture ordering of
- Suggested normal forms: us to sort big-picture order of
- Decision: accept (review_status: confirmed)

## was value By

- Cluster ID: `rc2_4b84409751c1fc48`
- Assertions: 1
- Phrases: was value By
- Suggested normal forms: value by
- Decision: pending (review_status: pending)

## was what on

- Cluster ID: `rc2_3d01cab3be0987cc`
- Assertions: 1
- Phrases: was what on
- Suggested normal forms: what on
- Decision: pending (review_status: pending)

## were capable To

- Cluster ID: `rc2_d90dbe502f0891c9`
- Assertions: 1
- Phrases: were capable To
- Suggested normal forms: capable to
- Decision: pending (review_status: pending)

## were listed in file deleted by

- Cluster ID: `rc2_38f134b7548a2d44`
- Assertions: 1
- Phrases: were listed in file deleted by
- Suggested normal forms: list in file delet by
- Decision: accept (review_status: confirmed)

## were listed in file deleted by actor to

- Cluster ID: `rc2_7212e8a21c79786b`
- Assertions: 1
- Phrases: were listed in file deleted by actor to
- Suggested normal forms: list in file delet by actor to
- Decision: accept (review_status: confirmed)

## were urged to follow

- Cluster ID: `rc2_89a3e8c3f025354f`
- Assertions: 1
- Phrases: were urged to follow
- Suggested normal forms: urg to follow
- Decision: pending (review_status: pending)

## wish to identify

- Cluster ID: `rc2_73e0b3e89ec9d440`
- Assertions: 1
- Phrases: wish to identify
- Suggested normal forms: wish to identify
- Decision: pending (review_status: pending)

## write to even when running under

- Cluster ID: `rc2_b7a49dff0186f12e`
- Assertions: 1
- Phrases: write to even when running under
- Suggested normal forms: write to even when runn under
- Decision: accept (review_status: confirmed)

## wrote if necessary configure SharePoint Server behind

- Cluster ID: `rc2_83244ebe4503993e`
- Assertions: 1
- Phrases: wrote if necessary configure SharePoint Server behind
- Suggested normal forms: wrote if necessary configure sharepoint server behind
- Decision: pending (review_status: pending)

## à une application hautement spécialisés

- Cluster ID: `rc2_68f1ef7c920605e2`
- Assertions: 1
- Phrases: à une application hautement spécialisés
- Suggested normal forms: à une application hautement spécialisés
- Decision: accept (review_status: confirmed)
