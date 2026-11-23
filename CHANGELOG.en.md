# Changelog

*[Tiếng Việt](CHANGELOG.md) · **English***

NAOTA release history. Newest first.

## [1.60.4] - 2026-11-23
### Fixed
- **The display name NAOTA is now NAOSO everywhere users see it:** the interface, notifications, chat bubbles, exports, docs, the browser notification title and accessibility labels.
- **Technical names are unchanged** so existing data and settings keep working: `NAOTA_*` environment variables, the `Naota/` folder in the brain, `naota_*` tool names, and the startup entry name.

## [1.60.3] - 2026-11-23
### Fixed
- **The footer keeps your own name.** "by Lê Quý Đại" and the Zalo number are back instead of the old author line.

## [1.60.2] - 2026-11-23
### Fixed
- **The 3D office numbers bar shows proper labels.** It used to show raw keys like `office.st_today`.

## [1.60.1] - 2026-11-22
### Added
- **All of the newest NAOTA release (1.47 to 1.60) is merged into NAOSO.** Every feature from those versions is in NAOSO, including the mascot in the new logo shape.
### Fixed
- **The Update button pulls from the NAOSO repo.** Every place now uses one release address, so it no longer merges from another repo and reports a conflict.
- **Installs with a different git history are no longer stuck.** When git cannot merge, the app saves the old code to a `backup/` branch and syncs to the new release. Your data and keys stay as they are.
### Improved
- **The display name is NAOSO everywhere**, while your data, keys and the internal NAOTA technical names stay unchanged.

## [1.60.0] - 2026-11-22
### Improved
- **The mascot takes the NAOTA logo shape**: the old orange star becomes a rounded square in NAOTA yellow on the Tasks page, the mascot at the screen edge and the Give a star card. A device still on the default star switches after the update; anyone who picked another shape or colour keeps it. The star is still in Settings > Mascot.

## [1.59.0] - 2026-11-22
### Added
- **Naota can click and fill forms with a stored cookie** (needs the Playwright connection). Each card on the Cookies page has its own switch, and older cookies stay read-only until you turn it on. Customer chatbots never get the signed-in browser.
- **Naota can run read-only scripts (`naota_code`)** that chain read calls and return only the result, saving tokens. Isolated, at most 40 calls, off with `NAOTA_CODE_MODE=0`.
### Fixed
- **Background jobs no longer stall on steps only you can do** (listening, approving, a file too large for a tool). Those steps move to a **Left for you** section on the job card, with a ring.
- **Team steps and Kanban jobs retry on their own after a brief network drop.** A tool call with a source prefix no longer falls back to another account, and the Hostinger install file is smaller so hPanel does not refuse it.

## [1.58.0] - 2026-11-22
### Added
- **Block, Leave group and Delete right in a chat's Info panel**, like the "..." menu in the list. Leaving a Zalo group also deletes its chat from Naota, and a deleted chat no longer comes back by itself.
- **The bot can step aside when staff answer from the Zalo OA app or the Page inbox.** Put minutes in the "Step aside after you type" box and the bot stays quiet that long, then answers again. Off by default.
### Fixed
- **The personal Zalo bot no longer says "no information" after you typed by hand**, and choosing who a bot replies to now opens on direct messages.
- **Facebook Pages uses every connection that is on** and skips one that is off. Webhook instructions can be up to 5,000 characters, and `NAOTA_BOT_MAX_IMAGES` sets how many images a bot sends.

## [1.57.0] - 2026-11-22
### Improved
- **The chat box is one row, like Claude.** Only +, the text box, the mic and send stay inside. Model, Effort and the usage ring move under the box on the right; the pinned folder and GitHub repos sit on the left. The box also sits closer to the bottom of the screen.
### Fixed
- **A clear X to remove a repo**, on the chat box, in the picker and on the Teams page. A stray tap on a repo row no longer drops it, and a new pick no longer "jumps back" to the old repo.
- **The plan usage ring no longer stays red after switching models.** One model hitting its own limit no longer paints the whole plan red.
- **Long chat answers ring the phone again** when you are not looking at that chat.

## [1.56.0] - 2026-11-21
### Added
- **Connect Asana.** The Connections page has an Asana card on the official V2 MCP: Naota finds and reads tasks, projects and due dates, creates and updates tasks, and adds comments. Sign in from the dashboard; works on a VPS too.
- You create an Asana MCP app once (about 5 minutes); the card walks you through it. It starts at Read-only.
- **Two-way brain sync links through the signed-in GitHub account.** On the Self-learning page, press Connect GitHub, then Create a private repo or Pick an existing one. No token to make, no URL to paste.
- **Linking syncs right away and turns automatic sync on.** A second machine that picks the same repo pulls the brain down.
- **A pasted token keeps working as before,** with a button to move onto the signed-in account so the token never runs out.
- **The Account page has a "Forgot your current password?" line** right under Change password. On Windows and Mac it opens the install folder with the reset file selected, so a double-click is all it takes. On a VPS, Docker or Hostinger it shows the reset steps.
- **Mac gets `reset-auth.command`**, doing what `reset-auth.bat` does on Windows: clear the old password so you can set a new one.
- **Claude Code and Codex sessions are saved into Naota automatically.** Each finished turn, your prompt and the agent's final answer, appears in History as "From Claude Code: ..." or "From Codex: ...", and feeds self-learning.
- **Setup is one "yes".** Connect Claude Code or Codex to Naota Gate and it asks whether to turn on Naota Sync; say yes and it installs itself on that machine, no command to type and no token to copy.
- **No quota spent, nothing lost.** Naota runs no model for it, API keys are masked before saving, and turns wait and resend when Naota is off. Its token can only save chats, nothing else.
### Fixed
- **Asking Naota to fix Naota's own code no longer ends in "cannot write to vuongtex/naota" on a user's install.** Every install used to clone the official repo, edit it for a whole turn and only fail at the push. Now an install without write access clones and edits nothing: Naota writes the bug report and suggested fix and hands you a link to a prefilled issue for the developer. Read it, press Submit, no token or extra access needed.
- **Facebook cookie cards load pages again.** When a page is opened with a card from the Cookies page, Naota now sends the navigation headers a real browser sends (`Sec-Fetch-*`, `Accept`, `Upgrade-Insecure-Requests`). Before, Facebook answered 400 before it even read the cookies, so a live sign-in still showed "last load failed".
- **The reset file no longer reopens the first-run wizard** (models, channels and API keys stay), and on a Mac the old password no longer comes back at the next start.
### Improved
- The Auto and Sync images switches take effect at once, no Save needed.
- **The Plugins page is rebuilt in the Tasks page style.** A left column filters by status and source, All is one list sorted by name, and your own tools and Naota Store tools carry a tag.
- **Each row shows only the name, one line of description, the permission in plain words and a switch.** Tap a row for its commands, version and Remove. Remove asks first on the page and can be undone.
- **One "Add a tool" button gathers the three ways in:** Naota Store, asking Naota in chat, and a .zip file. The "Install from .zip" button still stands on its own beside it.
- **The browser and the offline listener moved to "Software on this machine"**, and their Remove button is no longer solid colored. On a phone the left column becomes a row of chips with a round + in the corner.

## [1.55.0] - 2026-11-21
### Improved
- **Messenger bots know which ad a customer came from.** A click-to-Messenger ad, an m.me link with a ref, or the chat box on a website: the bot sees the ad title or the link's ref, even when the customer reopens an old chat from an ad and types afterwards.
- **The bot watches videos customers send** (a few frames, plus the speech when a speech-to-text key is set) instead of only receiving a link it cannot open.
- **Stickers and the like button (👍) are understood as reactions**, no longer downloaded and described as a photo. On Instagram, the bot knows when a customer replies to the account's story or mentions it in theirs.
- **When Messenger rate limits or has a temporary send failure, the bot waits and sends again** instead of losing the answer.
- **Slack bots answer in the right thread.** Before, if someone wrote in another thread of the same channel while the bot was answering, the answer could land in that other thread. Every answer now goes back to the thread of its question.
- **Customers continuing an old thread are still answered after Naota restarts**, instead of being treated as people talking to each other.
- **The inbox shows Slack channel names** (for example #sales), and the bot reports being added to or removed from a channel, like Telegram. Text such as `a < b`, `@Kim` and links now reaches Naota exactly as typed.
- **When Slack rate limits, the bot waits and sends again** instead of losing the rest of the answer. Apps made from the older guide keep working; for channel names, paste the new manifest and reinstall the app (docs/en/29-slack-whatsapp.md).
- **In Telegram groups with topics, the bot answers in the topic the question was asked in** instead of piling everything into General. In a group the answer also quotes the message it answers, so a busy group can tell who it is for.
- **When a customer sends several photos at once, the bot answers once** and looks at the whole set, instead of answering in two or three separate turns.
- **The bot watches videos customers send** (a few frames, plus the speech when a speech-to-text key is set). Locations, contacts, stickers and polls also reach the bot; before, they were ignored.
- **When Telegram rate limits, the bot waits and sends again**, long answers split at paragraph breaks, and videos the bot sends play right in the chat.
- **WhatsApp bots read catalog orders.** Before, when a customer sent their cart the bot ignored the whole order. It now sees each product, the quantity, the total and the note. Shared contacts, WhatsApp Flow forms, and a location's name and address also reach the bot.
- **The bot knows which ad the customer came from** (click-to-WhatsApp ads) and which catalog product they are asking about, so it can answer to the point.
- **A paused bot, or one you have taken over, no longer shows the customer "typing..." and then says nothing.** The indicator only appears when the bot is really answering.
- **When WhatsApp rate limits, the bot waits and sends again**, videos go out playable in the chat, and an image too large for WhatsApp goes as a document instead of failing.

## [1.54.0] - 2026-11-21
### Added
- **Leave a Zalo group from the "..." menu of the Conversations page.** The chat history stays in Naota, under the Hidden filter.
- **Block is offered on every channel.** Messenger and Zalo block on the platform; other channels block in Naota: the bot goes quiet, the chat is hidden and new messages do not bring it back.
- **Unblock** for a blocked chat, which restores its previous reply mode.
### Fixed
- **Telegram bot chats (and every other bot channel) show again in the history of the partner the bot uses.** A bot whose record held another spelling of the same brain (a full path from an older version, a trailing slash, or a brain folder that moved) answered as usual, but its chats never reached the partner's History column. Naota now matches the brain the chats are actually stored in, and a partner name with Vietnamese accents matches even when its file was made on macOS.
- **The chat folder's red dot shows only for a chat that has finished and is unread.** A chat still working shows its spinner and no longer lights the folder, the "Ungrouped" row, its own row or the side menu. The chat open on screen is not counted either. The dot appears once a run ends and you have not looked at it.
- **Reopening a chat no longer shows an old copy silently.** When the server is slow or fails, the chat says it is showing the copy kept on this device, with a Retry button, instead of passing the old messages off as current.
- **A chat that never finishes loading now says so.** After a few seconds Naota says the chat is taking long and offers Retry.
- **One message that fails to draw no longer hides the ones after it.** It shows as plain text, the rest of the chat is complete, and the error is logged on the Health page.
- **Self-learned profiles no longer say "shop owner".** A profile now calls the person in the chat the subject and describes them, for example how they are addressed and how they refer to themselves, which fits bots that are not used for business too. Existing profiles change at their next update.
- **Connecting a second Zalo account no longer cuts the first one off.** Two reports on 19 and 20/11/2026: one bot per account in two brains, and right after the second account's QR was scanned the first bot's card read "Another session of this account keeps taking the Zalo connection" and the bot missed most messages, with no Zalo Web open anywhere.
- **Scanning the QR with an account that is already connected is refused right away**, instead of adding a second connection. The message names the connection that holds that account. To connect another account, open the Zalo app signed in as it and scan again.
- **The personal Zalo bot reads link cards.** A link someone sent (shown by Zalo as a card with a title and a picture) was filed as "other", so the bot skipped it, even when the sender tagged the bot. A link card is now read as a text message with its title, description and link.
- **The inbox and the history keep the link.** A link card no longer shows only the page's description: the link itself is there too, also for messages brought back from the history.
### Improved
- **"Ungrouped" gets a red dot too.** A chat in no project with an unread reply now puts a red dot on Ungrouped in the project picker, just like a project. Reading it or moving it into a project clears the dot.
- **Mark the open chat as unread.** The "..." menu of the chat you are reading now has this option too. The red dot shows at once and stays until you open another chat and come back, so unfinished work is easy to flag for later.

## [1.53.0] - 2026-11-20
### Added
- **Ask Naota in chat to run a script on a schedule.** For example "run check_shop.py every minute": the job runs the script directly with no model, so it is cheap and can run every minute.
- **A team job that waits for you can be answered, not only retried.** Press **Reply** next to Retry: "Go on" has the member do the step again with your answer, "Ask back" asks first and the job keeps waiting.
- Both the answer and the question show in the team chat under a quote of why the job stopped, so it reads clearly later.
- **A team's Info tab is short again, like Zalo.** Pictures, Files and Links each show only the newest few, with a **See all** button.
- **Storage view:** See all opens right in the side panel, with Pictures, Files and Links tabs, a search box that ignores accents, rows grouped by day and 20 per page.
- Each file shows a coloured tile with its extension, its size, and **File is gone** when it was deleted or moved. Teams with more than 200 files can now see all of them.
### Fixed
- **Codex model lists include newer installed versions.** Naota compares the Codex CLI on `PATH` with the version installed in the user directory so newer models are not missed.
- **Approving a workflow step on the Tasks page runs the workflow on, with no second approval request.** Each answer used to start the workflow again from step one, so it stopped at the same step again. Now "Approve", "ok" or "yes" carries on from that step. A change request still makes the workflow redo the work with it, as before.
- **Workflow jobs on the Tasks page wait for the plan to reset.** A step that hit an exhausted subscription used to retry at once, spend all three attempts in seconds and get stuck. The job now waits until the plan resets, and the wait does not count as an attempt.
- **Naota no longer gets stuck dropping connections because a stray copy holds its port.** On a Mac the copy launchd manages now stops a stray Naota and takes over; any other extra copy exits at once, before its startup runs.
- **Updates on a Mac always restart through launchd**, even when the launchd check fails, so they no longer leave a copy running outside launchd.
- **Naota Store is no longer blank when no password is set.** Installing a pack needs a real sign-in, so the Store was shut with no reason given. It now says a password is needed, with a Set a password button that opens the Account page.
### Improved
- **A scheduled job keeps its whole result, no longer cut at 2,000 characters.** The next run still reads only the start, but now knows it was cut.
- **A repeating job that skipped runs shows "N missed" on the Tasks page.** Before, when one run was late or long, the next ones were skipped and nobody knew.

## [1.52.0] - 2026-11-20
### Added
- **Page videos post with a cover image.** The video tool takes a .jpg/.png thumbnail and can post as a Reel. The result says plainly whether the cover was set.
- **Naota can message a customer straight from chat.** Ask "tell Lan size M is in stock" and it finds the chat in the inbox and sends through that chat's own Messenger Page, Instagram, Telegram or Zalo bot, as if you typed it in the inbox. Before, Naota said it had no Messenger send tool and asked you to paste the message yourself.
- **The message is recorded as yours, and that chat's bot keeps running.** Only you can ask for this: a customer talking to a bot can never read or message other customers, and Naota sees only the chats of the brain in use.
- **Links Naota sends on WhatsApp show a preview card** with the page's title and picture, instead of a bare link.
- **The bot learns from replies you confirm.** The draft box in the Inbox has a "Bot learns this" tick, on by default. Sending a reply that carries your order, or one you rewrote, saves it to the Agent's documents (file `tri-thuc-chatbot/<agent>.md`). Next time another customer asks the same thing, the bot answers the way you confirmed. Untick it for something about one customer only.
### Fixed
- **Bot cards show the Facebook Page name instead of its numeric ID.** A Page added by pasting its token only stored the ID, so the channel chip showed a string of digits. Each time the bot starts, Naota now keeps the Page's real name and the chip shows it. A label you set yourself (a short name) still wins, and the ID shows when you hover the chip.
- **The reply draft button follows the owner's order.** Type "schedule confirmed 8pm on the 21st and 22nd" and press draft: the reply gives that schedule instead of "I have no confirmed schedule yet" just because no document had it or the bot earlier said it was checking. The owner's order is the newest word, above the documents and the chat history, with no list of banned phrases. Rewrite follows it too.
### Improved
- **"AI draft" is now "Naota draft"** on the composer button, the mode above the chat and the lines of the draft.

## [1.51.0] - 2026-11-20
### Added
- **Chat draws math formulas.** Formulas written as `$...$`, `$$...$$`, `\(...\)` or `\[...\]` now show as real fractions, roots and powers instead of raw code. KaTeX loads only the first time a formula appears; offline, the source text still shows. Money like "$5 and $10" is left alone.
- **A link that opens one task.** An address like `#task=<id>` opens the Tasks page and then that item: one of your own tasks (`m:`), a reminder (`r:`) or a job Naota does (`k:`). An outside page such as a home-made dashboard can lead straight to a task instead of only to the Tasks page.
### Fixed
- **Calling `naota_team` no longer says "does not exist" when the hub runs in lazy mode.** With many tools the hub hides most behind its search tool, but assistants call them by name and got an error. A call by name now reaches the right tool, through the same permission layer. The quick reminder cancel works again in lazy mode too.
- **/goal and /plan work at the end or in the middle of a message.** They used to work only at the start, so "...do it for me /goal" went out as a plain chat. The rest of the text becomes the goal.
- **Skills, agents and workflows installed mid-conversation can be called with "/" mid-sentence right away.** The page reloads its list before sending when it meets an unknown name, instead of treating it as plain text.
- **Agent and workflow names work without the prefix.** "/seo-pro" opens the seo-pro agent, same as "/agent-seo-pro".
- **Punctuation right after a command no longer hides it.** "/viet-email," and "/goal." are still recognized.
- **Zooming a chat image no longer pushes it to the left.** At actual size, a picture smaller than the screen stays centered, and a larger one opens at the spot you clicked.
### Improved
- **A much quieter bell.** Answers in chats, partner chats and teams no longer go to the bell. A **red dot** on Chat, Partners and Team in the menu shows them instead, like the dot already on each chat.
- **Scheduled jobs no longer ring on every run.** The result still reaches its chat or Telegram; the bell rings only when the job fails for good, or when the run itself finds something you must act on.
- **Readable notice titles.** Each run writes a short headline about its result instead of "Checking...", and the card no longer repeats the title below it.
- **Unread chats move to the top of the history.** Every chat with a red dot now sits in an **Unread** group right under Pinned, even an old one that used to be on a later page. Once read, it goes back to its place by date.
- **Typing while Naota works turns the Stop button into Send** in the same spot, saving room. Empty the box and Stop comes back.
- **The Learned and Documents tabs now show 20 items a page.** A long list gets a search box (ignores Vietnamese marks) and the Add button sits at the top, so adding never means scrolling to the end.
- **Learned notes are easier to scan.** Filter by Fact, Decision or Term; each kind has its own colour; your own notes carry an orange bar on the left.
- **Edit notes, lessons and document descriptions in a roomy box.** It replaces the browser's one-line prompt: the whole text shows, with a character count, the note type, and Ctrl+Enter to save. On a phone it slides up from the bottom.
- **Naota finds the right tool far more often when many sources are connected.** Everyday requests such as "today's POS revenue", "Zalo message history" or "Google Ads cost" now reach the right tool, even when tool descriptions are in English. On 55 real test requests, hits rose from 20 to 55.
- **Naming a source lists its tools**, and several accounts of one kind (three POS shops, two Zalo accounts) share one line instead of crowding out other tools.
- **Calling a tool without its source prefix or with a typo still works** when only one tool matches; with several matches Naota names them to pick from. Search results are also shorter, so tokens stay low.

## [1.50.0] - 2026-11-19
### Added
- **Bots read the files staff send customers on Zalo OA and Fanpage.** A PDF, Word or Excel quote, or a photo, sent from the OA app or the Page inbox now shows in the Inbox (labelled Staff) and the bot knows what it says when the customer asks about it. Photos are read by a connected brain that can see.
- **Bots read the PDF, Word and Excel files customers send**, instead of only knowing "there is a file".
- **The Partners page has a Learned tab for each assistant.** The top bar button now reads "Documents & Learned". The new tab lists what the assistant worked out while working, exactly the lessons it uses, with where each applies (private chat, a team, everywhere). Edit, delete or add a lesson right there, like a project's Learned tab.
- A lesson you add is used everywhere. A lesson you edit becomes yours and is never dropped when the list is full. Delete one and the assistant stops using it and does not learn those exact words again.
- **Naota Store has an All tab.** It comes first, puts every assistant, skill, workflow, tool and connector in one grid, and the Store opens on it. Its search box covers the whole Store, and each card says which kind it is.
- **A search that finds nothing in one tab offers to search All.** The button shows how many items match in the other tabs and keeps the words you typed.
### Fixed
- **An assistant's Jobs tab records each run it started on its own.** The Auto block could say "Worked on its own 1 times today" while the Jobs tab stayed empty, because the tab only read goals, team jobs, chat jobs and workflow runs. Each look around or self-review is now a card under the Auto source, with what it ended in: the work it did, a message to you, a job it proposed, or nothing that needed doing. Today's number and the cards always agree because both read the same ledger.
- **Waiting icons on the Chatbot page spin again.** The "AI is writing..." button, the draft's Send button, the mic while transcribing and the customer profile card used to stand still.
- **Playwright no longer says "browser not installed" right after Naota downloaded one.** Naota now hands Playwright the exact browser file it downloaded, so the two can run on different versions. A browser you chose yourself is left alone.
- **The repository picker in a project and a team is no longer cut off.** The "Selected" section used to show as a thin strip, and the list under it could not scroll to the last repositories. Every row now shows in full and the list scrolls, in the documents of a project or an assistant, the create-team box and the team chat.
- **A Store pack can be installed in several brains.** A pack installed in one brain used to show "Installed" in another brain with only Turn off and Uninstall, so its assistants and skills could never reach that brain. The card now offers "Install in this brain". Updating the pack brings every brain that has it to the new version, keeping what you edited. Uninstalling removes it from every brain, and the confirmation names each one.
- **The Chatbot group picker no longer shows bare ids.** A ticked group hidden by the search box, or older than the 80 latest chats, used to show as a long number. Every group now keeps its real name from the inbox, and a group with no known name reads "Group …" with the end of its id.
### Improved
- **One step to turn it on:** for Zalo OA, enable the `oa_send_text`, `oa_send_image` and `oa_send_file` events in the app's Webhook section. For a Fanpage, click **Repair** on the checklist so Naota turns on `message_echoes`.
- In the documents drawer of the Partners page the tabs sit above the "Of the assistant / Only this chat" switch, since that switch only belongs to the Documents tab.
- **Reuse a Google key for every Google service.** The "Reuse this key" row now sits at the top of the form, shows on Google Ads, Analytics, Merchant Center and Search Console too, and borrows a key (service accounts included) saved for any other Google service. Google shows a client secret only once, when it is made, so the key kept in Naota is often the only copy left.
- **Change a key right on the connection.** "Reconnect (sign in / change key)" on Gmail, Calendar, Analytics, Ads and the rest now opens a change-key form: pick a key saved for another service, or paste a new one, then sign in again.
- **A warning before a key is lost.** Deleting the last connection that holds a Google key says so in the confirmation, with how to keep it.
- **"AI reply" and "Rewrite" in the inbox now show what the AI is doing.** Where the draft will appear, an "AI is writing" box shows a pulsing icon, the current step (reading the chat, checking documents, looking at the customer's photo, writing the reply), the seconds so far and three moving lines. Past 25 seconds it calmly says the AI is still writing, so nobody thinks it broke.
- **Drafts come a little faster:** the document lookup, the plugin context and the look at the customer's photo now run together instead of one after another.

## [1.49.0] - 2026-11-19
### Fixed
- **The estimated saving on the Usage page now matches what is really sent.** Optimized used to count only the short rules and forgot the base that still goes with them (the chat channel rules included), so the page claimed 84% for every brain. Now an API-key brain sees the real figure, and a subscription plan (Claude Code, ChatGPT...) sees plainly that the full rules stay and only memory and skills load the relevant parts.
- **The running total of tokens saved no longer counts every Max-level turn as a shortcut turn.** Only simple questions take the shortcut, so the total uses the Optimized price; the measured part of the page still shows what the shortcut really saved.
### Improved
- **Background jobs on an API-key engine send about 60% fewer fixed tokens.** Kanban jobs, loops and reminders that do work carry a short background rule set instead of the whole chat rule set in every tool call. Every rule about acting stays: do exactly the job within its permission level, never invent numbers, report to whoever assigned it, no empty promises, no jobs created unasked, new plugins always off. Tested with a real model on 7 sample background jobs: results on par with the full rules.
- **Subscription engines are unchanged.** Claude Code, ChatGPT, Grok and Antigravity keep the full rules. It starts on about 10% of background jobs and follows the Off level.
- **Long skills load selectively, chosen by Naota before loading.** For a menu-style skill such as the agent/loop/plugin builder, Naota loads only the part a request needs plus every rules section (and any part it says to create first, such as the agent template for a workflow), about 47-63% lighter. Measured with a real model on 7 kinds of request, answers as complete as with the whole skill.
- **Every language alike.** The choice does not lean on Vietnamese or English: it reads every script (Chinese, Japanese, Korean and Thai included), matches words with inflected endings (Russian, German, Turkish, Korean), and finds filler words from the skill itself. When someone asks in another language than the skill, the model sums up the task in the skill's language so Naota picks the right part. When unsure it loads the whole skill as before, and a skill that is one procedure always loads whole.
- **Learns from use.** A part the model keeps fetching is loaded up front next time. It starts on about 10% of chat sessions and follows the Off level.
- **Long turns cost fewer tokens, on every brain.** When the model calls the same tool with the same arguments and the result is identical, it gets a one-line reference instead of the whole text again. The tool still runs every time, so changed data always reaches the model in full. For Claude Code and Codex this happens at the hub, and Naota forgets the turn's record whenever they compact their conversation.
- **Leaner JSON.** Indented or escaped JSON results are written compactly with the same content. Files, terminal output, web pages and skills stay exactly as they are.
- Choosing **Off** on the Usage page turns both savings off. What they save shows in the tool results line of that page.

## [1.48.0] - 2026-11-19
### Added
- **An @ button in team chats.** When an assistant tags you and the message has scrolled out of view, a round @ button with the number of waiting messages shows at the bottom right. Tap it to jump to that message, tap again for the next; it hides once you have read them or replied.
- **The Team tab shows each member's model.** Under each assistant's name is the engine and model it runs on, marked "Main model" when it has no model of its own, so the whole team is easy to keep an eye on.
- **Answer an approval card in the team chat.** The card has two big buttons with icons: Approve and Reply. Reply opens a box inside the card with three choices: Ask (a question in the chat that quotes the card and calls the member who asked, the card keeps waiting), Change (asks for changes as before) and Reject. Each choice offers a few quick answers. The quote button on a line (Will do, Impact) asks about that exact line. Ctrl or Cmd + Enter sends, Esc closes. No more grey browser prompt.
### Fixed
- **Opening a team no longer hangs on "Loading the team's messages".** Each open used to add up every model call the team ever made, slower the older the team, although the page no longer shows those figures. Opening a team skips that now.
- **The team Info tab no longer stays on "Loading...".** A team that opened on Jobs now shows its images, files and links as soon as you switch to Info.
- **The / skill list in a team chat no longer overlaps.** Each skill shows one line of name and one of description, a long name ends in "...", and the list scrolls when long.
- **The "Showing one job's messages" bar is one line** on a phone: the job's name, an icon for its acceptance and usage, an X to see every message again. It used to take three lines and push the chat down.
- **Pressing a job's title or "Open the Jobs tab" in the job pill's details now opens it;** the details used to just close.
- **A job you already answered no longer comes back on the pill** while you look at another job's messages. A job with no message yet says so in the chat.
- **The reply suggestion no longer lands on top of the "is typing" line** when that line shows up above the input, on the Teams page and in the main chat.
### Improved
- **The team's settings tab is much shorter and saves itself.** Advanced is gone (acceptance, usage, limit numbers, the deputy's detailed rights, the limits table, the reply log): Naota keeps its automatic defaults, and the deputy's rights follow the three levels. Name and description save when you leave the field, pause is one switch, there is no Save button. Archive and Delete stand apart at the end in a red-edged box. The two "outside actions" choices are choice cards like the three levels.
- **A reply stopped by a limit no longer offers "Open the team limits"**, since there are no numbers to open; Try again stays.
- **A team no longer has a daily reply cap.** A team that used its 100 replies of the day used to stop every member with "The team has used up its replies", and "Open the team limits" only raised it a step at a time. There is no daily cap now, also for a team that saved a number before, through "Give more turns", or in the deputy's rights. The caps of one job stay. A job stopped by the daily cap goes on with "Give more turns" or "Try again".
- **The button to tagged messages now sits at the top.** A round button with an up arrow and "@" plus the count under it, like Zalo, since the tagged messages are usually above. Showing or hiding it never moves the messages you are reading.
- **A team loads only its latest messages, and older ones as you scroll up.** Near the top of the chat the next page loads by itself and you stay on the same message, like the main chat and the Chatbot page. A "Loading older messages..." line shows meanwhile.
- **Team jobs run side by side.** Every job given to a team starts at once, jobs given to the whole team too (they used to wait for each other because they all counted as the deputy lead's).
- **Waiting only where a result is needed:** parts of one job that come one after another still wait for each other, and a job you word as "after … is done" or "one by one" still waits for the jobs before it. Each assistant works through the parts given to them, in the order given.
- **No cap on jobs per team (was 3) nor on teams at work (was 4).** A step waiting for an assistant busy with another job of the same team now waits its turn instead of stopping as "busy too long".
- **The team Jobs tab now follows the Tasks page.** Each job is a card, and right under it you see what every member is doing: done, working or waiting its turn, with what they were asked to do. Jobs waiting for you come first.
- **Icons replace text buttons.** Edit, acceptance, cancel, priority and move to Archive are icons; one text button is left, on a job that waits for you. The Info, Jobs and Team tabs have icons, and Jobs shows how many jobs are open.
- **Press a finished job to read a summary:** when it ended, the result, who did what. Finished jobs and the Archive are paged, five jobs a page.
- **The Archive is no longer cut at 30 jobs** and gets a search box once it is longer than one page. "Delete all" stands apart at the end.
- **A message added in a team is read at once.** A member still writing the answer to the previous message stops and answers both together, the newest one first in priority. No more waiting for the earlier answer before the next message is read.
- **A deputy busy with a step of a job reads the new message at its next step,** so the way of working can change mid-way. The status line says "Read mid-way".
- **An answered approval request stops ringing.** Approve, Change, Reject or a Reply question on the card turns its notice in the bell read. A request that expires or is cancelled does too.
- **The deputy stands out in the team settings:** right under the owner, on a tinted row with an accent edge and a star badge.
- **Team jobs fold into one pill right above the composer,** like background work in the main chat. Press it for the details: why a job stopped, the button that resolves it, who is working.
- **A job waiting for you leaves the pill once you have written in the chat after it stopped.** It stays in the Jobs tab until it is resolved.
- **Team roles renamed:** you, who made the team, are the Team lead; the assistant who leads the team is the Deputy lead (was "Coordinator"). Role badges stay on one line, and the role of each step ("Planning", "Working") is a small tag.
- **The Jobs tab comes first in the side panel** (Jobs, Info, Team). A team with jobs opens on Jobs, a team without any opens on Info.
- **A tidier approval card.** The deadline reads "5 h left" at the top next to "Waiting for you"; evidence and calls fold into one line with a count, and a long path shows only its file name (the full path on hover). The acceptance and opportunity cards share the solid, 16px-rounded frame.

## [1.47.0] - 2026-11-19
### Added
- **Background jobs can carry fixed done-criteria.** A job a script or workflow hands out every day keeps its wording and is checked against exactly those criteria, so it no longer passes one day and sticks the next.
- **Notify every answer when you are not viewing that chat.** Turn on the new box under Push notifications in the bell: when Naota finishes an answer the phone rings if you switched to another app or opened another chat. Viewing that chat keeps it quiet. Tapping the notice opens the chat.
### Fixed
- **Locking the phone no longer hides the answer.** Ask on the phone, lock it, and when you come back Naota pulls in the answer that finished while you were away, no need to ask again or keep the screen on.
- **A home-screen app that was closed shows the full answer when reopened.** The chat used to show only the old copy kept on the phone until you opened it again from History.
- **A background job that answers `[SILENT]` finishes quietly**, like reminders: no more "nothing to report" messages on every run, and the automatic check no longer fails it.
- **Editing a schedule changes its permission level, who gets the result and the spoken note.** Naota used to say "updated" while the old level stayed.
- **Short wikilinks like `[[log]]` open** even when many files mention the word. When an approval team refuses ChatGPT on Docker, the message now says how to turn the sandbox back on.
- **Text Naota writes before and after each tool call no longer runs together** (as in "needs a sign-in.Done with item 3"). Each new stretch starts on a new line, on Claude Code, Codex, Grok Build and Antigravity.
- **The notes Naota writes while it works follow your language too**, instead of drifting into English halfway through code or logs.
- **Playwright screenshots show right in the chat.** When Naota took a screenshot of a page with Playwright, the image reached the model as a long string of characters and nothing appeared in the chat. The image is now saved in the brain under `attachments/tool-images/` and Naota embeds it in its reply so you can preview it. Images returned by other tools (charts, designs) are handled the same way.
### Improved
- **Typing while a goal runs no longer pauses it.** Your message is added to the goal: the running round reads it at its next step and every later round carries it, so you can adjust or widen the goal while Naota works. Each such message gives one more round (10 at most). If a round reports the goal met before it read your message, Naota runs one more round for it. The Stop button still pauses the goal as before.
- The project selector and project list show a red dot when another project has unread replies. The selected project uses its chat dots without a duplicate folder alert.
- Opening a project keeps chats unread until they are opened. Badges update for new replies and reads in another tab.
- **After an update, work in flight carries on by itself.** A team job cut in the middle continues with the step it was on, and a team reply that was being written is written again; no more pressing "Continue" or "Retry".
- **A chat answer cut short is answered again** when the page comes back after the server restarts, in the main chat and in chats with an assistant.
- **Background jobs go back to the queue at once** instead of waiting 90 seconds, and the cut no longer counts as a failed attempt.
- **Nothing outside happens twice.** A step that had already sent a message, posted or created an order before the server stopped makes Naota stop and tell you instead of doing it again. A workflow run cut short no longer says "running" for ever.
- **A partner's unread count sits on the bottom left of the avatar.** The time keeps the bottom right corner to itself, rows breathe on a phone, and the collapsed avatar strip on desktop now shows who has new messages.
- **The "Add Naota to your Home Screen" prompt no longer pops up right after you sign in.** It used to show 12 seconds after the page opened, on top of the sign-in screen and the first-run setup. Now it shows only after about 3 minutes of real use (added up across visits), never while the sign-in screen, the setup or another dialog is open, and not while you are typing. The "Install on phone" button in the menu still opens the steps at any time.
- **The long-turn notice is no longer swallowed while you are in another chat.** It used to stay quiet whenever Naota was open; now only when the screen shows that very chat.

## [1.46.2] - 2026-11-17
### Fixed
- **Background commands show their quotes correctly.** On the Office page and the background work strip, a command with single quotes (like `<<'EOF'`) used to show as a hard-to-read run of quote marks. It now reads exactly as typed.

## [1.46.1] - 2026-11-17
### Fixed
- **The Chatbot page works again.** 1.46.0 shipped a stray line in the Chatbot page code, so the Bot tab stayed blank and no bot could be created. The line is gone, and a new check keeps this kind of slip out of future releases.
### Improved
- **Switch between Vietnamese and English right in the sidebar.** The interface language picker is back in its old spot above the version line, no trip to Settings needed. The one in Settings stays, and the two always match.

## [1.46.0] - 2026-11-16
### Added
- **Custom API connection.** Any service with a REST API and an API key but no MCP (POS, CRM, shipping, e-invoices...) now connects on the Connections page: paste the base URL and the key, and every engine can call that API.
- **The key never reaches the model.** It is encrypted, the server adds it to each call and only sends it to the host you entered; a key echoed in a result is masked.
- **Read-only by default.** At Read-only Naota only calls GET; to create, edit or delete on that service, raise the connection to Full access.
- **Webhooks can be edited after they are made.** The Configuration part of each webhook has an Edit button: change its name, its workflow or written job, the note and the permission level right in that window. The link and its key stay the same, so whatever sends events there needs no change.
### Improved
- **Add new GitHub repos right from a project, an assistant or the create-team box.** The repo picker in those three places now has the "+ Add repositories on GitHub" row, as in the chat. Grant more repos on GitHub, come back, and the list shows them without a reload.

## [1.45.0] - 2026-11-16
### Fixed
- **Chatting with Naota over Zalo no longer defaults to Vietnamese replies.** Naota answers in whatever language you write.
- **Reminders set over Telegram mention the time zone you chose in Settings**, instead of "Vietnam time" for everyone.
- **The Effort level now works on Gemini 4.** On a Gemini API key, Gemini 4 Hydrogen, Argon and Carbon ignored the Effort you picked and always ran at their own default. Your level is now sent, and later Gemini generations are recognised on their own.
- **The Usage page prices the new Gemini models correctly.** Gemini 4 used the old Gemini price and showed several times cheaper than it is, while Gemini 3.5 Flash-Lite was priced as Pro. Each model now has its own price.
### Improved
- **The core rules Naota sends to the model are now written in English, one copy for every language.** This covers the rules of each chat channel, token-saving mode, the Naota Core role, and the agent and skill paths. About a quarter of the instructions used to be Vietnamese and pulled replies into Vietnamese; Naota now keeps to the language you write in. Chatting in Vietnamese works as before, with Vietnamese replies.
- **The instructions take fewer tokens**, so every chat turn is a little lighter.

## [1.44.0] - 2026-11-15
### Fixed
- **A loop with its own task now finishes the whole task in one round instead of stopping after the first step.** The old instruction "carry out 1 concrete step" made multi-step loops (for example posting to every channel) do only the first step and report done. Each round now runs every step the task lists; a step that fails is noted and the next one still runs.

## [1.43.0] - 2026-11-15
### Fixed
- **Naota no longer answers in Vietnamese while you chat in English.** The language rule is now written in English, says a language you stated wins, and that the Vietnamese around it is no hint.
- **Background work (Kanban, reminders, loops) no longer always reports in Vietnamese.** It follows the task's own language.
- **Replies in Japanese, Korean, Chinese and Thai are read aloud by a native voice**, and an English message with an attached file is no longer read as Vietnamese.
### Improved
- **Naota replies in the language you write in, any language, like Claude or ChatGPT.** The language box in Settings now only changes the interface, and chatbots always answer customers in the customer's language. To always get one language, tell Naota once; a reply language pinned before becomes a sentence in your profile, so it is not lost.

## [1.42.0] - 2026-11-15
### Added
- **ChatGPT and Claude can set the model and effort inside the command they send through Naota Gate.** Tell ChatGPT "have Naota do this on Opus at high effort": the model is pinned on that chat as if you picked it in the model bar (the chip shows it, change it back any time), and the effort counts for that one message only, nothing in your settings changes. A new `naota_chat_models` tool lets the outside AI see which models Naota has.
- **When work ChatGPT sent finishes after it stopped waiting, the Naota bell rings your phone**, with the answer and the sentence to send ChatGPT ("check Naota results"). ChatGPT and Claude do not let outside servers wake a chat yet, so this is the shortest path: one message, and the new `naota_chat_updates` tool hands over every unread result, even in a new ChatGPT chat.
- **Add GitHub repositories to a Project.** Open the project panel, Documents tab, Add document, then GitHub repository. Every chat in the project gets the repository from its first message, each on its own branch.
- **Add repositories to an Assistant's documents.** Every private chat with that assistant gets them too, and Naota still commits, pushes and opens the PR as usual.
- **Pick repositories while creating a Team.** The documents part of the Create team box has an Attach a GitHub repository button, so the new team starts with its repositories.
### Fixed
- **Picking several photos at once in a team chat on iPhone now attaches and sends them.** Before, a multi-photo pick put nothing in the composer and only a single photo got through. Adding team documents and importing a team file share the fixed picker.
### Improved
- **ChatGPT waits longer for Naota within the same reply** (up to about 10 minutes) instead of giving up after half a minute, and knows how long Naota has been working.

## [1.41.0] - 2026-11-15
### Added
- **With Auto on, an assistant looks around with full access.** In its private chat, each time it wakes on its own it uses every connected tool (email, calendar, sales, web search...) and may take real actions within its role. Whatever it does is always reported to you.
- **Assistants set their own times to check back.** When something has a date (a race, a meeting, a deadline) the assistant sets a check-back, such as the morning or the evening before. At that time it wakes, checks the sources again, then decides whether to message you.
- **Suggestions and reminders, not notifications.** An assistant only messages you when something is new, timely and actionable: at most two short paragraphs, one concrete piece of advice, with real source links. Reminders go to the Reminders group, suggestions to the new "Assistant suggestions" group (it still reaches you by default; lower or turn it off on the Notifications page).
- **Ask for an improvement and it happens, with undo.** Say "improve yourself" or "rework this skill": the assistant changes its own role, instructions, skills and model, other assistants, skills, workflows, loops and memory. Every change gets an id and a backup; "undo #12" puts it back.
- **Naota can change its own source code.** With GitHub connected to the Naota source repo (`vuongtex/naota`), the assistant attaches the repo to the chat and works on its own branch; Naota checks, opens a PR and merges on green CI.
- **It updates itself to the release.** Say "update now": Naota waits for the chat turn to end, runs exactly what the Update button runs, and rolls back if the new version breaks.
### Fixed
- **Files the team writes open with a click.** A file link in a team chat used to do nothing visible. The file now opens right in the team's chat column; press X to get back to the conversation, with anything you were typing still there.
- **Pages with no room for the editor open the file in a popup**, such as a file link on the Tasks page, so no click on a file link goes nowhere any more.
### Improved
- **Turning Auto on asks once** and says plainly that it gives full access. The old line "Auto is not Full access" now matches how Auto works.
- **Only you can order it.** Auto's own wake-ups and customer-facing bots may only suggest. Old prompt lines that contradicted this now match.

## [1.40.0] - 2026-11-15
### Added
- **Links that open a dashboard page directly.** A link like `#p=tasks` (or another page name) opens that page, even in a Naota tab that is already open.
- **Cancel background jobs right in chat.** Ask Naota to cancel a job and it leaves the queue, a running job stops at once, and the reason goes into the job's log. When sending a job back to be redone, an extra note on how to fix it now reaches the redo.
- **Connecting a Facebook Page has a "Read post insights" tick.** This optional tick asks for reach and saves of posts. The Messenger checklist shows whether the Page has that permission.
### Fixed
- **Background commands Naota starts in an API-key chat report when they finish.** They used to stay "running" until the server restarted.
- **A chat pinned to a model keeps that model.** While the pinned model is out of quota or signed out, turns run on the main model for the moment, then go back to the pinned model once it works again.
- **File links with line numbers (like `agents/x.md#L66-L75`) open the file.** Answers no longer get a false "file not found in the brain" warning.
- **Messenger conversations show the customer's name instead of a bare ID.** When Meta refuses the profile, Naota takes the name from the Page conversation, and tries again after 10 minutes if it could not get it.
- **Hanging up while Naota is still working on something asked for in the call no longer drops it.** Naota finishes and posts the result to the call's chat, with a notification.
- **The Automatic call path no longer switches to ChatGPT Live just because the machine has a Codex sign-in.** ChatGPT Live is picked only when ChatGPT is the main model or connected on the Models page.
### Improved
- **System lines Naota adds under answers no longer hardcode a Vietnamese first-person pronoun.** Background job tracking, empty-promise and memory notes and missing-file links are written without a pronoun, so they match the chosen form of address.

## [1.39.0] - 2026-11-15
### Added
- **A "Keep me signed in on this device" box on the sign-in screen.** Ticked, as before, the device stays signed in for 30 days. Untick it on someone else's device: closing the browser signs you out, and Naota also signs you out after 4 hours unused or 24 hours at most.
- The Security page marks devices signed in without being remembered.
- **Tap a quote to scroll back to the original sentence.** Quote a sentence from a long answer to ask more, then later tap that quote in your message: the chat scrolls up to that exact sentence and highlights it for a few seconds.
- When the original sits in older messages not loaded yet, Naota loads them to find it. Works in the main chat and on the Teams page.
### Fixed
- **The model picker opens right above the model chip.** A tall composer (a file attached, a few lines typed) used to push it far above the chip, and a long list lost its first rows off the top. The model list, Effort, plan usage and the "+" menu now open just above the row of chips and always stay on screen.
- **The Team chat's "+" menu does the same**, along with the folder and GitHub panels it opens.
- **"Push again" and the warning mark on the GitHub card no longer stay stuck.** A job that had stored a branch name already taken on GitHub (from before the previous fix) kept pushing to that same name, so every retry said "has commits this machine lacks". Now, while nothing has been pushed yet, Naota picks a free branch name again (or follows the branch checked out on this machine), pushes, opens the PR, and the warning clears.
- **The second GitHub job in a chat no longer gets stuck at the push.** The PR title and branch name now come from the request itself, skipping the dashboard's bracketed context lines, so every job gets its own name. When the name is already used on this machine or on GitHub, Naota adds -2, -3 and pushes, instead of stopping with "has commits this machine lacks, Naota does not overwrite them".
- **The Google Workspace connection does real work on Forms, Drive and Sheets.** The card only turned on a reduced tool set, so Naota could not edit Form questions, read responses, browse a Drive folder, rename or copy a file, add a tab or append rows to Sheets. All of that works now, with no new Google sign-in.
- Connections made earlier move to the full tool set after the update.
- **Editing the compose in hPanel and pressing Deploy works again.** Version 1.37.0 made the Hostinger file 33,167 characters, over hPanel's 32,768 limit. It is now under 30,000 characters, and the update guard runs exactly as before.
- Opening Naota for the first time in a new browser no longer shows a wrong red "Your sign-in has expired" line.
- **Read-only reminders can see My Tasks.** A reminder that checks progress used to say it could not check; it now reads the list, while adding, editing, deleting and ticking still need write access.
### Security
- **Sharing a file or calendar with someone needs Full access.** So do deleting a whole tab, task list or contact group, creating Gmail filters and publishing Apps Script. At Read only, Naota cannot copy a Drive file or append rows to Sheets.

## [1.38.0] - 2026-11-14
### Added
- **Zalo messages can quote the message they answer.** When you ask Naota to reply to one specific message, the message goes out with the quoted original above it, like tapping "Reply" in Zalo. Only text messages can be quoted. The Zalo connection moves to naota-zalo 1.11.0 on its next start.

## [1.37.0] - 2026-11-13
### Added
- **New Claude models show up in the model picker on their own.** Naota also reads the model catalog Claude Code downloads from Anthropic, so a model released after the installed CLI was built appears right away instead of waiting for a Naota release to add its name.
- **A whole folder can be a document.** The search box under Add file for a project, a partner, a chat and a team (the create box and the Info tab) now lists folders whose name matches, with their own folder icon. Press Add to attach the whole folder instead of picking files one by one.
- **Naota knows what the folder holds.** An unpinned folder gives Naota its path, and it opens the files inside when it needs them. A pinned folder has its file list loaded into every turn. A folder added to a team is pinned at once.
- **Safer rows for folders.** A folder row has no delete-from-brain button, only remove from the list. Tapping the folder's name opens it on the Files page.
- **Projects learn their own context.** While working in a project, Naota notes what is durable and specific to it (facts, settled decisions, terms) and uses it in every later chat of the project. Read, edit and delete them in the new "Learned" tab. The Instructions box stays yours: Naota changes it only when you say so.
- **Dropping a document into the chat is enough.** A file or link for long-term use is attached to the project by Naota with one line saying what it holds, so it opens the right document without pinning the whole file.
- **Partners and teams get document descriptions too.** In a private chat, a partner attaches and describes its own documents; a team's documents carry a line every member reads.
### Fixed
- **Attaching a private repo to a chat no longer fails once its main branch has new files.** A private repo used to attach only the first time; as soon as the main branch gained or changed a file, a new chat stopped with `could not fetch ... from promisor remote`.
- **Changing a chat's base branch works on private repos too.** The same fault broke Change branch and the fresh branch Naota starts after a merge; both are fixed.
- **A conflicting PR on a private repo is merged back by Naota again.** The conflict fix round used to stop at downloading the main branch, because the AI's shell has no access to GitHub. Naota now downloads the main branch first, and the AI only merges and resolves the conflict.
- **If GitHub is unreachable at that moment, Naota waits and tries again.** A fix round is no longer spent on a merge that cannot work; the repo card says why it is waiting.
- **The automated tests pass again.** Two GitHub updates landed at the same moment and made one test fail for the wrong reason; that test is rewritten. Nothing changes in how Naota runs.
- **The conflict fix round works on a machine where git has no name and email.** On a fresh server or in Docker, the AI's merge command stopped at once with `empty ident name`. Each repo attached to a chat now has an identity of its own, the GitHub account you connected.
- **Commits the AI makes itself in that repo now carry the same author as Naota's commits.** A name and email you set for the repo yourself are kept.
- **No more slowing down over a long session.** Every visit to the Chat page left the whole previous page in memory, so the more you switched pages the heavier it got. The old page is now released.
- **The Graph screen no longer stutters.** The graph remembers where its dots came to rest, so the next opening shows at once instead of working it all out again (a brain of 2,600 notes: the longest freeze went from over 1 second to about 0.2). A dot you pointed at also no longer stays lit and keeps the graph drawing after the pointer has left.
- **The Windows installer is no longer replaced for no reason.** `Naota-Setup.exe` is not code-signed yet, so browsers and antivirus engines know it by its file hash alone. Any change to an install script (even the Linux one) used to replace the file, and each new file made Edge say "isn't commonly downloaded" from scratch. The file now changes only when the installer itself does.
- **The quick start explains what to do when the download is blocked.** It adds the **Keep anyway** step for when Edge or Chrome will not save the file, and a one-line install without the .exe for PCs where an antivirus or Smart App Control blocks it.
- **Heavy Team use no longer drops the connection to the server.** The more turns a team had run, the longer Naota took to add up its usage every time the team was opened: a team of a few thousand turns took a minute, the page gave up after 30 seconds and asked again, and the whole server stalled. It is now about 100 times faster and never runs twice at once.
- **A model call no longer makes the server pause.** The usage ledger kept one line for every Team model call for 30 days and was rewritten in full after each call, so the file grew to tens of megabytes and ordinary chat slowed down too. Naota cleans the file when it starts; your usage figures stay the same.
- **The Tasks page no longer hitches every so often while you look at it.** Every 30 seconds (5 while a task was running) it redrew the whole list even when nothing was new, freezing the screen for a beat and dropping the row under the pointer. Now nothing is redrawn when nothing changed.
- **Naota no longer freezes when the server's disk answers slowly.** On a VPS, every few seconds of slow disk froze all pages, bots and connections together, and the server could be reported as down. It was worst right after an update. The work that runs all the time (the sign-in check, the MCP hub, bots, shared links) no longer waits for the disk.
- **After a Docker update, MCP sources no longer download and install themselves again.** What they installed is kept on the data volume, so the server is not flooded while it starts. The update to this version still reinstalls them one last time.
- **At start-up, Naota opens MCP sources a few at a time** instead of all at once, so a small server is not overloaded.
- **A group no longer shows one person's profile.** The note box of a Zalo group used to show the profile of whoever wrote first in it, as if the whole group were one customer. A group now has its own note, and editing it touches nobody's profile.
- **Facebook, Instagram and Threads comments get no profile.** A commenter is not messaging the shop, so the AI no longer writes a profile from comment threads, and a public reply no longer carries a profile learned in a private chat.
- **The OpenAI Compatible and Claude Compatible cards no longer say "Could not load the model list" by mistake.** Naota reads the model list of more kinds of gateways, and a Base URL typed without `/v1` finds the right address on its own. A machine upgraded from an older version gets its models back too.
- **A model name you typed always stays in the picker**, even when the gateway has its own list or stops listing for a while.
- **When there really is no list, the picker says why** (wrong address, refused key, a gateway that lists nothing) with a link to the Models page to fix it. After the fix the list shows on the next open, with no wait of several minutes.
- **A key you just connected no longer disappears** when Naota happened to be loading another card's model list at that moment.
- **Stopping a dictation answers at once.** The bar switches to "rewriting" the moment stop is pressed, and the recording goes to be heard right away instead of waiting for the browser to close the mic.
- **The rewrite step is much faster.** The word fix that runs first could take several seconds and now takes a few hundredths of one. The quick model no longer spends its whole turn thinking and returns nothing, and on a subscription the main model thinks at its lowest level for this job.
- **Long dictations no longer lose words.** Text over about 2,000 characters used to come back cut after the rewrite; every word is kept now.
- **Fewer everyday words turned into names.** Common Vietnamese word pairs that merely sound like "Naota" or "Canva" are no longer replaced by those names.
- **A suggestion you took no longer vanishes when you delete part of it.** Pressing Tab to take the whole sentence (or taking it word by word to the end) and then deleting a few letters used to lose the suggestion. Now the rest shows in grey again as far as you delete. Empty the box and the whole suggestion is back. It only goes away when you send.
- **The > after a suggestion shows on a computer too.** It used to show on phones only. On a computer, click the **>** right after the last word to take the sentence.
- **Naota no longer vanishes (404) after an update.** On a VPS with a slow disk, Watchtower ran out of time while deleting the old container and gave up without creating the new one, so Naota was gone from Docker until a Redeploy.
- New `naota-guard` container: when Naota has been gone or stopped halfway for 2 minutes, it creates it again (on the new version) or starts it again. A Naota you stop yourself is left alone.
- An update from the button now gets 30 minutes instead of 10. Redeploy once to get the new compose file.
### Improved
- **Naota opens much faster.** The "Starting Naota…" screen used to stay for a full 4 seconds on any machine with more than one page of chats, although the data was there after about 1 second. Now the app shows as soon as the data arrives. The brain graph is also no longer built in the background when you open straight into Chat or Partners.
- **Left alone, Naota costs almost nothing.** The mascot's ring, the starfield and the graph no longer make the browser work 60 times a second when nothing changes, so scrolling and typing are smoother and the device runs cooler.
- **The Tasks page opens much more smoothly.** It used to draw the whole list twice on every opening and build both the wide and the phone layout. Now it draws once, and only the layout on screen. With 170 tasks on a slow machine: the freeze went from 0.45 seconds to about 0.1, and is all but gone on a phone.
- **The Partners page opens faster.** The list of assistants used to be drawn five times on each opening, now once, so hovering and scrolling no longer stutter right after the page appears.
- **Typing in the task search no longer lags.** The list follows a short moment after you stop typing instead of being redrawn after every letter.
- **The suggestion no longer vanishes at the first key you type.** Type along the suggestion and the rest stays in grey right after your text, even without accents or halfway through a word. Press **Tab** to take the rest, or **Right Arrow** to take one word. On a phone the Tab button is gone from the button row: a small **>** stands right after the last word of the suggestion, and a tap on it takes the suggestion.
- **Type something else and Naota finishes the sentence.** Pause for a moment and Naota writes the rest of what you are typing, following your new direction, like the predictive text on an iPhone. With an API key on the machine (Groq, OpenAI...) it is almost instant. On a subscription plan alone it takes a few seconds and runs at most 5 times per turn, so it does not eat the allowance.
- **A long suggestion shows in full.** The chat box grows to show the whole sentence, so a phone no longer cuts it mid line. Works in the main chat and on the Teams page.
- **Approve many waiting groups for a bot in one press.** In the bot's Status panel every waiting group or person is a tick box, with **Select all** and one shared **Allow** / **Ignore** bar. Nine waiting groups used to mean opening the panel and pressing nine times.
- **The panel no longer closes after each press.** After a batch it stays open with the rows still waiting. The button carries the number of ticked rows, for example "Allow (9)".
- **Easier to read on a phone.** Larger group names, the whole row is tappable, and the buttons stay within reach however long the list is.
- **No more "Tab" chip in the button row under the chat box.** The **>** does that job, so the row keeps only its own buttons (attach, model, effort, mic, send). The Tab key still takes the suggestion.
- **Files, folders and links share one "Documents" tab.** Icons tell them apart and Add document can paste a link too, so the drawer is one tab shorter.
### Security
- **Hooks and git config inside a repo can no longer read the GitHub token.** A hook sitting in the clone (installed husky-style by `npm install`, or written by the model) used to run while Naota fetched or pushed, and could see the token. Naota's git calls that carry the token now ignore every hook of the repo.
- **The token only goes to the repo on GitHub.** If the clone's git config was changed to steer the connection elsewhere (a different `origin`, `insteadOf`, a proxy), Naota stops and names the setting to remove instead of sending the token.
- **Worth knowing:** a repo's `pre-push` hook no longer runs when Naota pushes (Naota's own checks and CI run as before). Repos using Git LFS: new LFS files made in a chat are not uploaded by the push yet.

## [1.36.0] - 2026-11-13
### Added
- **An agent set to ChatGPT now really runs on ChatGPT in restricted background workflows.** Those steps always ran on Claude Code, whatever you picked. The step can call only its own tool list, at the job's permission level, with no shell, web or sub-agents.
- Without Codex installed the step still runs on Claude Code as before, with no error.
- **Create a team with its documents from the start.** The Create team box has a new "Add documents for the team (files, links)" block: find a file already in the brain by name, upload one from the device, or paste a link. Team members can read them from the first message.
- **No need to upload a file the brain already has.** The Info tab of each team has a box that searches the brain, and Add is one press. The file stays where it is, no copy is made.
- **One team can run several jobs at once.** A team used to run one job at a time, so one assistant's job waited for another assistant's job to end. Now up to 3 jobs run side by side when they belong to different assistants.
- **Jobs of the same assistant still run one after the other**, in the order of the queue. So do the jobs the coordinator plans.
- **To make a job wait for an earlier result, say so in the request.** A job with words such as "after ... is done", "one after another" or "in sequence" waits for every job before it, and no later job starts ahead of it.
- **A new team runs a job to its end.** Teams created from this version on have no cap on the replies and steps of one job, so a job no longer stops halfway to wait for "Give more turns". In exchange a hard job can use more tokens. The team's daily reply cap stays, and a job still stops by itself at two identical results.
- Teams created before keep their limits. To change them, open Advanced, Team limits, and tick "Unlimited" or type a number.
### Fixed
- **ChatGPT image generation no longer says "no account" while every account rests after a chat limit.** Naota still tries the first switched-on account, as it did before account rotation. Switched-off accounts stay unused.
- **Opening a team with hours of chat no longer slows the whole app.** Until now, opening a team on a wide screen also opened its Info tab, and the server read every message of the team again to look for files and links. The longer the team, the slower, and meanwhile loading messages, switching teams and sending all had to wait. The server now keeps the result and reads only new messages. Measured on a team with 3,000 messages: from 1.5 seconds per open to 0.003 seconds.
- The Documents list of a long conversation is faster too, since it reads the same way.
- **A new Claude Code chat no longer rewrites the whole prompt cache at token-saving levels.** A clock that changed every minute, and the memories picked for each question, sat inside the cached part of the prompt, so every new chat rewrote about 25 thousand tokens. They now travel with the first message of the chat, and the prompt stays the same between chats.
- **Rules written on the Profile page now reach the model at token-saving levels too.** At the saving levels (the default one included) the profile was dropped together with the memory index, so a form of address or a layout preference set once for every brain only worked with saving switched off.
- **The Messenger check now detects a webhook that cannot be reached.** Every line used to say fine while the HTTPS address was dead, so the bot stayed silent with no visible reason.
- **When the quick tunnel gets a new address, automatic repair points the webhook at the running one**, keeps the receiver path, and saves it only after Meta verifies it.
- **The usage ring stops being red as soon as the plan works again.** Before, after you reset the plan on the provider's site the ring stayed red at 100% and Naota's own work stayed paused until the old reset time.
- **A reset time that includes the year is read.** A notice like "try again at Nov 13th, 2026 3:32 PM" used to count as "no reset time given"; the real time now shows.
- **Background work refused for quota turns the usage ring red too.** Only chat turns recorded it before, so background work could use up the plan while the ring stayed green.
- **The "SDK engine: ProcessError... Check stderr output for details" error now gives the reason.** When Claude Code exits before answering, the chat shows what it printed instead of a line nobody can act on.
- **Three common cases come with the fix:** Naota running as root, a broken data source (MCP) configuration, and an outdated Claude Code on the machine.
- **Background fallback runs the model you picked on the card.** That choice was ignored before: when the background model ran out and the work moved to Claude Code, it ran the CLI's own default model, usually the one that uses the plan up fastest. A card with no model picked runs as before.
- **When ChatGPT (or Claude, Grok) loses its sign-in, Naota moves to another connected model by itself.** Before, only running out of quota moved a turn on; a lost sign-in failed every turn until you signed in again.
- **Customer bots and assistants with their own model are covered too.** A bot or an assistant set to ChatGPT answers on the main model while ChatGPT is signed out, so customers no longer hit failed turns.
- **You are told clearly.** The chat shows "Using ... because ChatGPT lost its sign-in", the model picker tags the card "Signed out", and the bell gets one reminder to sign in again on the Models page. After signing in, the old model is used again at once.
- **Rules on the Profile page now apply to shortcut answers too.** One gap was left: a greeting or a thank-you (at every level) and a simple question at the Max saving level were still answered without it, so Naota could get your form of address wrong on the very first hello.
- Answers written from data Naota has just read (on API-key brains) follow the profile as well.
- An empty profile changes nothing. The longest profile (4,000 characters) adds about 1,400 tokens to a shortcut turn.
- **The Reply judge item is always in the "..." menu of a bot card.** It used to appear only for a bot in Auto-judge mode, so many people could not find it.
- **For a bot not in Auto-judge mode the panel says the judge is idle**, with an Edit button to turn it on, instead of an empty list.
### Improved
- **The "Starting Naota…" screen hands over to the app sooner.** Once the first page has its data the screen goes almost at once.
- **A machine that loads data slowly is no longer covered for up to 12 seconds.** When the first page is open but a list is still loading, the app shows after 4 seconds and the unfinished part keeps its own "Loading" line, as on every other page.
- **Finding a file by name hits more often.** Several words such as "bang gia" now find `bang-gia-dich-vu.md`: the name only has to hold all the words, whatever the dashes or the order. This applies to every search of files by name, including the Documents drawer of a chat.
- **The job strip on top of the chat shows every running job**, not only one.
- To go back to one job at a time, set the environment variable `NAOTA_TEAM_JOBS=1`.
- **The Team settings tab is simpler.** What is in view is only what you decide for a team: its members, its goal, how far the coordinator decides alone, whether outside actions need approval, its name and status.
- **Acceptance and the usage figures moved into Advanced**, next to the limit numbers and the detailed rights. Nothing was removed: open Advanced and it is all there as before.
- **The team's goal now sits right under the member list.**
### Security
- **Facebook and Meta Ads tools no longer hand access tokens to the model.** Facebook's "next page" links and error messages carry the access token; Naota now strips it before the result reaches the model. Posts, comments and paging cursors are unchanged.

## [1.35.0] - 2026-11-13
### Added
- **Chat boxes continue a numbered list.** Under a line like `1. ...`, a new line starts with `2. `, as in Claude. A new line is Enter on a phone and Shift+Enter on a computer (Enter on a computer still sends). Works in the main chat, Teams, Conversations and the chatbot trial box.
- A new line on an item that is still empty removes the number and ends the list. A line added in the middle moves the numbers below it up.
- **Pin a folder to the top of the Vault tree.** Press the three-dot button of a folder and choose "Pin to top". A folder deep inside the brain can be pinned too, so you no longer unfold every level to reach it.
- **Folders that are open by default.** The same menu has "Open by default": that folder is already unfolded every time Naota opens, for example the wiki folder.
- **Saved per brain, on the server.** The phone and the computer show the same tree, and it works on a VPS. Renaming a folder in Naota keeps its pin.
- **The official Zalo bot receives files.** When Zalo passes a file to the bot, Naota downloads it and reads PDF, Word, Excel and plain-text files, so a question sent with it is answered from the file.
- **No more silence.** Zalo has no file message type for bots yet, so when Zalo includes no content the bot says plainly that it did not arrive and asks for a screenshot or pasted text. Before, the bot stayed silent.
- **Chatbots now answer on WeChat.** Chatbot, Add channel has a new **WeChat** entry: a dedicated bot answers the followers of your WeChat Official Account, every chat lands in the shared Inbox and you can take over as on the other channels.
- **Short setup.** The form shows the webhook address and the Token to paste into WeChat; on the Naota side you paste only the AppID and AppSecret. Check tells you right away which IP to add to the whitelist.
- **Good to know:** WeChat lets only a verified account (or the sandbox test account) reply through the API, only within 48 hours of the follower's last message, with text and images. Step-by-step guide in doc 36.
- **Customer profile.** After a private chat has been quiet for about 15 minutes, the background model writes down what is worth remembering about the customer: name, how to address them, contact details, what they are interested in, what was agreed, what is still open. The bot then reads this profile along with the last 30 messages, so it does not ask again, even when the customer comes back months later.
- **The note about the customer becomes the Customer profile section** of the Info panel on the Conversations page, up to 4,000 characters. You can still edit, add to or empty it, and what you write is kept at the next update.
### Fixed
- **Naota Store shows "Bundle" packs.** A pack made of several kinds, such as Customer management (CRM), sat under no tab, so it could not be found or installed from the Store page. There is now a "Bundle" tab at the end of the tab row.
- **The Windows installer no longer freezes.** An error used to wait for Enter in a black window hidden behind the wizard, and one helper installer (winget, npm, Grok, Antigravity) that never ended hung everything. Each step now has a time limit, then Setup moves on.
- **Git, Python and Node download much faster** on PCs without winget.
- **Dictating in English no longer comes back translated into Vietnamese.** After you press stop, Naota asks a model to tidy the sentence, and the model sometimes returned a Vietnamese translation instead of the English you spoke (mostly on longer sentences, such as a second recording). A sentence now stays in the language it was spoken in. If the model still translates, Naota drops the translation and keeps the words as heard. This covers the mic in the main chat, Teams, Conversations and the note editor.
- **Bots no longer forget a customer after every update.** A bot kept the history of a private chat in temporary memory only, so a restart of Naota made it meet a returning customer as a stranger. It now reads the chat back from the inbox, including what you answered by hand.
- **MCP servers with OAuth metadata on another host sign in (impact.com).** The card used to say the server declares no standard MCP OAuth. Naota now reads that metadata when it is on public https, returned by the MCP URL that was entered, and names that URL.
- **Opt out of the standalone 07:30 My Tasks agenda per brain.** Set `agenda_enabled: false` in the brain's `Naota/my-tasks.json`. Timed tasks, appointment reminders and habit nudges remain active; all other brains retain the previous default.
- **Zalo group @mentions keep targeting the bot after a Naota restart.** Retain an account ID verified from its own outgoing group messages, restore it after restart, and fail closed on conflicting identities.
- **ChatGPT image generation can use another signed-in account after quota exhaustion.** On a confirmed quota error, Naota retries on the next enabled account in Models order. Other errors do not trigger a retry, and disabled accounts remain unused.
### Improved
- **Each row of the Vault tree now has a single three-dot button.** Create file, create folder, pin, download, rename and delete all sit in the menu it opens, so the buttons no longer hide the file name, above all on a phone.
- **No separate black window when installing on Windows.** The progress shows inside the Setup window: a "Step 2 of 5" line, a bar that keeps moving and a box listing what is being done.
- **Errors show inside Setup.** A failed step says what is missing and where the log is, and the last page no longer claims the install finished when it did not.
- **Bots look back over the last 30 messages of a private chat instead of 20.** On every bot channel (Zalo Bot, personal Zalo, Telegram, Messenger...). In a chat with very long messages the bot drops the oldest ones. Groups still see the 30 messages before the one being asked.
- **Only private chats the bot has answered in get a profile.** Groups do not, nor do chats with friends and family on a personal Zalo account. Naota writes at most 5 profiles every 5 minutes, so it does not burn through your plan in one go.
### Security
- **The owner's bot fetches nothing from strangers.** Photos, voice messages and files are downloaded only for a chat that has been allowed.
- **Forged WeChat messages stop at the door.** Naota checks the signature of every message, refuses a request more than 15 minutes old, and an account in Safe mode accepts encrypted messages only.
- **Read-only connections stop asking for `mcp:write` style scopes.** On a discovered sign-in where the server offers a read scope (for example `mcp:read`), a connection set to read-only leaves out scopes whose name ends in `write`. The hub's tool-name check stays the main guard. Raising the level later needs a new sign-in.

## [1.33.0] - 2026-11-11
### Improved
- **A tidier composer on a phone.** The plan usage ring, the model name and the effort level are now one pill (for example "Opus 5.5 Medium"), and the model name is no longer cut down to "Op...".
- **Tapping the pill opens one sheet from the bottom** with all three: plan usage (one line per window), the effort slider with Fast mode, and the model list with its search box. Picking a model closes the sheet; so do X, the dimmed area and pulling it down.
- A computer keeps its three buttons and three small popovers as before.
- **Phone: the model picker moved into the input card, right next to the effort picker**, just like on a computer. Tapping it opens the model list right above the card, never wider than the screen.
- **A cleaner top bar:** only the menu button, the notification bell and the + for a new conversation remain.

## [1.32.0] - 2026-11-11
### Added
- **A "Same assistants, confirm all" button per pack** on the Collaborators page. When Naota still has to ask about several assistants of one pack, one click answers for all of them.
- **Click a file Naota made outside the brain to open it.** For example, a deck in ~/Documents. The chat used to show the file name as plain text. Now the full path is a link that opens the file in its default app on the computer, like a double click in Finder.
- The link appears only when you use Naota on the computer that runs it. On a VPS, through a domain or in Docker, the path stays plain text you can copy, as before. Links only open files inside the home folder. Programs and scripts never run; Naota only shows the folder that holds them.
### Fixed
- **Reinstalling a Store pack no longer asks to confirm Auto for each assistant.** Uninstall a pack and install it again and Naota takes its assistants back as the same ones: Auto switch, goals and conversations stay. A file you wrote yourself under an old assistant's name is still asked about, as before.
- **An assistant with Auto off and no open goal no longer shows "Needs confirmation"** when its file goes missing and comes back.
### Improved
- **Welcome screen: the password is typed twice.** When the two boxes differ Naota says so at once and takes you to the box to fix, before any account is created. One mistyped character no longer locks you out of a fresh install.
- **An eye button shows the password.** One tap shows both boxes so they are easy to compare, another tap hides them again.

## [1.31.0] - 2026-11-11
### Added
- **The inbox says when a bot reply did not reach the customer on personal Zalo.** A reply used to show in the inbox as sent as soon as the bot had written it, even when Zalo refused it or the send timed out. A reply that went out now shows nothing extra. One that was not sent, one whose outcome is unclear, or one dropped because the customer wrote again gets a small line under it, with the reason. A reply stuck on sending for more than 5 minutes turns into outcome unclear.
- **Large tool results no longer lose their middle.** Naota stores the full copy, hands the model a compact view with a reference, and the model reads back exactly what it needs. Reports stop missing orders and cost fewer tokens on every brain.
- **Computed by code, not by eye.** The `naota_query` tool pages through a source by itself, then sums, counts and ranks with read-only SQL. A large or a small model gets the same number.
- **A scout on the background model.** A read across several sources can go to the background model (`naota_scout`); only its findings return to the chat. A scout reads, it never sends or creates.
- **Recurring jobs remember how to get their numbers.** After the same run on two different days, Naota fetches the data itself next time. When the dates are not certain, the job runs as before.
### Fixed
- **A connector that cannot start is no longer reported as "sign-in expired".** Naota recognised a sign-in error by looking for 401 in the error text, so when the install path happened to contain 401, a "file not found" error was shown as a prompt to Reconnect. 401 (and 502, 503, 504) now count only when they stand alone as a status code.
- **Uninstalling a Store pack now says which brain its items are in.** A pack's assistants and skills go into the brain that was open at install time. Uninstalling from another brain removed them there, and the confirmation did not say which brain that was.
- The pack's card also says when its items are in a brain other than the one open, instead of a bare "Installed".
### Improved
- **Tool search answers are smaller**, and Suggestions on the Usage page says how much of the tool results stayed out of the conversation.

## [1.30.0] - 2026-11-11
### Added
- **Each brain pins the tools it uses most.** When a brain has many sources connected, a tool must be searched for before it is called, one extra round each time. Naota now counts which tools each brain calls most and pins a few of them (up to 4 by default; Naota Core widens that up to 8 when needed): a pinned tool is called directly. Background work such as loops gains the most, because it had to search again on every run. Nothing to set up, and a notice in the bell tells you when tools are pinned.
- **See and switch it off by talking.** Ask Naota "which tools are pinned" for the list with how many calls went direct and how many still needed a search. Say "stop pinning tools" to turn it off.
- **The background model has an Automatic mode, and it is the default.** Background work used to run on the provider's default model, which on a plan is usually the strongest and costliest. Naota now uses MAIN's provider and picks two models from that provider's own list: a light one for the work Naota starts itself (self-learning, next-message suggestions, judging), a middle one for the jobs you hand over (reminders, loops, Kanban). The Models page names both. Naota picks again only when that provider's model list changes, and leaves a notice in the bell each time.
- **Each background job finds the model that is just enough for it.** The two models above are only where a job starts. Every reminder, loop, kind of Kanban job and self-learning has its own rung: a failure caused by a model that was too weak climbs one rung for the next run, several good runs in a row try one rung lower, and a failed try goes back up. A spent quota, a lost sign-in or a dropped connection does not change the model. Each change leaves a notice in the bell with its reason.
- **Adjust background work by talking; there is no setting.** Say "save tokens for me", "the report job must be reliable", "this morning's report was wrong" or "which model is background work running on": Naota records what you want for everything or for one job, adjusts, and undoes a model change when you ask.
- **A model you choose yourself is never changed.** Press Change model in the Background model block and choose one: it stays. To go back, choose "Automatic (recommended)" at the top of the list. On existing installs, a background model still on its starting setup moves to Automatic; one you had changed stays as it is.
- **Naota's own work waits when the plan is nearly used up.** Once the plan's 5-hour window is 80% used, self-learning and next-message suggestions wait for the reset, and what is left is kept for your chat.
- **Naota Core runs one improvement loop.** Any part of Naota that wants to tune itself registers a "knob" with Naota Core. The loop moves every knob the same way: one step at a time, inside its bounds, at most once a day, with its reason logged, a notice in the bell, and a way back by talking. The loop is plain code: it calls no model and does not touch a chat turn.
- **Self-learning tunes when a batch starts.** When most recent batches learned nothing (common when you ask one or two quick questions), Naota Core raises the number of turns a batch needs; when batches are useful again it lowers it. Turns below the bar stay queued and are learned with the next ones.
- **Tell Naota how to learn, by talking.** Say "do not turn each day's revenue into a memory" or "only remember settled decisions": Naota Core keeps it as a lesson and every learning batch reads it first. Review and revoke it like any assistant's lessons.
### Improved
- **The pinned list follows your habits.** A tool you stop using leaves the list and a newly frequent one joins. One brain's list changes at most once a day and has a size bound, so the prompt does not grow and the provider's cache is rarely refreshed.
- **What you tell Naota Core stands.** A value you set by talking, for any self-tuning knob, is not changed back by Naota Core for 30 days, restarts included.
- **Self-learning learns memories and wiki notes only by default.** Skill learning adds a second verify pass to every batch and switches on the background skill judging, the costliest part while you are not typing. Existing installs were switched off once too; turn the Skill switch on the Self-learning page back on if you need it.
- **Self-learning runs 15 minutes after the last event, once per conversation.** A batch used to fire every 3 chat turns, so a 12-turn chat opened four batches that each re-read much the same messages. Naota now waits until the brain has been quiet for 15 minutes (you asking again, a background job finishing or a customer talking to a chatbot all start the wait over) and learns in one batch, reading each message once. A day with no event learns nothing and costs nothing. "Remember this" is still learned after 30 seconds, and a brain that is never quiet (a chatbot with customers all day) still learns after 2 hours at most.
- **The daily ceilings of self-learning are gone.** 40 batches and 15 million tokens a day fit neither a heavy user nor a light one, and at the ceiling Naota still ran the batch and only kept its result from being written. The new rhythm already ties the number of batches to the number of conversations.
- **Next-message suggestions and other text-only turns are much lighter.** These turns (the suggestion after every chat turn, the reply judges, incident triage, habit lines) use no tool, yet still sent Claude Code's own rules and every tool description. The measurement already in the code for the same question: 27,665 tokens with them, 183 without. They are no longer sent.
- **A wrongly learned memory counts.** A memory Naota learned by itself that you ask it to forget counts as a learning mistake, so the next batch runs one model stronger. Forgetting a memory you wrote yourself changes nothing.
- **One place to look and to undo.** Ask Naota "what is background work and learning adjusting": one answer with the model of each background job, the knobs being tuned, the recent changes and the lessons about learning.

## [1.29.0] - 2026-11-11
### Improved
- **Personal Zalo: a message is read the moment it arrives, no more scan every 20 seconds.** Naota used to ask Zalo all day even when nothing came in, and a group message waited up to 20 seconds before a bot saw it. A message is now read when it arrives; on a day with no message nothing is read.
- With no message Naota runs no timer for Zalo at all. When the Zalo process stops, Naota restarts it at once and catches up. A machine still on the older Zalo version keeps the timer and loses nothing.

## [1.28.0] - 2026-11-11
### Added
- **A scheduled task now sends the pictures it just made.** A recurring report drawn as an image (ads, sales on a fixed template) used to reach Zalo Bot and Telegram as text only, while the picture stayed in the brain. Images named in the answer and created during that run now come with it, up to 4 per run.
- Zalo Bot only takes images, so PDFs and spreadsheets are unchanged. A picture that fails to send does not fail the reminder: the text still arrives.
### Fixed
- **A recreated assistant can confirm its Auto again.** The card said "Auto: Needs confirmation", but the right column had neither "Same assistant" nor "This is a new assistant", so Auto could never be turned back on. Both buttons now show right under the assistant's settings.
- **The Models page no longer slows the app down over time.** Every visit left a set of drag listeners behind that was never removed. One shared set remains.
- **Chatbots on a ChatGPT plan now move to the next account when one runs out.** A dedicated bot always called with account 1 and ignored the account order on the Models page, so it failed with a 429 while another account still had usage.
- A bot only switches accounts before it has said anything or called any tool, so customers never get a duplicate message.
- **Claude answers again on Windows machines that installed it with npm.** After an update every Claude chat turn failed with "Refusing to execute batch script ...claude.CMD". Naota now finds the real `claude.exe` next to that file (or the native install, or the one bundled with the SDK), so nothing needs reinstalling. Codex was not affected.
- **Codex runs at the chosen reasoning level right after Naota restarts.** Until someone opened the Models page, bots and background jobs on Codex fell back to Codex's own default (usually high) even when low or medium was set, which was slower and used more of the plan.
- **A scheduled Codex job is no longer dropped because the tool hub came up late.** A hub that took over 20 seconds used to cost the whole reminder or recurring run until its next slot. Naota now waits up to 45 seconds and tries once more after 30 seconds. The failure happens before the model is called, so the retry costs no turn and repeats no action.
- Restore Edit configuration for custom MCP connections signed in with OAuth. URL edits retain authentication and prevent forwarding OAuth credentials to another origin.
- **Claude Fable 5.2 is in the model picker.** The Claude model list used to come only from the installed Claude Code, so a machine whose Claude Code had not updated yet missed new models even after updating Naota. The list now also includes the models this Naota release knows, newest first.
- **Claude Haiku 5.5 joins the fallback list and the cost estimates are corrected** for Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5 on the Usage page.
- Lazy Hub tools accept JSON-encoded arguments so compatible gateways can preserve dynamic fields. Invalid arguments are rejected before dispatch, with existing permission checks preserved.
- **A group bot drops the wrong "missed" labels it learned earlier.** This version stopped new wrong labels, but the old ones stayed in the store and kept pushing the bot to talk. The first time the store opens after the update, Naota removes "missed" labels put on reactions, gives the affected groups their threshold back, and stops treating labels it inferred from an owner's message as something the owner taught.
- What the owner really taught (a thumb, telling the bot to stop, a lesson in chat) is kept.
- **A group bot no longer teaches itself to answer reactions.** An owner's heart on a customer's message, or two reactions in a row from one person, used to count as the bot having missed the earlier message, which made it talk more in exactly the groups where staying quiet was right.
- "up" inside an ordinary sentence and the Vietnamese for "ask again" inside a long instruction are no longer read as a customer asking again.
- A label the bot inferred from an owner's message no longer weighs as much as something the owner taught it directly.
- **Teams no longer stay stuck on an account that ran out.** With several accounts on a Claude Code, ChatGPT or Grok Build card, a team member's turn now runs on the account that still has quota, like chat and background work. Before, teams always ran on account 1, so once it hit its weekly limit the whole team answered "You've hit your weekly limit" while the other account still had quota.
- **A team turn that runs out of quota runs again on the next account.** When the account refuses before any tool call, Naota rests it and runs the turn again at once, and the reply says which account answered. A step that already called a tool is not run again, so nothing is sent or posted twice.
- **The out-of-quota sentence is no longer posted as a member's reply.** Claude Code sometimes prints it as a normal answer; teams now recognise it and treat it as an out-of-quota error.
- **Workflows rotate accounts too.** A workflow step on Claude Code or ChatGPT starts on the account that still has quota; when the account runs out before the step did anything, the step runs again on the next account and the run carries on. Before, the whole run stopped with "the plan is out of quota" while the other account still had quota.
- **The card on the Models page names the account in use.** Its first line shows the name, e-mail and plan of the account that is running. Before, it always showed account 1, so a card running on a Max account still read "Pro".
- **A workflow step now runs at its assistant's reasoning level.** The level set on an assistant only applied to its chat and team turns; a workflow step, including a Kanban job routed to a workflow, always ran at the model's default. A step whose assistant set no level runs as before.
### Improved
- **Long answers stream without stutter.** While text is arriving, Naota only redraws the block being written and leaves the finished ones alone. Measured with a 20,000 character answer on a slow phone: render time from 5.4 seconds down to 1 second, and no more freezes.
- **The home screen rests lighter.** The starfield behind the sphere draws less often when nobody is speaking and Naota is not thinking, and looks the same. A phone left open runs cooler and uses less battery.

## [1.27.0] - 2026-11-11
### Added
- **The Claude Agent SDK updates itself.** The "Update Claude Code automatically every day" switch on the Models page now also keeps the Claude Agent SDK package on the newest release of its series. Naota only takes a release at least three days old, checks it before keeping it and puts the old one back if the check fails. The new version is used from the next restart. The Docker build still gets it with each Naota image.
### Fixed
- **Connecting Google Ads no longer demands a developer token.** The box is optional now and the guide follows the Google Cloud path: enable the Google Ads API, apply for Explorer access inside the project, then create the OAuth client. New users are no longer stuck asking for a token Google no longer requires.
- **Chat images no longer turn blank after 30 days.** A sign-in used to expire exactly 30 days after login however often it was used; chat kept working while images and lists silently failed. A session in use now renews itself.
- **A sign-in that expires mid-use brings up the sign-in screen** instead of leaving the page quietly broken.
### Improved
- **Chat is lighter on the disk, and one broken connection no longer slows every turn.** Each chat turn forces far fewer disk syncs (most visible on a VPS). When a data source hangs twice in a row, Naota answers at once with the tools it has and retries in the background.
### Security
- **Google Ads label tools no longer run at Read only.** Google's newer MCP adds tools that create, edit and delete labels and upload a video to YouTube; the two label tools were wrongly classified as read. They now need Full access, creating assets needs Draft writes, and the connection card says what each level can change.
- **Tighter chat rendering, tool hub and background runs.** Text in a message can no longer slip code into the dashboard. The tool hub only answers the machine Naota runs on. A run at the Draft level only writes ordinary files inside the brain.
- **A customer chatbot below Full access can no longer queue work for the AI to run later.** It can still create a reminder that only says its text. Raise the bot to Full access if it should queue work itself.
- **A brain imported from a file always arrives at rest.** Loops, plugins and reminders are off however the file spells them, and engine settings that run commands are not imported. The PDF library moves to a patched release.

## [1.25.6] - 2026-11-10
### Fixed
- **The AI cost tile on the Office page now shows only money actually spent.** It used to add the API-equivalent price of turns run on a monthly plan (Claude Code, Grok), so a Pro or Max plan showed tens of dollars that were never charged. It now adds only what API keys are billed; plan turns are still counted, at $0.

## [1.25.5] - 2026-11-10
### Fixed
- **The logo no longer breaks when the server's network is shaky.** The browser used to keep the logo for 1 minute only, so a reload during a network drop showed a broken image on the start-up screen and the sidebar. The logo is now kept for a long time, and a new logo is picked up on its own.

## [1.25.4] - 2026-11-10
### Fixed
- **Opening or reloading the page is fast again, about 1 to 2 seconds.** The "Starting Naota..." screen used to stay a full 12 seconds every time, waiting on the "Loading more..." line at the end of the chat list, which never goes away. The start-up screen now skips that line.

## [1.25.3] - 2026-11-10
### Fixed
- **No more codes like `page.chat.label` or `app.pin_meta` in place of text.** Left menu tooltips, file tree buttons and the line under a pinned file in the chat box used to stay as codes when they were drawn before the text dictionary arrived. They now switch to real text as soon as it does.

## [1.25.2] - 2026-11-10
### Improved
- **The node and link counts move into the top-left corner of the brain map**, out of the top bar. The eye button hides them with the folder labels.
- **The brain picker shows the node and link counts on one line**, no longer split in two.

## [1.25.1] - 2026-11-10
### Improved
- Tidied sample data in the tests and the pronunciation dictionary.

## [1.25.0] - 2026-11-09
### Added
- **Every chat in the history column has a ⋯ button** instead of four separate icons. The menu: Pin to top, Move to project, Rename (in place), Share link, Export as .md, Mark as unread, Archive and Delete. Right-click, or a long press on a phone, opens it too.
- **Archive a chat:** it leaves the list but keeps every message; Naota still remembers it and search still finds it. "Archived" at the bottom of the column lists them, and a new message brings one back.
- **Choose which brain is the default.** Tap the star on a brain in the picker. The old default then becomes an ordinary brain and can be deleted (to the trash for 30 days).
- **Deleting a brain says first** how many loops and reminders stop with it and which bots answer from it.
- **Connecting GitHub checks for git and installs it when missing**, before the sign-in step. If it cannot, it shows the command to run by hand, Try again and Skip.
### Fixed
- **Notice times follow the timezone in Settings**, not the server clock (UTC on a VPS).
- **Workflow steps on a Claude agent get every Naota connection**, no more "missing tool" for Gmail, Sheets, Zalo or other MCPs.
- **Chatbot page, Conversations shows only the open brain's chats**, counts included.
- **git installed while Naota runs is found right away**, no restart needed.
- **The install button in the left menu foot no longer overflows** on touch tablets and laptops.
### Improved
- **Changing the password asks for the new one twice**, and saves only when they match.
- **The graph screen and MCP tool lists no longer freeze the app every few minutes.**
- **Delete asks inside the menu**, suggesting Archive if you only want it out of the way.
- **No more "Show more":** scrolling to the end loads the next page.
- **Tidier chat rows:** a pinned chat has a small pin before its title.

## [1.24.0] - 2026-11-09
### Improved
- **A tidier Account page.** The page header is gone, the Account and Security tabs sit right at the top.
- **CLI API tokens moved to the Integrations page** (Work group, formerly Webhooks), tab API token. Both are doors for another program to call Naota, so they now live together. Existing tokens keep working.

## [1.23.0] - 2026-11-09
### Added
- **File editors save by themselves, like Google Docs.** About a second after you stop typing the file is saved, and the Save button shows "Saving…" then "Saved". Closing, switching files, reloading or a stray Back swipe no longer loses typed text.
- **Text survives a lost connection.** Unsaved text is kept in the browser and restored the next time the file opens.
- **A dictation mic in the .md and .txt editors.** Press, speak, and the words land at the cursor, rewritten in context, like the mic in the chat box.
- **Export and upload a whole brain as one .zip file:** each row of the brain picker has an Export button. The file carries notes, images, agents, skills, workflows and memory, and leaves out tokens, keys, raw chats and git history. "Upload a brain (.zip)" always makes a new brain and never overwrites one. Plugins, loops and reminders that come with the file arrive switched off; turn them on where they live if you want them. There is no fixed size limit: the server takes what its free disk can hold, up to a million files. Packing and unpacking run in the background with progress, and the upload goes in 32MB pieces, so a large brain still gets through Cloudflare Tunnel.
- **Rename and delete right on each row of the brain picker**, with New brain, Upload a brain and Open an outside folder at the bottom. The four separate buttons beside the picker in the top bar moved into it.
### Fixed
- **Text blocks (such as an email draft's TEXT block) wrap** instead of running off to the right. While editing, a sideways touchpad swipe no longer sends the browser Back.
### Improved
- **Start-up screen:** opening Naota shows the logo and "Starting Naota…" until the first page has its data. Right after an update or a restart it also says the first open can take a little longer.
- **Every screen that waits for data uses the Partners page's loading look:** a small spinner with "Loading", or a centered one for a whole page. A page still loading no longer says "in development" by mistake.
- **The node and link counts in the top bar show only on the neural graph screen**, so other pages are tidier.
- **The brain picker shows each brain's node and link counts**, as its graph counts them. They are counted only when the picker opens, so page load is not slowed.
- **The Partners and Teams pages show "Loading…"** where a list or a conversation has not arrived yet, instead of an empty space that looked frozen.
- **A team opens with its Info tab showing** in the side panel on a wide screen. Close the panel and Naota remembers it next time.
- **Team search, settings and close buttons look cleaner:** square, borderless, in the same style as the tabs beside them.
- **The team list loads about 2.5 times faster**, and opening a team takes the same time whether it holds a hundred or tens of thousands of messages.

## [1.22.0] - 2026-11-09
### Improved
- **The app opens noticeably faster.** The ~110 interface files loaded at startup now travel as one bundle. With 150 ms of network delay the Partners list shows after about 2 seconds instead of nearly 5.
- **No stall on the first page after a restart or an update.** Minified files are kept on disk; only files that just changed are minified again.
- **The Partners page no longer waits in a queue.** The reads for the list, the Resonance status and background work run off the main loop and stop holding up other requests.
### Fixed
- **ChatGPT (Codex) keeps its tools when a chat resumes after a few idle minutes.** Calendar, Zalo and Drive work on the next turn.
- **On Windows, Codex background work at the "Can write" level writes files again.**
- **Memories no longer break or lose their details after a chat turn.** A memory with a colon in its description keeps its type, description and tags. A memory already broken heals when edited in the app.
- **Ollama Local runs Team jobs and background work.** No more "engine is not ready" when Ollama at home has no key.
- **Behind Caddy (Hostinger VPS) the Facebook sign-in button is no longer locked.**
- **The CapCut card signs in.**
- **GitHub in chat uses the saved check commands** and understands apps in a subfolder.
- **Opening a chat on the Partners page no longer says "taking too long" by mistake.** No error while the page is reconnecting. A Naota Core open that hangs shows the error with Retry, and Retry really loads again.
- **Background work on ChatGPT (Codex) that was refused file writes now says it is an environment problem**, with what to change, instead of sitting in "waiting for your answer".
- **Memories written by background work no longer get the source of a chat** that happened to be open at the same time.

## [1.21.0] - 2026-11-09
### Added
- **Personal Zalo bots show "typing..." in groups.** It starts only after the bot has decided to answer (it was called, or the judge chose to speak up) and lasts until the reply is sent, so a group no longer sits in silence for 20-30 seconds. A message the bot leaves alone shows nothing.
- **An on/off switch in each bot's settings on the Chatbot page**, on by default.
### Fixed
- **Zalo's Import old messages button actually imports.** Any chat with even one message in the Inbox used to be skipped, so on an account already recording conversations the import added almost nothing. A chat that has messages now gets the ones older than its first message, placed above it in time order.
- Imported old messages do not land at the bottom of an open chat, the bot does not take them for new messages, and groups still keep only their latest messages.
- **Private-chat "typing..." no longer goes quiet for an hour.** One chat that Zalo refused, or an MCP restart, used to switch it off in every chat of the account for an hour. Now only that turn loses it, and it lasts until the message has gone out.
### Improved
- **Opening the neural graph no longer freezes the whole app.** The graph's file watcher is built on its own thread, so a brain with many folders no longer makes everything else wait up to 2 seconds.
- **Every outgoing connection shares one set of security certificates**, loaded once at start-up. Before, each outgoing call (Telegram, Zalo, models...) loaded the whole set again, once freezing the app for almost 2 seconds.
- **Reading the personal Zalo history runs in the background.** Looking for missed messages in the history file no longer blocks anything else.
## [1.20.1] - 2026-11-09
### Improved
- Third-party docs cleanup.

## [1.20.0] - 2026-11-09
### Added
- **The chat shows the engine's task plan as a checklist.** When Claude Code, ChatGPT (Codex) or Grok Build plans a multi-step job, a "Plan 2/5" card appears above the answer: done items ticked and struck through, the running one in bold, the rest open. The activity line under the chat says which step it is on. The card stays after a reload and costs no extra tokens.
- **The seven API-key brains show the Plan card too.** OpenRouter, OpenAI, Anthropic API, Gemini, Groq, DeepSeek and Ollama get a `naota_plan` tool: for a job of three steps or more the model lists the steps and ticks each one off. It costs about 200 tokens a request; switch it off in the composer **+** menu, **Plan long jobs (API brains)**. Only the owner's chat gets it, not customer bots or background jobs.
- **The Jobs tab on the Partners page shows what the assistant is doing in the chat**: a "Working in the chat" card with the step count and the plan, gone when the turn ends.
- **The Jobs tab lists the workflow runs the assistant took part in.** A running one says which step and whose, one waiting for review sits under Needs you, a failed one is marked failed, and Open goes to that workflow. The source filter gains "Workflows".
- **Each chat in the left column carries a small folder tag with its project name.** The tag hides while the list is filtered to that one project.
- **The engine tag names the brain:** "Claude", "Codex", "Grok", "OpenRouter" and so on instead of internal ids such as "cli".
### Improved
- **Answers stretch across the whole chat** instead of leaving a wide gap on the right. On the Partners page on an iPad an answer grows from about 780px to over 1,000px; on a very wide monitor it stops at about 120 letters per line. The Chat and Teams pages follow the same rule.
### Fixed
- **The status dot on an assistant's card agrees with its Jobs tab.** A job you pressed Done on or deleted no longer lights the green or red dot.
- **A workflow run cut off mid-way** (the server stopped during it) no longer stays In progress for ever.
- **Reinstalling a Store agent brings it back on the Partners page.** Renaming or editing a pack's agent, uninstalling and installing again used to skip it. Your copy is kept and the pack's copy is added under a new name, shown on screen.
- **Deleting a pack's agents, workflows or skills in the app makes the Store stop saying "Installed"**, and the card offers Install again. Uninstalling a pack also cleans up a turned-off skill and the copy Claude Code loads.

## [1.19.0] - 2026-11-09
### Security
- **To do after updating:** open each chatbot's Agent, add the price lists, policies and guides the bot should read, then press **Try** to make sure it still answers well. A bot with no listed file answers from its Agent's role only.
- **A bot reads only the documents in its Agent's Documents section**, plus the `rieng-theo-nhom/` folder and the Google files linked from the Agent. Before, every note of the brain counted as a document, so a bot could quote the owner's private notes to customers.
- **New Security tab on the Account page.** See 2FA, the devices signed in (IP, browser, last activity) and the history of successful and failed sign-ins and every account change. Sign out one device or all others without changing the password.
- **Instant alerts on account changes.** Username, password or 2FA changes and sign-ins from a new network reach the owner's bell and Telegram right away.
- **If the settings file is edited outside NAOTA**, every device is signed out and a red warning shows. The first start on this version only records the current account and signs no one out.
- **The AI assistant can no longer touch secret files** (settings, encryption key, sessions) at any permission level.
- **Removing 2FA when locked out:** add `NAOTA_RESET_2FA=1` and redeploy. Each value works once.
- **Hostinger: port 7777 closes to the Internet once an HTTPS domain is set**, leaving only the encrypted way in.
- **A leaked admin link stays out of Google.** Every NAOTA page now carries `noindex`, the login screen and share links included.
- **AI bots cannot read NAOTA.** GPTBot, ClaudeBot, PerplexityBot, SEO tools and scanners such as Shodan and Censys get a 403. NAOTA also serves a `/robots.txt` that forbids them.
- Real browsers, link previews in Zalo or Telegram, the Meta, Threads and Zalo OA webhooks, `/s/` share links and Naota Gate work as before. To turn the blocking off, set `NAOTA_BLOCK_BOTS=0`.
- **Account security files stay out of git and Docker images** when you run `git add -A` or a local `docker build`.
### Fixed
- **Bot document lookups, auto learning and reminders no longer freeze the app for seconds.** They run on worker threads and no longer walk the whole brain.
- **The Partners page no longer waits on the Resonance data lock**, and the connection catalog is no longer re-checked on disk at every call.

## [1.18.0] - 2026-11-09
### Fixed
- **A failure that needs you is now an urgent notice.** It used to be "important", and the default notice filter sends only urgent ones to Telegram, so on a fresh install a failed job never reached your phone. You can still turn the Incidents group down in Notifications.
- **A failed job now always reaches the owner's Telegram.** A job made in a web chat that fails and needs you used to report only to that chat; it now also sends one message to your Telegram, so you hear about it away from the computer.
- **A Team job that is blocked, fails or waits for your approval** used to stay in the bell only; it now also goes to your Telegram.
### Improved
- **No more overlapping text in the 3D Office.** Each desk's name sits on that desk, never wider than it, and a long name wraps onto two lines. Where two cards meet on screen, the more important one stays (department, running job, failed job) and the other hides until you zoom in.
- The **Needs you** section of the Office page says whether failure alerts reach Telegram. With Telegram not connected it says the alerts stay in the bell, with a button to Settings.

## [1.17.0] - 2026-11-09
### Added
- **Meeting room in the 3D office**: while a team leader splits a job or sums it up, the whole team walks into the meeting room and sits round the table, then walks back to their desks.
- **Talk bubbles** over an assistant speaking in a team: splitting the work, talking, working for the team, helping.
- **News ticker** under the 3D office: who just gave what to whom, which run just passed or failed, newest first.
- **AI cost of the day** joins the numbers at the top, with the number of AI calls. It covers the whole server; engines on a monthly plan count 0.
- **Each department sign** now adds its assistants, runs and failures of the day, and each department has **glass walls** on three sides, the front left open.

## [1.16.0] - 2026-11-09
### Added
- **Office: see assistants hand work to each other.** A new **Handoffs this day** list shows who gave what to whom, when, and whether it is in progress, done or failed. It reads team leaders assigning members, members asking each other for help, board cards given to an assistant, and workflow steps passing work along.
- **In 3D** each handoff is a sheet flying along a dashed route from the giver's desk to the receiver's, with the job's name; the receiver starts typing. Work you hand out leaves from the **You** figure at the front of the office. **Replay this day** plays the handoffs too, at their real times.
- An assistant working on a team step or a board card lights its desk and shows in **Running right now**. New work handed out reloads the page at once.

## [1.15.0] - 2026-11-09
### Added
- **3D office**: press **3D view** on the Office page. One area per department, one desk per assistant and per automated job, each lamp in the job's real state.
- **Tap a desk** to see that job: runs passed, last run, why it stopped and what to do.
- **Running right now**: a strip at the top of the Office page shows what runs at this second (loops, schedules, board tasks, background commands), since when and for how long. It asks the system every 5 seconds and the clock counts each second.
- In 3D a running desk turns its **lamp blue**, shows a **Running** tag and its worker keeps typing; when the run ends the lamp shows the result and a Pass or Fail mark appears at once.
- **Replay a day**: pick a day and press **Replay this day**; each run appears in order with a Pass or Fail mark over its desk.
- Workers move only when the logs show a new run. The 3D part loads only when you ask, and a device without 3D keeps the cards.

## [1.14.0] - 2026-11-09
### Added
- **Office page** (sidebar, under Tasks): one card per department. Green runs right, blinking red is broken or paused itself, grey means nobody.
- **Needs you list**: jobs that paused, failed, ran late, missed a target or wait for review, with the reason and what to do.
- **Real numbers from the logs**: runs and failures in your time zone, refreshed every 30 seconds; pick a past day to look back.
- **Daily targets** live in `Naota/office.json`. The page only reads, and hides tokens and server paths.

## [1.13.1] - 2026-11-08
### Fixed
- **Zalo messages after a short connection drop** now reach the inbox, not only the chat history.
- **One Zalo message that fails to process** no longer takes the messages that arrived with it down too.
- **Zalo connection errors are written to the log** instead of being ignored, so a lost message leaves a trace.

## [1.13.0] - 2026-11-08
### Added
- **The ChatGPT plan hears your voice**, at no cost beyond the plan. The ear follows the model in use, nothing to set.
- **Zalo OA connects with Zalo's OAuth v4 sign-in**, no pasted refresh token.
- **Accept or send back a job** that failed its automatic check, right from chat.
### Improved
- **GitHub cross review is your call**, off by default, on the chat's own model or the model picked on each card.
- **A job that fails its automatic check** goes back to the worker instead of asking you an empty question.
- **Dictation keeps running** when you switch tab or app.
### Fixed
- **After an update the dashboard stays on your brain**, so teams no longer vanish.
- **The Partners page chat box** no longer stays locked after an update.

## [1.12.0] - 2026-11-08
### Added
- **Admin channel chats** show in the history of Naota Core and of the linked agent, the owner's Zalo bot included.
- **Agent cards show their tags** on the line under the name, next to the avatar.
### Improved
- **Chats and pages open instantly** from what this browser saw before, then update once the server answers.
- **App start, page and chat switches** read everything they need in one round trip.
- **Chat turns, Kanban jobs and heavy page reads** no longer slow down other clicks.
- **Read aloud** picks an English or Vietnamese voice by the answer's language.
### Fixed
- **The iPhone app (iOS 26, 27)** no longer shows a blur strip at the top. An icon added before needs to be removed and added again.
- **Customer chatbots stay silent** when the Claude plan hits its monthly spend limit, instead of sending the English error to a customer.

## [1.11.0] - 2026-11-08
### Added
- **Name each account** at its first sign-in and rename it later, so two accounts never read alike.
- **Upload your own avatar picture** and use it as the browser tab icon, so several NAOTA side by side are easy to tell apart.
- **Chat over the API without waiting** (`POST /chat/jobs`): send the job, come back for the result later.
### Improved
- **The provider list on the Models page** opens in place, not in a separate sheet.
- **An assistant's role** sits in an (i) button next to the name, no more grey line cut off halfway.
- **The Team page** folds its explanations and the team description into the (i).
- **Voice calls with a partner** keep long instructions and pinned rules.
- **No more time caps** on Grok, Claude Code, ChatGPT, background work and Teams: long jobs run to the end, the Stop button still works.
- **Pages and chat switches no longer freeze** while background jobs write.
### Fixed
- **Missing private Zalo messages** are caught up from the history, only when the history really has new ones.
- **Zalo voice messages** are heard again by Groq and OpenAI.
- **Antigravity** no longer stops at 15 minutes.
- **A chat that moves to a second Claude account** no longer dies with "ProcessError exit code 1".
- **A merged PR** no longer keeps the chat's "waiting for checks" icon.

## [1.10.0] - 2026-11-08
### Added
- **A suggested next message** shows faded in the empty chat box, press Tab to fill it in.
- **A red unread dot** on every chat history list, gone once you open that chat.
- **Pick a ChatGPT Live voice** for each partner.
- **Turn scheduled jobs off on one machine**, so two machines on the same brain do not run the same job twice.
### Improved
- **A voice call with a partner** introduces itself as that partner, not as the main assistant.
- **A workflow agent** with no model of its own runs on the main model instead of falling back to Claude.
- **The Chatbot page** opens faster on a big inbox.
### Fixed
- **Chat no longer gets stuck on "Lost the connection"** after one failed message or an expired sign-in.

## [1.9.0] - 2026-11-07
### Added
- **Share links page rebuilt:** change the address after `/s/`, see views per link, search, filter, sort and page through them.
- **A QR code** for every share link.
- **Cloudflare is a built-in connection**, next to GitHub, by token or web sign-in.
- **One priority star a day.**
- **Sounds when you tick a task**, with an on/off switch next to the light/dark button.
- **A missed habit** gets Skip and Delete buttons.
- **Everything in Mine now reaches the notifications**, not just part of it.
### Improved
- **Dictation rewrites the sentence:** words appear right in the chat box, and when you finish a model rewrites them in context before sending. On any error the sentence stays as heard.
- **The mic hears AI names right**, such as Groq, Claude and Gemini, without pushing your own words aside.
- **A failed GitHub push retries itself**, and resumes as soon as GitHub is connected again.
- **A GitHub merge keeps running** when the panel or tab is closed.
- **The GitHub repo list** takes the look of the Tasks page.
- **The chat's model chip** shows the model really answering during a fallback.
### Fixed
- **No lost messages** when you switch apps right after sending on a phone: a message is kept until the server confirms it.
- **When ChatGPT Live runs out** it moves to another account or call path instead of staying on the exhausted plan.
- **Android** no longer loses or repeats words in dictation.
- **GitHub push from chat** no longer stalls on another OS's check.
- **The chat's GitHub icon** no longer stays orange after a merge.
- **GitHub cross review** no longer picks a plan that can never run it.
- **iPhone:** the menu no longer covers the language picker, and a home screen app takes taps in the right place again.
- **The + button on the Tasks page** no longer covers the last row on a phone.
- **No empty answer bubble** when coming back to a chat that is still running.

## [1.8.1] - 2026-11-07
### Fixed
- **A Zalo account that gets signed out now rings the bell:** the bot used to go silent with the owner unaware, because the error only reached the server log. The bell and Telegram now say which account must sign in again, and the bot card gives the real reason.

## [1.8.0] - 2026-11-05
### Security
- **Several leaks closed after a review:** chatbots and background work below Full access can no longer write where code runs, scheduled jobs cannot exceed their maker's level, HTML files opened from the brain run in a sandbox, and other pages on the machine cannot send commands into NAOTA.
### Added
- **A new Models page:** Disconnect on every card, OpenAI Compatible and Claude Compatible take several keys and switch when one runs out, and Antigravity on a VPS can add accounts (not yet tried with a real `agy`).
- **Naota Core edits like any assistant** and can have its own name per brain. **One bot serves up to 100 Facebook Pages.** The Avatar has a menu you arrange, and a voice call from an assistant's chat speaks as that assistant.
### Improved
- **Background work on an API key runs to the end**, up to 500 tool rounds, with a real terminal at Full access. **Chat can edit every task and appointment** in your to-do list.
- **Faster and lighter:** switching chats, Tasks, Teams and Assistants is instant, the speak-to-type mic reaches the customer reply box, Enter sends, and Android no longer repeats words.

## [1.7.0] - 2026-11-05
### Added
- **My tasks gets a daily pulse**: a Clean day streak, a star on up to 3 priorities, Skip this time for repeats, Move and Delete icons on each row (Undo if you delete by mistake), and a word of praise when you finish.
- **A long answer rings your phone**: from 3 minutes up the bell rings, unless the device is open. A background command reports to the right chat when it ends and carries on with what was planned.
### Improved
- **Scheduled jobs made in a partner chat** report to that chat and run as that assistant, and failures go back there too. Jobs made earlier run as before. Schedules on Codex can now hand work to a Team.
- **The inbox opens a chat at once** and loads only what is new. **Claude plan names are right** per vendor (Ultra, for example).

## [1.6.1] - 2026-11-04
### Added
- **Edit Agent button in the Chatbot form**: edit the bot's Agent on the spot, and what you typed in the form stays.
### Fixed
- **Rules taught to an assistant in chat now reach its bot**: at every permission level, with no need to copy them into the Agent file.
- **Bots read Zalo contact cards**: when a customer sends one, the bot and the inbox see the name and phone number.
- **Read only, Reads documents and Can write bots know the current time**: asked about today or opening hours, the bot no longer has to guess.

## [1.6.0] - 2026-11-04
### Added
- **Threads on the Meta connection card**: replies under your Threads posts reach the inbox and the bot can answer publicly. Each account picks off, inbox only, or bot replies. Threads only lets you hide a reply, not delete it, so NAOTA says that and asks first.
- **Teams do more**: attach a GitHub repo (edits on its own branch, opens a PR, red CI gets at most 3 fix rounds), call `/skill` in the team chat, and members open a job when given one in the chat, at most 5 a day by default.
- **My tasks get Tags and subtasks**: old Projects become tags, nothing is lost. Notes can link to pages, `[[notes]]` and files.
- **Internal API channel (experimental)**: one of your servers asks a Chatbot over HTTP. The key shows once, the bot only reads, and by default only the machine running NAOTA can call it.

### Improved
- **Drag to reorder** projects, pinned chats and tags, the same order on every device. The Naota Core card says which model it runs on and can pick one. Phones get an **Install on phone** button in the menu.
- **Claude Code waits for background work** before it carries on, up to 30 minutes. The answer to a message added mid-turn shows right below it. Antigravity no longer warns by mistake that it could not read the context file.

## [1.5.0] - 2026-11-04
### Added
- **Message a commenter privately** from their comment thread: pick Reply publicly or Message privately above the box. Meta allows one per comment, within 7 days.
- **Instagram in the shared inbox**: tick "Also connect the Page's Instagram" when connecting, and Instagram messages and comments arrive in the same place, with the same bot as the Page.
- **The "..." menu on each chat** now has View profile, Block and Delete chat. NAOTA always asks before Delete, because deleting a comment or a personal Zalo chat really deletes it there.

### Improved
- The Facebook Messenger card is now **Meta connection**, with an icon for each app and a **Disconnect** button on each Page. Past chats stay. Comments and Instagram get their own icons in the inbox.

## [1.4.0] - 2026-11-03
### Added
- **Pick a time zone** in **Settings** (the Language and time zone block) and in the last step of first-run setup. "Today", "yesterday", reminders and report numbers follow it, even when the server runs on UTC. The default is Vietnam time.

### Fixed
- **No more freezing while NAOTA is answering**, and no more "Reconnecting" over and over on a slow device or network.
- **A small server (1-2 vCPU VPS) no longer stalls** because a few slow jobs blocked the whole app. The voice-note listener leaves one core to the server.
- **The Claude 5-hour limit notice shows the reset time in your time zone**, not UTC.
- Windows: `npx` connections no longer break when a path has a space, and `/C:/...` links in answers open.

### Improved
- **New Claude Code chats use less of your plan limit**: the system prompt stays identical between chats, so it is read back from the cache.
- Tables with 4 or more columns in Chat get more width on a computer, while ordinary text keeps an easy line length.

## [1.3.6] - 2026-11-03
### Fixed
- **On a phone, the Update button at the foot of the menu closes the menu**, so the Update page shows right away. The page used to change behind a menu that stayed open.
- **Tapping Advanced on a phone no longer closes the menu**, so the items inside can be picked.

## [1.3.4] - 2026-11-03
### Fixed
- **The Zalo bot notices when it is tagged in a group by the account's Zalo name**, even right after a server restart. NAOTA used to forget that name on every restart, so a tag that did not match the connection name got no answer.

## [1.3.3] - 2026-11-03
### Fixed
- **The Chatbot page names the brain you picked**, instead of the word "brain" or a folder path.

## [1.3.2] - 2026-11-03
### Improved
- **Page titles match the sidebar names**: Brain map, Tasks, Partners, Connections, Models.
- **On phones the brain picker sits at the top of the menu**, so you see which brain you are in as soon as you open it.

## [1.3.1] - 2026-11-03
### Improved
- Version number only. The two changes meant for this release are in 1.3.2.

## [1.3.0] - 2026-11-03
### Improved
- **A new one-column sidebar**: items in blocks with small names (Team, Knowledge, Connections, System).
- **Plainer item names in the sidebar** (Vietnamese interface): brain map, chat, to-do, assistants, data connections, model picker.
- **The version and an Update button always show at the foot of the sidebar**; the button turns yellow when a new version is out.
- **Advanced sits under Account** and unfolds Terminal, Plugins, Webhooks, Logins, Share links and the NAOTA community. Language is picked in Settings. Pages and the top bar stay as in 1.2.1.

## [1.2.1] - 2026-11-03
### Improved
- **The Store has Naota Gate**: ChatGPT and Claude connect to Naota through one pack, read and post into your chats, and keep a log. Machines with the **Naota in ChatGPT** pack see Gate as an update, no need to reconnect.
- **14 Store packs now have English ids**, for example Customer management is `naota.crm`. Installed packs show **Update available** and update in place, keeping their data.

## [1.2.0] - 2026-11-03
### Added
- **ChatGPT and Claude keep a log in Naota.** When you work something out with an outside AI connected to Naota, it notes what you said, what you decided and why. Naota keeps the context and remembers your decisions, at no cost in Naota runs.
### Improved
- The **Learn** page names **NAOTA** throughout: sync NAOTA with GitHub, NAOTA learns from your chats, what NAOTA has learned.

## [1.1.1] - 2026-11-03
### Fixed
- **The phone menu no longer overlaps.** The last items (Connections, Store, System...) used to spill over the language, brain picker and version rows. Everything now sits in order; scroll down to reach it.

## [1.1.0] - 2026-11-02
### Added
- **Desktop installers.** Download Naota-Setup.exe (Windows) or Naota-macOS.dmg (Mac) and open it like any app, no commands to type.
- **Connect a Facebook Page once for three jobs:** press Log in with Facebook and the bot answers Messenger messages, replies to comments under posts, and Naota posts to the Page now or on a schedule. A step-by-step guide is included.
- **Voice messages without Groq:** use an OpenAI or Gemini key, or a listener that runs on the machine itself. The personal Zalo chatbot hears voice messages and looks at videos customers send.
- **Outside AI can hand Naota work:** find, read and send a message into a Naota conversation as if you typed it, which you can watch live and stop at any time.
### Improved
- **Answers appear as they are written** on every brain: Claude Code, Grok Build, Antigravity and the API key brains.
- **Redesigned Webhook page:** a one-line overview, each webhook opens in its own window, and workflows can be searched by name.
- **Brain picker** drawn by Naota, the same on every device, with your own order. An .html file opens on its live page with the code one tab away. A long paste shows a preview first, then you choose to paste or attach it.
- **Teams retry** a step that hit a temporary error, and each part of a plan states which parts it waits for.
### Fixed
- Claude sign-in finishes on its own on a machine with a browser, no code needed. Dropping a file on the main chat works again, memory recall no longer picks up old run logs, and accented file names stay intact on download.
## [1.0.5] - 2026-11-02
### Fixed
- **The Update button on a VPS no longer waits forever.** When the server runs NAOTA as a normal user that may not update itself, the page now shows the error at once, with the manual update command and how to enable the button, instead of waiting 10 minutes and asking for a reload.

## [1.0.4] - 2026-11-02
### Improved
- **New icon set** across the sidebar and the whole app.
- **Mascot** is now called **Avatar**.
- **Updates** has its own sidebar item right under **Account**, with a **New** badge when a newer version is out.
- Leftover "brain" wording in the interface, the Plugins page and the Learn page now reads clearly: brain means your notes vault, AI model means Claude, ChatGPT and the like.

## [1.0.3] - 2026-11-02
### Improved
- The Account and Settings name block and the Models main-card badge now come from translations (Vietnamese: Tên NAOTA, Chính).

## [1.0.2] - 2026-11-02
### Improved
- **One name for the store** in Vietnamese: the Agents, Data sources and Plugins pages now match the sidebar.
- **Fewer English terms in Vietnamese** on the Learn, Models and Account pages. The account name field reads **Your NAOTA name**.

## [1.0.1] - 2026-11-02
### Improved
- **A tidier sidebar.** Every item shows at once, no groups to open. Rarely used pages sit in a folded **Advanced** group and **System** is pinned to the bottom.
- **Clearer menu names** in Vietnamese. Voice commands accept the new names too.
- **A plainer welcome screen.** Pick a brain by the plan you already have, then click **Sign in with Claude** on the **Models** page, no terminal command needed.
- **Home page labels** are translated in Vietnamese (vault, agents, skills, workflows, note counts).
## [1.0.0] - 2026-10-31
### Added
- **NAOTA is born.** Your own AI brain, built by Hoang Ngoc Vuong for the NAOTA community.
