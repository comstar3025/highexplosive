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
2. Every simulator and comparator release is one HTML file copied verbatim to
   `static/tools/…/index.html`. It was fully self-contained through v1.44;
   **from v1.5 the simulator fetches one sidecar at runtime**, the order-of-battle
   database on `archive.highexplosive.net`, and degrades to its former order of
   battle when that is unreachable.
3. `md5` is of that file as it sits in the repo and as it is served.
4. Sources are named where a claim was measured rather than asserted. **Verified
   live** means checked from a browser against the running site after the push;
   **measured** means checked against the byte-identical file before it.

---

## v1.63 — Tactical Scenario Simulator · 23 Sep 2026

4,936,146 bytes · `057887bb46770d9968a30e7154c4b917`
Rollback: v1.62, `633e1b9e2547677b6697db5350dec95d`

**Two prose rounds and one renderer fix.**

1. **The world card says whose flag it is.** A new token resolves to the holder's
   adjective where the naming system has one — *"It has flown the Kuritan flag"* —
   and falls back to *"their"* where it does not. Two qualifiers now follow the
   objective they qualify instead of preceding it, the Objective Raid night
   override is cut to one sentence, and *"No other flag has ever flown over it"*
   no longer repeats the line above it. The holding clause is rewritten to *"Since
   it was settled, it has been held by …"*.
2. **The seam half-hex takes the right ink.** Where two mapsheets meet, the shared
   north half-hex was drawn as **one unclipped hex in the left sheet's colour**
   whenever both halves carried the same ground — so a grassland sheet's green ran
   across the seam onto a desert one. The gate now tests the ink as well as the
   data. A road-exit inference at the same half-hex could also point into the
   neighbouring sheet.

*Measured on the byte-identical file, against v1.62 on the same seeds:* the world
card moves on **30 of 40** sheets, *"their flag"* goes **3 to 0** and *"has flown
the <adjective> flag"* **0 to 3**, *"No other flag has ever flown over it"* **6 to
0**, and the new holding clause appears on 4. The exercise paragraph is untouched
on all 40.

**The seam fix, isolated:** the Annex B deployment plate changes on **4 of 22**
sheets, and on each the node count rises by exactly one or two — one seam half-hex
that had been a single unclipped hex is now the two clipped halves it should
always have been. The battlefield-layout diagram is untouched on **34 of 34**,
single-sheet and multi-sheet alike.

Entry-edge agreement 0 of 10. Sticky row 67px resting and held at 1180, 768 and
390px, no horizontal scroll, no page errors. Same seed twice from cold:
identical. The sidecar is unchanged — one request on a cold load, still one after
five sheets; no fallback note; both annexes drawing. The export files are
byte-identical to v1.62.

---

## v1.62 — Tactical Scenario Simulator · 22 Sep 2026

4,930,306 bytes · `633e1b9e2547677b6697db5350dec95d`
Rollback: v1.61, `ee7e77db881949d940c5fdab74cb02ec`

**One change: how a force is divided into formations.** Twelve Kurita machines
were coming out as two reinforced lances where they should have been three full
ones.

One rule generates every row and there are no exceptions: of the ways a total can
be split, take the one whose groups sit closest to nominal strength in total,
breaking ties on the most full formations and then the fewest groups. Three
consequences worth naming:

1. **Twelve lance machines are 4+4+4**, and the reinforced size is reserved for a
   lone formation.
2. **The parity set carries the role** — Ambush the attacker, Extraction and Steel
   Rain the defender — which a mission-only list could not, and it reaches the
   Waves complication, which it could not at all.
3. **Waves deploys half the formations, rounding down.** It had been deploying the
   first group and withholding every other, which was right at two and three and
   wrong from four up.

The table is data, in `data/oob/shape.json`, every row generated and none typed.

**What this does to old links: a v1.61 link keeps its world, its year, its
mission and its ground, and its forces change.** Measured on 39 sheets carried
across, the ground sentence is **identical on 39 of 39** and the world card on
**39 of 39** — the board draw sits earlier in the random stream than the force
draw — while the crews differ on almost all of them. Twelve-machine lance forces
came out **4+4+4** on every instance in the sample.

**The diagram is not touched:** 20 battlefield plates compared with generated ids
normalised — **0 differ**, which is the same fact their battery measures as an
unchanged plate hash.

**One known residual, theirs and documented rather than found:** seed `1266222`
builds a lance force of ten that reads 6+4, which the table forbids. The table
governs the plan; that sheet planned a larger force, the budget bought ten, and
the first group arrived at its planned six. It reproduces exactly as described.
Re-slicing once the delivered count is known is a round of its own.

Entry-edge agreement 0 of 10. Sticky row 67px resting and held at 1180, 768 and
390px, no horizontal scroll, no page errors. Same seed twice from cold:
identical. The sidecar is unchanged — one request on a cold load, still one after
five sheets; no fallback note; both annexes drawing.

---

## v1.61 — Tactical Scenario Simulator · 21 Sep 2026

4,919,078 bytes · `ee7e77db881949d940c5fdab74cb02ec`
Rollback: v1.6, `fd59eb6b13281af90e455caed0915a63`

**Two prose fixes. Nothing about the page, the exports, the plates or the draw
changes.**

1. **The Clan size word reaches the prose.** A sheet could print **Bid-down** in
   the order of battle three inches under *"an understrength assault Star"* — the
   label was corrected in the band on 16 September and the paragraph takes its
   size words from a different string. One string now feeds the fielding
   sentence, the meeting sentence, the pay clause and the deployment line alike.
   Inner Sphere and ComStar forces keep *understrength*: neither bids.
2. **The tail ladder had a second caller it never knew about.** Where exactly one
   side is a hired command the sentence a reader sees is the pay clause, not the
   meeting sentence — the same shape, the same claim, and no slot for the tail, so
   the tail never printed there at all. The ladder is one function with two
   callers now, and the pay clause gains the whole ladder rather than one rung: a
   hired sheet can say a side has older machines or came off a garrison posting,
   which was always true of it and never said.

*Measured on the byte-identical file, against v1.6 on the same seeds:* of 46
sheets, **8 paragraphs differ and every one is classified** — 4 are the size-word
substitution and 4 are a tail insertion, with nothing unexplained. The
substitution is exact: *understrength* before a Clan formation goes **4 to 0**,
*bid-down* **0 to 4**, and 11 occurrences of *understrength* before a Lance or
Level II are untouched. The tail changes are **pure insertion on 4 of 4** — no
word of the v1.6 paragraph removed.

**Nothing outside the paragraph moved, checked rather than taken:** across 34
sheets the order of battle, the formation lines and the world card are identical
on **34 of 34**, and 20 battlefield plates compared with generated ids normalised
**0 differ**. The export chain still produces the same three files with the same
names.

Entry-edge agreement 0 of 10. Sticky row 67px resting and held at 1180, 768 and
390px, no horizontal scroll, no page errors. Same seed twice from cold:
identical. The sidecar is unchanged — one request on a cold load, still one after
five sheets; no fallback note; both annexes drawing.

---

## v1.6 — Tactical Scenario Simulator · 21 Sep 2026

4,917,213 bytes · `fd59eb6b13281af90e455caed0915a63`
Rollback: v1.55, `bbd62061c0593029354a6339fe70691e`

**The second digit. An exercise can now leave the page, and the prose has learned
what to call people.**

1. **Import and export.** An exercise leaves as a MegaMek V2 scenario and either
   force leaves as a unit list. A force can be imported from a `.mul` and is then
   locked, with a padlock on its own heading. The download control on the
   designator row does one thing — it downloads the scenario — and each force
   carries its own control on its heading, offering export, import and release.
   The files name themselves after what they hold:
   `FWCX-929114142 COMMANDO GREY.mms`, and
   `FWCX-929114142 - Clan Jade Falcon (Recon Star).mul`.
2. **A faction naming system.** A faction carries an ordered list of short forms
   per printed name and a resolver answers each slot's ask, so a paragraph that
   has already said *Clan Wolf* can later say *the Wolves*. First naming is
   measured rather than assumed: a faction whose full name is not yet in the
   paragraph gets the full name.
3. **A notable line per era**, the narrowest window winning, and a **two-formation
   plan tail** — where a side fields two formations the sentence says what the two
   are for together.
4. **Five smaller rulings**, including the Volcanic and Glacier map packs and the
   Fire and Ice battlemats now off by default, being the only default-on products
   with no board file behind any design.

*Measured on the byte-identical file:* the export binding holds end to end — the
Blue heading's control yields a `.mul` whose commander is the Blue force's own
lead machine and crew, the Red heading's the Red force's, and the scenario file
carries the serial and the exercise name. No new external dependency: one
`fetch` (the sidecar), five external URLs, none added; export and import are
`Blob` and `FileReader`, entirely local.

**Two things about this release are worth knowing before you share a link.**
The terrain clause moved: on 18 sheets carried over from v1.55, the world and the
opening sentence are identical on **18**, and the ground sentence differs on
**17**. On free draws the order of battle follows it on 5 of those 18. On a fully
pinned sheet — same faction, era, scale and map library — the forces are
**identical** and only the ground differs. So a v1.55 exercise link reproduces its
forces under v1.6 but not always its ground.

The `NAMING` switch restores **full names**, which is what its own code comment
says; it does not restore v1.55 prose, because the forces clause was rewritten
alongside it.

Sticky row 67px resting and held at 1180, 768 and 390px, no horizontal scroll, no
page errors. Entry-edge agreement 0 of 10. Same seed twice from cold: identical.
The sidecar is unchanged — one request on a cold load, still one after five
sheets; no fallback note; both annexes drawing.

---

## v1.55 — Tactical Scenario Simulator · 18 Sep 2026

4,766,346 bytes · `bbd62061c0593029354a6339fe70691e`
Rollback: v1.54, `706c889e8c475acbf9134f32c3976878`

**Three changes, all in the order of battle: how a force is sliced into
formations, what order those formations print in, and the Clans.**

1. **The split is drawn from the count actually delivered.** The shape was chosen
   before the machines were, and then overwritten twice — by the scorer and by
   delivery, where only 42.3% of forces arrived as the shape had planned. The
   slice is now re-cut once the real count is known, and each changed group draws
   its type from the machines actually in it. **Six machines splitting into two
   threes: 24% before, 71% after**, on identical seeds.
2. **A Command formation prints first and a Support formation last.** Display
   only — the builder is not told, and nothing about the force changes. Matching
   is on the exact formation name, because a substring test demoted every *Fire
   Support* lance, which is a combat role.
3. **The Keshik, and the availability rung becomes a per-formation fact.** A
   front-line Clan force's Command Formation is appointed Keshik on a 1-in-6; the
   appointment forces that formation to elite and draws its machines from the
   Keshik table, which is now reached only by appointment rather than by 8.2% of
   Clan forces. Four tags print on the formation line after the quality — KESHIK,
   SOLAHMA and PROVISIONAL GARRISON per formation, GARRISON per force:
   `Command Star · ELITE · KESHIK`.

*Measured on the byte-identical file, against v1.54 on identical seeds:* the
six-machine split goes **2 of 8 to 5 of 7**; **49 of 49** multi-formation bands
print in the specified order.

**The Clan change is contained, and this was checked against the cut it was made
on rather than taken:** of 38 non-Clan forces on sheets with no Clan force,
**0 differ**. The only non-Clan forces that move are on sheets that have a Clan
force, which share one random stream with it. 5 of 11 Clan forces differ.

**The builder ran on every force, checked directly.** The order-of-battle builder
falls back to a legacy roster that carries no designation and no skill pair, and
that fallback is caught, so a zero page-error count does not prove the builder
ran. Across 52 forces and 230 crews: **0 crews with an empty designation or skill
pair, 0 forces on the legacy roster**, Clan forces included.

**The diagram is not touched:** 20 battlefield plates compared between the builds
with generated ids normalised — **0 differ**. Entry-edge agreement holds at 0 of
10. The button row is 67px resting and held at 1280, 768 and 390px with no
horizontal scroll and no page errors. Same seed twice from cold: identical.

The sidecar is unchanged — same URL, same expected length and hash. One request
on a cold load, still one after five sheets; no fallback note; both annexes
drawing; no JavaScript errors.

---

## v1.54 — Tactical Scenario Simulator · 18 Sep 2026

4,737,978 bytes · `706c889e8c475acbf9134f32c3976878`
Rollback: v1.53, `dedd739537ab71a63809c974dcd4fbf9`

**The quality label was being read off the wrong table, and the order of battle
now looks like two forces rather than four lances.**

1. **The formation rating is derived correctly.** Lances of 4/4s and 4/5s were
   reading VETERAN and lances of 3/3s and 3/4s were reading ELITE: the formation's
   average was compared against the round-110 *aiming* medians, which sit between
   the rungs by construction, rather than against the four bands' own BV
   multipliers. The rule is now thresholds rather than nearest rung — worse than a
   4/5 average reads green, better than a 3/4 average reads elite, the middle
   splits at the midpoint, and the average is the mean. **The employer's liaison
   officer is out of that average**: he carries no gunnery and no piloting, so he
   was contributing a fallback of 1 and dragging every hired command down.
2. **Every exception note speaks in the College's voice.** Twenty-three strings.
   His own example, *"complication pin kept, condition pin dropped"*, now reads
   *"the exercise keeps the complication and drops the condition"*. Two notes lost
   a second line that only echoed the first.
3. **The button row holds at the top of the window.** A sentinel and an
   IntersectionObserver give it a rule and a soft shadow when it holds; both are
   paint-only, because changing a sticky element's height would reflow the page
   under a reader mid-scroll.
4. **The order of battle reads as two forces.** Force-to-force was no further
   apart than formation-to-formation, so the band read as a flat list. Each force
   name now carries a hairline rule, and the gap above it is wider than the gap
   between its own formations.
5. **The rating tag moved into the roster grid** and lost its box. Four badges
   used to sit at four different horizontal positions in three different widths;
   the tag now shares a column with the skill pairs, so it aligns to them by
   construction at every width and in print. All one grey.

*Measured on the byte-identical file, against v1.53 on 30 seeds including pinned
era, scale, mission and condition:* **the briefing paragraph differs on 0, and the
order of battle — every formation, every roster, every crew's gunnery and
piloting — differs on 0** once the rating word is set aside. The builder is
untouched; only the label and the layout moved. The rating changed on 20 of those
30 sheets.

**The new rating rule, checked against the page's own table rather than taken:**
the two cuts are read off `quality.levels` — regular 4/5 at 1.00, veteran 3/4 at
1.32, midpoint 1.16 — and across 36 formations the printed band matches the rule
on **36 of 36**. Both squeezed bands are back: green and elite both appear.

Measured layout: the button row is **67px resting and held** at 1280, 768 and
390px, holds at the top of the window, with no horizontal scroll and no page
errors at any width. Force-to-force spacing is **20px** against **9px** between
formations, with a 1px rule under each force name. The four rating tags' right
edges span **8px**, against **134px** on v1.53, in one grey with no border.

**The diagram is not touched:** 20 battlefield plates compared between the builds
with generated ids normalised — **0 differ**. Entry-edge agreement holds at 0 of
10. Same seed twice from cold: identical.

The sidecar is unchanged — same URL, same expected length and hash. One request
on a cold load, still one after five sheets; no fallback note; both annexes
drawing; no JavaScript errors.

---

## v1.53 — Tactical Scenario Simulator · 17 Sep 2026

4,716,548 bytes · `dedd739537ab71a63809c974dcd4fbf9`
Rollback: v1.52, `ad0c3bb44dee21fc7de288ba528b4094`

**Six of the day's rulings, and four of them are the order of battle learning to
speak per formation rather than per side.**

1. **The deployment line sits under its formation heading.** It used to be
   hoisted to the side and printed once wherever every formation entered the same
   way. Its position now carries meaning, and on a contracted side it no longer
   lands between the command's heading and the liaison's.
2. **Steel Rain splits by formation.** A side of two lances printed *"two on turn
   one and two on turn two"* twice, each lance halving itself. One lance now drops
   on turn one and the other on turn two. Ambush and Extraction have worked this
   way since rounds 41e and 48D.
3. **Waves splits between formations too** — one formation *"from the [edge],
   turn one"*, the other *"from the [edge], withheld"*. A lone formation is
   unchanged and still withholds half of itself, which is round 39b and stands.
4. **Focal Point's sentence pluralises where the diagram draws two objective
   markers**: *"Two positions in the centre decide it."*
5. **The liaison line breathes.** 9px under it, the sheet's own block-boundary
   gap, so the command's heading ends before its first formation begins.
6. **Both "no detailed records" notes move to the Instructor's notes**, numbered,
   with their tags on the things they are about — `[1]` on the Order of battle
   heading and `[2]` after the independent-command line. They were loose
   paragraphs inside the Order of Battle band.

*Measured on the byte-identical file, against v1.52 on the same seeds:* **12 of
14 sheets are identical**, and the two that differ do so only by the note
relocation and one hoisted deployment line. Before and after, same seed each
time: Steel Rain at scale 4 seed `1373210` goes from the halving line printed
twice to *"on turn one"* / *"on turn two"*; Waves at scale 4 seed `2369094` from
four *"two … on turn one, two to follow"* lines to *"turn one"* / *"withheld"*
per formation, while a lone formation at scale 1 is untouched; seed `14129077`
from *"One position in the centre decides it."* to *"Two positions…"*; the
liaison line's measured gap from 1px to 9px.

**The diagram is not touched, checked rather than taken:** 20 battlefield plates
compared between the two builds with generated ids normalised — **0 differ**.
Entry-edge agreement carried from v1.51 at 0 disagreements of 10. Same seed twice
from cold: identical.

The sidecar is unchanged — same URL, same expected length and hash. One request
on a cold load, still one after five sheets; no fallback note; both annexes
drawing; no JavaScript errors.

---

## v1.52 — Tactical Scenario Simulator · 17 Sep 2026

4,707,669 bytes · `ad0c3bb44dee21fc7de288ba528b4094`
Rollback: v1.51, `60490df28029747c887250c9082cfac2`

**Three rulings from 17 Sep, and one of them reverses an older one.**

1. **The Setup card prints the temperature the dice gave.** Where the roll asks
   for a level the ground cannot reach, the card used to print the local maximum;
   it now prints the rolled level, and the footnote carries the reconciliation.
   This reverses an earlier ruling, on the grounds that substituting the local
   maximum contradicted the *respect the rolled exercise* principle. The level
   the ground can actually show is still what every temperature claim downstream
   is built from — the tool still does not assert a reading it cannot produce.
2. **That footnote is one sentence.** It read *"No ground here reaches Extreme
   Heat 3. The exercise is played at Extreme Heat 2."* and now reads *"The
   exercise requires Extreme Heat 3; the most this ground can reach is Extreme
   Heat 2."*
3. **The employer's liaison officer is named on the sheet.** He has been attached
   to every contracted sheet since round 38, carrying the employer's rank and the
   employer's faction rather than the mercenary's, and round 40 took him off the
   roster. A diegetic line under the independent-command line now puts him where
   the roster is not: *Liaison officer recorded as [rank] [name]*.

*Measured on the byte-identical file, against v1.51 on the same seeds:* **19 of
20 sheets are identical**, and the twentieth differs by exactly the new liaison
line. On the two divergent-temperature sheets, v1.51 printed `Extreme Heat 1`
with a two-sentence footnote and v1.52 prints `Extreme Heat 3` with the single
sentence. The same seed generated twice from cold is identical.

v1.51's fix is carried: **0 disagreements of 10 sheets** between the plate's
home-edge strips and the order of battle's entry line, matching v1.51 exactly.

The sidecar is untouched — same URL, same expected length and hash. One request
on a cold load, still one after five sheets; no fallback note on any of them;
both annexes drawing; no JavaScript errors.

---

## v1.51 — Tactical Scenario Simulator · 17 Sep 2026

4,703,951 bytes · `60490df28029747c887250c9082cfac2`
Rollback: v1.5, `a3ec6de94259d2caeb81a05550beda71`

**One fault. The entry edge now follows the slot, not the tactical role.**

The rule has been settled since round 47Z — the role follows `roleInvert`, the
edge stays with the slot — and the battlefield plate always implemented it. The
order of battle's entry line and the briefing paragraph both derived the edge
from the role letter instead, so on every sheet where the attacker sat in the
second box, the picture and the prose disagreed: the diagram showed a force
entering from the south while the text sent it in from the north. One function
now, read by all three.

*Measured on both builds, reading the home-edge strip colours out of the diagram
and the entry line out of the order of battle:* **the live v1.5 disagrees with
its own plate on 5 of 10 sheets; v1.51 on 0 of 10.** The reported case, seed
`72756687`, is one of the five — the plate marks north for side one, and v1.5's
order of battle sends the Federated Suns in from the south.

The sidecar is unchanged and the page's expected length and hash still match the
file on R2. One request on a cold load, still one after five sheets; no fallback
note on any of them; both annexes drawing; no JavaScript errors.

---

## v1.5 — Tactical Scenario Simulator · 16 Sep 2026

4,702,523 bytes · `a3ec6de94259d2caeb81a05550beda71`
Rollback: v1.44, `85b7ae2532912285d65485b9a763eda0`

**The order of battle is drawn from real machines.** This is the first release
that fetches anything at runtime: `oob-db-v1.json.gz` on
`archive.highexplosive.net` — 4,187,958 bytes, sha256 `e4ba1b45…7fbd59`, 10,988
units and 145 availability slices. The page carries the expected length and hash
and treats a mismatch as unreachable.

1. **A full pre-release review** — 48 items answered, 21 built. Focus restored to
   the button, the failure card offering only pins actually set, the year capped
   at 3200, achieved BV beside each side, `aria-labelledby` on the form, a gold
   focus ring, West/Centre/East on the battlefield caption, the exercise title as
   an `h2`, and the order of battle reading blue then red on every sheet.
2. **Per-formation quality skew.** Each formation draws its own quality from the
   side's table, so a command lance leans veteran and a support lance the other
   way: a green command lance is 0.8% against 5.0% for an ordinary battle lance,
   over 2,600 front-line forces.
3. **The crew quality band is derived from the crews**, per formation, rather
   than from the draw — a lance of 3/4s and 4/3s no longer reads as Regular.
4. **The even split**, rank floors, a Level II being six machines and labelled
   Understrength when short, and R9's spend relief for a Clan force that cannot
   spend 90% of its ceiling.
5. **The LosTech era is fixed** — it dated every exercise 3014 and never came up
   on a free draw; it now spans 2904–3018.
6. **Printing from dark mode** no longer puts pale tints on white paper.

**The fallback is real, and measured rather than asserted.** Served from an
origin the archive's CORS policy does not allow, the sidecar fetch fails and the
page degrades exactly as designed: six sheets generated, the order of battle
present, both annexes drawing (Annex B 2,468 nodes, Annex C 1,964), and the
diegetic note — *"Detailed strength records could not be reconstructed for this
engagement"* — on the sheet. No JavaScript errors; the only console output is the
failed request itself.

---

## v1.44 — Tactical Scenario Simulator · 13 Sep 2026

4,224,211 bytes · `85b7ae2532912285d65485b9a763eda0`
Rollback: v1.43, `6160b472619c833aae8af728b3c64fd1`

**The Third Succession War is on the sheet, the sentence that hid it is fixed,
and Annex C gained a hover reach.**

1. **149 years with no war on the sheet.** Between the Second Succession War
   ending 2864 and the Fourth beginning 3028 the war table carried no
   House-vs-House entry at all, so every Succession-era exercise told a reader
   there was no war — while the tool's own planet record carried 936 changes of
   ownership across the same span.
2. **The missing rows were not a bug in the source.** The table is built from
   MekHQ's `factionhints.xml`, which exists to compute *probabilities of
   conflict*: `<war>` marks **limited periods of intense fighting**. It is a rate
   modifier for a contract generator, not a chronicle. The Third Succession War
   is 159 years of low-intensity border raiding — MekHQ's baseline — so marking
   it would double a rate already normal.
3. **So the sentence was fixed as well as the rows**, and that half matters more:
   *"No recorded war between them in 3059"* asserted something the source cannot
   support in any year. It now reads *"No war between them is named in the record
   for 3059."* *Verified on live sheets:* the retired wording renders on none of
   120 seeds.
4. **Ten data corrections, nine of them upstream faults in MekHQ's file** — the
   Fourth Succession War dated 3026 against canon's 3028, a Capellan war with no
   Capellan in it, and two `Combine-Ghost Bear War` rows that are really the
   Hell's Horses raids wearing a borrowed label.
5. **Annex C: hovering a system draws its one-jump reach** — a dashed 30 ly
   circle and faint lines to every system inside it — and a route stop's ring now
   always contains a dot in the colour that system would carry off the route, so
   the ring says whose journey it is and the dot says whose ground it stopped on.
6. **Nothing the plate draws leaves the plate.** A system whose coordinates fall
   on the window's own edge used to straddle the frame, and a 30 ly circle
   centred near an edge spilled much further. One clip rect per panel now wraps
   everything inside the frame and nothing outside it. *Verified by rendered
   pixels, not by inspection:* with a hover circle active on a star sitting
   **0 px** from the frame, the 12 px bands immediately outside all four edges
   contain **zero** non-background pixels.
7. **A pre-existing fault, older than the hover:** `<text>` labels are painted
   after the marks, so a label crossing a star took the pointer and the star
   answered nothing. Labels now give up the pointer — this affected Annex B too.

**The exercise moves on some seeds, and only where it was sitting on a wrong date
or a wrong belligerent.** *Measured over 120 free seeds against the live v1.43:*
world, year, mission and boards identical on **113 of 120 (94%)**, matching the
283 of 300 measured upstream. **Pinned** draws move further: narrowing the year
window to the intersection of both sides' lifespans reshuffles the pick even
where the old year was legal.

*Cut five times under this number.* The figures above are the round-94 cut, the
only one that shipped; four superseded cuts sit beside it in `Release/` and were
never live.

---

## v1.43 — Tactical Scenario Simulator · 12 Sep 2026

4,205,481 bytes · `6160b472619c833aae8af728b3c64fd1`
Rollback: v1.41, `bfbe7ff42675dc19f95f011abeaef3bc`

A **Print** button in the form's button row, and three fixes. **v1.42 carries the
same first two fixes and was withdrawn before it shipped** — its print built an
annex only if that annex's dialogue happened to be open, so printing a freshly
generated sheet produced no plates at all. Nothing carrying `v1.42` was ever
live.

1. **Both annexes now print, always.** They are built at print time from the
   exercise itself, through the same two builders the dialogues use, with no
   dialogue involved. *Verified through a real print rather than by calling the
   builder:* with **no dialogue ever opened**, `beforeprint` fires once and the
   `#printannex` container holds exactly two plates — Annex B at 1,198 SVG nodes
   and Annex C at 2,359 — and is removed afterwards. With a dialogue **open** at
   print time it still holds exactly two, and the document has **zero duplicate
   ids**, because each build stamps its patterns and clip paths with its own
   random suffix. Under print media `.actions` is `display:none`, so the button
   cannot print itself.
2. **The annex plates were destroyed below about 520px.** The 520px floor stays
   wherever it can be delivered; below that the centring box put the overflow
   where `scrollLeft` cannot reach. *Measured on both builds:* on the live v1.41
   the plate is 520px wide with its left edge at **−80px at 360, −65px at 390 and
   −20px at 480**, and the scroller reaches only 119, 105 and 61px — less than
   the overflow, so the cut part is genuinely unreachable. On v1.43 the plate
   fits: 282, 310 and 397px wide, left edge at 39–42px, nothing cut.
3. **Steel Rain was losing half the dropping side.** Identical arrival lines were
   collapsed by string identity, which is right for a direction and wrong for a
   count: two lances of four printed one line and four machines had no arrival
   turn. A line carrying a count is never collapsed now.

**The draw is untouched.** *Measured over 60 seeds against the live v1.41:*
battlefield row identical on **60 of 60**, world identical on **60 of 60**, and
exactly **one** Order of Battle changed — a Steel Rain sheet, which is fix 3
doing its work. The only other text that moves is the new Print button.

---

## v1.41 — Tactical Scenario Simulator · 12 Sep 2026

4,196,979 bytes · `bfbe7ff42675dc19f95f011abeaef3bc`
Rollback: v1.4, `3e80316c6d81daadbc6928d8ed7985bb`

Three fixes, no features.

1. **The battlefield caption was being cut off on phones.** The position word
   hangs out of the card on a negative left margin; the narrow-width query drops
   the gutter column that margin exists for, but the margin stayed — so the list
   sat 27px off the left edge of the page, where the document does not scroll and
   the overhang is destroyed rather than merely offscreen. `Map Pack: City`
   printed as `Pack: City`. *Measured on both builds, twelve sheets at each of
   320, 360, 390, 430 and 479px:* **v1.4 clipped 12 of 12 at every width, worst
   −27px; v1.41 clips 0 of 12 at every width.** The one item a reader would have
   noticed.
2. **One idiom per kind of absence in the World card.** HPG class printed `None`
   on some sheets and a bare em dash on others for what looked like the same
   absence. It now says **`None on record`** where there is no record and `None`
   where the fact is a known nil. No lone em-dash field values remain; every em
   dash still on a sheet is inside real prose.
3. **The third-party note named one holder where the record carries several.** On
   a jointly held world the note credited the first and dropped the rest, while
   the World card a hand's width below named them all. Both lines now come from
   the same two helpers.

**The draw is untouched** — a bookmark still resolves to the same exercise on the
same ground. *Measured over 60 seeds against the live v1.4:* battlefield row
identical on **60 of 60**, world identical on **60 of 60**. Twenty-two sheets
changed text, and every change is item 2 or item 3.

---

## v1.4 — Tactical Scenario Simulator · 11 Sep 2026

4,193,112 bytes · `3e80316c6d81daadbc6928d8ed7985bb`
Rollback: v1.33, `15b56986e019692a848b2ce9300184fc`

**Annex C, the jump plate** — the route a force flew to reach the exercise, on
every exercise, with its stops, its recharge days and its uncharted stretches, an
index of the Inner Sphere with the plate's own window marked, and a one-line
approach strip in the masthead that says the shape of the journey without being
opened. *Verified:* it draws on all twelve missions and on 30 of 30 free draws,
alongside Annex B.

Also in this release:

1. **The aimed board draw.** Boards are drawn toward the seam they will make and
   the whole field's order *and* rotation are solved together rather than greedily
   left to right. Two-board fields go from 7.2% poor seams to 0.6%, three-board
   from 15.6% to 4.8%, drawing the same 155 boards.
2. **The instructor's notes band**, with every note on the sheet rewritten into
   one sentence in the instructor's voice.
3. Sublevel contours on the deployment plate, and roads that infer their exits
   only inside their own mapsheet.
4. **A jump graph without 172 islands in it.** Components a hair over the 30-light-year
   jump are joined at the cost their own distance implies, which puts the Marian
   Hegemony, Nueva Castile, the Hanseatic League and the Fronc Reaches back on the
   map.

**Shared links.** The new draw changes which boards some exercises get, so a link
shared before this release can render a different battlefield. *Measured over 60
seeds against the live v1.33:* the battlefield row is identical on 44 and changed
on 16 — ten two-board fields, three three-board, one one-board, and two that were
two boards and are now one. **The world is identical on all 60**, so the exercise
itself does not move; only the ground does. Second release to do this, after
v1.32.

*Cut four times under this number.* The figures above are the round-81 cut, the
only one that shipped; three superseded cuts sit beside it in `Release/` and were
never live.

---

## v1.33 — Tactical Scenario Simulator · 9 Sep 2026

4,022,745 bytes · `15b56986e019692a848b2ce9300184fc`
Rollback: v1.32, `36f119ec71240681bc5cb2c94df31b34`

**The plate draws the printed sheet edge to edge.** Everything is in the drawing;
*measured against the live v1.32 over 70 seeds, the exercise text is identical on
all 70* — so unlike v1.32, this release moves no shared link.

1. **A mapsheet is seventeen hexes tall.** MegaMek stores a whole hex where the
   paper prints only the top half of one, so the south edge is trimmed: one clip
   rectangle, the printed sheet, cuts every hex, contour, road and overlay.
   *Measured:* the plate's height falls from 372 to 364 units.
2. **The north half row is drawn** — the half hexes above a pushed-down column,
   which two stacked sheets share and MegaMek stores in neither. Four rules
   supply them (road connector, river connector, both flankers paved or both
   water, then clear level 0) and 59 boards carry a row set by hand. Over the
   shelf, 1,686 north half hexes: the rules settle 13.5% and the floor takes the
   rest. *Measured:* hex count per plate rises from 1,107 to 1,140.
3. **A turned sheet uses its own real data at both edges.** A 180° turn maps
   printed column `c` to `16-c` and row `r` to `17-r`, and both preserve parity,
   so a cut column maps to a cut column: a turned sheet's north half row is its
   own stored row 17, and its trimmed south edge is the hand-set row 00 mirrored.
   Turned Archipelago 1's row 17 now reads identically to the same sheet upright.
4. **Roads join across the sheet's edge.** The no-exits inference stopped at the
   playable field, so column 01 could not see column 00. Six boards affected.
5. **A half-hex road with no exits recorded draws its road** — mask 0 means "work
   it out from the neighbours" everywhere else in the file and now means it here.
6. **The seam corner takes each half from its own sheet** whichever way either
   sheet is laid, including a middle piece with a seam on both sides.

*Known and accepted:* nine hand-set north rows carry a dash where a code belongs
and fall back to the rule; `16x17 Business District`'s terrain string is shifted
one place, so its north edge draws as pavement throughout. Two road stubs on
Corporate Campus reach a hexside and meet nothing, because that is what the data
says.

---

## v1.32 — Tactical Scenario Simulator · 9 Sep 2026

3,997,507 bytes · `36f119ec71240681bc5cb2c94df31b34`
Rollback: v1.31, `bf383da46714ff81a90e3cc4250b2765`

**Two different files carry the string `v1.32`.** The one above is what was
built, pushed and served. A later cut of the same number,
`e97b1a6d9848be25e183e905e1eb93c9` (3,999,814 bytes), was made after this one had
already shipped and **was never live**. If a rollback to v1.32 is ever needed it
is the md5 above, which is in this repo at the v1.32 commit.

**The deployment plate now draws the mapsheet as it is printed**, which is a
functional addition rather than a fix.

1. **The turned-sheet mirror.** A mapsheet laid 180° round was drawn as its
   *mirror*: a pushed-down column moves one row further under the turn,
   `r' = (h-1) - r - (c & 1)`, where a plain double reverse is a reflection.
   Every turned sheet on every plate was wrong before this.
2. **Column 00 exists again.** MegaMek keeps 16 columns per sheet — the 15
   playable ones and the east half column as its column 16 — and throws the west
   half column away. All 162 have been rebuilt: 41 lifted out of larger boards
   that embed the same sheet, 4 from a printed partner, 29 set by hand, the rest
   by rule. The rules agree with the 41 real ones on 97.4% of hexes.
3. **The seam is drawn as two halves.** Two sheets share their touching half
   hexes as one hex, now painted twice — once in each sheet's ink — with
   terrain, features, elevation and roads each following the half they belong
   to. A road runs across only when both sheets bring one to it.
4. **The two outer half columns are drawn**, so the plate is the whole printed
   sheet rather than the playable rectangle. *Measured* on seed `938109900`: the
   plate widens from 446 to 455 units and its hex count rises from 563 to 1,107.
5. **The knife-fight cut runs to the paper's edge**, because the cut takes paper
   out of play rather than hexes. Objective areas and deployment zones stop at
   the last playable hex, which is the opposite case.
6. **A road strip down column 00 or 16** is stored with no exits and was drawn as
   a comb of diagonal stubs. It now works its exits out from its neighbours.
7. Contours run against every half hex; Urban Sweep carries its footnote on every
   exercise; roads and pavement are told apart on the plate.
8. **The seam nudge — and this one is in the draw, not the plate.** Ignoring solo
   and no-info boards: on a 5+, force a perfect join; otherwise draw normally but
   redraw the first *poor* once. Over 1,721 scoreable two-sheet fields: perfect
   3.6% → 16.7%, good 59.8% → 72.1%, poor 36.6% → 11.2%. It takes its own RNG
   stream, and the board draw still takes exactly one number from the main stream
   in every branch.

Riding with this release, in `push.sh`: **the script now fetches `origin` and
fast-forwards to it before applying the bundle.** A release uploaded through
GitHub's web interface lands on `origin/main` and never reaches the Mac, so the
next bundle is built on a base that clone does not have and the push fails with
*"Repository lacks these prerequisite commits"*. That happened twice. It
fast-forwards only, so real divergence still stops rather than being papered over
with a merge.

**Shared links.** This release changes which boards some exercises draw, so a
link shared before it can render a different battlefield. *Measured over 150
seeds against v1.31, masthead excluded:* 111 identical, 39 changed — 34 of them
two-sheet fields, and five not. Of those five, all Urban Sweep, three changed the
boards drawn, including a **one-sheet** field. The exercise, world, year,
belligerents and mission are unaffected.

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
