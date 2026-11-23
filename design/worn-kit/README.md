# Worn kit (owner ask, Nov 23): show every shirt being worn, automatically

Owner: "It's more about how you feel when you wear it than what exactly you're wearing." Each shirt gets a feel-first set built from **Printify's real on-model mockups**. These are real renders of our exact design, so they're honest and Etsy-safe. Never AI-generate a person wearing a design.

## Output (per product, in `listings/worn-kit/<slug>/`)
1. `01-worn-hero.jpg`: a person wearing it, with the feeling line beside them (Etsy photo 1)
2. `02-back.jpg`: the statement back
3. `03-colours.jpg`: every colour, worn
4. `04-detail.jpg`: a chest close-up and fit notes
5. `05-size.jpg`: Printify's size chart
6. `<slug>-worn.mp4`: a 9:16 feel-first video, 11 s: the feeling hook, the person wearing it, the back, a colour cycle, and an identity close. Use it as the Etsy listing video (Etsy plays it muted) and as a social post.

## How to run
```
python3 design/worn-kit/fetch.py <printify_id> design/worn-kit/<slug>.json <assets_dir>
node design/worn-kit/build.js design/worn-kit/<slug>.json <assets_dir> <out_dir>
node social/motion/render.js <out_dir>/video.html <out_dir>/<slug>-worn.mp4
```
Config: `name`, `kicker`, `feel` (2 short lines: the moment and the feeling), `back_line`, `close` (an identity line, never a price), `palette`, `colours`.

## Rules
- Feeling first, product second: the first beat is the moment, not the shirt.
- Only real Printify renders of the shirt. Never invented mockups or AI people "wearing" it.
- Bob makes a worn kit for every new Comfort Colors draft and links it on the HQ batch card.
- Putting a kit on a **live** Etsy listing (new photo order or video) is an owner action in Shop Manager, or needs the owner's OK. Changing live listings through the API was blocked by the permission check on Nov 22.
