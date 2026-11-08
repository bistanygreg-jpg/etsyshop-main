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

## Ownership: Shout runs all social media

**Shout** (`anthropic-skills:shout-etsy-social-promoter`) owns every social promotion activity for this shop: content ideas, asset creation, captions, calendars and Metricool scheduling, across all products and channels. For any social media request, invoke the Shout skill first and follow its rules: asset specs, copy rules, hashtag counts (IG 8–12, TikTok 4–6), posting windows and honesty. Log each campaign in `agents/Agent-roster.md` as `SHOUT_<product>_campaign.md`, with Hawk's metrics to watch.

## Content management: Archie

**Archie** (project skill `.claude/skills/archie-content-manager`) owns the content library and inventory (`agents/content-inventory.md`), intake of new uploads, Metricool calendar hygiene, naming and versioning, these memory files and public-repo safety. Archie hands ready assets to Shout.

## Two homes for team memory (read both)

Earlier sessions kept the team's docs in a claude.ai **Project**: `agents/Agent-roster.md`, `agents/Privacy-rules.md`, `hawk/Goal-1000.md`, `hawk/Hawk-log.md`, `reach/`, `products/social/`. Live status, decisions and to-dos are in the **HQ** artifact's database (claude.ai/artifact/QGJopFL731DnaQX5DuNHpY). This repo holds the skills, campaign assets and this file. When they disagree, HQ and the Project docs are newer for anything decided before Nov 8, 2026.

Facts from HQ (as of Nov 8, 2026):
- **Goal:** $1,000 in sales by Dec 31, 2026. Checkpoints: $200 by Nov 30, $550 by Dec 15, $900 by Dec 24.
- **Live:** 12 listings (9 printables, 3 shirts). The printables include Elf Letters, a Countdown Kit ($5.99), a Scavenger Hunt and Tooth Fairy kits. Kids' and toddler Big Brother/Sister shirts are live through Printify ($21.99 toddler).
- **25% launch sale** runs Nov 4–18 on the Nice List Kit, Christmas Eve Bundle, Wish List and Scavenger Hunt. Cyber Specials at 25% off are approved for Nov 23–Dec 1 (8 digital listings, no shirts).
- **Decided:** Etsy Ads, not now; revisit after Hawk's Nov 9 check. The About story, not now. A dateless big-sibling tee, not now. Share & Save bio links are done.
- **Metricool free plan caps published posts at about 20 a month.** New Instagram and Facebook posts move to Meta Business Suite from Nov 9. Archie should check the cap against everything scheduled.
- **Privacy:** never write the owner's real name or personal details. Use the shop name only.

## The agent team

| Agent | Owns | Skill |
|---|---|---|
| Shout | Social promotion and scheduling | `anthropic-skills:shout-etsy-social-promoter` (account skill) |
| Archie | Content library, intake, calendar hygiene, memory files, repo safety | `.claude/skills/archie-content-manager` |
| Reach | All research and analysis: product ideas, pricing benchmarks, SEO and growth, strategy | `.claude/skills/reach-research-analyst` |
| Hawk | Watcher: weekly shop check, goal progress, listing fixes. **Already on autopilot**: scheduled task "Hawk: weekly Etsy shop check", Mondays 7:43 PM ET | Scheduled-task prompt (claude.ai project docs `hawk/`) |
| Mack | Manager: routes approvals, daily brief. **Already on autopilot**: "Daily brief" scheduled task, 8:52 AM ET | Scheduled-task prompt |
| Penny | Listings and prices | `.claude/skills/penny-listings-pricing` |
| Bob | Product design and production | `.claude/skills/bob-design-production` |

Subagent definitions are in `.claude/agents/`. Research lives in `research/`, listing copy in `listings/`.

## Printify: one new listing a day

- **Goal (owner, Nov 8, 2026): one new Printify product listing per day.** Playbook: `docs/printify-playbook.md`. Backlog: `listings/printify/backlog.md`. Log: `listings/printify/log.md`.
- Printify shop id **29591075** (Etsy). The API token is a network secret on the etsyshop-main environment (send `Authorization: Bearer proxy-injected`). As of Nov 8 it has 8 products: 4 golf prints (bp 282 and 284, provider 99) and 4 Big Brother/Sister tees (kids bp 157/provider 29 at $19.99; toddler bp 580/provider 39 at $21.99).
- Bob creates a draft each day. The owner approves on HQ, and the next run publishes it through the Printify API. The Etsy listing fee ($0.20) is the only cost; no samples or upgrades.

## Autopilot (scheduled tasks, all ET) and the no-cost rule

| Agent | Run | Schedule |
|---|---|---|
| Archie | Content and calendar check | Daily 7:17 AM |
| Mack | Daily brief (created in claude.ai) | Daily 8:52 AM |
| Shout | Weekly social plan | Sundays 2:23 PM |
| Hawk | Weekly shop check (created in claude.ai) | Mondays 7:43 PM |
| Reach | Weekly research brief | Tuesdays 1:37 PM |
| Penny | Weekly listings and price check | Wednesdays 3:41 PM |
| Bob | **Daily Printify drop** (plus weekly listing-image work on Thursdays) | Daily 1:13 PM |

- **No new spending** (owner, Nov 8, 2026): no ads, boosts, paid upgrades, trials, samples or purchases. The only allowed cost is Etsy listing fees, and the owner publishes listings. Shout schedules only with the owner's tap (review queue or drafts). When Metricool's free slots run out, posts become hand-post packs.
- The five runs created Nov 8 have **no connectors yet**. The owner adds Metricool and Dropbox in claude.ai → Scheduled tasks. Until then those runs skip Metricool and Dropbox work and note it.
- Runs share the branch `claude/focused-dirac-hd5erf`. Always `git pull --rebase` before pushing.

## Escalation policy (all agents)

Agents solve problems themselves first: re-read the memory files, check every reachable source, ask another agent, or use a safe default the house rules allow. They escalate to the owner only for things only the owner can do (Etsy account, money, credentials, product photos), approvals the house rules require, safety or permission blocks (never worked around), or reversing an owner decision. Escalations go in one message: what was tried, the specific ask, and a recommended option. The full policy is in `agents/Agent-roster.md`.

## Social accounts (all through Metricool)

- Metricool brand `milestoneandmeaning`, **brandId 7837631**, timezone America/New_York.
- Instagram `@milestoneandmeaning`, TikTok `@milestone.and.mea`, Pinterest `MilestoneAndMeaning`, Facebook page id 1421214861075289.
- Scheduling media must be at a public URL; Metricool copies it to static.metricool.com when the post is created. This repo is **public** (since Nov 7, 2026), so use `https://raw.githubusercontent.com/bistanygreg-jpg/etsyshop-main/<commit-sha>/<path>`. Push first, and pin to a commit SHA rather than a branch. Everything committed here is public, so never commit secrets or customer data.
- Cadence (as of Nov 7, 2026): something posts nightly at 8pm ET through Nov 17, plus the 7 trend carousels at 12pm ET on Nov 9, 11, 13, 15, 17, 19 and 21 (IG + FB + TikTok), plus a TikTok-only shirt and golf-poster series at 6pm ET on Nov 10, 14, 16, 18, 20 and 22 (`social/tiktok/SHOUT_shirts-golf-tiktok_campaign.md`). The account's best TikTok times are 10am and 6pm ET. Pinterest pins link to the Etsy listings. IG/TikTok captions say "link in bio" or "Find us on Etsy: MilestoneAndMeaning".

## House rules for content

- Designs are made with AI tools. Keep the disclosure: "AI design tools were used in creating this design" on pins, `isAiGenerated` on IG/TikTok, "Art created with AI tools" on posters.
- Use only real facts and numbers. No made-up sales counts, reviews or backstory.
- Use "link in bio" CTAs. Comment-keyword CTAs ("comment WORD for the link") only work once an auto-DM tool such as ManyChat is set up, and it isn't yet.
- Golf posters: "Not affiliated with any club or tour."
- **Shirt and poster photos = Printify mockups.** Every Printify product has real mockups on `images.printify.com` (allowed in the environment). Use those; never invent mockups.
- Don't publish or schedule to Metricool without the owner's go-ahead.

## Brand look

- Listing mockups: cream background `#EBE2D1`, paper `#FBF6EC`, cranberry `#8D1B1B`, forest green `#204D39`, gold accents `#C9A24A`.
- Header type is a rounded geometric sans (we use **Poppins**). Product pages use a holiday script with holly accents.
- Shared CSS: `social/carousel-trends/src/brand.css`.

## Repo map

- `social/assets/metricool/`: original post images and videos downloaded from Metricool (named by Metricool file id). `social/assets/crops/`: product-mockup crops.
- `social/carousel-trends/`: 7 trend carousels. `src/*.html` are the sources and `src/img/` holds the processed product images. Re-render with `node social/carousel-trends/src/render.js [name]` (uses the preinstalled Playwright). Output goes to `<name>/slide-N.png` at 1080x1350. `SHOUT_trend-carousels_campaign.md` has the captions, schedule and metrics.
- `social/tiktok/`: TikTok photo-mode slideshows (1080x1920). The copy is in `src/build.py` and they render with `src/render.js`.
- `agents/Agent-roster.md`: agents (Shout, Archie, Bob, Penny, Hawk), the escalation policy, and the campaign and activity logs.
- `research/`: Reach's weekly briefs plus `product-ideas.md`, `pricing-benchmarks.md` and `growth-playbook.md`.
- `listings/`: Penny's paste-ready listing copy, one file per product.
- `agents/content-inventory.md`: Archie's inventory of every asset by product, plus calendar findings.
- `.claude/skills/archie-content-manager/SKILL.md`: Archie's instructions.
- `docs/conversation-log.md`: running log of every working session.

## Dropbox (connector)

- The social media folder is **`/Milestone & Meaning – Social`** (ns path `ns:32471771//Milestone & Meaning – Social`). It has subfolders:
  - `nice-list-kit/` and `christmas-eve-mega-bundle/`: IG carousel slides, pins, IG story, a vertical reel, contact sheets, plus a `tiktok/` subfolder of photos and short mp4s
  - `2026-Christmas/`: `week-01_Nov04-10`, `week-02_Nov11-17`, `social-batch-01` and `social-batch-02`, with dated post images and videos
  - `profile-assets/`: profile pictures, Facebook covers, IG highlight covers, Pinterest board covers
- Shirt and poster photos go to `shirts-and-posters/`, filled through a Dropbox upload link the owner has (created Nov 8, 2026, open, no deadline). Never commit that link here, because the repo is public. Check that folder before building any shirt or poster content.
- Apart from that folder, it holds only Christmas printable content. There's nothing for the shirts or the golf posters. The rest of the Dropbox account is personal and old work files, so stay inside this folder.

## Environment notes

- Cloud environment **etsyshop-main** (personal) allows `static.metricool.com`, `i.etsystatic.com` and `www.etsy.com`, so sessions can download Metricool media and Etsy listing photos. The Default environment can't reach those hosts.
- Metricool media URL pattern: `https://static.metricool.com/planner/<YYYYMM>/7837631-file-<id>.<ext>`.
