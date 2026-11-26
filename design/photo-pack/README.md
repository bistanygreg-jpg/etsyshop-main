# Photo packs: "10+ images and a short video" for every listing (Nov 25, 2026)

Etsy emailed the owner on Nov 25: "Add a short video and 10+ images from different angles or in use to help buyers quickly understand your product". The listings named were the Official Nice List kids tee and the Big Cousin toddler sweatshirt. Printify pushes only 3–4 mockups for most of our shirts (Comfort Colors: 9) and no video.

A photo pack adds 10 square photos (2000x2000) and a 10 s square video to a listing. Everything comes from **real Printify renders of the exact product**: front, back, colours, Printify's on-model cameras and the size chart. These are framed in the design system with honest copy. Never use AI-generated people or invented mockups.

## Run
```
python3 design/photo-pack/build.py <printify_product_id> design/photo-pack/configs/<slug>.json listings/photo-pack/<slug>
```
Then add a row to `listings/etsy-upload-queue.md`. The Mac agent uploads the video first, then the photos, after the existing Printify photos.

## Camera ids by blank (found Nov 25 by comparing renders; most ids return a default image, so check them visually)
| Blank | Front | Back | On-model / in use | Size chart |
|---|---|---|---|---|
| Rabbit Skins toddler sweatshirt (bp 1644) | 110548 | 110549 | 110552 boy front, 110553 boy back, 110554 girl front, 110555 girl back; 110550 folded | 110556 |
| Kids tee (bp 157) | 105377 | 105378 | none found | none |
| Comfort Colors 1717 (bp 706) | 98445 | 98446 | 98448 woman front | 110132 |
| Gildan 5000 (bp 6) | 102005 | 102006 | 101994 man front, 101990 man back, 101996 two women (best for women's roles) | 101998 |
| Youth sweatshirt (bp 1256) | 101396 | 120166? | not found yet (the camera range is wide and renders time out; retry) | – |

## Rules
- Honest dates only ("Order by Dec 8 for Christmas delivery in the US" until Dec 8, then switch `order_line`).
- Rebuild a pack when its art changes. Once a pack is uploaded, Printify republishes use `images: false`.
- Daily (Bob, from Nov 26): build packs for up to 3 live listings, in this order: the listings Etsy flagged, reveal and family shirts, Comfort Colors tees, then the rest.
