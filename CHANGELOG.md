# Changelog

What has been released at [highexplosive.net](https://www.highexplosive.net),
newest first.

**Why this file exists.** Several releases were published by uploading the built
page through GitHub's web interface, from a phone, because the page is one
self-contained file and that route does not need a laptop. It works, but it
replaces the commit message with whatever the web form was given — so the repo
history reads `TacSim v1.2`, `TacSim 1.31`, and nothing else. This file is the
record those commits do not carry.

**Conventions.**

1. The second digit is functionality; the third digit is fixes.
2. Every simulator and comparator release is one self-contained HTML file copied
   verbatim to `static/tools/…/index.html`. Nothing is fetched at runtime.
3. `md5` is of that file as it sits in the repo and as it is served.
4. Sources are named where a claim was measured rather than asserted. **Verified
   live** means checked from a browser against the running site after the push;
   **measured** means checked against the byte-identical file before it.

---

## v1.31 — Tactical Scenario Simulator · 8 Sep 2026

`657b115` · 3,928,830 bytes · `bf383da46714ff81a90e3cc4250b2765`
Rollback: v1.3, `f3158b809095a23870e0409251e48669`

Three fixes, no features. All three came out of the first day of v1.3 being live.

1. **The arrangement chooser refused 50 legal board pairs.** A special connector
   stranded at a seam was always rejected; it may now be *out of play* at an
   outside edge instead. **50 unarrangeable pairs of 8,911 → 0.** HPG
   Engineering + Seaport now comes out right-to-right with the Seaport turned.
   All four genuine feature pairs still join on their feature.
2. **General Melee's deployment zones were a hex out and asymmetric** — rows 7-8
   against 11-12. Now 6-7 and 11-12. *Verified live:* v1.3 placed them 8.45 and
   14.15 from the board's centre; v1.31 places them 14.15 either side. The
   rulebook's own parenthetical (07-08) does not survive its own arithmetic.
3. **A three-piece field could be unarrangeable and fall back to every piece
   unturned** — a plate that looks settled and is not. `arrangeChain` now
   backtracks and `orderField` reorders only when the field cannot otherwise be
   laid. *Verified live* on seed `18660042`: v1.3 lays Large Lakes #2 / AeroBase
   #2 / Scattered Woods and cannot arrange it; v1.31 lays Large Lakes #2 /
   Scattered Woods / AeroBase #2 and does.

Unchanged: head strings, both social cards, the three external URLs, and the
draw engine — 299 of 300 seeds byte-identical, the one difference being fix 3
doing its job.

Published through the GitHub web route.

---

## v1.3 — Tactical Scenario Simulator · 7 Sep 2026

`42651c2` · 3,921,683 bytes · `f3158b809095a23870e0409251e48669`
Rollback: v1.22, `536942d33a223e2c8cb9b1179b0aa68c`

**The deployment plate** — the first functional addition since v1.2.

1. **A hex-accurate map of the drawn battlefield**, opened from an eye on the
   Battlefield row: which pieces, which way round, and where every zone of the
   mission falls. Drawn from real MegaMek board data, inlined, so the dialogue
   draws with no fetch. That is where most of the quarter-megabyte went.
2. **Deterministic from the exercise serial**, so a shared URL always shows the
   same plate. It chooses rotation only; the draw engine is untouched. *Verified
   live*: a cold reload of the same URL returns an identical plate.
3. **Two faults in the shipped plain diagram**, found only because the plate can
   be counted against hexes. A far-edge off-by-one in every mission zone; and
   **Control the Field drew no objective areas at all**, because `missions.json`
   had no entry for it. *Measured:* 0 of 10 Control the Field sheets drew
   objective zones on v1.22, 10 of 10 on v1.3.
4. **Ambush was drawing the wrong side's edges.** `roleInvert` swaps which slot
   holds the mission's first role, and both diagrams assumed the splitter is
   always side one. The paragraph and the Order of Battle were right; the
   pictures disagreed with them.
5. **The solo-board curation reaches the picker.** 29 boards curated as solo
   were being joined to mapsheets — 131 illegal fields in 6,000 exercises. Now
   zero.
6. **Colliding board names are gone.** No design name identifies two different
   pieces anywhere on the shelf, same-artwork reprints discounted.
7. **The exercise names are refilled** to a floor of 20 modifiers and 40 nouns
   per bucket. *The name a given serial produces has changed:* an old shared link
   still resolves, but its exercise carries a different name.
8. Smaller: a lone 'Mech is no longer split in half on Ambush, Extraction or
   under Waves; the Order of Battle tints each belligerent in its side's colour;
   two notes that reported a success as a shortfall are gone.

Also in this commit's parent, `6b7177b`: **the transfer bundle is renamed** from
`hx-racing.bundle` to `site-update.bundle`. The old name came from the first
thing it ever carried and made every later push look like it was touching the
racing page.

---

## v1.22 — Tactical Scenario Simulator · 6 Sep 2026

`c540fb4` · 3,675,359 bytes · `536942d33a223e2c8cb9b1179b0aa68c`
Rollback: v1.21, `be2b87d4c25747f07d43b9301e3fbe8e`

Two prose corrections and the masthead. **No code changed** — verified by diff:
12,898 lines in both builds, exactly two differ, and inside the 2.9 MB data blob
exactly two changed regions in 268,840 tokens.

1. The `edge_commanders + forced_withdrawal` pair rewritten. The old wording read
   as an objective raid but fired on eleven of the twelve missions.
2. "Rain coming sideways" cut from the `rain + wind` pair — all nineteen sheets
   that fired it also carried "in driving rain", so the sentence duplicated the
   weather clause. The effects sentence is kept.

Second release of the day.

---

## v1.21 — Tactical Scenario Simulator · 6 Sep 2026

`efd1443` · 3,675,386 bytes · `be2b87d4c25747f07d43b9301e3fbe8e`
Rollback: v1.2, `de24f5104b09481d59975806f2571dbc`

Third digit, with one recorded caveat: it carries two things that are not fixes —
the Discord control and the codenames — by explicit decision when the release was
scoped.

1. **The briefing paragraph re-ordered.** 52 phrases rewritten, 38 overrides
   re-slotted, one turn pair killed, and a structural bug fixed: Steel Rain was
   dragging its mission-line phrases up the paragraph.
2. **Exercise codenames.** Every sheet is now `EXERCISE BOMBER SPEAR` — two words
   harvested from around 820 real operation names, letter-bound so the first
   encodes the mission and the second the era group. Drawn off the serial, so a
   serial always carries the same name.
3. **The sheet head rebuilt** around the codename, with `FWCX-<serial>` as an
   anchor to its own exercise and a copy control.
4. **Share to Discord** — codename, subtitle, whole briefing and a link that
   suppresses the preview card. Longest of 1,500 measured: 892 characters against
   Discord's 2,000.
5. **Share links now carry the pins.** A bare `?seed=` reproduced a pinned sheet
   in only 7 of 399 cases — both the head link and the Discord card pointed at a
   different exercise. The most important fix in the release.
6. **The "cannot set this exercise" message** now gives exact spans, the last
   loss and to whom, the rename, and who holds the ground in the year asked.
7. **Nothing from our century on paper** — the print date is gone and the build
   number is hidden in print.
8. **A pinned era can no longer be dropped in silence.** It was consulted in four
   places in the solver and not in the branch that wins when a world is pinned.
   The sheet still generates; the era row is marked adjusted, with a note saying
   which year the pins do meet in.
9. Four wording fixes, including a data note that had been wrong since round 43S.

Two release candidates exist in the archive under this number and were never
live.

---

## v1.2 — Tactical Scenario Simulator · 4 Sep 2026

`8357776` · 3,640,716 bytes · `de24f5104b09481d59975806f2571dbc`
Rollback: v1.11, `4645af00700f20da7c0786288e7f20f7`

The climate model, the tag grammar, the ground clause and the weather clause —
functionality, hence the second digit.

1. **One temperature.** The picker and the ground clause read the same figure.
2. **Graded climate and hydrography gates.** `woods`, `water` and `river` step
   down by the world's water; `woods` also needs breathable air.
3. **The hydrography rule is on the draw too.** Dry-world sheets carrying a
   `woods:3`/`water:3`/`river:3` board fell from 12.8% to 0%.
4. **The ground clause is a tag pair** out of 91 phrases, with a separate variant
   set for airless ground.
5. **The weather clause fires on every sheet.** All eight battlefield conditions
   are spoken 100% of the time they are rolled.
6. **Fourteen hour bands**, four sub-bands per twilight, three temperature
   registers carried by the quality of the light.
7. **Night only where it is dark.** A world with a named moon can be fought on at
   night with no Night condition, and the card says *Moonlight*.
8. **No twilight without air.**
9. **Gravity is a battlefield condition**, reaching 100% of the sheets that roll
   it, up from 43%.
10. **Continentality**, calibrated on Terra, driving both the temperature swing
    and the map draw.
11. **A strategic clause** — where this ground sits between the two sides — on
    about half of all sheets.
12. **Bloodnames are earned**: the chance is the formation's quality, not a flat
    22% for everybody.

Measured: 2,600 of 2,600 exercises solved, zero page errors, zero silent ground
or weather clauses, 133 distinct weather clauses.

First release published through the GitHub web route.

---

## v1.11 — Tactical Scenario Simulator · 1 Sep 2026

`4a569d9` · 3,514,903 bytes · `4645af00700f20da7c0786288e7f20f7`
Rollback: v1.1, `7aab378d2595157dc121d5bcfcaa786a`

Eight things raised after v1.1 went live.

1. **One map had the wrong size.** `Trenches` was recorded as 16×17 and is a
   32×17 double sheet — on a piece whose other face was already 32×17, which is
   impossible and is now checked for.
2. **Map sets became Maps**, the dialog became Map Library, and the count became
   designs rather than products: *"172 of 237 maps enabled, across 56 published
   map products"*.
3. **The shelf survives a version change.** A shelf saved under one release is
   read correctly by the next, through an ordinal table rather than positions.
4. **The `sets=` parameter is a bitmask** — a three-product delta is four
   characters, and a whole share URL 71.

*Known and left:* the empty-shelf failure note still names the old button.

---

## v1.1 — Tactical Scenario Simulator · 1 Sep 2026

`1b2bcec` · 3,498,216 bytes · `7aab378d2595157dc121d5bcfcaa786a`
Rollback: v1.02, `15d79e6534d972b352c15e3e809a21b8`

**The map shelf is rebuilt on real purchasable products** rather than MegaMek
folders. The picker is now products and the pieces inside them, and the solver
draws from **237 designs across 34 products** rather than 199 MegaMek board rows.
A two-sided piece yields one face per game, which is the physical rule a player
already plays by.

Measured against v1.02 over 2,600 seeds: same world 100% of the time, same ground
area, **zero** cases of two faces of one piece in a field. 198 exercises pinned to
airless worlds laid zero pieces without an `airless` tag. 150 seeds with a
mercenary and a faction pinned together: v1.02 lost the pin on 67, this build
loses none.

Published through the GitHub web route — the first time, and the reason that
route exists.

---

## v1.02 — Tactical Scenario Simulator · 31 Aug 2026

`ed50450` · 3,383,420 bytes · `15d79e6534d972b352c15e3e809a21b8`

Five bugs reported by readers of the live v1.01, one found on the way, and four
corrections made reading the printed sheet. Among them: the standing sentence
dated a holding to the wrong year on 355 of 1,810 clause-bearing sheets, and
named the previous holder at that wrong year.

**`bodies.json` fires for the first time in this build** — the moon and
uninhabited-body feature was written, complete, and loaded by no released build
through v1.00 and v1.01.

---

## v1.01 — Tactical Scenario Simulator · 30 Aug 2026

`147948c` · 3,226,790 bytes · `a2f1f6f736e61ec0a75cd25e330d6c2b`

Mario's own social card and meta text, the ComStar mark in the masthead, a
favicon, map-set bulk controls, and a mercenary-declaration fix.

**The social card changed name**, from `social-card-simulator-3025.png` to
`social-card-simulator-3052.png`, because scrapers cache `og:image` by URL and
refetch lazily or never. **The 3025 card stays in the repo, unreferenced and
deliberately**, so previews scraped while v1.00 was live still resolve. The 3052
card has not changed since and must not be re-copied.

---

## v1.00 — Tactical Scenario Simulator · 30 Aug 2026

`c45d09d` · 3,204,740 bytes · `4fe12b4360b947246a1cf387504128a8`

**First release of the simulator**, at `/tools/simulator/`. One self-contained
HTML file; the display face is inlined as base64 and nothing is fetched at
runtime.

The same commit takes **the Weapon Package Comparator to v1.07**, whose only
change is the display-face alias: both tools declared `BTDisplay` and now declare
`HXDisplay`, which is what `/racing/` had used since August. The typeface is
unchanged — Anta by Sergej Lebedev under the SIL OFL, byte-identical everywhere.
`BTDisplay` is retired site-wide.

---

## The splash regrouping · 28 Aug 2026

`9fc81f8` — the homepage stops being a flat list of links and becomes two groups
under in-universe headings: **Focht War College** over the two tools, **ComStar
Entertainment Ltd** over the MechSports Division.

The rule behind the headings: a heading may only be the name of a body that could
plausibly have letterhead. Never a category, never a descriptor.

---

## The MechSports Division page · 20–22 Aug 2026

`81f53f2` through `0330fec` — `/racing/`, the BattleTech 'Mech racing rules,
issued in the voice of ComStar Entertainment Ltd.

Built over several passes: the display face and social card; the Crossfire and
Division cards with the navy palette and the masthead seal; division metadata and
the card lockup; a hanging indent on the memo; **straight quotes throughout**,
which is the house style and is why the Markdown build has smart quotes disabled
while keeping dashes and ellipses; and the back link in the display face, in
caps.

`e5833c1` and `de434e4` in the same window make `push.sh` read **one exact
bundle path** rather than the newest `.bundle` in a directory — so a second
bundle left nearby, the full-history backup say, can no longer quietly become the
thing that gets pushed.

---

## The comparator, and the site itself · 14 Aug 2026

`da80b6c` the initial site. `599c11c` the Weapon Package Comparator at v1.03,
`cc4b54a` alignment and default-movement fixes, `2daa7d0` v1.06 and the favicons.

The site is built by `scripts/build.py`, a hand-written static generator with two
dependencies, and deployed to GitHub Pages by a push to `main`.
