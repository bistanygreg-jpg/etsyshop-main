# Agent roster: Milestone & Meaning

| Agent | Owns | How to run it |
|---|---|---|
| **Shout** | **All social promotion:** content creation, captions, calendars and Metricool scheduling for every product (printables, big sibling shirts, golf posters), across Pinterest, Instagram, Facebook and TikTok | Skill `anthropic-skills:shout-etsy-social-promoter` |
| **Archie** | **Content management:** content library and inventory, intake of new uploads, Metricool calendar hygiene, naming and versioning, shop memory upkeep (CLAUDE.md, roster, log), public-repo safety | Project skill `archie-content-manager` (`.claude/skills/archie-content-manager/SKILL.md`) |
| Bob | Product page renders and video (Shout's inputs) | n/a |
| Penny | Listing titles, prices and keywords (Shout's inputs) | n/a |
| Hawk | Metrics and analytics (receives Shout's "metrics to watch") | n/a |

## Escalation policy (all agents)

Every agent tries to solve a problem on its own before bringing it to the owner.

**1. Solve it yourself first.** Before escalating, try at least two reasonable approaches:
- Re-read CLAUDE.md, this roster, `agents/content-inventory.md` and the conversation log. The answer is often already recorded.
- Look in every source you can reach: the repo, the Dropbox social folder, Metricool (scheduled posts, analytics, best times) and web search.
- Ask another agent. Archie finds or fixes assets, Shout handles anything about posting, Hawk handles numbers, Penny handles listing copy and prices, and Bob handles renders.
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
| Shirts and golf posters, product round | Big sibling shirts, golf posters | TikTok (+ IG, Pinterest) | When photos arrive | **Blocked:** needs real photos in Dropbox `shirts-and-posters/` | n/a |

## Archie activity log

| Date | What Archie did |
|---|---|
| 2026-11-08 | Built `agents/content-inventory.md`. Checked the calendar: added missing alt text to 5 humor and product posts (Nov 8–12; Metricool gave them new ids). Flagged 4 stale drafts dated in the past and 6 humor posts with fewer than 8 IG hashtags (passed to Shout). |

## Open items for Shout

1. **Etsy Share & Save links** (Shop Manager → Marketing → Share & Save) for every listing. Sales from these earn a fee credit. Put them in the Instagram and TikTok bio links and the Pinterest pin links. The owner has to generate them, because Claude has no Etsy access.
2. Listing links for the shirts and golf posters, so Pinterest pins can link straight to them.
3. Real product photos of the shirts and posters.
