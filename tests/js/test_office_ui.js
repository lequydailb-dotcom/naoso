// Office page (dashboard/office.js): draws only what GET /office returned, escapes every owner text, shows "[?]" for a
// number the server could not count, and every string it uses exists in both languages.
const path = require("path");
const fs = require("fs");
const O = require(path.join(__dirname, "../../dashboard/office.js"));

let fails = 0;
function check(name, ok) { console.log((ok ? "ok   " : "FAIL ") + name); if (!ok) fails++; }

const data = {
  day: "2026-11-07", today: "2026-11-07", days: ["2026-11-07", "2026-11-06"], now_at: "21:00:00",
  files: { reminders: true, work_log: true, loop_state: true, kanban: false },
  totals: { runs: 12, fails: 3, broken: 2, waiting: null, empty_depts: 1 },
  jobs: [
    { id: "dang", kind: "loop", name: "Đăng <b>bài</b>", dept: "marketing", dept_guessed: true, state: "paused",
      paused_reason: "3 lần liền không đạt", result: "✗", last_at: "20:00", target: null, day: { runs: 9, ok: 6, fail: 3 } },
    { id: "r1", kind: "reminder", name: "Đăng Threads", dept: "marketing", state: "ok", result: "ok", last_at: "09:00",
      target: 2, day: { runs: 1, ok: 1, fail: 0 } },
  ],
  depts: [
    { id: "marketing", light: "red", status: "broken", staff: [{ slug: "a", name: "Người viết", role: "" }], jobs: ["dang", "r1"], waiting: [] },
    { id: "sales", light: "grey", status: "empty", staff: [], jobs: [], waiting: [] },
    { id: "SEO", light: "grey", status: "idle", staff: [{ slug: "s", name: "SEO", role: "" }], jobs: [], waiting: [] },
  ],
  issues: [
    { kind: "paused", level: 0, job: "dang" },
    { kind: "twin_running", level: 2, job: "r1", other: "dang" },
    { kind: "dept_empty", level: 4, dept: "sales" },
  ],
  feed: [{ ts: 1, at: "20:00", job: "dang", name: "Đăng", result: "verified_fail", note: "<script>x</script>" }],
};

const html = O.pageHtml(data);
check("owner text is escaped", html.includes("Đăng &lt;b&gt;bài&lt;/b&gt;") && !html.includes("<script>x"));
check("a number the server could not count shows [?]", O.kpiHtml(data).includes("[?]"));
check("paused issue carries the reason and what to do", html.includes("3 lần liền không đạt") && html.includes("office.do_paused"));
check("red department light", html.includes("of-l-red"));
check("an empty department says so", html.includes("office.no_staff"));
check("a department named by the owner keeps the owner's name", O.deptName("SEO") === "SEO" && O.deptName("sales") === "office.dept_sales");
check("runs and target on a job row", O.jobRowHtml(data.jobs[1]).includes("office.target_day"));
check("missing file named in the footer", html.includes("office.missing"));
check("live badge on today", html.includes("of-live on"));
check("a past day is a record, not live", !O.pageHtml(Object.assign({}, data, { day: "2026-11-06" })).includes("of-live on"));

// running right now: the strip ticks on from the last answer, escapes names, says so when nothing runs
const live = { now: 1000, now_at: "21:00:00", items: [
  { kind: "loop", id: "dang", name: "Đăng <i>bài</i>", since: 880, since_at: "20:58", secs: 120 },
  { kind: "task", id: "t1", name: "Viết email", since: 0, since_at: "", secs: null, agent: "viet-email" },
] };
const nowH = O.nowHtml(live, 5);
check("strip lists each running item with its kind", nowH.includes("office.k_loop") && nowH.includes("office.k_task"));
check("strip escapes running names", nowH.includes("&lt;i&gt;") && !nowH.includes("<i>"));
check("strip counts on from the last answer (120s + 5s)", nowH.includes("office.now_since"));
check("strip without a start time just says running", nowH.includes("office.now_running"));
check("busy strip pulses, idle one does not", nowH.includes("of-now busy") && O.nowHtml({ now: 1, items: [] }, 0).includes("of-pulse idle"));
check("nothing running says so", O.nowHtml({ now: 1, items: [] }, 0).includes("office.now_none"));
check("before the first answer it says it is asking", O.nowHtml(null).includes("office.now_wait"));
check("durations pick their unit", O.dur(42) === "office.dur_s" && O.dur(125) === "office.dur_m" && O.dur(7300) === "office.dur_h");
check("the strip sits under the numbers in both views", O.pageHtml(data, false, live, 0).includes("of-now")
  && O.pageHtml(data, true, live, 0).indexOf("of-now") < O.pageHtml(data, true, live, 0).indexOf("of-3d-slot"));

// handoffs: newest first, names escaped, the owner named, empty day says so
const hd = Object.assign({}, data, { handoffs: [
  { kind: "team", from: "a", to: "s", from_name: "Người <b>viết</b>", to_name: "SEO", title: "Bài", where: "Nhóm", ts: 1, hm: "09:00", status: "done" },
  { kind: "board", from: "owner", to: "a", from_name: "", to_name: "Người viết", title: "Ảnh", where: "", ts: 2, hm: "10:00", status: "running" },
] });
const hh = O.handoffsHtml(hd);
check("handoffs listed newest first", hh.indexOf("10:00") < hh.indexOf("09:00"));
check("handoff names are escaped", hh.includes("&lt;b&gt;") && !hh.includes("<b>viết"));
check("the owner is named, not 'owner'", hh.includes("office.owner") && !hh.includes(">owner<"));
check("handoff status shown", hh.includes("office.hs_running") && hh.includes("office.hs_done"));
check("a day with no handoff says so", O.handoffsHtml(data).includes("office.hand_empty"));
check("handoffs sit on the page in both views", O.pageHtml(hd, false).includes("of-hand") && O.pageHtml(hd, true).includes("of-hand"));

// every office.* and page.office.* key used in the file exists in both languages
const src = fs.readFileSync(path.join(__dirname, "../../dashboard/office.js"), "utf8");
const vi = JSON.parse(fs.readFileSync(path.join(__dirname, "../../dashboard/i18n/vi.json"), "utf8"));
const en = JSON.parse(fs.readFileSync(path.join(__dirname, "../../dashboard/i18n/en.json"), "utf8"));
const used = new Set((src.match(/"office\.[a-z_]+"/g) || []).map(s => s.slice(1, -1)));
// keys built from codes
["ok", "failed", "paused", "late", "never", "off", "removed", "cancelled", "done"].forEach(s => used.add("office.st_" + s));
["loop", "reminder", "once"].forEach(s => used.add("office.kind_" + s));
["ok", "fail", "verified_ok", "verified_fail", "run", "other"].forEach(s => used.add("office.r_" + s));
["reminders", "work_log", "loop_state", "kanban"].forEach(s => used.add("office.f_" + s));
["marketing", "sales", "care", "finance", "ops", "system", "unsorted"].forEach(s => used.add("office.dept_" + s));
["page.office.label", "page.office.sub"].forEach(k => used.add(k));
const missing = [...used].filter(k => !(k in vi) || !(k in en));
check("every key exists in vi and en" + (missing.length ? ": " + missing.join(", ") : ""), !missing.length);
check("Office sits on the rail after Tasks", /ids: \["home", "chat", "tasks", "office"\]/.test(
  fs.readFileSync(path.join(__dirname, "../../dashboard/console.js"), "utf8")));

process.exit(fails ? 1 : 0);
