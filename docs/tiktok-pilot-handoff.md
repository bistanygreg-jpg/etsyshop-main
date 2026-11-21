# TikTok Shop pilot: handoff to a Chrome-capable session (Mac, Claude desktop app)

Written 2026-11-21. This is a separate brand from Milestone & Meaning. Keep the two apart: no shared accounts, no cross-posting of Etsy content.

**Why a handoff:** cloud sessions cannot drive the owner's browser. Claude in Chrome runs only in the Claude desktop app on the owner's Mac (same reason Shout's posting job is a desktop task, see `docs/shout-chrome-posting.md`). A cloud session prepares assets and copy; the Mac session clicks through Printify and TikTok.

**Public repo rule:** everything here is public. Never write the owner's name, address, phone, email, SSN/EIN, ID or bank details. The owner types those into TikTok and Printify forms.

## State as of Nov 21, 2026

- **Brand:** Mixtape Mercantile (era-neutral 80s and 90s nostalgia, print on demand, TikTok Shop only). Test: 80s vs 90s, same products, same schedule, same video style, 2 to 3 weeks of posting before judging. Orders count most.
- **Done by the owner:** new TikTok account, TikTok Shop application submitted (waiting for approval), Printify store connected, pickup and return warehouses added, Seller Shipping template created. Both Printify and TikTok are logged in in the Mac's Chrome.
- **Not done:** the TikTok Shop is not yet approved, so no product can be published. Pricing is not set (needs Printify's shipping cost per product). Trademark checks on the slogans are not done.
- **Profile image:** Canva design "Mixtape Mercantile logo", design id DAHba_WXVQ8, exported 1080x1080.
- **Bio (80-character limit), pre-approval:** `80s or 90s? Pick a side 📼 Retro tees & mugs, launching soon. Follow along!` Once the shop is live: `80s or 90s? Pick a side 📼 Retro tees & mugs for the nostalgic. Shop below ↓`

## Designs (all AI-generated: turn on TikTok's AI-generated content toggle and keep the disclosure)

Canva media ids (open at `https://www.canva.com/M/<id>`). Background-removed (transparent) versions exist only for the first pair; the rest still need the Canva remove-background step.

| # | Era | Slogan | Original media id | Transparent version |
|---|---|---|---|---|
| 1 | 80s | Neon Nights Club | MAHbhLvF-1k | MAHbhNZITuw |
| 2 | 80s | Arcade After Dark | MAHbhOXO-Tc | needed |
| 3 | 80s | Roller Rink Regular | MAHbhAF7DZ4 | needed |
| 4 | 80s | Totally Analog | MAHbhKuSJ24 | needed |
| 5 | 80s | Pixel Paradise | MAHbhPMP0cQ | needed |
| 1 | 90s | Whatever, Forever | MAHbhFsGMYA (die-cut) | MAHbhI1pzeI |
| 2 | 90s | Sorry, I Was On Dial-Up | MAHbhPRcZ9M | needed |
| 3 | 90s | Skate Park Sundays | MAHbhJkCoSU | needed |
| 4 | 90s | Sleepover Season | MAHbhHlx-6M | needed |
| 5 | 90s | Can't Talk, Burning a CD | MAHbhEiZWS0 | needed |

Notes: originals are 2048x2048, about 170 dpi at a 12-inch print, so check Printify's quality warning. The first 90s attempt (MAHbhF8a1yI) is a full-bleed black image that cannot be cut out; do not use it. Sellable art is not committed to this repo; it stays in Canva.

## Guardrails (same spirit as the Etsy team)

- Designs capture the feeling of an era only: no real brands, logos, show names, characters, band names or catchphrases tied to a property. Run each slogan through a trademark search (USPTO database plus a web search, in apparel and mugs) before listing.
- Spend nothing: no ads, boosts, samples, paid tools or paid upgrades. TikTok Shop has no listing fee; its referral fee (reported near 6% for apparel) only applies on a sale.
- Honest copy: no invented sales counts, reviews, "limited edition" or "handmade". Designs are AI-assisted; say so where the platform allows.
- The owner approves designs before anything is listed or posted.
- Stop and leave a note instead of guessing if a login, 2-step check, CAPTCHA, ID or tax form, or permission dialog appears. Never work around a security check. Never type SSN, EIN, ID numbers or bank details; the owner does.

## Next steps for the Mac session, in order

1. While the shop is pending: export approved designs from Canva as transparent PNGs; run Canva remove-background on the ones marked "needed"; zoom in on the edges.
2. Build the Printify products for the TikTok store as drafts only (tee first; mugs only if the owner confirms them). Read Printify's shipping cost per product before setting any price. TikTok recommends a flat shipping rate of 5.99 USD or less; if Printify's cost is higher, raise the product price instead.
3. Write TikTok Shop titles and descriptions for each design (original wording).
4. Do not publish until the owner says the shop is approved and the designs are approved.
5. Videos: 2 per design for the first round (5 to 6 designs per era), a strong hook in the first two seconds, same style for both eras. The posting rate is 1 to 2 posts a day on the new account.
6. Log what was done in `docs/conversation-log.md` (no personal details).

## Prompt to paste into a new Claude desktop session on the Mac

Open the Claude desktop app, start a new Code session in the local clone of this repo, make sure the Claude in Chrome extension is connected, then paste:

---
You are working on the Mixtape Mercantile TikTok Shop pilot. Read `docs/tiktok-pilot-handoff.md` in this repo first, then CLAUDE.md for the house rules (honesty, no new spending, privacy). Load the Chrome tools in one ToolSearch call (tabs_context_mcp, tabs_create_mcp, navigate, computer, read_page, form_input, tabs_close_mcp), call tabs_context_mcp first, and work in a new tab. Printify and TikTok Seller Center are already signed in. Follow the "Next steps" list in the handoff, starting at step 1. Stop and leave a note if a login, 2-step check, CAPTCHA, ID or tax form, or permission dialog appears; never enter SSN, EIN, ID or bank details. Do not publish anything. At the end, add a dated entry to `docs/conversation-log.md` and tell me what is done and what needs my approval.
---
