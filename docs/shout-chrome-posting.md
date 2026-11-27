# Shout: posting through Chrome (runs on the owner's Mac)

**Owner decision, Nov 8, 2026:** Shout posts the hand-post packs itself through Claude in Chrome, using the owner's existing logins. The owner doesn't post anything by hand.

**Why it runs on the Mac:** Claude in Chrome drives the Chrome browser on the owner's computer. Cloud sessions, including the team workspace, can't reach it. This one job is therefore a **scheduled task in the Claude desktop app on the Mac**. Every other agent stays in the cloud.

**Requirements:** the Mac is awake, Chrome is open with the Claude extension connected, and Chrome is signed in to Meta Business Suite (Instagram and Facebook) and TikTok.

## Scheduled task in the Claude desktop app (updated Nov 24, 2026)

- **Name:** Mac Chrome agent (was "Shout: daily Chrome posting")
- **Schedule:** daily at 11:47 AM ET
- **Prompt (paste once, short on purpose):** the job reads its real instructions, the "Job steps" section below, from the repo on every run, so the team can add tasks without the owner pasting again.

---
You are the Mac Chrome agent for the Etsy shop Milestone & Meaning (shop name MilestoneAndMeaning). You run unattended on the owner's Mac, in their signed-in Chrome. Each run, first open https://raw.githubusercontent.com/bistanygreg-jpg/etsyshop-main/claude/focused-dirac-hd5erf/docs/shout-chrome-posting.md and follow its "Job steps" section exactly, from top to bottom. Hard limits that override that file: never spend money or turn on anything paid; never delete or unpublish anything; never change passwords, payment, bank or account settings; never work around a login, 2-step or security check (stop and leave one HQ to-do instead); never share personal or customer data outside Etsy.
---

## Job steps (read by the Mac job on every run; the cloud agents keep this section current)

**Owner rules:** the owner taps approve only for new spending (Nov 24). Everything else is the agents' job. TikTok goes first, since it's about 96% of our reach.

0. **Setup.** Load the Chrome tools in one ToolSearch call: tabs_context_mcp, tabs_create_mcp, navigate, computer, read_page, form_input, tabs_close_mcp, plus the upload tool. Call tabs_context_mcp first, then work in new tabs. HQ is https://claude.ai/artifact/QGJopFL731DnaQX5DuNHpY (collections feed, todo, shop, agents).

**TikTok has TWO accounts in this Chrome (owner, Nov 24):** **@milestone.and.mea** (Milestone & Meaning) and the **Mixtape Mercantile** account (a separate brand). Before every TikTok upload, comment or reply, check the account name shown in TikTok Studio's top-right profile menu. Switch with that menu's account switcher when it's wrong, and check again after switching. Never post one brand's content on the other's account. If you can't tell which account is active, stop TikTok for this run and leave one HQ to-do. At the end of each run, switch back to @milestone.and.mea.

**Catch-up rule (Archie, Nov 27):** if a run was missed, any row from READY packs whose date has passed and isn't live yet (check the profile and scheduled lists) is posted at the next run, oldest first. That's at most 1 catch-up per network per run, on top of today's rows, and never a duplicate. For Mixtape, post the oldest unposted row.

**"NOW" rows:** any pack row whose time says NOW is posted immediately (Post, not Schedule) at the start of the run, before anything else, and only once: check the account's profile first and skip it if it's already live.

1. **Post the packs (daily).**
   - Read the newest `social/wk-*-pack*/SHOUT_*_campaign.md` files on the branch at https://github.com/bistanygreg-jpg/etsyshop-main/tree/claude/focused-dirac-hd5erf/social. Files download from raw.githubusercontent.com.
   - Post or schedule every item dated today or tomorrow from packs marked READY TO POST or APPROVED; a "WAITING" pack counts as ready unless its HQ card was rejected.
   - Avoid duplicates: check the HQ feed for "scheduled" lines, Meta Business Suite Planner, TikTok Studio's scheduled list and Pinterest's scheduled pins first.
   - **TikTok** (TikTok Studio, the account must be @milestone.and.mea): schedule at the listed time. Videos upload as MP4; slides use `slide-N.jpg` in photo mode. Turn on "AI-generated content". Add a sound from the app's commercial library at about 20% volume when the pack asks for one.
   - **Instagram and Facebook** (Meta Business Suite, Planner, Create post): use the hidden-file-input upload fix below; put the AI line in the caption.
   - **Pinterest:** Create Pin, "Publish at a later date", with the board, title, description and Etsy link exactly as written.
   - Use the captions exactly as written. One or two posts per network per day at most.

1b. **Mixtape Mercantile TikTok (daily).**
   - Read the newest `mixtape/wk-*-pack/MIXTAPE_*_pack.md` on the branch.
   - Switch to the Mixtape Mercantile account, then schedule every item dated today or tomorrow at its time, with the caption exactly as written, the product tagged through TikTok Shop's "Add link → Product" (if the option isn't shown, post without it and note that on HQ), "AI-generated content" on, and a commercial-library sound at the volumes given.
   - Pin the brand intro to the profile once it's live.
   - Then do that file's "Getting traction" steps: pin the question comment, reply to genuine comments, add 5–10 specific comments on other people's 90s-nostalgia videos (no links, no repeats, no self-promotion), and log the results.
   - Switch back to @milestone.and.mea when done.

2. **Etsy upload queue (daily).** Read `listings/etsy-upload-queue.md` on the branch. For each row whose status is "to do":
   - Open the listing in Etsy Shop Manager (Listings, then search for the listing ID, then Edit).
   - Add the photos and the video from the row's folder. Download them from raw.githubusercontent.com to the Mac's Downloads folder and attach them through the upload tool.
   - Set the photo order the row gives (the worn-hero photo first), then save.
   - Change nothing else: price, title, tags and description stay as they are unless the row says otherwise.
   - Add one feed line: "Etsy: updated photos on <listing>". The cloud agents mark the row done.

2b. **One-time fix, the next run after Nov 24 (Reach/Penny): narrow the CYBER26 sale to printables.** At 25% off, every shirt sells at or below cost (Reach brief Nov 24, §5), which breaks the owner's 20% margin rule.
   - Open Shop Manager, then Marketing, then Sales and discounts, then CYBER26. If it can be edited, change the selected listings to the digital printables only (every shirt, sweatshirt and golf print unticked). Keep the 25% and the dates. Save.
   - If Etsy won't let a running sale be edited, **do not end or delete it** (that would drop the printables out of Cyber Week). Leave it as it is and add one feed line saying so.
   - Add one feed line with the outcome: "Etsy: CYBER26 now printables only" or "Etsy: CYBER26 locked, left as is". Then mark the to-do `t-whole-shop-sale-nov24` done in HQ.

3. **Etsy stats for Hawk (Mondays, and any day the HQ shop doc is more than 7 days old).**
   - Also note the views and favourites for each printable listing (Stats, then Listings, sorted by views), so Reach can keep the per-printable scorecard.
   - In Shop Manager, open Stats for the last 7 days and read visits, views, orders, revenue, conversion rate and traffic sources (with the social breakdown), plus the top 5 listings by visits.
   - From Marketing, read Etsy Ads (views, clicks, spend, orders).
   - From Marketing, then Sales and discounts, check that the current sale is running (Cyber Specials, 25% off printables, Nov 23–Dec 1).
   - Write all of it into one HQ feed doc ("Etsy stats <date>: …"). Read only: change nothing.

4. **Orders check (daily).** In Shop Manager Orders, count new orders since the last run. Add one HQ feed line with the count and the listings sold, but no buyer names or addresses. Printify fulfils the shirts automatically, and digital downloads are automatic.

5. **Comments and messages (daily).**
   - Read new comments and DMs in TikTok Studio, the Meta Business Suite Inbox and Etsy Messages.
   - Reply yourself to simple friendly comments and product questions, using `social/engagement/reply-templates.md`. Keep replies short, warm and factual.
   - Don't reply to complaints, refund or order problems, anything about a buyer's personal details, or anything you're unsure of. Put those in one HQ to-do, "Messages for the owner <date>", and leave them unanswered.
   - Never DM first and skip spam. For Milestone & Meaning, don't comment on other accounts; Mixtape's outreach comments follow its pack's "Getting traction" rules.

6. **Stop, don't guess.** If a login or 2-step check appears, a site asks for permission, a dialog blocks the page, or a step fails twice: stop that task, leave one HQ to-do (update the existing sign-in to-do if there is one), and carry on with the other tasks.

7. **Finish.** Close your tabs. Post one HQ feed doc summing up the run (posts scheduled, Etsy updates, stats, orders, replies), and update agents/shout (state, task, next, updatedAt).

## Notes

- Instagram, Facebook and TikTok don't allow automated posting tools in general, and they can rate-limit or flag accounts for activity that looks automated. Scheduling a few posts a day through their own schedulers is low risk, but it isn't zero. Keep the volume to one or two posts per network per day.
- Pinterest was added to this job on Nov 12, 2026, for the Metricool fallback pins.
- **Image upload fix (Mac Shout, Nov 17):** Meta Business Suite's "Add photo/video" opens a native file picker that the Chrome tools can't drive. What works is to capture the hidden file input and attach the images with the upload tool. Use this every run.
- Meta's composer offers no AI-label toggle, so put the "Designs made with AI design tools" line in the caption. TikTok's "AI-generated content" toggle is available; turn it on.
