# Etsy upload queue (the Mac Chrome agent works through it daily; job step 2)

Cloud agents (Bob, Penny, Archie) add rows. The Mac agent uploads in Etsy Shop Manager, and the cloud agents mark rows done after seeing its feed line. Files are in the repo; download them from raw.githubusercontent.com on branch `claude/focused-dirac-hd5erf`.

| Status | Listing ID | Product | Folder | Photo order to set | Video |
|---|---|---|---|---|---|
| to do | 4624014130 | Night Shift Society tee | `listings/worn-kit/night-shift-society/` | 01-worn-hero, 02-back, 03-colours, 04-detail, 05-size, then the existing Printify photos | night-shift-worn.mp4 |
| to do | 4609141967 | Christmas Eve Mega Bundle | `listings/images/` | christmas-eve-mega-bundle_lifestyle.jpg first, then existing | – |
| to do | 4609111971 | Nice List Kit | `listings/images/` | nice-list-kit_lifestyle.jpg first, then existing | – |
| waiting: goes live Nov 27 (Bob adds the Etsy ID) | – (Printify 6b05d4c93bd19e59d60273e1) | Field Trip Survivors Club tee | `listings/worn-kit/field-trip-survivors/` | 01-worn-hero, 02-back, 03-colours, 04-detail, 05-size, then the existing Printify photos | field-trip-survivors-worn.mp4 |
| waiting: goes live Nov 28 (Bob adds the Etsy ID) | – (Printify 6b07263632b4d5c00b0ce1cc) | Snow Day Committee tee | `listings/worn-kit/snow-day-committee/` | 01-worn-hero, 02-back, 03-colours, 04-detail, 05-size, then the existing Printify photos | snow-day-committee-worn.mp4 |

| to do | 4618717339 | Big Cousin toddler sweatshirt (photo pack: Etsy asked for 10+ photos and a video, Nov 25) | `listings/photo-pack/toddler-sweatshirt-big-cousin/` | Keep the existing Printify photos first, then add 01-hero to 10-order (Etsy allows 20 photos in total) | toddler-sweatshirt-big-cousin-video.mp4 |
| to do | 4617297514 | Big Brother toddler sweatshirt (photo pack: Etsy asked for 10+ photos and a video, Nov 25) | `listings/photo-pack/toddler-sweatshirt-big-brother/` | Keep the existing Printify photos first, then add 01-hero to 10-order (Etsy allows 20 photos in total) | toddler-sweatshirt-big-brother-video.mp4 |
| to do | 4617297824 | Big Sister toddler sweatshirt (photo pack: Etsy asked for 10+ photos and a video, Nov 25) | `listings/photo-pack/toddler-sweatshirt-big-sister/` | Keep the existing Printify photos first, then add 01-hero to 10-order (Etsy allows 20 photos in total) | toddler-sweatshirt-big-sister-video.mp4 |
| to do | 4609448036 | Big Brother kids tee (photo pack: Etsy asked for 10+ photos and a video, Nov 25) | `listings/photo-pack/kids-tee-big-brother/` | Keep the existing Printify photos first, then add 01-hero to 10-order (Etsy allows 20 photos in total) | kids-tee-big-brother-video.mp4 |
| to do | 4615009470 | Big Sister kids tee (photo pack: Etsy asked for 10+ photos and a video, Nov 25) | `listings/photo-pack/kids-tee-big-sister/` | Keep the existing Printify photos first, then add 01-hero to 10-order (Etsy allows 20 photos in total) | kids-tee-big-sister-video.mp4 |
| to do | 4613415513 | Big Cousin kids tee (photo pack: Etsy asked for 10+ photos and a video, Nov 25) | `listings/photo-pack/kids-tee-big-cousin/` | Keep the existing Printify photos first, then add 01-hero to 10-order (Etsy allows 20 photos in total) | kids-tee-big-cousin-video.mp4 |
| to do | 4614995197 | Official Grandma tee (photo pack, Nov 26) | `listings/photo-pack/adult-tee-grandma/` | Keep the existing Printify photos first, then add 01-hero to 10-order | adult-tee-grandma-video.mp4 |
Rows marked "waiting" are skipped until their status says "to do".

**Order of work (Nov 25):** the Etsy video first on each row (Etsy flagged missing videos), then the photos. Work top to bottom; stop after about 30 minutes and carry on the next day.

**Rule for cloud agents (Nov 25):** once a row is done, never republish that Printify product with `images: true`. Printify would replace the uploaded photos and video. Use `images: false`; if the art changes, rebuild the pack and queue it again.

Still missing worn kits (Bob builds them; Penny queues them once built): Hot Cocoa Social Club 4622861183, Black Lab Mama 4622869328, Cookie Exchange 4624014062, Trail Snack 4624014260, Lights Tour 4624782705, Chapter Chasers 4625581199.

## Other Shop Manager changes (Mac agent, same run)

| Status | When | Change |
|---|---|---|
| to do | **Tue Dec 1 or later run, before Dec 15** | Marketing → Sales and discounts → Create a sale: **20% off, Dec 15 to Dec 23, printables only** (the digital listings: Nice List Kit, Christmas Eve Mega Bundle, Wish List, Countdown Kit, Scavenger Hunt, Elf Letters, Tooth Fairy kits, sports award, plus the Complete Bundle and NYE kit if live). **No shirts, sweatshirts or prints** (at 20% off they fall below the 20% margin floor). Name it HOLIDAY20. Approved by the owner Nov 12 (card `ap-penny-listings-nov11`). Add one feed line when it's set up. |
| to do | next run | CYBER26 narrowed to printables (job step 2b in `docs/shout-chrome-posting.md`). |

