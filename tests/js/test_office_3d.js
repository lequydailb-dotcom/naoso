// Office page, 3D view (dashboard/office3d.js): one desk per real assistant and per real job, an empty desk only where a
// department has nobody, lamps from the job state, a replay built only from that day's runs in order, three.js vendored
// and fetched only on demand, and every string in both languages.
const path = require("path");
const fs = require("fs");
const O3 = require(path.join(__dirname, "../../dashboard/office3d.js"));
const O = require(path.join(__dirname, "../../dashboard/office.js"));

let fails = 0;
function check(name, ok) { console.log((ok ? "ok   " : "FAIL ") + name); if (!ok) fails++; }

const data = {
  day: "2026-11-07", today: "2026-11-09",
  jobs: [
    { id: "dang", kind: "loop", name: "Đăng theo lịch", state: "paused", paused_reason: "3 lượt liền không đạt", day: { runs: 9, ok: 6, fail: 3 } },
    { id: "r1", kind: "reminder", name: "Đăng Threads", state: "ok", day: { runs: 1, ok: 1, fail: 0 } },
    { id: "old", kind: "loop", name: "Cũ", state: "removed", day: { runs: 0, ok: 0, fail: 0 } },
  ],
  depts: [
    { id: "marketing", light: "red", status: "broken", staff: [{ slug: "a", name: "Người viết", role: "viết" }], jobs: ["r1", "dang"], waiting: [] },
    { id: "sales", light: "grey", status: "empty", staff: [], jobs: [], waiting: [] },
    { id: "ops", light: "grey", status: "idle", staff: [], jobs: ["old"], waiting: [] },
  ],
  day_feed: [],
};
const hms = ["08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "18:00", "19:00", "20:00"];
const okk = [1, 1, 0, 1, 1, 1, 0, 1, 0];
hms.forEach((hm, i) => data.day_feed.push({ ts: i, hm, job: "dang", name: "Đăng theo lịch", result: okk[i] ? "verified_ok" : "verified_fail" }));
data.day_feed.splice(1, 0, { ts: 0.5, hm: "09:00", job: "r1", name: "Đăng Threads", result: "ok" });

const mk = O3.zoneDesks(data, data.depts[0]);
check("marketing: the assistant, then the broken job first, then the healthy one",
  mk.map(d => d.kind + ":" + d.id).join(",") === "staff:a,job:dang,job:r1");
check("a paused job's lamp is red, a healthy one green", mk[1].lamp === "bad" && mk[2].lamp === "ok");
const sales = O3.zoneDesks(data, data.depts[1]);
check("an empty department gets exactly one empty desk", sales.length === 1 && sales[0].kind === "empty");
check("a removed job keeps a grey desk", O3.zoneDesks(data, data.depts[2])[0].lamp === "off");

const L = O3.layout(data);
check("one zone per department", L.zones.length === 3);
check("desks are not stacked on each other", L.zones.every(z => new Set(z.desks.map(d => d.x.toFixed(2) + "," + d.z.toFixed(2))).size === z.desks.length));
check("zones do not overlap", L.zones.every((a, i) => L.zones.every((b, j) => i === j
  || Math.abs(a.x - b.x) >= (a.w + b.w) / 2 - 1e-6 || Math.abs(a.z - b.z) >= (a.dz + b.dz) / 2 - 1e-6)));
check("two columns on request (a phone)", new Set(O3.layout(data, 2).zones.map(z => z.x.toFixed(2))).size === 2);

const steps = O3.replaySteps(data);
const mine = steps.filter(s => s.job === "dang");
check("replay of 07/11: 9 runs of the posting loop, 3 crosses", mine.length === 9 && mine.filter(s => s.mark === "bad").length === 3);
check("replay keeps the day's order and clock", steps[0].hm === "08:00" && steps[steps.length - 1].hm === "20:00");
check("the lamp after the last run is red", mine[mine.length - 1].lamp === "bad");
const mixed = O3.replaySteps({ day_feed: [{ ts: 10, hm: "09:00", job: "x", result: "ok" }, { ts: 30, hm: "11:00", job: "x", result: "fail" }],
  handoffs: [{ ts: 20, hm: "10:00", from: "owner", to: "a", status: "done", title: "T" }] });
check("a replay plays handoffs between runs, in time order", mixed.length === 3 && !!mixed[1].hand
  && mixed[1].hand.to === "a" && mixed[0].mark === "ok" && mixed[2].mark === "bad");
check("a replay of a day with no run has no steps", O3.replaySteps({ day_feed: [] }).length === 0);

// the desk card (office.js describe)
const card = O.describe(data, { kind: "job", id: "dang" });
check("tapping a paused job shows its reason and what to do", card.includes("office.why_paused") && card.includes("office.do_paused"));
check("tapping an empty desk shows nothing", O.describe(data, { kind: "empty", id: "empty:sales" }) === "");
check("the desk card escapes the owner's text", O.describe({ jobs: [{ id: "x", name: "<b>x</b>", state: "ok", day: {} }] }, { kind: "job", id: "x" }).includes("&lt;b&gt;"));
check("the 3D view puts a slot where the cards were", O.pageHtml(Object.assign({ days: [], files: {}, totals: {}, issues: [], feed: [] }, data), true).includes("of-3d-slot")
  && !O.pageHtml(Object.assign({ days: [], files: {}, totals: {}, issues: [], feed: [] }, data), true).includes("of-depts"));

// three.js is vendored and only imported on demand
const src = fs.readFileSync(path.join(__dirname, "../../dashboard/office3d.js"), "utf8");
const vend = path.join(__dirname, "../../dashboard/vendor");
check("three.js and OrbitControls are in the repo, with the MIT licence",
  fs.existsSync(path.join(vend, "three-0.160.0.module.min.js")) && fs.existsSync(path.join(vend, "three-LICENSE.txt"))
  && /from '\.\/three-0\.160\.0\.module\.min\.js'/.test(fs.readFileSync(path.join(vend, "three-0.160.0-orbit-controls.js"), "utf8")));
check("three.js comes only from our own server, by dynamic import", /import\(THREE_URL\)/.test(src) && !/https?:\/\//.test(src.replace(/\/\*[\s\S]*?\*\//g, "")));
const html = fs.readFileSync(path.join(__dirname, "../../dashboard/index.html"), "utf8");
check("index.html does not load three.js up front", !/<script[^>]+three-0\.160/.test(html));
check("nothing moves on a timer of its own: the only interval is the replay", (src.match(/setInterval\(/g) || []).length === 1);

const vi = JSON.parse(fs.readFileSync(path.join(__dirname, "../../dashboard/i18n/vi.json"), "utf8"));
const en = JSON.parse(fs.readFileSync(path.join(__dirname, "../../dashboard/i18n/en.json"), "utf8"));
const keys = new Set([...(src.match(/"office\.[a-z0-9_]+"/g) || []), ...(fs.readFileSync(path.join(__dirname, "../../dashboard/office.js"), "utf8").match(/"office\.[a-z0-9_]+"/g) || [])]
  .map(s => s.slice(1, -1)));
const missing = [...keys].filter(k => !(k in vi) || !(k in en));
check("every key exists in vi and en" + (missing.length ? ": " + missing.join(", ") : ""), !missing.length);

process.exit(fails ? 1 : 0);
