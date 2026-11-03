# Changelog

*[Tiếng Việt](CHANGELOG.md) · **English***

VANHANH release history. Newest first.

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
