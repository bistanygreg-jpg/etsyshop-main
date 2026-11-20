# Content inventory (kept by Archie)

Last checked: 2026-11-11.

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

## Calendar check (2026-11-10, Archie daily run)

- **Dropbox:** no new uploads. `shirts-and-posters/` is still empty.
- **Problem found: TikTok rejects PNG photo posts.** The Nov 9, 12 PM Follow the Line carousel (419947529) went out on Instagram and Facebook, but **failed on TikTok**: "image/png not allowed, use jpeg". A second copy, 422518687, was posted by hand at 6:12 PM and also failed on TikTok. It **published again on Instagram and Facebook**, so those two networks now have the carousel twice.
- **Fixed (free):**
  - Converted the media of all 12 upcoming PNG posts to JPEG (`social/assets/metricool-jpg/`, commit 7cd2d1f) and updated them in Metricool.
  - Only the media changed: text, times, alt text and flags are the same.
  - New ids:
    - Nov 10, 6 PM golf: 423083359
    - Nov 11 Swipe to Reveal: 423084370
    - Nov 13 Santa Didn't Pay: 423084511
    - Nov 14 shirts: 423083644
    - Nov 15 Hold the Dots: 423084793
    - Nov 16 golf: 423083797
    - Nov 17 Swipe to Zoom: 423084908
    - Nov 18 shirts: 423083933
    - Nov 19 Traveling Icon: 423085023
    - Nov 20 golf: 423084154
    - Nov 21 Walking Through: 423085189
    - Nov 22 shirts: 423084261
- **Rule:** TikTok images must be JPEG or WebP. The pack TikTok folders and Follow the Line now have `slide-N.jpg` copies.
- **Other:**
  - The Nov 9 toddler humor post was moved to 6:20 PM (now 422524730) and published on all 3 networks.
  - 1 stale past-dated Story draft is left (416965600).

## Calendar check (2026-11-11, Archie daily run)

- **Dropbox:** no new uploads. `shirts-and-posters/` is still empty.
- **JPEG fix works:** the Nov 10, 6 PM TikTok golf slideshow (423083359) published with JPEG media. The Nov 10, 8 PM elf humor post (420963639) published on all 3 networks.
- **No failures** since the Nov 9 PNG error.
- **Cap watch:** about 19 posts published in November so far. Today's 12 PM carousel, the 8 PM pin and the 8 PM big brother post would take it to about 22. If the free plan really stops at about 20, today or tomorrow is when failures would start. Tomorrow's run checks every status, and Shout's Chrome job is the fallback.
- **Upcoming queue:** alt text, AI flags and pin links are all fine on Nov 11–22.

## Calendar check (2026-11-12, Archie daily run)

- **Dropbox:** no new uploads. `shirts-and-posters/` is still empty.
- **Free-plan limit hit on Nov 11.**
  - The 12 PM Swipe to Reveal carousel (423084370) published on all 3 networks.
  - The 8 PM pin (415968495) and the 8 PM Big Brother humor post (420963683, FB, IG and TikTok) failed: "You have reached your Metricool account limit."
  - Every post still queued in November will fail the same way: 7 pins, the Nov 12 golf humor post, 5 trend carousels and 5 TikTok slideshows.
- **Free fix:** `social/wk-nov12-fallback-pack/SHOUT_metricool-fallback_campaign.md`, with captions copied word for word and the posts ranked by value. Shout's Chrome job posts it through Meta Business Suite, TikTok Studio and Pinterest once the owner approves HQ card `ap-archie-metricool-fallback`.
  - The Chrome prompt now covers Pinterest and checks that card before posting.
  - Added `slide-N.jpg` copies to 5 carousel and 5 TikTok folders (48 files).
- **The failed Metricool posts stay in place** (never deleted). Metricool should be usable again from Dec 1, within about 20 posts.

## Calendar check (2026-11-13, Archie daily run)

- **Dropbox:** no new uploads. `shirts-and-posters/` is still empty.
- **New in the repo (Bob, Nov 12):**
  - First-photo images for Etsy: `listings/images/nice-list-kit_first-photo.jpg` and `listings/images/christmas-eve-mega-bundle_first-photo.jpg` (2000x1600)
  - Mockups: `listings/printify/2026-11-12_*` (Grandpa tee, Cookie Taster kids tee, Big Brother toddler sweatshirt)
  - Shout can use the 3 newly live shirts (Nice List adult and toddler, Big Sister sweatshirt) once their Etsy listings are confirmed.
- **Metricool:**
  - The Nov 12, 8 PM pin (415968525) and the golf humor post (420964092) failed with the account limit, as expected.
  - Today's 12 PM Santa Didn't Pay carousel (423084511) and the 8 PM pin (415968548) will fail too.
- **Fallback card `ap-archie-metricool-fallback`** is still pending, so the Chrome job posts nothing from the fallback pack yet. I adjusted the pack: P1 pin moved to Nov 19, golf humor (K) dropped because its date passed.
- **No "Shout scheduled" line on HQ for Nov 12.** That suggests the Chrome job didn't run, or ran without logging. Nov 12's pack posts may not have gone out:
  - FB Wish List, 1 PM
  - TikTok Wish List, 8:30 PM
  - TikTok Follow the Line re-post, 10 AM

  I can't check Meta or TikTok from the cloud, so this goes to the owner as a to-do.

## Calendar check (2026-11-14, Archie daily run)

- **Dropbox:** no new uploads.
- **Metricool:** the Nov 13, 12 PM Santa Didn't Pay carousel (423084511) and the 8 PM pin (415968548) failed with the account limit. Today's 6 PM TikTok (423083644) and 8 PM pin (415968567) will fail too.
- **HQ:** no owner activity since Nov 12. The fallback card, both shirt batch cards and the Chrome-check to-do are all still open, and there's still no "Shout scheduled" feed line.
- **Fallback pack adjusted:** carousel A moved to Sun Nov 22, 12 PM, and pin P2 moved to Nov 20. Load stays at 2 or fewer per network per day.

## Calendar check (2026-11-15, Archie daily run)

- **Dropbox:** no new uploads.
- **Metricool:** the Nov 14, 6 PM TikTok (423083644) and 8 PM pin (415968567) failed with the account limit. Today's 12 PM Hold the Dots carousel (423084793) and 8 PM pin (415968590) will fail too. Both are in the fallback pack for today.
- **The fallback card was approved Nov 14 (9:06 AM ET), but there is still no "Shout scheduled" line on HQ.**
  - The Mac Chrome job has never logged a run since it was set up on Nov 8. Even the old prompt posts that line, so the job is most likely not running.
  - Possible causes: the Mac is asleep at 11:47 AM, Chrome isn't open, or the extension isn't connected.
  - Until it runs, none of the hand-post packs or the fallback pack go out.
- **Fallback pack:** moved TikTok E to Tue Nov 17, 6 PM and pin P3 to Nov 21.

## Calendar check (2026-11-16, Archie daily run)

- **Dropbox:** no new uploads.
- **Metricool:** the Nov 15 Hold the Dots carousel (423084793) and pin (415968590) failed with the account limit. Today's 6 PM golf TikTok (423083797) and 8 PM pin (415968616) will fail too.
- **Chrome job:** still no run logged. The owner was active this morning (sent Etsy stats) but hasn't run it.
- **Fallback pack:** moved carousel B to Wed Nov 18, 12 PM, and pin P4 to Nov 22.
- **New owner data:** Social media is the biggest Etsy traffic source (11 of about 29 visits in 30 days). Getting the Chrome job running matters more than any calendar fix.

## Calendar check (2026-11-17, Archie daily run)

- **Dropbox:** no new uploads.
- **Metricool:** the Nov 16 golf TikTok (423083797) and the cocoa-night pin (415968616) failed on the account limit. The remaining November Metricool posts will fail the same way. I'm leaving them in place, since Archie never deletes.
- **Posting backlog:** the owner said "Done" on Nov 16 for the Mac run of `docs/posting-backlog.md` (28 posts, Nov 16–22). There's still no "Shout scheduled" feed line or results table, so I can't confirm what's queued in Meta, TikTok or Pinterest.
  - A Mac-side Shout session did post an outreach comment on Nov 16, so Claude in Chrome does work on the owner's Mac.
  - No more re-slotting: `docs/posting-backlog.md` is the single plan through Nov 22.
- **Dec 1:** Metricool's free slots should reset. Use them for the Cyber Specials week and pins first.

## Calendar check (2026-11-18, Archie daily run)

- **Dropbox:** no new uploads.
- **Posting is working again.** The Mac Chrome job ran on Nov 17 and scheduled 5 posts for Nov 18 after finding the upload fix: Hold the Dots on IG, FB and TikTok at 12 PM; the TikTok "Now Hiring" post at 6 PM; the IG last-day post at 7 PM.
  - The Nov 16 "Done" run scheduled nothing, so the Nov 16–17 backlog rows were lost.
  - The Nov 18 pin and everything from Nov 19 onward wait for the next Chrome run.
- **Metricool:** the Nov 17 posts failed on the limit, as expected.
  - Metricool post 423083933 (TikTok "Now Hiring", Nov 18 6 PM) duplicates the TikTok Studio post. It will fail on the limit, so nothing goes out twice. Left in place (never delete).

## Calendar check (2026-11-19, Archie daily run)

- **Dropbox:** no new uploads (`shirts-and-posters/` is still empty).
- **The Mac job ran on Nov 18** and scheduled 4 posts for Nov 19: Traveling Icon on IG, FB and TikTok at 12 PM, and TikTok shirts at 8:30 PM.
- **Fixed: "New this week" was skipped.** The Mac job thought its card wasn't on HQ, but `ap-shout-new-nov19` was approved on Nov 16. It probably looked only at open to-dos, and approved cards are marked done. The pack file now says APPROVED, so today's 11:47 AM run should schedule IG tonight and FB Fri 1 PM.
- **Metricool:** Nov 17–18 posts failed on the limit, as expected. Pending Metricool posts 423085023 (Nov 19), 423084154 (Nov 20), 423085189 (Nov 21) and 423084261 (Nov 22) will fail the same way. 423085023 duplicates today's Mac-scheduled Traveling Icon, so the failure means nothing goes out twice. Left in place (never delete). No new owner card: the Mac job covers the backlog for free.
- **Not covered yet:** Pinterest pins from the backlog (Nov 19, 20, 21 and 22 at 8 PM). Pinterest is in the Chrome prompt (step 3), but the last run said it wasn't part of the job, so the Mac task is probably still on the old prompt. HQ to-do `t-chrome-prompt-engagement` (paste the new prompt) is still open.

## Calendar check (2026-11-20, Archie daily run)

- **Dropbox:** no new uploads (full scan: 98 files, all dated Nov 3–5; `shirts-and-posters/` is empty).
- **The Mac job ran on Nov 19** and scheduled 4 posts: "New this week" on IG (Nov 19, 9 PM; moved from 7 PM) and FB (Nov 20, 1 PM), big-sibling shirts on IG (Nov 20, 7 PM), and TikTok golf "dad translated" (Nov 20, 6 PM). Yesterday's fix worked.
- **Still unscheduled:** the Nov 21–22 backlog rows (today's 11:47 AM run should pick them up) and every Pinterest pin. The Mac task still runs the old prompt.
- **Metricool:** 423085023 (Nov 19) failed on the limit, as expected; the Mac job had already posted it. Pending 423084154 (Nov 20 TikTok golf) duplicates the Mac-scheduled TikTok, but it will fail on the limit, so nothing posts twice. 423085189 (Nov 21) and 423084261 (Nov 22) will fail the same way. Left in place (never delete). No new owner card.
- **CLAUDE.md:** recorded that the owner rejected pausing shirts on Nov 20 (Bob keeps 3 drafts a day) and that batch 9 was "not now".

