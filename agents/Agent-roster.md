# Agent roster: Milestone & Meaning

| Agent | Owns | How to run it |
|---|---|---|
| **Shout** | **All social promotion:** content creation, captions, calendars and Metricool scheduling for every product (printables, big sibling shirts, golf posters), across Pinterest, Instagram, Facebook and TikTok | Skill `anthropic-skills:shout-etsy-social-promoter` |
| **Archie** | **Content management:** content library and inventory, intake of new uploads, Metricool calendar hygiene, naming and versioning, shop memory upkeep (CLAUDE.md, roster, log), public-repo safety | Project skill `archie-content-manager` (`.claude/skills/archie-content-manager/SKILL.md`) |
| **Reach** | **All research and analysis:** product ideas, pricing benchmarks, Etsy SEO and visibility, promotion tactics, and weekly performance analysis. Works with **Hawk**, the existing watcher agent (weekly scheduled shop check), who supplies the numbers. | Project skill `reach-research-analyst` |
| **Hawk** | Watcher: weekly shop check and goal progress. On autopilot, Mondays 7:43 PM ET, in the team workspace since Nov 10. Writes `hawk/Hawk-log.md` and the HQ stats. | Scheduled task delivered to the workspace |
| **Mack** | Manager: daily brief and routing approvals. Already on autopilot, daily 8:52 AM ET. | Scheduled task |
| **Penny** | Listings and pricing: titles, tags, descriptions, attributes, and the CLAUDE.md price table. Paste-ready changes until there's Etsy access. | Project skill `penny-listings-pricing` |
| **Bob** | Design and production: printables (fillable PDFs), 300-dpi renders, listing images, product videos. Sellable files never go in the public repo. | Project skill `bob-design-production` |

All seven agents run on autopilot as scheduled tasks; the times are in CLAUDE.md. Each agent also has a subagent file in `.claude/agents/<name>.md`, so it can run unattended (for example as a scheduled task).

## Escalation policy (all agents)

Every agent tries to solve a problem on its own before bringing it to the owner.

**1. Solve it yourself first.** Before escalating, try at least two reasonable approaches:
- Re-read CLAUDE.md, this roster, `agents/content-inventory.md` and the conversation log. The answer is often already recorded.
- Look in every source you can reach: the repo, the Dropbox social folder, Metricool (scheduled posts, analytics, best times) and web search.
- Ask another agent. Archie finds or fixes assets, Shout handles anything about posting, Reach handles research and numbers, Penny handles listing copy and prices, and Bob handles renders.
- Use a safe default the house rules allow, and note it in the log. For example: pick a posting time from Metricool's best-time data, write alt text yourself, or trim hashtags to the platform limit.

**2. Escalate only when the owner is truly needed:**
- something only the owner can do: Etsy account actions such as prices, listings or Share & Save links; money; credentials; physical product photos
- a house rule requires the owner's approval: a new campaign's first schedule, deleting or unpublishing posts, making something public
- a safety or permission block. Never work around a refusal, bot check or permission denial. Report it instead.
- the fix would change a decision the owner already made

**3. When you escalate, send one short message** with:
- what you tried
- the specific thing you need
- your recommended option, so the owner can just say "yes"

Batch several asks into one message. Don't send a drip of questions.

**4. Log it.** Record what you solved yourself and what you escalated in `docs/conversation-log.md`.

## Shout campaign log

| Campaign | Products | Channels | Dates | Status | Doc |
|---|---|---|---|---|---|
| Launch posts (Metricool batches 01/02, weeks 1–2) | Nice List Kit, Mega Bundle, Wish List | Pinterest, IG, FB, TikTok | Nov 4–17, 2026 | Scheduled or published (made before Shout took ownership) | Dropbox `/Milestone & Meaning – Social/2026-Christmas/` |
| Viral carousel trends (7) | Mega Bundle, Nice List Kit, shop intro | IG, FB, TikTok | Nov 9–21, 2026, 12pm ET | Scheduled | `social/carousel-trends/SHOUT_trend-carousels_campaign.md` |
| Shirts and golf posters, TikTok series (6) | Big sibling shirts, golf posters | TikTok | Nov 10–22, 2026, 6pm ET | Scheduled | `social/tiktok/SHOUT_shirts-golf-tiktok_campaign.md` |
| Shirts and golf posters, product round | Big sibling shirts, golf posters | TikTok (+ IG, Pinterest) | Nov 9–22 | Unblocked Nov 8: uses real Printify mockups (Dropbox folder still empty); now inside the two hand-post packs below | n/a |
| Hand-post pack, week of Nov 9–15 (9 posts) | Golf prints, Wish List, big sibling shirts, sale reminder | IG, FB, TikTok (by hand) | Nov 9–15, 2026 | Rebuilt and pushed Nov 8; owner approved (HQ `ap-shout-pack-nov9`) | `social/wk-nov9-pack/SHOUT_week-nov9_pack_campaign.md` |
| Hand-post pack, week of Nov 16–22 (9 posts) | Mega Bundle and Nice List sale, last day, shirts (+ Big Cousin if live), golf prints | IG, FB, TikTok (by hand) | Nov 16–22, 2026 | Rebuilt and pushed Nov 8; owner approved (HQ `ap-shout-pack-nov16`) | `social/wk-nov16-pack/SHOUT_week-nov16_pack_campaign.md` |

## Archie activity log

| Date | What Archie did |
|---|---|
| 2026-11-08 | Built `agents/content-inventory.md`. Checked the calendar: added missing alt text to 5 humor and product posts (Nov 8–12; Metricool gave them new ids). Flagged 4 stale drafts dated in the past and 6 humor posts with fewer than 8 IG hashtags (passed to Shout). |
| 2026-11-09 | Daily run: no new Dropbox uploads; no failed Metricool posts; cap forecast and ranked fallback recorded in the inventory; 6 stale drafts flagged; Etsy links for shirts and golf prints added to CLAUDE.md. |
| 2026-11-10 | Found TikTok rejecting PNG photo posts (the Nov 9 carousel failed on TikTok). Converted all 12 upcoming TikTok posts to JPEG and recorded the new ids. Added JPEG copies to the packs. Flagged a duplicate Nov 9 carousel on Instagram and Facebook. |
| 2026-11-11 | Daily run: no uploads, no failures; the JPEG fix confirmed (the Nov 10 TikTok published). About 19 November posts published, so the cap may hit today or tomorrow; watching. |
| 2026-11-12 | Metricool's free limit hit on Nov 11: the 8 PM posts failed. Moved the 18 remaining November posts into a ranked fallback pack for Shout's Chrome job (`social/wk-nov12-fallback-pack/`), added Pinterest and an approval gate to the Chrome prompt, and made TikTok JPEGs. HQ card `ap-archie-metricool-fallback`. Synced CLAUDE.md with HQ. |

## Reach activity log

| Date | What Reach did |
|---|---|
| 2026-11-10 | Brief 2 (`research/2026-11-10_weekly-brief.md`): $0 and almost no social traffic (0 Pinterest outbound clicks), so Etsy search carries the season. Top ideas: Nice List family set, Grandpa/Aunt/Uncle tees, baby bodysuit. Backlog re-ranked. |
| 2026-11-08 | First brief (`research/2026-11-08_weekly-brief.md`); started the product-idea backlog, pricing benchmarks and growth playbook. Top ideas: Tooth Fairy Kit and Easter Bunny Kit. |

## Hawk activity log

| Date | What Hawk did |
|---|---|
| 2026-11-09 | Last claude.ai run: $0, 0 sales, 17 listings live. Summary copied to `hawk/Hawk-log.md` and HQ. |
| 2026-11-10 | Moved into the team workspace; the first workspace run is Mon Nov 16. |

## Penny activity log

| Date | What Penny did |
|---|---|
| 2026-11-11 | First weekly run: paste-ready listing files for the 3 core printables, shirt title fixes for Bob, pricing table synced to Printify, sale calendar (Dec 15–23 sale proposed). No caption price mismatches. |

## Bob activity log

| Date | What Bob did |
|---|---|
| 2026-11-08 | First daily Printify draft: Big Cousin kids tee (6af0cee97a7a4ea34b0b0fe3). |
| 2026-11-09 | Published the Big Cousin kids tee to Etsy (listing 4613415513); drafted the Big Cousin toddler tee (6af20dc1fdce7ca0fe081e2e), waiting for approval. |
| 2026-11-11 | Published the Nov 10 batch (Nice List kids tee, Grandma tee, Big Brother sweatshirt, kids Big Sister tee). Batch 2: Nice List adult and toddler tees, Big Sister sweatshirt. |
| 2026-11-10 | Published the toddler Big Cousin tee (listing 4614211984). First 3-a-day batch: Nice List kids tee, Grandma adult tee, Big Brother youth sweatshirt, on one HQ card. |
| 2026-11-12 | Published the Nov 11 batch (Nice List adult and toddler tees, Big Sister sweatshirt). Applied the 3 kids-tee title fixes. Batch 3 drafts: Grandpa tee, Cookie Taster kids tee, Big Brother toddler sweatshirt (new bp 1644). Made first-photo images for the Nice List Kit and the Mega Bundle. |

## Open items from Hawk's pipeline (Nov 9)

These printables are overdue or due soon in Hawk's goal plan. They need the owner's go-ahead before Bob builds them in full, and Reach should rank them in the next brief:
- all-sports awards pack (due Nov 8)
- Nice List Kit in 2 more colour themes (Nov 12)
- New Year's Eve kit (Nov 15)
- Winter Break kit (Nov 19)
- gift tags and thank-you notes (Nov 26)

Merging the two tooth fairy kits into one listing is an Etsy edit: Penny writes the copy, and the owner makes the change.

## Open items for Shout

1. **Etsy Share & Save links** (Shop Manager → Marketing → Share & Save) for every listing. Sales from these earn a fee credit. Put them in the Instagram and TikTok bio links and the Pinterest pin links. The owner has to generate them, because Claude has no Etsy access.
2. Listing links for the shirts and golf posters, so Pinterest pins can link straight to them.
3. Real product photos of the shirts and posters.
