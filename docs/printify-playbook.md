# Printify playbook: one new listing a day

**Goal (owner, Nov 8, 2026):** one new Printify product listing per day. **Raised Nov 10:** 3 drafts a day, shirts and sweatshirts only, all on one HQ batch card (`ap-pf-batch-<date>`). One tap approves all three, and Bob publishes them on the next run. The owner prefers Printify products. Bob runs it daily, using Reach's ideas and Penny's copy rules.

## Access

- Printify API `https://api.printify.com/v1`. The token is saved as a network secret on the **etsyshop-main** environment. In commands, send `Authorization: Bearer proxy-injected` and the proxy swaps in the real token. Never print, store or commit the token.
- Printify shop **"Milestone and Meaning"**, id **29591075**, sales channel Etsy.
- Mockup images come from `images.printify.com`, which the environment allows. **These are the real product photos** for social posts and HQ cards.

## Costs (the no-new-spending rule)

- Creating products, uploading designs and mockups: **free**. Printify charges only when an order is placed, and that comes out of the sale.
- Publishing to Etsy: **$0.20 Etsy listing fee**. That's allowed, but only after the owner approves the card on HQ.
- Never order samples, upgrade Printify, buy mockup or design tools, or turn on ads.

## Proven setups (copy these first)

| Product | Blueprint / provider | Cost | Our price | Notes |
|---|---|---|---|---|
| Kids tee (Gildan 5000B) | 157 / 29 (Monster Digital) | $7.36 | $19.99 | 15 enabled variants: XS–XL × White, Light Blue, Sport Grey. Reference product 6aea8ee3365c19e4ba07e3c9 |
| Toddler tee (Bella+Canvas 3001T) | 580 / 39 (SwiftPOD) | $11.02 | $21.99 | 12 variants: 2T–5T × 3 colours. Reference 6aea9b1240a6113740075848 |
| Poster, matte | 282 / 99 | $10.62–15.79 | $34.99–44.99 | 18x24 and 24x36. Reference 6aee7a7a95c04f1e240a1ba4 |
| Panorama print | 284 / 99 | $9.35–12.40 | $29.99–44.99 | Reference 6aee804f2f433c3eae035dfb |

Before trying a new blueprint (mugs, ornaments, sweatshirts, onesies), check its cost in the catalog API. Profit after Etsy fees (about 10% plus $0.20, and Offsite Ads can take 12–15% more) must be at least $5–6.

## Daily run

1. **Pick:** take the top unbuilt item from `listings/printify/backlog.md` (Reach keeps it filled). It must be IP-safe: original wording, no characters, brands, sports teams or famous quotes, and no real golf course names. Don't re-pitch an idea the owner rejected on HQ.
2. **Design:**
   - Make it with free tools (HTML plus Playwright, or PIL) in brand style, as a transparent PNG.
   - **Crop tight to the artwork** before uploading. Big empty margins print tiny.
   - Shirts: place at x 0.5, y about 0.36, scale about 0.8.
   - Keep print files in the session scratchpad. **Never commit full-resolution print files**, because the repo is public.
3. **Create:** `POST /uploads/images.json` (base64), then `POST /shops/29591075/products.json`, copying the reference product's variants and price.
   - A `PUT` update must list **all** variant ids in `print_areas.variant_ids`, not only the enabled ones.
   - Title: 140 characters max, buyer phrase first.
   - 13 tags, 20 characters max each.
   - The description ends with the design-tools disclosure.
   - Size note for kids sizes.
4. **Check:** download the default mockup from `images.printify.com` and look at it. Fix placement if the print is small or off-center. Save a small mockup to `listings/printify/<date>_<slug>_mockup.png`.
5. **Ask:** put ONE HQ approval card per product: "Publish <title> to Etsy", with chips "$0.20 Etsy listing fee" and the price. Include the mockup link and `ifYes`.
6. **Publish approved drafts:** on the next run, for each approved card, call `POST /shops/29591075/products/<id>/publish.json` with `{"title":true,"description":true,"images":true,"variants":true,"tags":true,"keyFeatures":true,"shipping_template":true}`. Then read the product back for its Etsy link (`external.handle`) and record it in CLAUDE.md and `listings/printify/log.md`.
   - Rejected cards: leave the draft unpublished. Never delete.
7. **Hand-offs:** Shout gets the mockups for posts; Archie adds them to the inventory.

**Season:** Printify shirts need ordering by about **Dec 8** to arrive for Christmas. After Dec 1, switch to evergreen and spring products (pregnancy and sibling reveals with no holiday, birthdays, Valentine's, Easter, Mother's Day).
