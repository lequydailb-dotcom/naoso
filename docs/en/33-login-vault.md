# 33 - Cookies (Login vault)

*[Tiếng Việt](../33-kho-dang-nhap.md) · **English***

Naota has a **Cookies** page: a place to keep your own sign-ins (cookies) so Naota can reuse them. You sign in once in your own browser, hand the cookies to Naota, and Naota can then read pages that only show when you are signed in: your Shopee seller center, affiliate dashboards, your website's admin pages.

The vault is optional. With no sign-ins in it, Naota works exactly as before.

## Add a sign-in

1. Install the **Cookie-Editor** extension for Chrome or Edge.
2. Open the site while signed in, click the Cookie-Editor icon, choose **Export** then **JSON**. The cookies are copied to the clipboard.
3. In Naota open the sidebar, group **Connections**, item **Cookies** (the cookie icon). Press **Add cookies**.
4. Give it a name you will recognise (for example "Shopee seller"), paste the cookies and press **Save and check**.

If you already have a cookie file (a JSON file exported by Cookie-Editor, or a `cookies.txt` from the Get cookies.txt LOCALLY extension), press **Upload file** at the top of the page, the **Choose file** button in the form, or drop the file on the box. Naota reads the file in your browser and names the entry after the file when the Name box is empty. Files are limited to 1 MB.

Naota also reads a `cookies.txt` file and a `name=value; ...` string (then also fill in the Website field, for example `shopee.com`).

## What each card tells you

| Part | Meaning |
|---|---|
| **Signed in** | The last check opened the page without being sent to the sign-in screen |
| **Expired** | The site sent us to its sign-in page or answered 401/403 |
| **Page failed to load** | The page could not be loaded (network, site down). Not necessarily expired |
| **Valid until / N days left** | From the expiry dates inside the cookies |
| **Let Naota use it** | Off means the AI and page watches no longer use this sign-in; the cookies stay |
| **Let Naota click and fill forms** | On means Naota may act for real with this sign-in in the browser. Off keeps Naota to reading |
| **In Naota's browser now** | This session currently sits in the browser Naota drives |

**Check** opens the **test page** with that sign-in. It defaults to the domain's home page; set it in the three-dot menu to a page you can only see when signed in (an orders page, say) for a more accurate answer. **Update** is where you paste fresh cookies when the session expires.

## Where Naota uses a sign-in

- **In chat:** every engine has the `naota_login` tool. Say "check my Shopee orders page" with the link, and Naota opens the page with the stored sign-in and reads it. When the sign-in has expired Naota says so plainly and asks you to update it, instead of retrying.
- **Page watch:** the form on the Page watch tab (Recurring work page) has a **Sign-in** field. Pick one and Naota can watch a page that needs a sign-in. When the session expires the watch pauses itself and tells you once.
- **Clicking and filling forms:** say "open my Shopee seller page and fill in the reply to this review". Naota puts the sign-in into the browser, opens the page and works on it like a user.

Reading (the first two) only downloads the page and takes its text, so a page built entirely in JavaScript may give little. When something has to be clicked or typed, or the page is JavaScript-heavy, Naota uses the browser.

## Clicking and filling forms in the browser

Three things are needed:

1. The **Playwright connection** on the Connections page (the browser Naota drives). Without it Naota says plainly that it is missing.
2. The **Let Naota click and fill forms** switch on that sign-in's card. A newly added sign-in has it on. A sign-in stored before this feature has it **off**, because Naota could only read when you stored it: Naota asks you once when you turn it on.
3. A run at the **Full access** level. Background work set to a lighter level (read only, drafts only) cannot open the signed-in browser.

Naota puts the cookies straight into the browser through the Playwright connection itself: no cookie file is written to disk and the connection is not restarted.

What Naota takes care of:

- **A renewed session is not overwritten.** Many sites change cookies while they are used. On a later open Naota only adds the cookies that are missing and never writes the older stored copy over the browser's newer one. After each page that loads signed in, the newer copy is saved back to the vault (still encrypted), so reading and page watches use the renewed session too.
- **Pasting new cookies** (Update) makes the next open replace the browser's copy.
- **Two accounts of one site** (two Shopee shops): the browser holds one at a time. Naota switches to the one you name.
- **Switching it off or deleting it** also removes that session from the browser. If that fails Naota tells you at once, so you can sign out on the website yourself.

## Safety

- Cookies are **encrypted** on the server. When the machine cannot encrypt (the `cryptography` library is missing) Naota refuses to save instead of writing them in the clear.
- **Naota's tools never hand a cookie value to the AI.** The tool returns the page text and the sign-in's name only, also when the browser reports an error.
- A cookie only goes to the domain it belongs to, checked again on **every redirect hop**: a page that redirects to another site does not carry the cookies along.
- The Cookies page needs a **real dashboard sign-in**: an API token can neither read nor add sign-ins.
- **Customer chatbots never see this tool.** And once the browser has held one of your sign-ins, customer chatbots also **lose that browser connection**, so a stranger cannot browse with your account.

## Honest caveats

- A cookie is a key to the account. Never paste someone else's, never send yours to anyone.
- **The risk is yours.** When allowed to click and fill forms, Naota acts for real with your account: it submits forms, posts, places orders, changes settings, and what it does cannot be undone. Prefer an account made for Naota over your main one.
- A web page can carry text written to push an AI into doing things you did not ask for. Naota treats page content as data, not orders, but no guard is absolute.
- While Naota drives the signed-in browser, the AI sees everything in that session, like a person sitting at the screen.
- A service may ask for verification or lock the account when it sees a session driven automatically, and many services forbid this in their terms.
- Facebook and Google often ask to verify when a session is used from a different IP than the one you signed in from (for example Naota on a VPS). Smaller sites are usually more relaxed.
- Every session expires at some point. Then sign in again in your browser, export the cookies and press **Update**.
- If a site has an official API or MCP (Facebook Ads, Gmail, Calendar), prefer that: it is sturdier and safer than cookies.

## Technical details

Module `server/login_vault.py`, store `login_vault.sqlite3` in the data folder (mode 600), routes `/logins` and `/logins/action`, tool `naota_login` (plugin `naota-login`: `list` and `fetch` at level `readonly`, `browser` at level `full`; listed in `OWNER_ONLY_TOOLS`), page `dashboard/login-vault.js`. Page watches gain a `login_id` column. The browser part lives in `server/browser_login.py`: it adds, reads and clears cookies through the Playwright connection's code tool (`browser_run_code_unsafe`), the vault has two more columns (`allow_act`, `browser_at`), and `mcp_hub.discover_all` drops the browser connection from a customer chatbot's tools.
