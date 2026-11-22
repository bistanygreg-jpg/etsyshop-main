# Milestone & Meaning design system (apparel and print), v3, Nov 22, 2026

**Why this exists:** the owner judged our shirt designs amateur, saying they "do not convey thoughtful and experienced designs that align to our brand and our value proposition." This is the standard every design must meet before it goes on an HQ card. Bob owns it; Reach adds what competitors are doing; Penny makes sure the words match the listing.

## 0. Retail standard (v3, owner, Nov 22): what retail buyers pay for

The owner rated v2 a 4.5/10. These are the standards that top-selling Etsy and boutique shirts meet. **They override anything below.**

1. **The garment is half the design.** Default blank: **Comfort Colors 1717** garment-dyed heavyweight tee (Printify blueprint 706, provider 29 Monster Digital) in muted colours (Ivory, Bay, Butter, Blossom; darker ones only with a light-ink version). Sweatshirts: the Comfort Colors 1566 garment-dyed crewneck. Plain white Gildan reads cheap; use it only for kids and toddler sizes where Comfort Colors isn't available.
2. **Boutique layout: a small front, a statement back.** A left-chest mark (about 3.5 inches; x 0.76, y 0.17, scale about 0.27) plus a full back design. That's the current retail norm and the reason buyers pay $28–35. A large front-only design is allowed for kids and novelty shirts.
3. **Readable in one second, specific in the second.** One clear identity ("Hot Cocoa Social Club", "Black Lab Mama"), then oddly specific details ("members since the first snow", "walks · naps · tennis balls"). Generic phrases lose.
4. **Typography is the craft.** High-contrast serif headlines (Fraunces at large optical size: roman caps for the statement, italic for the soft line) with tracked condensed caps. Tight, deliberate spacing, thin rules and balanced widths. No cartoon fonts, no bouncy scripts, no word stacks.
5. **One or two inks that suit the garment:** cocoa or ink-green plus one cranberry accent on light garments. No rainbow, no gradients.
6. **Illustration is optional and small.** A neat icon (mug, black lab) supports the type; the type carries the design. Every dog is a black lab.
7. **Identity and keepsake angle:** "club", "est.", years and roles. People buy shirts that say who they are or mark a moment; matching family sets sell as bundles.
8. **Presentation:** create products **with the back print from the start**, so Printify includes back-view and size-chart photos. Lead with the front, then the back, a second colour and the size chart. Lifestyle photos beat white flat mockups (when free templates allow).
9. **Price to the retail band and the 20% floor:** 1717 front + back costs $19.73, so it's **$28.99** (2XL $30.99, 3XL $33.99). That's in line with Comfort Colors tees on Etsy.
10. **The bar:** before an HQ card, ask "Would this sit on a boutique rack next to a $30 shirt without looking homemade?" If not, redo it. Score it honestly; a 4 on the rubric means retail-ready, not "fine".

Reference build: `design/apparel-kit/retail.html` (Hot Cocoa Social Club and Black Lab Mama) and real mockups in `design/apparel-kit/retail-preview/`.

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
