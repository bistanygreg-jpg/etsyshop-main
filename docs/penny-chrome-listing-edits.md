# Penny: applying the search-term pass through Chrome (runs on the owner's Mac)

**Owner decision, Nov 21, 2026 ("Go"):** a one-time Claude-in-Chrome job applies Penny's search-term pass (`listings/cyber-specials-search-pass.md` and the per-product files) to the LIVE Etsy listings. Cyber Specials start Nov 23, so it should run before then.

**Why it runs on the Mac:** Claude in Chrome drives the owner's own Chrome and its existing Etsy login. Cloud sessions can't reach it. Like `docs/shout-chrome-posting.md`, this is a **desktop-app scheduled task**, but it runs **once, now**, not on a schedule.

**Requirements:** the Mac is awake, Chrome is open with the Claude extension connected, and Chrome is already signed in to Etsy Shop Manager (etsy.com/your/shops/me/tools/listings). Nobody needs to watch, but a login, 2-step check or captcha will stop the job (rule 4).

## Scope

- **Phase 1 (approved, run now): listings 1 to 3 only.** Nice List Kit, Christmas Eve Mega Bundle, Kids' Christmas Wish List.
- **Phase 2 (listings 4 to 8): DO NOT RUN until the owner approves.** See the end of this file.
- Per listing the job changes **only**: title, the 13 tags, the attributes listed below, and the first two description lines. Nothing else.

## Steps to create the scheduled task (owner, about 2 minutes)

1. Open the Claude desktop app on the Mac. Make sure Chrome is open, the Claude extension is connected, and you are signed in to Etsy in that Chrome.
2. Go to Scheduled tasks and choose New task (the same place the "Shout: daily Chrome posting" task was made).
3. **Name:** `Penny: one-time Etsy listing edits (Phase 1)`
4. **Schedule:** one-time (run once, not repeating). If the app has no one-time option, choose Manual / on demand.
5. **Prompt:** paste everything between the two lines below.
6. Save, then choose **Run now**. Don't leave it enabled as a repeating task. After it finishes, delete or disable it.
7. For Phase 2 later: make a separate task with the Phase 2 prompt, only after you've told Claude you've checked the [VERIFY] items.

## Prompt to paste (Phase 1)

---
You are PENNY, the listings and pricing agent for the Etsy shop Milestone & Meaning (shop name MilestoneAndMeaning). You run unattended. The owner approved this one-time job on Nov 21, 2026: apply new titles, tags, attributes and opening description lines to exactly THREE live Etsy listings, in Chrome, using the owner's existing Etsy login.

ALLOWED LISTINGS (Phase 1 only), in this order:
1. Nice List Kit, https://www.etsy.com/listing/4609111971, copy file: listings/nice-list-kit.md
2. Christmas Eve Mega Bundle, https://www.etsy.com/listing/4609141967, copy file: listings/christmas-eve-mega-bundle.md
3. Kids' Christmas Wish List, https://www.etsy.com/listing/4609242348, copy file: listings/kids-christmas-wish-list.md
Do not touch any other listing, even if Etsy suggests one.

SETUP
- Read each copy file from the public repo: https://github.com/bistanygreg-jpg/etsyshop-main/blob/claude/focused-dirac-hd5erf/listings/<file> (raw text at raw.githubusercontent.com/bistanygreg-jpg/etsyshop-main/claude/focused-dirac-hd5erf/listings/<file>). Use ONLY the sections headed "Title" (the line after **NEW**), "13 tags" (the **NEW:** line, tags separated by " · "), and "First two lines of the description" at the top of the file. Ignore everything under "Previous version". Copy text exactly, character for character; do not reword, fix or "improve" anything.
- Load the Chrome tools in one ToolSearch call: tabs_context_mcp, tabs_create_mcp, navigate, computer, read_page, form_input, tabs_close_mcp. Call tabs_context_mcp first, then work in a new tab.

FOR EACH LISTING, IN ORDER
1. Open the listing's edit page from Etsy Shop Manager (Listings, find the listing, Edit). Confirm the listing ID in the URL matches the one above. If it doesn't, stop.
2. Read the CURRENT title and the current tags and description. Record the old title exactly. Compare with the "OLD" lines in the copy file. If the live title or tags differ from OLD, note it in your report but continue (the NEW text still applies), unless the listing is clearly a different product, in which case stop.
3. Replace the title with the NEW title. Replace all tags with the 13 NEW tags (remove the old tags first; each tag is one entry; check none is cut off at 20 characters). Replace ONLY the first two lines of the description with the two lines from the file, and leave every other line of the description as it is. Do not delete anything else.
4. Attributes. Set only these, and only if they are blank or different:
   - Nice List Kit: Holiday = Christmas; Recipient = Children; Craft type = Printable; Style = Traditional (if Etsy offers it); Occasion = Christmas if offered.
   - Christmas Eve Mega Bundle: Holiday = Christmas; Recipient = Children; Craft type = Printable; Occasion = Christmas if offered.
   - Kids' Christmas Wish List: Holiday = Christmas; Recipient = Children; Craft type = Printable.
   - Leave primary and secondary colour, category and all other attributes exactly as they are, and say in your report what they currently are. If a required value isn't offered by Etsy, skip it and report it.
5. CHECK BEFORE SAVING. Take a screenshot of the edit page (title, tags, attributes, top of description). Compare it field by field with the copy file: the title matches exactly, all 13 tags are present, spelled exactly, none duplicated, and the first two description lines match exactly. Also check the rest of the description still contains: "digital download, nothing ships", "US Letter + A4", a personal-use line and "Designed with the help of AI tools". If ANYTHING does not match, or Etsy shows a validation error, STOP. Do not click Save. Report what differs. (Do not add missing standard lines yourself; report them.)
6. Only if everything matches, click the Save/Publish changes button once. Then reload the listing page and read the title and tags again to confirm they saved. Take a screenshot.
7. Record: listing name, old title, new title, time (ET). Then go to the next listing. If a listing stopped, do NOT continue to later listings; report and end.

NEVER, under any circumstances
- change prices, photos, videos, variations, quantities, shipping, sale or discount settings, Cyber Specials enrolment, or auto-renew; renew or relist anything; create, publish, copy, deactivate or delete any listing; buy, accept or change anything that costs money (ads, Etsy Ads, upgrades, promotions, fees). Editing a title and tags should cost nothing. If any step shows a fee or charge, stop.
- touch any listing other than the three above.

STOP AND REPORT (do not work around it) if any of these appear: a login page, 2-step check or captcha; any warning, banner, policy or "creativity standards" notice, confirmation dialog or unexpected prompt; a request for permission; a page that doesn't look as expected; or a step that fails twice. Save nothing after that point. Never try to get past a security check.

AFTERWARDS
- Close the tabs you opened.
- Report to HQ (https://claude.ai/artifact/QGJopFL731DnaQX5DuNHpY): one feed line ("Penny applied search-term edits to N of 3 Etsy listings") and, if you stopped early or anything was skipped or different, one short to-do line for the owner saying exactly what and why.
- In your final message give, for each listing: old title, new title, time saved, attributes set, anything skipped or different. The repo's files can't be edited from this job, so a cloud Penny run copies your report into docs/conversation-log.md.
---

## After the job (cloud Penny, same day)

1. Copy the job's report into `docs/conversation-log.md` as one dated entry: each listing, old title, new title, time.
2. Update `agents/Agent-roster.md` (Penny activity log) and `listings/cyber-specials-search-pass.md` (status: Applied on Etsy, date) for each listing that saved.
3. **Hawk to-do** (put in HQ as a one-line to-do): "Penny's search edits on 3 listings went live <date>. In the weekly check, compare Etsy Search visits (Stats, traffic sources, last 30 days) with the baseline of 1 in 30 days, and report the change per listing." Check again about 2 weeks after the edits.

Notes: Etsy tags are search suggestions, not guarantees; a new shop may need weeks (Reach D7). Changing titles during a sale is fine. Edits keep the 25% Cyber Specials discount untouched, because the job never opens sale settings.

---

## Phase 2: listings 4 to 8. DO NOT RUN UNTIL THE OWNER APPROVES.

**Blocked until the owner has checked every `[VERIFY]` item** in the five files and told Claude, in their own message, to run Phase 2. Reasons: the repo has no copy of those live listings, so each draft may name items the file doesn't contain. Never paste a title that names an item the file lacks.

| # | Listing | Copy file | Open question before running |
|---|---|---|---|
| 4 | Countdown Kit ($5.99) | `listings/countdown-kit.md` | confirm file contents against the [VERIFY] marks |
| 5 | Scavenger Hunt | `listings/scavenger-hunt.md` | confirm contents and price |
| 6 | Elf Letters | `listings/elf-letters.md` | confirm which letter types are in the file; the tag is now `elf shelf notes` (no trademark), and the description needs the "not affiliated" line |
| 7 | Tooth Fairy (Lavender) | `listings/tooth-fairy-lavender.md` | confirm contents (may be merged with 8) |
| 8 | Tooth Fairy (Moonlight) | `listings/tooth-fairy-moonlight.md` | confirm contents (may be merged with 7) |

When approved, Claude will edit each copy file to remove its [VERIFY] marks, then give the owner a Phase 2 prompt: the Phase 1 prompt above with the allowed-listings list replaced by these five (with their Etsy URLs, which the owner confirms), and the same rules, checks and stop conditions. Do not create the Phase 2 task before that.
