# Changelog

*[Tiếng Việt](CHANGELOG.md) · **English***

VANHANH release history. Newest first.

## [1.25.1] - 2026-11-10
### Improved
- **Documentation links point to the new NAOSO repository.** Install, guide, bug report and security links in README, QUICKSTART, DEPLOY and the docs folder now open the `naoso` repo. Old links redirect automatically.
- **The README title now reads NAOSO.**

## [1.25.0] - 2026-11-09
### Added
- **Every chat in the history column has a ⋯ button** instead of four separate icons. The menu: Pin to top, Move to project, Rename (in place), Share link, Export as .md, Mark as unread, Archive and Delete. Right-click, or a long press on a phone, opens it too.
- **Archive a chat:** it leaves the list but keeps every message; Vanhanh still remembers it and search still finds it. "Archived" at the bottom of the column lists them, and a new message brings one back.
- **Choose which brain is the default.** Tap the star on a brain in the picker. The old default then becomes an ordinary brain and can be deleted (to the trash for 30 days).
- **Deleting a brain says first** how many loops and reminders stop with it and which bots answer from it.
- **Connecting GitHub checks for git and installs it when missing**, before the sign-in step. If it cannot, it shows the command to run by hand, Try again and Skip.
### Fixed
- **Notice times follow the timezone in Settings**, not the server clock (UTC on a VPS).
- **Workflow steps on a Claude agent get every Vanhanh connection**, no more "missing tool" for Gmail, Sheets, Zalo or other MCPs.
- **Chatbot page, Conversations shows only the open brain's chats**, counts included.
- **git installed while Vanhanh runs is found right away**, no restart needed.
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
- **CLI API tokens moved to the Integrations page** (Work group, formerly Webhooks), tab API token. Both are doors for another program to call Vanhanh, so they now live together. Existing tokens keep working.

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
- **Start-up screen:** opening Vanhanh shows the logo and "Starting Vanhanh…" until the first page has its data. Right after an update or a restart it also says the first open can take a little longer.
- **Every screen that waits for data uses the Partners page's loading look:** a small spinner with "Loading", or a centered one for a whole page. A page still loading no longer says "in development" by mistake.
- **The node and link counts in the top bar show only on the neural graph screen**, so other pages are tidier.
- **The brain picker shows each brain's node and link counts**, as its graph counts them. They are counted only when the picker opens, so page load is not slowed.
- **The Partners and Teams pages show "Loading…"** where a list or a conversation has not arrived yet, instead of an empty space that looked frozen.
- **A team opens with its Info tab showing** in the side panel on a wide screen. Close the panel and Vanhanh remembers it next time.
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
- **Opening a chat on the Partners page no longer says "taking too long" by mistake.** No error while the page is reconnecting. A Vanhanh Core open that hangs shows the error with Retry, and Retry really loads again.
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
- **The seven API-key brains show the Plan card too.** OpenRouter, OpenAI, Anthropic API, Gemini, Groq, DeepSeek and Ollama get a `vanhanh_plan` tool: for a job of three steps or more the model lists the steps and ticks each one off. It costs about 200 tokens a request; switch it off in the composer **+** menu, **Plan long jobs (API brains)**. Only the owner's chat gets it, not customer bots or background jobs.
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
- **If the settings file is edited outside VANHANH**, every device is signed out and a red warning shows. The first start on this version only records the current account and signs no one out.
- **The AI assistant can no longer touch secret files** (settings, encryption key, sessions) at any permission level.
- **Removing 2FA when locked out:** add `VANHANH_RESET_2FA=1` and redeploy. Each value works once.
- **Hostinger: port 7777 closes to the Internet once an HTTPS domain is set**, leaving only the encrypted way in.
- **A leaked admin link stays out of Google.** Every VANHANH page now carries `noindex`, the login screen and share links included.
- **AI bots cannot read VANHANH.** GPTBot, ClaudeBot, PerplexityBot, SEO tools and scanners such as Shodan and Censys get a 403. VANHANH also serves a `/robots.txt` that forbids them.
- Real browsers, link previews in Zalo or Telegram, the Meta, Threads and Zalo OA webhooks, `/s/` share links and Vanhanh Gate work as before. To turn the blocking off, set `VANHANH_BLOCK_BOTS=0`.
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
- **Daily targets** live in `Vanhanh/office.json`. The page only reads, and hides tokens and server paths.

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
- **Admin channel chats** show in the history of Vanhanh Core and of the linked agent, the owner's Zalo bot included.
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
- **Upload your own avatar picture** and use it as the browser tab icon, so several VANHANH side by side are easy to tell apart.
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
- **Several leaks closed after a review:** chatbots and background work below Full access can no longer write where code runs, scheduled jobs cannot exceed their maker's level, HTML files opened from the brain run in a sandbox, and other pages on the machine cannot send commands into VANHANH.
### Added
- **A new Models page:** Disconnect on every card, OpenAI Compatible and Claude Compatible take several keys and switch when one runs out, and Antigravity on a VPS can add accounts (not yet tried with a real `agy`).
- **Vanhanh Core edits like any assistant** and can have its own name per brain. **One bot serves up to 100 Facebook Pages.** The Avatar has a menu you arrange, and a voice call from an assistant's chat speaks as that assistant.
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
- **Threads on the Meta connection card**: replies under your Threads posts reach the inbox and the bot can answer publicly. Each account picks off, inbox only, or bot replies. Threads only lets you hide a reply, not delete it, so VANHANH says that and asks first.
- **Teams do more**: attach a GitHub repo (edits on its own branch, opens a PR, red CI gets at most 3 fix rounds), call `/skill` in the team chat, and members open a job when given one in the chat, at most 5 a day by default.
- **My tasks get Tags and subtasks**: old Projects become tags, nothing is lost. Notes can link to pages, `[[notes]]` and files.
- **Internal API channel (experimental)**: one of your servers asks a Chatbot over HTTP. The key shows once, the bot only reads, and by default only the machine running VANHANH can call it.

### Improved
- **Drag to reorder** projects, pinned chats and tags, the same order on every device. The Vanhanh Core card says which model it runs on and can pick one. Phones get an **Install on phone** button in the menu.
- **Claude Code waits for background work** before it carries on, up to 30 minutes. The answer to a message added mid-turn shows right below it. Antigravity no longer warns by mistake that it could not read the context file.

## [1.5.0] - 2026-11-04
### Added
- **Message a commenter privately** from their comment thread: pick Reply publicly or Message privately above the box. Meta allows one per comment, within 7 days.
- **Instagram in the shared inbox**: tick "Also connect the Page's Instagram" when connecting, and Instagram messages and comments arrive in the same place, with the same bot as the Page.
- **The "..." menu on each chat** now has View profile, Block and Delete chat. VANHANH always asks before Delete, because deleting a comment or a personal Zalo chat really deletes it there.

### Improved
- The Facebook Messenger card is now **Meta connection**, with an icon for each app and a **Disconnect** button on each Page. Past chats stay. Comments and Instagram get their own icons in the inbox.

## [1.4.0] - 2026-11-03
### Added
- **Pick a time zone** in **Settings** (the Language and time zone block) and in the last step of first-run setup. "Today", "yesterday", reminders and report numbers follow it, even when the server runs on UTC. The default is Vietnam time.

### Fixed
- **No more freezing while VANHANH is answering**, and no more "Reconnecting" over and over on a slow device or network.
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
- **The Zalo bot notices when it is tagged in a group by the account's Zalo name**, even right after a server restart. VANHANH used to forget that name on every restart, so a tag that did not match the connection name got no answer.

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
- **Advanced sits under Account** and unfolds Terminal, Plugins, Webhooks, Logins, Share links and the VANHANH community. Language is picked in Settings. Pages and the top bar stay as in 1.2.1.

## [1.2.1] - 2026-11-03
### Improved
- **The Store has Vanhanh Gate**: ChatGPT and Claude connect to Vanhanh through one pack, read and post into your chats, and keep a log. Machines with the **Vanhanh in ChatGPT** pack see Gate as an update, no need to reconnect.
- **14 Store packs now have English ids**, for example Customer management is `vanhanh.crm`. Installed packs show **Update available** and update in place, keeping their data.

## [1.2.0] - 2026-11-03
### Added
- **ChatGPT and Claude keep a log in Vanhanh.** When you work something out with an outside AI connected to Vanhanh, it notes what you said, what you decided and why. Vanhanh keeps the context and remembers your decisions, at no cost in Vanhanh runs.
### Improved
- The **Learn** page names **VANHANH** throughout: sync VANHANH with GitHub, VANHANH learns from your chats, what VANHANH has learned.

## [1.1.1] - 2026-11-03
### Fixed
- **The phone menu no longer overlaps.** The last items (Connections, Store, System...) used to spill over the language, brain picker and version rows. Everything now sits in order; scroll down to reach it.

## [1.1.0] - 2026-11-02
### Added
- **Desktop installers.** Download Vanhanh-Setup.exe (Windows) or Vanhanh-macOS.dmg (Mac) and open it like any app, no commands to type.
- **Connect a Facebook Page once for three jobs:** press Log in with Facebook and the bot answers Messenger messages, replies to comments under posts, and Vanhanh posts to the Page now or on a schedule. A step-by-step guide is included.
- **Voice messages without Groq:** use an OpenAI or Gemini key, or a listener that runs on the machine itself. The personal Zalo chatbot hears voice messages and looks at videos customers send.
- **Outside AI can hand Vanhanh work:** find, read and send a message into a Vanhanh conversation as if you typed it, which you can watch live and stop at any time.
### Improved
- **Answers appear as they are written** on every brain: Claude Code, Grok Build, Antigravity and the API key brains.
- **Redesigned Webhook page:** a one-line overview, each webhook opens in its own window, and workflows can be searched by name.
- **Brain picker** drawn by Vanhanh, the same on every device, with your own order. An .html file opens on its live page with the code one tab away. A long paste shows a preview first, then you choose to paste or attach it.
- **Teams retry** a step that hit a temporary error, and each part of a plan states which parts it waits for.
### Fixed
- Claude sign-in finishes on its own on a machine with a browser, no code needed. Dropping a file on the main chat works again, memory recall no longer picks up old run logs, and accented file names stay intact on download.
## [1.0.5] - 2026-11-02
### Fixed
- **The Update button on a VPS no longer waits forever.** When the server runs VANHANH as a normal user that may not update itself, the page now shows the error at once, with the manual update command and how to enable the button, instead of waiting 10 minutes and asking for a reload.

## [1.0.4] - 2026-11-02
### Improved
- **New icon set** across the sidebar and the whole app.
- **Mascot** is now called **Avatar**.
- **Updates** has its own sidebar item right under **Account**, with a **New** badge when a newer version is out.
- Leftover "brain" wording in the interface, the Plugins page and the Learn page now reads clearly: brain means your notes vault, AI model means Claude, ChatGPT and the like.

## [1.0.3] - 2026-11-02
### Improved
- The Account and Settings name block and the Models main-card badge now come from translations (Vietnamese: Tên VANHANH, Chính).

## [1.0.2] - 2026-11-02
### Improved
- **One name for the store** in Vietnamese: the Agents, Data sources and Plugins pages now match the sidebar.
- **Fewer English terms in Vietnamese** on the Learn, Models and Account pages. The account name field reads **Your VANHANH name**.

## [1.0.1] - 2026-11-02
### Improved
- **A tidier sidebar.** Every item shows at once, no groups to open. Rarely used pages sit in a folded **Advanced** group and **System** is pinned to the bottom.
- **Clearer menu names** in Vietnamese. Voice commands accept the new names too.
- **A plainer welcome screen.** Pick a brain by the plan you already have, then click **Sign in with Claude** on the **Models** page, no terminal command needed.
- **Home page labels** are translated in Vietnamese (vault, agents, skills, workflows, note counts).
## [1.0.0] - 2026-10-31
### Added
- **VANHANH is born.** Your own AI brain, built by Dai Le for the VANHANH community.
