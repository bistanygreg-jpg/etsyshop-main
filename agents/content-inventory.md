# Content inventory (kept by Archie)

Last checked: 2026-11-09.

## By product

| Product | Assets we have | Where | Missing |
|---|---|---|---|
| Nice List Kit ($6.99) | Pins (5), IG carousel (7), IG story, vertical reel, TikTok photos (7) and mp4s (3), contact sheet | Dropbox `nice-list-kit/`; copies of the Metricool versions in `social/assets/metricool/` | none |
| Christmas Eve Mega Bundle ($12.99) | Pins (8), IG carousel (10), IG story, vertical reel, TikTok photos (8) and mp4s (3), contact sheet; mockup crops | Dropbox `christmas-eve-mega-bundle/`; `social/assets/crops/`; `social/carousel-trends/src/img/` | none |
| Kids' Christmas Wish List ($3.99) | IG post, FB image, TikTok mp4 | Dropbox `2026-Christmas/social-batch-01/` | a pin set and a carousel |
| Big Brother / Big Sister shirts | 1 text graphic (star badge); 3 TikTok slideshows | `social/assets/metricool/5990074724123993563.jpeg`; `social/tiktok/bigbro-*` | **real product photos** (waiting on Dropbox `shirts-and-posters/`); Etsy listing link |
| Golf course posters | 2 text graphics (flag, golf ball); 3 TikTok slideshows | `social/assets/metricool/17844548497389654577.jpeg`, `9666596862434131454.jpeg`; `social/tiktok/golf-*` | **real product photos**; Etsy listing link |
| Brand / profile | Profile pictures (3), FB covers (2), IG highlight covers (5), Pinterest board covers (3) | Dropbox `profile-assets/` | none |

## Campaign assets (generated, public in this repo)

| Campaign | Folder | Slides | Scheduled |
|---|---|---|---|
| Viral carousel trends | `social/carousel-trends/<name>/` | 7 carousels, 30 slides | Nov 9–21, 12pm ET |
| Shirts and golf TikTok series | `social/tiktok/<name>/` | 6 slideshows, 30 slides | Nov 10–22, 6pm ET |
| Hand-post pack Nov 9–15 | `social/wk-nov9-pack/<post>/` | 6 posts, 23 slides | By hand (Meta Business Suite, TikTok app) |
| Hand-post pack Nov 16–22 | `social/wk-nov16-pack/<post>/` | 7 posts + 2 optional Big Cousin slides, 30 slides | By hand |

Shared pack sources: `social/packs-src/` (`build.py`, `render.js`, `img/` with resized Printify mockups and crops of the shop's listing graphics).

## Calendar hygiene findings (2026-11-08)

- **Fixed:** missing alt text on 5 posts. New ids: 420963492 (Nov 8 golf humor), 420963563 (Nov 9 toddler), 420963639 (Nov 10 elf), 420963683 (Nov 11 big brother), 420964092 (Nov 12 golf posters).
- **Stale drafts (past dates, will not publish):** 416965572 (IG Nov 6), 416965583 (FB Nov 7), 416965641 (TikTok Nov 6). 416965600 is an IG Story draft for Nov 8 at 7pm; as a draft it won't post. They're harmless, but the owner can delete them in Metricool to tidy up. Archie never deletes posts.
- **Passed to Shout:** the 6 humor and product posts (Nov 7–12) carry 6 hashtags across IG, FB and TikTok. That's fine for TikTok but under Shout's 8–12 for Instagram. Future posts should split captions by network.
- **Load check:** no network has more than 3 posts on any day through Nov 22.

## Calendar check (2026-11-09, Archie daily run)

- **Dropbox:** `shirts-and-posters/` is still empty, and nothing else is new in `/Milestone & Meaning – Social`. Shirt and golf content keeps using the Printify mockups in `social/packs-src/img/`.
- **Nothing failed.** Every Metricool post dated before now went out, including last night's Nov 8, 8 PM golf humor post on Facebook, Instagram and TikTok (420963492).
- **Free-plan cap forecast.** November has 14 published posts and 24 more queued for Nov 9–22, 38 in total.
  - If the cap really is about 20 posts a month, posts after roughly the Nov 11, 12 PM carousel could start failing.
  - Ranked fallback if they fail, most valuable first:
    1. Product posts and the sale-ending posts: the trend carousels with prices (Nov 15 Hold the Dots, $6.99), the Nov 11 and 13 bundle carousels, and the shirt and golf TikToks.
    2. Pinterest pins.
    3. Humor posts last (Nov 9 toddler, Nov 10 elf).
  - Free fix: Shout's daily Chrome job (`docs/shout-chrome-posting.md`) re-posts any failed post through Meta Business Suite or TikTok Studio. The images are in `social/carousel-trends/`, `social/tiktok/` and `social/assets/metricool/`.
- **Stale drafts dated in the past (6, won't publish):** 416965563, 416965624, 416965641, 416965572, 416965583, 416965600. They're harmless; the owner can delete them in Metricool. Archie never deletes.
- **Load:**
  - Instagram has 3 posts on Nov 9 (12 PM carousel, 7 PM pack post, 8 PM humor) and 3 on Nov 11. That's at the limit, not over.
  - TikTok has 2 posts on Nov 12, 30 minutes apart (8 PM golf, 8:30 PM pack Wish List).
- **Hashtags (known, passed to Shout):** these posts share one caption across networks.
  - The 4 humor and product posts carry 6 tags, under Instagram's 8.
  - The 6 trend carousels carry 8–9 tags, over TikTok's 6.
  - Splitting them would mean separate posts, which costs more cap slots, so they stay as they are.
- Alt text, AI flags and pin links are all present and correct on every upcoming post.
