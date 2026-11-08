# Changelog

*[Tiếng Việt](CHANGELOG.md) · **English***

VANHANH release history. Newest first.

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
