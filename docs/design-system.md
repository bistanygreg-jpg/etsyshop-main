# Milestone & Meaning design system (apparel and print), v2, Nov 22, 2026

**Why this exists:** the owner judged our shirt designs amateur, saying they "do not convey thoughtful and experienced designs that align to our brand and our value proposition." This is the standard every design must meet before it goes on an HQ card. Bob owns it; Reach adds what competitors are doing; Penny makes sure the words match the listing.

## 1. Brand and value proposition

- **Who we are:** Milestone & Meaning makes keepsakes for family milestones: a new sibling, a first Christmas, a grandparent promotion, a cozy season.
- **The promise:** *mark the moment.* Every design should feel like something you'd keep after the moment has passed. It should be warm and witty, never generic.
- **Feel:** modern heirloom. Vintage emblem and badge structure, warm serif headlines, small honest details (a year, an "est.", a role). A thoughtful gift, not a meme tee.
- **We are not:** clip art, five fonts, rainbow colours, word-stacks with no idea, "live laugh love" quote tees.

## 2. Type system (Google Fonts, OFL, commercial use OK)

| Role | Font | Use |
|---|---|---|
| Headline | **Fraunces** 800–900, `SOFT 100, WONK 1` | The one word or phrase the shirt is about, in title case or caps |
| Labels and dates | **Barlow Condensed** 700, caps, tracking 0.12–0.22em | Arcs, "EST.", years, supporting lines |
| Accent script | **Yellowtail** | At most one short line per design (a wink: "and honestly, same") |

Rules:
- At most these 3 fonts, and usually only 2.
- **Three-level hierarchy:** one dominant headline (60–70% of the visual weight), one support line, one detail line.
- Never stretch or squash type. Never use faux bold. Watch the spacing between big letters in headlines.
- Retired: Poppins and Dancing Script as the main look (fine for printables' UI text, not apparel).

## 3. Colour

- Base palette: cranberry `#8D1B1B`, forest `#204D39`, antique gold `#B8862B`, cocoa `#5A3A26`, cream `#FBF6EC` (for knockouts and fills).
- **Two colours plus one accent, maximum**, per design. Gold is the accent: rules, stars, small details only.
- Seasonal and theme palettes are allowed (navy for soccer, terracotta for plants) but keep the 2+1 rule.
- Check contrast on every blank colour you enable (white, sport grey, natural). Never print cream or gold as the only colour on a light shirt.

## 4. Layout structures that work

Pick one per design:
1. **Seal:** a circular badge with arc text top and bottom, an icon, and the headline in the centre (Big Brother seal).
2. **Arc lockup:** arc label over an illustration, headline below, script and detail line (black lab).
3. **Club badge:** arc headline, a central icon with a knocked-out detail, a banner, then a detail line (Hibernation Club).
4. **Certificate:** box frame, small caps "OFFICIAL NOTICE", headline, script and detail (the back prints).

Spacing:
- Equal breathing room around groups.
- The artwork's proportion should be close to square (from 0.8:1 to 1.2:1), so it prints large on the chest. Long thin lockups print tiny.
- Back prints: the certificate structure, at most 0.95 of the width, y 0.24.

## 5. Illustration

- One illustration per design. It should be **flat or monoline, with a consistent stroke weight** (10–12 px at the 1000-unit artboard), rounded caps and joins.
- Build from deliberate shapes, not emoji or clip art. It must read at 300 px wide.
- **Every dog is a black lab** (owner rule): broad head, drop ears, amber eyes, black coat with dark-grey structure lines, and often a cranberry collar with a gold tag. The master is `#blackLab` in `design/apparel-kit/samples.html`; reuse it.
- Santa hat: cranberry curved cone, cream band, cream pompom, cranberry outline (master in the Big Brother seal).
- No characters, brands, team marks, logos, real places or famous quotes.

## 6. Words

- One clear idea, then one witty twist. Specific beats generic: "Officially promoted by Santa · Arriving 2027" beats "Big Brother".
- Add the meaning detail that makes it a keepsake: a year, a date, a role, "est.".
- Original wording only. If a phrase is everywhere on Etsy word for word, rewrite it.

## 7. Process: every design, every time

1. **Brief, in 2 lines:** who buys it, for what moment, and the one feeling.
2. **Concept:** pick a layout structure (§4) and write the words (§6).
3. **Build** in `design/apparel-kit/` (copy `samples.html` patterns; render with `render.js`).
4. **Self-critique.** Score it 1–5 on each line below. **Every line must score 4 or more**, or redo it:
   - Concept: one clear idea and a twist? Fits Milestone & Meaning?
   - Hierarchy: is it obvious what to read first, second and third?
   - Typography: only system fonts, good spacing, no awkward wraps or orphans?
   - Craft: aligned, balanced, consistent strokes, nothing cramped or touching?
   - Thumbnail test: legible and attractive at 300 px on the mockup?
   - Print-ready: tight crop, transparent, near-square, placed large (scale 0.85–1.0)?
5. **Mockup check** on the real Printify mockup (front and back views).
6. Only then put it on an HQ card, with the score line ("Rubric 5/5/4/5/4/5").

## 8. Files

- Kit: `design/apparel-kit/kit.css`, `samples.html` (the masters: seal, lab, club badge) and `render.js`.
- Commit HTML sources and small previews only. Full-size PNGs are print files: keep them in the scratchpad.
