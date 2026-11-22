# Social creative standard (owner, Nov 22, 2026)

**Owner ask:** "step the social media content up. We need creativity. Animation, captivating designs that make our viewers feel excited to go check out our content."

Shout follows this for every post, and Bob builds the visuals to it. Static, flat product grids are now the exception, not the default.

## 1. Lead with motion

- **Default format: a 9:16 animated video** (Reel, TikTok, Short), **8–12 seconds**, built with `social/motion/` (HTML/CSS animation rendered frame by frame to MP4 by `social/motion/render.js`).
- At least **3 of every 5 posts are motion**. Carousels are for "save this" lists; single images are for Pinterest only.

## 2. Anatomy of a post that stops the scroll

| Beat | Time | What happens |
|---|---|---|
| **Hook** | 0–1.5 s | Motion in the first frame plus a bold promise or POV line ("Santa magic in five minutes", "For the black lab people"). Never open on a logo or a still product shot. |
| **Reveal** | 1.5–5 s | The real product in motion: pages flying in and fanning, a front-to-back shirt flip, an iris or wipe reveal of the art, a name typing in. A scene change every 1.5–2.5 s. |
| **Proof or value** | 5–7.5 s | What you get (13 pages, 4 colours, "type, print, cut"), the price slam or sale stamp. |
| **Call to action** | last 2 s | A clean end card: product name, price, a pulsing "LINK IN BIO", and the sale dates if there's a sale. |

- **Text on screen carries the story** (many people watch muted): large, at most 6 words a beat, in the brand fonts (Fraunces, Barlow Condensed).
- **Real assets only:** product page renders, Printify mockups, lifestyle photos. Never a fake mockup or a fake review.
- **Brand look:** cream and paper backgrounds, cranberry, forest and gold; gentle snow or texture for the season.
- **Loop-friendly:** the end card should flow back to the hook.
- **Sound:** add a popular royalty-free instrumental from the app's own library at posting time (Mac Chrome job). Never use copyrighted songs outside the app library.

## 3. Captions

- Line 1 repeats the hook. Line 2: the benefit or detail. Line 3: price or sale plus "link in bio".
- IG 8–12 hashtags, TikTok 4–6, Pinterest keywords in the description.
- Keep the AI disclosure: "AI design tools were used in creating this design" (and the platform's AI label where it exists).

## 4. Quality bar before posting (score each 1–5; every line must be 4 or more)

1. Hook: would I stop scrolling in the first second?
2. Motion: smooth, purposeful, nothing static for over 2.5 s?
3. Legibility: every text beat readable on a phone in under a second?
4. Product truth: real product, real price, real dates?
5. Brand: looks like Milestone & Meaning (fonts, palette, warmth)?
6. Ending: a clear, pulsing call to action, and does it loop back?

## 5. Production

- Templates: `social/motion/cyber-specials-reel.html` (printables: fly-in, typing, price slam) and `social/motion/black-lab-mama-reel.html` (shirts: iris reveal, 3D front-to-back flip, colour cycle). Copy one and swap the assets and words.
- Render: `node social/motion/render.js <file.html> <out.mp4>` (30 fps, H.264, about 30 s per 10 s video).
- Packs go in `social/wk-<date>-motion-pack/` with an MP4, a cover JPG and captions in `SHOUT_*_campaign.md`. Posting still needs the owner's tap (HQ card).
