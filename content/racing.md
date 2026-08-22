---
# ---------------------------------------------------------------------------
# ADDING A DOWNLOAD IS A CHANGE TO `releases:` BELOW AND NOTHING ELSE.
# No markup, no prose. Chen's memo deliberately never names a file, which is
# what keeps it that way — if the memo is ever edited, don't let it start
# listing things.
# ---------------------------------------------------------------------------
template: racing.html
title: MechSports Division
back_label: HighExplosive.net

# The browser/search title and the social card. Kept apart from `title:`, which
# is the h1 — people search for "BattleTech mech racing rules", not for the
# name of a fictional division.
page_title: BattleMech Racing — Formula Thunder rules and record sheets | HighExplosive.net
summary: >
  Free BattleTech 'Mech racing rules. The Formula Thunder competitor pack: full
  regulations, ten record sheets and a printable circuit map, for use with the
  BattleTech Core Rulebook. Unofficial fan-made material, no charge.
og_title: BattleMech Racing — Formula Thunder
og_description: >
  Free BattleTech 'Mech racing rules: regulations, record sheets and a printable
  circuit map. Two laps, ten machines, and a racing line seeded with mines.
og_image: /racing/img/og-racing.jpg
og_image_width: 1200
og_image_height: 630
og_image_alt: The five Formula Thunder racing BattleMechs in team livery
standfirst: Competitor materials issued by ComStar Entertainment Ltd.

# The Division's seal, in the masthead's left gutter. SVG for the masthead;
# the card instance uses the raster.
seal: /racing/img/msd-logo.svg
seal_alt: MechSports Division

hero: /racing/img/ft-grid-hero.webp
hero2x: /racing/img/ft-grid-hero@2x.webp
hero_fallback: /racing/img/ft-grid-hero.png
hero_alt: The five Formula Thunder Type R racing BattleMechs in team livery.

memo_head:
  - To: Adept Ilse Voss, MechSports Division
  - From: Precentor Ansel Chen
  - Re: "Handover: competitor materials, and what to do with them"

signoff:
  name: — A. Chen, Precentor
  lines:
    - MechSports Division, ComStar Entertainment Ltd
    - Galatea, 3054

schedule_heading: Schedule of issued material
preamble: >
  Issued without charge to any party intending to run a sanctioned event.
  Materials include racing regulations, technical specifications and record
  sheets. Circuit surveys are issued separately, at full survey scale. Nothing
  here restates general 'Mech operating doctrine; organisers and competitors
  are assumed to hold a current copy.


# One entry per series. A second series brings its own mark, blurb and files,
# and nothing about the page changes.
series:
  Formula Thunder:
    mark: /racing/img/ft-logo.webp
    mark_fallback: /racing/img/ft-logo.png
    blurb: |
      Two laps. Ten machines. You win by crossing the line, not by winning a fight.

      Every team fields two 'Mechs: a runner, and a Locust whose only job is to
      put mines on the racing line and survive long enough to do it again. Race
      Control is a 90-ton Highlander that sets the pace, and three turrets that
      shoot rule-breakers.

  Formula Crossfire:
    mark: /racing/img/fc-logo.webp
    mark_fallback: /racing/img/fc-logo.png
    blurb: |
      Two laps of a figure-eight. Ten machines, all of them hostile. Twice a lap
      the crossover brings the whole field back together nose to nose, where
      being quick stops being an answer and the other nine are the hazard.

  MechSports Division:
    mark: /racing/img/msd-logo.webp
    mark_fallback: /racing/img/msd-logo.png
    # Lower than the shared 140px cap. The seal is authority, not merchandise,
    # and should not outweigh the two series marks beside it.
    mark_max_height: 83
    blurb: |
      This section contains technical specification forms for sanctioned
      MechSports events, and other administrative materials.

# `href` publishes a link. `status` instead of `href` renders it italic and
# unlinked — the "in preparation" state. `href` may be a path on this site or a
# full URL somewhere else.
releases:
  - series: Formula Thunder
    label: Competitor Pack — Series 1, 3054 season
    meta: PDF · regulations and record sheets
    href: https://archive.highexplosive.net/Formula-Thunder-Competitor-Pack-3054-Series-1.pdf

  - series: Formula Thunder
    label: Circuit Survey — Kinnekulle Speedway
    meta: JPG · prints at 44 × 25 in
    href: https://archive.highexplosive.net/Kinnekulle-Speedway-Oval-300dpi.jpg
    thumb: /racing/img/ft-kinnekulle-thumb.webp
    thumb_fallback: /racing/img/ft-kinnekulle-thumb.png

  - series: Formula Thunder
    label: Form TS-1 — Series 1, 3054 season
    meta: PDF · technical specification
    href: https://archive.highexplosive.net/Formula-Thunder-Form-TS-1-3054-Series-1.pdf

  - series: Formula Crossfire
    label: General Regulations
    meta: PDF · sporting regulations and race formats
    href: https://archive.highexplosive.net/Formula-Crossfire-General-Regulations.pdf

  - series: Formula Crossfire
    label: Form TS-1 — Crossfire Trophy, 3131 season
    meta: PDF · technical specification
    href: https://archive.highexplosive.net/Formula-Crossfire-Form-TS-1-3131-Trophy.pdf

  - series: Formula Crossfire
    label: Circuit Survey — Magna Speedrome
    meta: JPG · prints at 44 × 25 in
    href: https://archive.highexplosive.net/Magna-Speedrome-Figure-eight-300dpi.jpg
    thumb: /racing/img/fc-magna-thumb.webp
    thumb_fallback: /racing/img/fc-magna-thumb.png

  - series: MechSports Division
    label: Form TS-1 — blank
    meta: PDF · blank form, fillable
    href: https://archive.highexplosive.net/MechSports-Division-Form-TS-1-Blank.pdf
---

You have the Division from the first of next month, so this is the last of these I write.

The official history says Series 1 began with a wager between two men. There was no wager. I know, because I filed the paperwork afterwards, and had there been a wager I would have had to find a category for it.

In my youth I worked for the Mercenary Review Board on Rasalhague. I was the clerk who received the applications when the hall opened, and I was still receiving them a decade later, which will tell you as much about my early career as you need to know. The Board itself no longer exists. It was wound up the year before last and nobody thought to write and tell me.

Part of that desk was contract outcomes. Who came back, who did not, and how much of the machine came back with them. After four years of it I could tell you which scout pilots were going to lose their 'Mech before they signed. It was not skill; the good ones and the dead ones scored the same on skill. It was something else, and there was no box on the form for it.

So I proposed a screening ground. Surplus land, some borrowed light machines, and a set of exercises to sort the ones who could judge a risk from the ones who simply enjoyed taking one. It was approved because it was cheap. I will be honest with you: it did not work. It never told me anything the contract outcomes had not already told me.

What it did do was this. I went out there one afternoon in the fourth month and found six of them racing. Not exercising — racing, on a course they had marked out themselves, watched by about forty people who had walked out from the hall, with a book being run on the outcome by a man from the commissary.

I want something on the record, because I have heard it said and I have not always corrected it. I did not invent 'Mech racing. People have raced these machines for as long as there have been machines to race, locally and amateurishly, on stock chassis, in front of whoever could be bothered to turn up. What I saw at that fence was not new. It was only the first time I had seen it and understood that somebody could sell tickets.

The mines were not mine either. The screening ground had live charges scattered across it, a legacy of an earlier exercise and a filing failure I was too junior to be blamed for, and the men out there worked out inside a fortnight that this made the course more interesting. All I did was write it down as a regulation instead of as an incident. Getting it up off the ground and into a launcher took rather longer, and took an Adept-Zeta in Science and Research who agreed to build me a few prototype warheads as an after-hours matter. I never asked what she booked them as. She never asked what I wanted them for.

What I added was the rest. Two machines to a team, so a constructor could be persuaded to pay for it. A technical specification, so the paying constructors had something to argue about. And a set of regulations that treated the whole business as a sport rather than as an unusually elaborate accident.

It took sixteen years to get that proposal read by anyone who mattered. I spent a good part of that time in the Marian Hegemony, which nobody at the time could have found on a map and which we could, watching people run ovals better than anyone in the Inner Sphere and considerably less honestly. It was then a bandit kingdom with delusions and it is now a bandit kingdom with a tourist board. I came back with a second draft. I am not going to pretend my motives across that period were pure. I wanted the promotion. I had been passed over four times, and I was aware that my file read *administratively sound, limited initiative*.

There were races before there was a series. Loose things, five or six machines, rules that changed between heats because somebody complained. The first Series 1 race proper was run in 3039. I was a Precentor within the year, which tells you what this Order values, and it is not initiative.

Now. The materials.

Everything the Division holds is below, and my instruction to you is the one I have followed from the beginning: issue it to anyone who asks, at no charge, without conditions. I am aware of Licensing's position. I have been aware of Licensing's position since our second season. I am told we are a different organisation now. I will believe it when Licensing writes back.

The sport does not grow because we protect it. It grows because somebody in a garrison town two jumps from anywhere reads the regulations, decides they could run something better, and does.

You will be asked to approve new material. An amended technical specification, a new circuit, another class entirely. Approve it. Add it to the schedule below and leave everything above it exactly as it stands. The list grows; the text does not need to.

One last thing, and it is not administrative.

The screening ground never told me which pilots would come home. It was a bad instrument and I have said so in writing. But I have now watched fifteen seasons of people who volunteer to drive twenty tons of unarmoured scout 'Mech into a minefield they laid themselves, and I have formed a view about the type, and it is not the view I held at that desk, on a world that still had a queue outside it.

They are the best of them. Write that down somewhere the Order will not find it.
