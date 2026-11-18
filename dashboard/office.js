/* Office page.
 *
 * One card per department answers five questions for the owner: does anyone work here, is the work running, is it
 * right, does it reach the target, what waits for me. Above the cards, "Needs you" lists what is broken with what to
 * do; below them, the latest real runs. Everything comes from GET /office (server/office.py), which reads the brain's
 * own logs, masks secrets and paths, and returns codes; this file only draws them through i18n.
 *
 * Truth rule: nothing here animates or invents. A number the server could not count shows as "[?]". The page reloads
 * every 30 seconds while it shows today and the tab is visible; a past day is a fixed record.
 *
 * Render helpers are pure (tested under node); `mount` wires the API call.
 */
(function () {
  "use strict";

  function tw(key, vars) {
    var s = (typeof window !== "undefined" && window.t) ? window.t(key, vars) : key;
    if (vars) {
      s = String(s).replace(/\{(\w+)\}/g, function (m, name) {
        return Object.prototype.hasOwnProperty.call(vars, name) ? String(vars[name]) : m;
      });
    }
    return s;
  }
  function esc(t) {
    return String(t == null ? "" : t).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  var ic = function (n) { return (typeof window !== "undefined" && window.ic) ? window.ic(n) : ""; };
  function infoBtn() { var J = typeof window !== "undefined" && window.NaotaInfo; return J ? J.btn(tw("info.more")) : ""; }
  function infoBody(html) {
    var J = typeof window !== "undefined" && window.NaotaInfo;
    return J ? J.body(html) : '<div class="info-body">' + html + "</div>";
  }

  // Every key is written out whole: the i18n test finds keys by their full name.
  var DEPT_KEY = { marketing: "office.dept_marketing", sales: "office.dept_sales", care: "office.dept_care",
    finance: "office.dept_finance", ops: "office.dept_ops", system: "office.dept_system", unsorted: "office.dept_unsorted" };
  function deptName(id) { return DEPT_KEY[id] ? tw(DEPT_KEY[id]) : String(id || ""); }
  var STATE_KEY = { ok: "office.st_ok", failed: "office.st_failed", paused: "office.st_paused", late: "office.st_late",
    never: "office.st_never", off: "office.st_off", removed: "office.st_removed", cancelled: "office.st_cancelled",
    done: "office.st_done" };
  var KIND_KEY = { loop: "office.kind_loop", reminder: "office.kind_reminder", once: "office.kind_once" };
  var RESULT_KEY = { ok: "office.r_ok", fail: "office.r_fail", verified_ok: "office.r_verified_ok",
    verified_fail: "office.r_verified_fail", run: "office.r_run", other: "office.r_other" };
  var FILE_KEY = { reminders: "office.f_reminders", work_log: "office.f_work_log", loop_state: "office.f_loop_state",
    kanban: "office.f_kanban" };
  // job state -> tone (colour) and i18n key
  var TONE = { ok: "ok", failed: "bad", paused: "bad", late: "ask", never: "calm", off: "off", removed: "off",
    cancelled: "off", done: "off" };
  function stateChip(st) {
    var tn = TONE[st] || "calm";
    return '<span class="of-chip of-' + tn + '">' + esc(STATE_KEY[st] ? tw(STATE_KEY[st]) : st) + "</span>";
  }
  function num(v) { return v == null ? "[?]" : String(v); }

  function kpiHtml(d) {
    var t = (d && d.totals) || {};
    var cell = function (n, key, tone) {
      return '<div class="of-kpi' + (tone ? " of-k-" + tone : "") + '"><b>' + esc(num(n)) + "</b><span>" + esc(tw(key)) + "</span></div>";
    };
    return '<div class="of-kpis">'
      + cell(t.runs, "office.k_runs")
      + cell(t.fails, "office.k_fails", t.fails ? "bad" : "")
      + cell(t.broken, "office.k_broken", t.broken ? "bad" : "")
      + cell(t.waiting, "office.k_waiting", t.waiting ? "ask" : "")
      + cell(t.empty_depts, "office.k_empty", t.empty_depts ? "ask" : "")
      + aiCell(d)
      + "</div>";
  }
  // money AI calls really billed that day on this server (API keys only); a plan turn is $0,
  // so a day run only on a monthly plan says that instead of a bare "$0"
  function aiCell(d) {
    var a = d && d.ai;
    var v = a ? "$" + (a.cost < 10 ? a.cost.toFixed(2) : Math.round(a.cost)) : "[?]";
    var onlyPlan = a && !a.cost && a.plan_turns && a.plan_turns === a.turns;
    var label = !a ? tw("office.k_ai_none") : tw(onlyPlan ? "office.k_ai_plan" : "office.k_ai", { n: a.turns });
    return '<div class="of-kpi" title="' + esc(tw("office.k_ai_note")) + '"><b>' + esc(v) + "</b><span>"
      + esc(label) + "</span></div>";
  }

  // The line of news running along the bottom of the 3D office: handoffs and runs, newest first.
  function tickerItems(d) {
    var who_ = function (n, id) { return id === "owner" ? tw("office.owner") : (n || id); };
    var hs = ((d && d.handoffs) || []).map(function (h) {
      return { ts: h.ts || 0, text: tw("office.tk_hand", { at: h.hm, from: who_(h.from_name, h.from), to: who_(h.to_name, h.to), title: h.title }),
        tone: HAND_TONE[h.status] || "calm" };
    });
    var fs = ((d && d.feed) || []).map(function (f) {
      return { ts: f.ts || 0, text: tw("office.tk_run", { at: f.at, name: f.name, result: tw(RESULT_KEY[f.result] || "office.r_other") }),
        tone: FEED_TONE[f.result] || "calm" };
    });
    return hs.concat(fs).sort(function (a, b) { return b.ts - a.ts; }).slice(0, 14);
  }
  function tickerHtml(d) {
    return tickerItems(d).map(function (x) { return '<span class="o3-tki o3-' + x.tone + '">' + esc(x.text) + "</span>"; }).join("");
  }

  // The sign over each department in 3D: its state, then how many assistants, jobs and runs it has today.
  function zoneSub(d, dep) {
    var js = (dep.jobs || []).map(function (id) { return jobById(d, id); }).filter(Boolean);
    var runs = js.reduce(function (a, j) { return a + ((j.day && j.day.runs) || 0); }, 0);
    var fails = js.reduce(function (a, j) { return a + ((j.day && j.day.fail) || 0); }, 0);
    return tw(STATUS_KEY[dep.status] || "office.ds_ok") + " · "
      + tw("office.zone_sub", { s: (dep.staff || []).length, r: runs }) + (fails ? " · " + tw("office.zone_fail", { f: fails }) : "");
  }

  function jobById(d, id) { return ((d && d.jobs) || []).filter(function (j) { return j.id === id; })[0]; }

  // One "needs you" row: what happened, why, and what to do.
  function issueHtml(d, it) {
    var j = it.job ? jobById(d, it.job) : null;
    var name = j ? j.name : "";
    var what = "", why = "", todo = "", tone = it.level <= 1 ? "bad" : "ask";
    if (it.kind === "paused") {
      what = tw("office.i_paused", { name: name });
      why = j && j.paused_reason ? j.paused_reason : "";
      todo = tw("office.do_paused");
    } else if (it.kind === "failed") {
      what = tw("office.i_failed", { name: name });
      why = j && j.result ? j.result : "";
      todo = tw("office.do_failed");
    } else if (it.kind === "late") {
      what = tw("office.i_late", { name: name, at: (j && j.last_at) || "[?]" });
      todo = tw("office.do_late");
    } else if (it.kind === "below_target") {
      what = tw("office.i_below", { name: name, ok: j ? j.day.ok : "[?]", target: j ? j.target : "[?]" });
      todo = tw("office.do_below");
    } else if (it.kind === "twin_running") {
      var o = jobById(d, it.other);
      what = tw("office.i_twin", { name: name, other: o ? o.name : it.other });
      todo = tw("office.do_twin");
    } else if (it.kind === "waiting") {
      what = tw("office.i_waiting", { n: it.count });
      todo = tw("office.do_waiting");
    } else if (it.kind === "dept_empty") {
      what = tw("office.i_empty", { dept: deptName(it.dept) });
      todo = tw("office.do_empty");
      tone = "calm";
    } else if (it.kind === "dept_idle") {
      what = tw("office.i_idle", { dept: deptName(it.dept), n: it.count });
      todo = tw("office.do_idle");
      tone = "calm";
    } else {
      return "";
    }
    return '<li class="of-issue of-' + tone + '"><div class="of-iw">' + esc(what) + "</div>"
      + (why ? '<div class="of-iy">' + esc(why) + "</div>" : "")
      + '<div class="of-id"><b>' + esc(tw("office.todo")) + "</b> " + esc(todo) + "</div></li>";
  }

  // Does a failure reach the owner's phone? One line under "Needs you", with a way to fix it when it does not.
  var ALERT_KEY = { ok: "office.tg_ok", off: "office.tg_off", no_owner: "office.tg_no_owner", error: "office.tg_error" };
  function alertHtml(d) {
    var a = d && d.alert;
    if (!a || !ALERT_KEY[a.tg]) return "";
    var ok = a.tg === "ok";
    return '<div class="of-alert of-alert-' + (ok ? "ok" : "warn") + '">' + ic(ok ? "bell" : "bell-off") + " "
      + esc(tw(ALERT_KEY[a.tg]))
      + (ok ? "" : ' <button type="button" class="btn btn-sm ofTg">' + esc(tw("office.tg_fix")) + "</button>") + "</div>";
  }

  function issuesHtml(d) {
    var list = (d && d.issues) || [];
    if (!list.length) return '<section class="of-box"><h3>' + esc(tw("office.needs_you")) + "</h3>" + alertHtml(d)
      + '<div class="of-none">' + ic("check") + " " + esc(tw("office.none")) + "</div></section>";
    return '<section class="of-box"><h3>' + esc(tw("office.needs_you")) + ' <span class="of-count">' + list.length + "</span></h3>"
      + alertHtml(d) + '<ul class="of-issues">' + list.map(function (it) { return issueHtml(d, it); }).join("") + "</ul></section>";
  }

  function jobRowHtml(j) {
    var day = j.day || {};
    var target = j.target ? ", " + tw("office.target_day", { n: j.target }) : "";
    var runs = '<span class="of-runs">' + esc(tw("office.runs_day", { ok: day.ok, n: day.runs }) + target)
      + (day.fail ? ' <span class="of-bad-t">' + esc(tw("office.fails_day", { n: day.fail })) + "</span>" : "") + "</span>";
    var detail = [];
    if (j.last_at) detail.push(tw("office.last_run", { at: j.last_at }));
    if (j.paused_reason) detail.push(tw("office.why_paused", { why: j.paused_reason }));
    else if (j.result && j.result !== "ok" && j.result !== "fail") detail.push(j.result);
    if (j.dept_guessed) detail.push(tw("office.guessed"));
    return '<details class="of-job"><summary>' + stateChip(j.state) + '<span class="of-jn">' + esc(j.name) + "</span>"
      + '<span class="of-kind">' + esc(KIND_KEY[j.kind] ? tw(KIND_KEY[j.kind]) : "") + "</span>" + runs + "</summary>"
      + '<div class="of-jd">' + detail.map(function (x) { return "<div>" + esc(x) + "</div>"; }).join("") + "</div></details>";
  }

  var STATUS_KEY = { broken: "office.ds_broken", late: "office.ds_late", empty: "office.ds_empty", idle: "office.ds_idle",
    waiting: "office.ds_waiting", ok: "office.ds_ok" };
  function deptHtml(d, dep) {
    var jobs = (dep.jobs || []).map(function (id) { return jobById(d, id); }).filter(Boolean);
    var staff = dep.staff || [];
    var people = staff.length ? '<div class="of-staff">' + staff.map(function (s) {
      return '<span class="of-person" title="' + esc(s.role) + '">' + ic("bot") + " " + esc(s.name) + "</span>";
    }).join("") + "</div>" : '<div class="of-empty">' + esc(tw("office.no_staff")) + "</div>";
    var work = jobs.length ? jobs.map(jobRowHtml).join("") : '<div class="of-empty">' + esc(tw("office.no_jobs")) + "</div>";
    var wait = (dep.waiting || []).length ? '<div class="of-wait">' + ic("circle-help") + " "
      + esc(tw("office.waiting_n", { n: dep.waiting.length })) + ": " + dep.waiting.map(function (w) { return esc(w.title); }).join(", ") + "</div>" : "";
    return '<article class="of-dept of-l-' + esc(dep.light) + '"><header><span class="of-light" aria-hidden="true"></span>'
      + "<h3>" + esc(deptName(dep.id)) + '</h3><span class="of-ds">' + esc(tw(STATUS_KEY[dep.status] || "office.ds_ok")) + "</span></header>"
      + '<div class="of-sub">' + esc(tw("office.staff_n", { n: staff.length })) + "</div>" + people
      + '<div class="of-sub">' + esc(tw("office.jobs_n", { n: jobs.length })) + "</div>" + work + wait + "</article>";
  }

  function deptsHtml(d) {
    return '<div class="of-depts">' + ((d && d.depts) || []).map(function (dep) { return deptHtml(d, dep); }).join("") + "</div>";
  }

  var FEED_TONE = { ok: "ok", verified_ok: "ok", fail: "bad", verified_fail: "bad", run: "calm", other: "calm" };
  function feedHtml(d) {
    var f = (d && d.feed) || [];
    var rows = f.length ? f.map(function (x) {
      return '<li class="of-f of-' + (FEED_TONE[x.result] || "calm") + '"><span class="of-ft">' + esc(x.at) + "</span>"
        + '<span class="of-fr">' + esc(tw(RESULT_KEY[x.result] || "office.r_other")) + "</span>"
        + '<span class="of-fn">' + esc(x.name) + (x.note ? ' <span class="of-fx">' + esc(x.note) + "</span>" : "") + "</span></li>";
    }).join("") : '<li class="of-empty">' + esc(tw("office.feed_empty")) + "</li>";
    return '<section class="of-box"><h3>' + esc(tw("office.feed")) + '</h3><ul class="of-feed">' + rows + "</ul></section>";
  }

  // ---- what runs at this second (GET /office/live, asked every 5 seconds) ----
  var TALK_KEY = { plan: "office.talk_plan", synthesize: "office.talk_sum", work: "office.talk_work", help: "office.talk_help",
    leader_reply: "office.talk_reply", member_reply: "office.talk_reply", member_volunteer: "office.talk_reply" };
  var NOW_KIND = { loop: "office.k_loop", reminder: "office.k_reminder", task: "office.k_task", job: "office.k_job",
    team: "office.k_team" };
  function dur(secs) {
    secs = Math.max(0, Math.floor(secs || 0));
    var h = Math.floor(secs / 3600), m = Math.floor((secs % 3600) / 60), s = secs % 60;
    if (h) return tw("office.dur_h", { h: h, m: m });
    if (m) return tw("office.dur_m", { m: m, s: s });
    return tw("office.dur_s", { s: s });
  }
  // live = the /office/live answer, ago = seconds since it arrived (the clock keeps ticking between asks)
  function nowHtml(live, ago) {
    if (!live) return '<section class="of-box of-now"><h3><span class="of-pulse off"></span>' + esc(tw("office.now_title")) + "</h3>"
      + '<div class="of-now-none">' + esc(tw("office.now_wait")) + "</div></section>";
    ago = Math.max(0, ago || 0);
    var items = live.items || [];
    var rows = items.map(function (x) {
      var secs = x.secs == null ? null : x.secs + ago;
      return '<li><span class="of-nk">' + esc(tw(NOW_KIND[x.kind] || "office.k_job")) + "</span>"
        + '<span class="of-nn">' + esc(x.name) + (x.agent ? ' <span class="of-fx">' + esc(x.agent) + "</span>" : "") + "</span>"
        + '<span class="of-nt">' + esc(secs == null ? tw("office.now_running") : tw("office.now_since", { at: x.since_at, dur: dur(secs) })) + "</span></li>";
    }).join("");
    var clockAt = live.now ? new Date((live.now + ago) * 1000) : null;
    var hms = clockAt ? [clockAt.getHours(), clockAt.getMinutes(), clockAt.getSeconds()].map(function (n) { return (n < 10 ? "0" : "") + n; }).join(":") : "";
    return '<section class="of-box of-now' + (items.length ? " busy" : "") + '"><h3><span class="of-pulse' + (items.length ? "" : " idle") + '"></span>'
      + esc(tw("office.now_title")) + ' <span class="of-nclock">' + esc(hms) + "</span>"
      + (items.length ? ' <span class="of-count">' + esc(String(items.length)) + "</span>" : "") + "</h3>"
      + (items.length ? '<ul class="of-nlist">' + rows + "</ul>" : '<div class="of-now-none">' + esc(tw("office.now_none")) + "</div>")
      + "</section>";
  }

  // ---- who handed what to whom that day (team assignments, board cards given to an assistant, workflow steps) ----
  var HAND_KEY = { team: "office.h_team", board: "office.h_board", workflow: "office.h_workflow" };
  var HAND_ST = { running: "office.hs_running", done: "office.hs_done", failed: "office.hs_failed",
    waiting: "office.hs_waiting", cancelled: "office.hs_cancelled" };
  var HAND_TONE = { running: "run", done: "ok", failed: "bad", waiting: "calm", cancelled: "calm" };
  function who(name, id) { return id === "owner" ? tw("office.owner") : (name || id); }
  function handoffsHtml(d) {
    var h = ((d && d.handoffs) || []).slice().reverse().slice(0, 40);
    var rows = h.length ? h.map(function (x) {
      return '<li class="of-h of-' + (HAND_TONE[x.status] || "calm") + '"><span class="of-ft">' + esc(x.hm) + "</span>"
        + '<span class="of-hw"><b>' + esc(who(x.from_name, x.from)) + '</b> <span class="of-ha">' + ic("chevron-right") + "</span> <b>"
        + esc(who(x.to_name, x.to)) + "</b></span>"
        + '<span class="of-fn">' + esc(x.title) + ' <span class="of-fx">' + esc(tw(HAND_KEY[x.kind] || "office.h_board"))
        + (x.where && x.where !== x.title ? " · " + esc(x.where) : "") + "</span></span>"
        + '<span class="of-hs">' + esc(tw(HAND_ST[x.status] || "office.hs_waiting")) + "</span></li>";
    }).join("") : '<li class="of-empty">' + esc(tw("office.hand_empty")) + "</li>";
    return '<section class="of-box"><h3>' + esc(tw("office.hand_title"))
      + (h.length ? ' <span class="of-count of-count-n">' + esc(String(((d && d.handoffs) || []).length)) + "</span>" : "")
      + '</h3><ul class="of-feed of-hand">' + rows + "</ul></section>";
  }

  function toolbarHtml(d, live, view3d) {
    var days = (d && d.days) || [];
    var opts = days.map(function (x) {
      var label = x === d.today ? tw("office.today") : x.split("-").reverse().join("/");
      return '<option value="' + esc(x) + '"' + (x === d.day ? " selected" : "") + ">" + esc(label) + "</option>";
    }).join("");
    return '<div class="of-bar"><label class="of-daypick">' + esc(tw("office.day")) + ' <select class="ofDay">' + opts + "</select></label>"
      + '<span class="of-live' + (live ? " on" : "") + '">' + esc(live ? tw("office.live") : tw("office.record")) + "</span>"
      + '<span class="of-sp"></span>'
      + '<button type="button" class="of-btn ofView">' + ic(view3d ? "list" : "layers") + " "
      + esc(view3d ? tw("office.view_cards") : tw("office.view_3d")) + "</button>" + infoBtn() + "</div>"
      + infoBody(esc(tw("office.info_1")) + "<br><br>" + esc(tw("office.info_2")) + "<br><br>" + esc(tw("office.info_3")));
  }

  function footHtml(d) {
    var miss = Object.keys((d && d.files) || {}).filter(function (k) { return !d.files[k]; });
    return '<div class="of-foot">' + esc(tw("office.foot", { at: (d && d.now_at) || "[?]" }))
      + (miss.length ? "<br>" + esc(tw("office.missing", { files: miss.map(function (k) { return FILE_KEY[k] ? tw(FILE_KEY[k]) : k; }).join(", ") })) : "")
      + "</div>";
  }

  // view3d: the department cards give way to a slot the 3D stage (office3d.js) is moved into, so the canvas
  // survives the 30-second redraw of everything around it.
  function pageHtml(d, view3d, now, ago) {
    var live = d.day === d.today;
    // in 3D the office comes right under the numbers, before the list of what needs the owner
    return '<div class="of-root">' + toolbarHtml(d, live, view3d) + kpiHtml(d) + nowHtml(now, ago)
      + (view3d ? '<div class="of-3d-slot"></div>' + issuesHtml(d) : issuesHtml(d) + deptsHtml(d)) + handoffsHtml(d) + feedHtml(d)
      + footHtml(d) + "</div>";
  }

  // What to do about a job, from its state (the 3D desk card).
  var TODO_KEY = { paused: "office.do_paused", failed: "office.do_failed", late: "office.do_late" };
  // The card a tapped desk opens in the 3D view.
  function describe(d, pick) {
    if (!pick || pick.kind === "empty") return "";
    if (pick.kind === "staff") {
      var dep = ((d && d.depts) || []).filter(function (x) { return (x.staff || []).some(function (s) { return s.slug === pick.id; }); })[0];
      return '<div class="o3-t">' + esc(pick.name) + "</div>" + (pick.role ? "<div>" + esc(pick.role) + "</div>" : "")
        + (dep ? '<div class="o3-m">' + esc(deptName(dep.id)) + "</div>" : "");
    }
    var j = jobById(d, pick.id);
    if (!j) return "";
    var day = j.day || {};
    var lines = [tw("office.runs_day", { ok: day.ok, n: day.runs }) + (j.target ? ", " + tw("office.target_day", { n: j.target }) : "")
      + (day.fail ? ", " + tw("office.fails_day", { n: day.fail }) : "")];
    if (j.last_at) lines.push(tw("office.last_run", { at: j.last_at }));
    if (j.paused_reason) lines.push(tw("office.why_paused", { why: j.paused_reason }));
    else if (j.result && j.result !== "ok" && j.result !== "fail") lines.push(j.result);
    return '<div class="o3-t">' + stateChip(j.state) + " " + esc(j.name) + "</div>"
      + '<div class="o3-m">' + esc(KIND_KEY[j.kind] ? tw(KIND_KEY[j.kind]) : "") + "</div>"
      + lines.map(function (x) { return "<div>" + esc(x) + "</div>"; }).join("")
      + (TODO_KEY[j.state] ? '<div class="o3-do"><b>' + esc(tw("office.todo")) + "</b> " + esc(tw(TODO_KEY[j.state])) + "</div>" : "");
  }

  var VIEW_KEY = "naota.office.view";
  function savedView() { try { return localStorage.getItem(VIEW_KEY) === "3d"; } catch (e) { return false; } }
  function saveView(v) { try { localStorage.setItem(VIEW_KEY, v ? "3d" : "cards"); } catch (e) { /* private mode */ } }

  var current_ = null;

  function mount(box, opts) {
    unmount();
    opts = opts || {};
    var O3 = typeof window !== "undefined" && window.NaotaOffice3D;
    var st = { day: "", timer: 0, alive: true, data: null, view3d: !!(O3 && O3.supported() && savedView()), v3: null, host3d: null,
      live: null, liveAt: 0, liveTimer: 0, tick: 0 };
    current_ = st;
    async function load() {
      if (!st.alive) return;
      var brain = (opts.current && opts.current()) || "brain";
      var url = "/office?brain=" + encodeURIComponent(brain) + (st.day ? "&day=" + encodeURIComponent(st.day) : "");
      var d = null;
      try { d = await (await fetch(url)).json(); } catch (e) { d = null; }
      if (!st.alive || !box.isConnected) return;
      if (!d || !d.depts) {
        if (!st.data) box.innerHTML = '<div class="of-root"><div class="of-none">' + esc(tw("office.load_fail")) + "</div></div>";
        return;
      }
      // keep open details open across a refresh
      var open = {};
      box.querySelectorAll("details.of-job[open] .of-jn").forEach(function (n) { open[n.textContent] = 1; });
      st.data = d;
      draw();
    }
    function draw() {
      var d = st.data, open = {};
      box.querySelectorAll("details.of-job[open] .of-jn").forEach(function (n) { open[n.textContent] = 1; });
      box.innerHTML = pageHtml(d, st.view3d, st.live, ago());
      if (st.view3d) place3d(d);
      box.querySelectorAll("details.of-job").forEach(function (el) {
        var n = el.querySelector(".of-jn");
        if (n && open[n.textContent]) el.open = true;
      });
    }
    function place3d(d) {
      var slot = box.querySelector(".of-3d-slot");
      if (!slot) return;
      if (!st.host3d) {
        st.host3d = document.createElement("div");
        st.host3d.className = "o3-host";
        st.v3 = O3.create(st.host3d, {
          describe: function (pick) { return describe(st.data, pick); },
          deptName: deptName,
          ownerName: function () { return tw("office.owner"); },
          deptStatus: function (dep) { return zoneSub(st.data, dep); },
          ticker: function (dd) { return tickerHtml(dd); },
          meetingName: function () { return tw("office.meeting_room"); },
          talkText: function (role) { return tw(TALK_KEY[role] || "office.talk_reply"); },
        });
      }
      slot.appendChild(st.host3d);
      st.v3.update(d);
      st.v3.running(runningIds());
      if (st.live) st.v3.people(st.live);
    }
    function ago() { return st.liveAt ? Date.now() / 1000 - st.liveAt : 0; }
    // loop and reminder ids running now, the ones that own a desk in the 3D office
    function runningIds() {
      var ids = {};
      ((st.live && st.live.items) || []).forEach(function (x) {
        if (x.kind === "loop" || x.kind === "reminder") ids[x.id] = true;
        if (x.agent_slug) ids[x.agent_slug] = true;   // an assistant working on a team step or a board card
      });
      return ids;
    }
    function paintNow() {
      var el = box.querySelector(".of-now");
      if (el) el.outerHTML = nowHtml(st.live, ago());
    }
    async function loadLive() {
      if (!st.alive) return;
      var brain = (opts.current && opts.current()) || "brain";
      var live = null;
      try { live = await (await fetch("/office/live?brain=" + encodeURIComponent(brain))).json(); } catch (e) { live = null; }
      if (!st.alive || !box.isConnected || !live || !live.items) return;
      var before = (st.live && st.live.items) || [];
      var gone = before.some(function (x) { return !live.items.some(function (y) { return y.kind === x.kind && y.id === x.id; }); });
      st.live = live; st.liveAt = Date.now() / 1000;
      paintNow();
      if (st.v3) { st.v3.running(runningIds()); st.v3.people(live); }
      var added = live.items.some(function (y) { return !before.some(function (x) { return x.kind === y.kind && x.id === y.id; }); });
      // a run just ended or new work was handed out: fetch the office again so the result or the handoff shows at once
      if ((gone || (added && st.liveSeen)) && !st.day) load();
      st.liveSeen = true;
    }
    box.addEventListener("click", function (ev) {
      if (ev.target.closest(".ofTg")) { try { window.NaotaNav.go("channels"); } catch (e) {} return; }
      if (!ev.target.closest(".ofView") || !st.data) return;
      st.view3d = !st.view3d && !!(O3 && O3.supported());
      saveView(st.view3d);
      if (!st.view3d && st.v3) { st.v3.destroy(); st.v3 = null; st.host3d = null; }
      draw();
    });
    box.addEventListener("change", function (ev) {
      if (ev.target && ev.target.classList.contains("ofDay")) {
        st.day = ev.target.value === (st.data && st.data.today) ? "" : ev.target.value;
        load();
      }
    });
    st.liveTimer = setInterval(function () { if (!document.hidden) loadLive(); }, 5000);
    st.tick = setInterval(function () { if (!document.hidden && st.live) paintNow(); }, 1000);
    loadLive();
    st.timer = setInterval(function () {
      if (document.hidden || st.day) return;   // a past day is a fixed record; a hidden tab costs nothing
      load();
    }, 30000);
    load();
  }

  function unmount() {
    if (!current_) return;
    current_.alive = false;
    clearInterval(current_.timer);
    clearInterval(current_.liveTimer);
    clearInterval(current_.tick);
    if (current_.v3) { try { current_.v3.destroy(); } catch (e) { /* page already gone */ } }
    current_ = null;
  }

  var api_ = { mount: mount, unmount: unmount, pageHtml: pageHtml, issueHtml: issueHtml, deptHtml: deptHtml,
    jobRowHtml: jobRowHtml, kpiHtml: kpiHtml, feedHtml: feedHtml, nowHtml: nowHtml, dur: dur, handoffsHtml: handoffsHtml, tickerItems: tickerItems, zoneSub: zoneSub, alertHtml: alertHtml, issuesHtml: issuesHtml, deptName: deptName, describe: describe };
  if (typeof window !== "undefined") window.NaotaOffice = api_;
  if (typeof module !== "undefined" && module.exports) module.exports = api_;
})();
