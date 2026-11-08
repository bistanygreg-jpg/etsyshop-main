# Milestone & Meaning: shop memory

Claude reads this file at the start of every session in this repo. Keep it current: after each working session, add a dated entry to `docs/conversation-log.md` and update the facts below if anything changed.

## The business

- **Shop:** Milestone & Meaning on Etsy (shop name `MilestoneAndMeaning`). Owner account email for Metricool: milestonememoriesshop@gmail.com.
- **What we sell:** printable (instant-download) Christmas Eve and Santa kits for kids. Nothing ships. Every page is a fillable PDF in US Letter and A4. Pitch: "Type their name, print at home, cut. About five minutes."
- **Products and links:**
  | Product | Price | Etsy listing |
  |---|---|---|
  | Nice List Kit: letter from Santa, Nice List certificate, North Pole toy receipts, reindeer food tags (6/page), 24 Days of Kindness countdown | $6.99 | https://www.etsy.com/listing/4609111971/letter-from-santa-printable-kit-nice |
  | Christmas Eve Mega Bundle (13 pages): box labels, Santa's magic key tags, North Pole boarding passes, cookie thank-you notes (2/page), Nice List door hangers, round reindeer food tags, cocoa night menu, plus all Nice List Kit pages | $12.99 (live on Etsy since Nov 8, 2026) | https://www.etsy.com/listing/4609141967/christmas-eve-box-printable-bundle-santa |
  | Kids' Christmas Wish List: wish list, draw-your-wishes page, sibling page, "Received!" cards from Santa's mail room | $3.99 | https://www.etsy.com/listing/4609242348 |
- **Other items promoted in posts:** big brother/big sister pregnancy announcement shirts, and realistic golf course posters (free shipping). No listing links are recorded here yet.

## Pricing (recommended Nov 7, 2026; confirm each against what Etsy shows)

| Product | Price | Why |
|---|---|---|
| Kids' Christmas Wish List | $3.99, keep | Entry-level impulse buy, in line with single printables (~$2–4). |
| Nice List Kit | $6.99, keep | 5 pages, mid-range for Santa letter kits. |
| Christmas Eve Mega Bundle | **$12.99**, set by owner Nov 8 | 13 pages and includes the whole $6.99 kit. Comparable full Christmas Eve bundles sell for about $10–13. It reads as the obvious upgrade: about 2x the price for 2.6x the pages. Don't go below $9.99, or it undercuts the Nice List Kit. |
| Big brother/sister shirts | **$22.99** with free shipping | Etsy toddler tees run about $9–25, plus a few above $30. If print-on-demand cost plus shipping is about $13–15, that leaves about $6 after Etsy fees. Raise to $24.99 if cost is higher. |
| Golf course posters | **$29.99** (12x18) / **$39.99** (18x24), free shipping | Comparable course prints run about $18–45. Check that the print cost plus shipping is under about 55% of the price. |

Rules of thumb: Etsy takes about 10% (transaction + processing) plus $0.20 per listing. Price physical items so profit after costs and fees is at least $5–6. Prefer one "Mega Bundle" upsell over discounting the small kits.

## Social accounts (all through Metricool)

- Metricool brand `milestoneandmeaning`, **brandId 7837631**, timezone America/New_York.
- Instagram `@milestoneandmeaning`, TikTok `@milestone.and.mea`, Pinterest `MilestoneAndMeaning`, Facebook page id 1421214861075289.
- Scheduling media must be at a public URL; Metricool copies it to static.metricool.com when the post is created. This repo is **public** (since Nov 7, 2026), so use `https://raw.githubusercontent.com/bistanygreg-jpg/etsyshop-main/<commit-sha>/<path>`. Push first, and pin to a commit SHA rather than a branch. Everything committed here is public, so never commit secrets or customer data.
- Cadence (as of Nov 7, 2026): something posts nightly at 8pm ET through Nov 17, plus the 7 trend carousels at 12pm ET on Nov 9, 11, 13, 15, 17, 19 and 21 (IG + FB + TikTok). Pinterest pins link to the Etsy listings. IG/TikTok captions say "link in bio" or "Find us on Etsy: MilestoneAndMeaning".

## House rules for content

- Designs are made with AI tools. Keep the disclosure: "AI design tools were used in creating this design" on pins, `isAiGenerated` on IG/TikTok, "Art created with AI tools" on posters.
- Use only real facts and numbers. No made-up sales counts, reviews or backstory.
- Use "link in bio" CTAs. Comment-keyword CTAs ("comment WORD for the link") only work once an auto-DM tool such as ManyChat is set up, and it isn't yet.
- Golf posters: "Not affiliated with any club or tour."
- Don't publish or schedule to Metricool without the owner's go-ahead.

## Brand look

- Listing mockups: cream background `#EBE2D1`, paper `#FBF6EC`, cranberry `#8D1B1B`, forest green `#204D39`, gold accents `#C9A24A`.
- Header type is a rounded geometric sans (we use **Poppins**). Product pages use a holiday script with holly accents.
- Shared CSS: `social/carousel-trends/src/brand.css`.

## Repo map

- `social/assets/metricool/`: original post images and videos downloaded from Metricool (named by Metricool file id). `social/assets/crops/`: product-mockup crops.
- `social/carousel-trends/`: 7 trend carousels. `src/*.html` are the sources and `src/img/` holds the processed product images. Re-render with `node social/carousel-trends/src/render.js [name]` (uses the preinstalled Playwright). Output goes to `<name>/slide-N.png` at 1080x1350. `PLAN.md` has the captions and posting plan.
- `docs/conversation-log.md`: running log of every working session.

## Environment notes

- Cloud environment **etsyshop-main** (personal) allows `static.metricool.com`, `i.etsystatic.com` and `www.etsy.com`, so sessions can download Metricool media and Etsy listing photos. The Default environment can't reach those hosts.
- Metricool media URL pattern: `https://static.metricool.com/planner/<YYYYMM>/7837631-file-<id>.<ext>`.
