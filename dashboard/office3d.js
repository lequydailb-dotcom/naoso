/* Office page, 3D view.
 *
 * The same data as the cards (GET /office), drawn as one office: a floor zone per department, a desk per assistant and
 * a desk per automated job. A job desk carries a lamp in the job's real state (green ran right, blinking red failed or
 * paused itself, amber late, grey off or never ran). A department with nobody gets one empty desk and a sign.
 *
 * Truth rule: nothing moves on its own. A worker only types, and a check mark or a cross only rises, when a NEW run
 * appears in the logs, or while a past day is replayed from that day's own runs in order.
 *
 * three.js (MIT, dashboard/vendor) is fetched only when the owner opens this view, so the page costs nothing extra
 * until then. Without WebGL the view says so and the cards stay.
 */
(function () {
  "use strict";

  var THREE_URL = "/static/vendor/three-0.160.0.module.min.js";
  var ORBIT_URL = "/static/vendor/three-0.160.0-orbit-controls.js";

  function tw(key, vars) {
    var s = (typeof window !== "undefined" && window.t) ? window.t(key, vars) : key;
    if (vars) {
      s = String(s).replace(/\{(\w+)\}/g, function (m, name) {
        return Object.prototype.hasOwnProperty.call(vars, name) ? String(vars[name]) : m;
      });
    }
    return s;
  }

  function supported() {
    try {
      var c = document.createElement("canvas");
      return !!(window.WebGLRenderingContext && (c.getContext("webgl2") || c.getContext("webgl")));
    } catch (e) { return false; }
  }

  // ---------- pure layout (tested under node) ----------
  var LAMP = { ok: "ok", failed: "bad", paused: "bad", late: "ask", never: "off", off: "off", removed: "off", cancelled: "off", done: "off" };
  var COLS_IN_ZONE = 3, DESK_DX = 3.2, DESK_DZ = 3.0, ZONE_PAD = 1.4, ZONE_GAP = 1.6;

  // Desks of one department: assistants first, then live jobs, then finished ones; an empty department gets one empty desk.
  function zoneDesks(d, dep) {
    var jobs = (dep.jobs || []).map(function (id) { return (d.jobs || []).filter(function (j) { return j.id === id; })[0]; })
      .filter(Boolean);
    var rank = { failed: 0, paused: 0, late: 1, ok: 2, never: 3, off: 4, done: 5, cancelled: 5, removed: 6 };
    var r = function (j) { return j.state in rank ? rank[j.state] : 9; };   // 0 is a real rank, not "missing"
    jobs.sort(function (a, b) { return r(a) - r(b); });
    var desks = (dep.staff || []).map(function (s) { return { kind: "staff", id: s.slug, name: s.name, role: s.role }; })
      .concat(jobs.map(function (j) { return { kind: "job", id: j.id, name: j.name, state: j.state, lamp: LAMP[j.state] || "off" }; }));
    if (!desks.length) desks.push({ kind: "empty", id: "empty:" + dep.id, name: "" });
    return desks;
  }

  // Zones on a grid of up to 3 columns; each zone sized by its desks. Returns plain numbers, no three.js.
  // cols: how many departments side by side (2 on a tall phone screen, else 2 or 3 by count).
  function layout(d, cols) {
    var deps = (d && d.depts) || [];
    cols = cols || (deps.length <= 4 ? 2 : 3);
    var zones = deps.map(function (dep) {
      var desks = zoneDesks(d, dep);
      var rows = Math.ceil(desks.length / COLS_IN_ZONE);
      var w = Math.min(desks.length, COLS_IN_ZONE) * DESK_DX + ZONE_PAD * 2;
      return { dep: dep, desks: desks, w: Math.max(w, COLS_IN_ZONE * DESK_DX + ZONE_PAD * 2), dz: rows * DESK_DZ + ZONE_PAD * 2 + 0.6 };
    });
    var colW = [], rowD = [];
    zones.forEach(function (z, i) {
      var c = i % cols, r = Math.floor(i / cols);
      colW[c] = Math.max(colW[c] || 0, z.w);
      rowD[r] = Math.max(rowD[r] || 0, z.dz);
    });
    var totalW = colW.reduce(function (a, b) { return a + b; }, 0) + ZONE_GAP * (colW.length - 1);
    var totalD = rowD.reduce(function (a, b) { return a + b; }, 0) + ZONE_GAP * (rowD.length - 1);
    zones.forEach(function (z, i) {
      var c = i % cols, r = Math.floor(i / cols);
      var x0 = -totalW / 2, z0 = -totalD / 2;
      for (var k = 0; k < c; k++) x0 += colW[k] + ZONE_GAP;
      for (var m = 0; m < r; m++) z0 += rowD[m] + ZONE_GAP;
      z.x = x0 + colW[c] / 2; z.z = z0 + rowD[r] / 2; z.w = colW[c]; z.dz = rowD[r];
      z.desks.forEach(function (dk, n) {
        var cc = n % COLS_IN_ZONE, rr = Math.floor(n / COLS_IN_ZONE);
        var inRow = Math.min(COLS_IN_ZONE, z.desks.length - rr * COLS_IN_ZONE);
        dk.x = z.x + (cc - (inRow - 1) / 2) * DESK_DX;
        dk.z = z.z - z.dz / 2 + ZONE_PAD + 0.6 + rr * DESK_DZ + DESK_DZ / 2;
      });
    });
    return { zones: zones, w: totalW, d: totalD };
  }

  // What a replay shows at each step: the lamp of a job after each of that day's runs, in order.
  // A handoff of that day becomes a step too ({hand: {from, to}}), in time order with the runs.
  function replaySteps(d) {
    var lamps = {};
    var runs = ((d && d.day_feed) || []).map(function (f, i) {
      var good = f.result === "ok" || f.result === "verified_ok";
      var bad = f.result === "fail" || f.result === "verified_fail";
      return { ts: f.ts || 0, n: i, f: f, good: good, bad: bad };
    });
    var hands = ((d && d.handoffs) || []).map(function (h, i) { return { ts: h.ts || 0, n: 100000 + i, h: h }; });
    return runs.concat(hands).sort(function (a, b) { return (a.ts - b.ts) || (a.n - b.n); }).map(function (x) {
      if (x.h) return { hand: { from: x.h.from, to: x.h.to, status: x.h.status }, hm: x.h.hm, name: x.h.title };
      var f = x.f;
      lamps[f.job] = x.good ? "ok" : (x.bad ? "bad" : (lamps[f.job] || "off"));
      return { job: f.job, hm: f.hm, mark: x.good ? "ok" : (x.bad ? "bad" : "run"), lamp: lamps[f.job], name: f.name, note: f.note || "" };
    });
  }

  // ---------- the scene ----------
  function create(host, opts) {
    opts = opts || {};
    var st = { alive: true, data: null, T: null, seen: 0, replay: null };
    host.innerHTML = '<div class="o3-stage"><div class="o3-msg">' + tw("office.loading_3d") + "</div></div>";
    var stage = host.firstChild;

    var ready = Promise.all([import(THREE_URL), import(ORBIT_URL)]).then(function (m) {
      if (!st.alive) return;
      build(m[0], m[1].OrbitControls);
    }).catch(function () {
      if (st.alive) stage.innerHTML = '<div class="o3-msg">' + tw("office.no_webgl") + "</div>";
    });

    function build(T, OrbitControls) {
      st.T = T;
      stage.innerHTML = '<div class="o3-hud"><span class="o3-clock"></span><span class="o3-sp"></span>'
        + '<button type="button" class="o3-btn o3Replay"></button></div>'
        + '<div class="o3-hint">' + tw("office.hint_3d") + '</div><div class="o3-card" hidden></div>';
      var dark = matchMedia && matchMedia("(prefers-color-scheme: dark)").matches
        && !document.documentElement.matches('[data-theme="light"]');
      if (document.documentElement.matches('[data-theme="dark"]')) dark = true;
      st.dark = dark;
      var R = new T.WebGLRenderer({ antialias: true, alpha: false, powerPreference: "low-power" });
      R.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
      R.shadowMap.enabled = true;
      R.shadowMap.type = T.PCFSoftShadowMap;
      R.setClearColor(dark ? 0x15171c : 0xf4f3ef);
      stage.insertBefore(R.domElement, stage.firstChild);
      var scene = new T.Scene();
      var cam = new T.PerspectiveCamera(38, 1, 0.5, 200);
      var ctl = new OrbitControls(cam, R.domElement);
      ctl.enableDamping = true;
      ctl.maxPolarAngle = Math.PI * 0.44;
      ctl.minDistance = 8;
      ctl.maxDistance = 70;
      ctl.screenSpacePanning = false;
      scene.add(new T.HemisphereLight(0xffffff, dark ? 0x30343c : 0xd8d2c4, dark ? 0.9 : 1.15));
      var sun = new T.DirectionalLight(0xffffff, dark ? 1.1 : 1.6);
      sun.position.set(14, 24, 10);
      sun.castShadow = true;
      sun.shadow.mapSize.set(1024, 1024);
      sun.shadow.camera.left = -40; sun.shadow.camera.right = 40; sun.shadow.camera.top = 40; sun.shadow.camera.bottom = -40;
      scene.add(sun);
      st.R = R; st.scene = scene; st.cam = cam; st.ctl = ctl; st.world = new T.Group(); scene.add(st.world);
      st.lamps = {}; st.workers = {}; st.picks = []; st.fx = []; st.flights = [];
      var ro = new ResizeObserver(resize); ro.observe(stage); st.ro = ro;
      resize();
      wire();
      if (st.data) draw(st.data, true);
      loop();
    }

    function resize() {
      if (!st.R) return;
      var w = stage.clientWidth || 600, h = stage.clientHeight || 420;
      st.R.setSize(w, h, false);
      st.cam.aspect = w / h;
      st.cam.updateProjectionMatrix();
    }

    // ---- materials and labels ----
    var COL = { ok: 0x2fa86a, bad: 0xe0453a, ask: 0xf0a020, off: 0x9aa0a8, run: 0x2f8fff };
    function mat(c, extra) { var T = st.T; return new T.MeshStandardMaterial(Object.assign({ color: c, roughness: 0.75, metalness: 0.05 }, extra || {})); }
    function box(w, h, d, m) { var T = st.T; var o = new T.Mesh(new T.BoxGeometry(w, h, d), m); o.castShadow = true; o.receiveShadow = true; return o; }
    function label(text, sub, tone, scale) {
      var T = st.T, c = document.createElement("canvas"), g = c.getContext("2d");
      var font = '600 44px "Be Vietnam Pro", system-ui, sans-serif', fsub = '400 32px "Be Vietnam Pro", system-ui, sans-serif';
      g.font = font; var w1 = g.measureText(text).width; g.font = fsub; var w2 = sub ? g.measureText(sub).width : 0;
      var W = Math.ceil(Math.max(w1, w2) + 56), H = sub ? 128 : 76;
      c.width = W; c.height = H;
      g.fillStyle = st.dark ? "rgba(32,35,42,.94)" : "rgba(255,255,255,.95)";
      var r = 18; g.beginPath(); g.moveTo(r, 0); g.arcTo(W, 0, W, H, r); g.arcTo(W, H, 0, H, r); g.arcTo(0, H, 0, 0, r); g.arcTo(0, 0, W, 0, r); g.fill();
      if (tone) { g.fillStyle = "#" + COL[tone].toString(16).padStart(6, "0"); g.fillRect(0, 0, 10, H); }
      g.fillStyle = st.dark ? "#f2f2f2" : "#0e1116"; g.font = font; g.textBaseline = "top"; g.fillText(text, 28, 14);
      if (sub) { g.fillStyle = st.dark ? "#b8bcc4" : "#555b63"; g.font = fsub; g.fillText(sub, 28, 72); }
      var tex = new T.CanvasTexture(c); tex.colorSpace = T.SRGBColorSpace; tex.anisotropy = 4;
      // a fixed size on screen, so a far department reads as well as a near one
      var s = new T.Sprite(new T.SpriteMaterial({ map: tex, depthTest: false, transparent: true, sizeAttenuation: false }));
      var k = (scale || 1) * 0.00028 * (st.lab || 1);
      s.scale.set(W * k, H * k, 1);
      s.renderOrder = 10;
      return s;
    }
    function short(s, n) { s = String(s || ""); return s.length > n ? s.slice(0, n - 1) + "…" : s; }

    // ---- building the office from the data ----
    function clear() {
      var w = st.world;
      w.traverse(function (o) {
        if (o.geometry) o.geometry.dispose();
        if (o.material) { if (o.material.map) o.material.map.dispose(); o.material.dispose(); }
      });
      st.scene.remove(w);
      st.world = new st.T.Group(); st.scene.add(st.world);
      st.lamps = {}; st.workers = {}; st.picks = []; st.fx = []; st.flights = [];
    }

    function person(color) {
      var T = st.T, g = new T.Group();
      var body = new T.Mesh(new T.CapsuleGeometry(0.26, 0.42, 4, 10), mat(color));
      body.position.y = 0.78; body.castShadow = true; g.add(body);
      var head = new T.Mesh(new T.SphereGeometry(0.22, 18, 14), mat(0xf1c9a5));
      head.position.y = 1.36; head.castShadow = true; g.add(head);
      g.userData.head = head;
      return g;
    }
    function robot() {
      var T = st.T, g = new T.Group();
      var body = box(0.5, 0.55, 0.42, mat(st.dark ? 0x5b6472 : 0x8c96a5, { metalness: 0.4, roughness: 0.45 }));
      body.position.y = 0.72; g.add(body);
      var head = box(0.44, 0.34, 0.36, mat(st.dark ? 0x6c7584 : 0xa9b2bf, { metalness: 0.4, roughness: 0.4 }));
      head.position.y = 1.22; g.add(head);
      var eye = new T.Mesh(new T.BoxGeometry(0.3, 0.06, 0.02), new T.MeshBasicMaterial({ color: 0x9fe0ff }));
      eye.position.set(0, 1.25, -0.19); g.add(eye);
      g.userData.head = head;
      return g;
    }

    function desk(dk, zone, accent) {
      var T = st.T, g = new T.Group();
      g.position.set(dk.x, 0, dk.z);
      g.scale.setScalar(1.4);
      var wood = mat(st.dark ? 0x6b5a48 : 0xc8a67e), leg = mat(st.dark ? 0x3a3e46 : 0x6d727a);
      var top = box(1.7, 0.07, 0.85, wood); top.position.y = 0.76; g.add(top);
      [[-0.78, -0.36], [0.78, -0.36], [-0.78, 0.36], [0.78, 0.36]].forEach(function (p) {
        var l = box(0.06, 0.74, 0.06, leg); l.position.set(p[0], 0.37, p[1]); g.add(l);
      });
      var chair = box(0.55, 0.08, 0.55, mat(st.dark ? 0x2b2f36 : 0x3d434c)); chair.position.set(0, 0.48, 0.75); g.add(chair);
      var back = box(0.55, 0.6, 0.07, mat(st.dark ? 0x2b2f36 : 0x3d434c)); back.position.set(0, 0.8, 1.02); g.add(back);
      if (dk.kind !== "empty") {
        var mon = box(0.78, 0.48, 0.05, mat(0x1d2128)); mon.position.set(0, 1.08, -0.18); g.add(mon);
        var scr = new T.Mesh(new T.PlaneGeometry(0.7, 0.4), new T.MeshBasicMaterial({ color: dk.kind === "job" ? 0x22324a : 0x23384a }));
        scr.position.set(0, 1.08, -0.15); g.add(scr);
        var who = dk.kind === "job" ? robot() : person(accent);
        who.position.set(0, 0, 0.72); g.add(who);
        st.workers[dk.id] = who;
        // labels hang in the world, not in the scaled desk group, so they keep their screen size
        var tag = label(short(dk.name, 22), null, dk.kind === "job" ? dk.lamp : null, 1.0);
        tag.position.set(dk.x, 2.7, dk.z + 0.6); st.world.add(tag);
      } else {
        var sign = label(tw("office.empty_desk"), null, "off", 1.0); sign.position.set(dk.x, 2.2, dk.z); st.world.add(sign);
      }
      if (dk.kind === "job") {
        var lamp = new T.Mesh(new T.SphereGeometry(0.13, 16, 12), new T.MeshStandardMaterial({ color: COL[dk.lamp], emissive: COL[dk.lamp], emissiveIntensity: 1.2 }));
        lamp.position.set(0.66, 0.92, -0.2); g.add(lamp);
        var glow = new T.PointLight(COL[dk.lamp], dk.lamp === "off" ? 0 : 1.4, 2.6);
        glow.position.set(0.66, 1.1, -0.2); g.add(glow);
        var blink = dk.state === "failed" || dk.state === "paused";
        st.lamps[dk.id] = { mesh: lamp, glow: glow, lamp: dk.lamp, blink: blink, base: dk.lamp, baseBlink: blink };
      }
      // an invisible box for tapping the desk
      var hit = new T.Mesh(new T.BoxGeometry(2, 2.2, 2.2), new T.MeshBasicMaterial({ visible: false }));
      hit.position.y = 1.1; hit.position.z = 0.3; hit.userData.pick = dk; g.add(hit); st.picks.push(hit);
      st.world.add(g);
    }

    var ACCENT = [0xfccb1d, 0x009fe3, 0x7c5cff, 0x2fa86a, 0xff7a45, 0xe0457b, 0x18a4a0, 0x8a8f98];
    function draw(d, fit) {
      var T = st.T;
      clear();
      // labels shrink on a narrow stage so a phone is not covered in names
      st.lab = Math.min(1, Math.max(0.62, (stage.clientWidth || 900) / 900));
      var L = layout(d, (st.cam.aspect || 1) < 1 ? 2 : 0);
      var floor = new T.Mesh(new T.PlaneGeometry(L.w + 16, L.d + 16), mat(st.dark ? 0x1c1f25 : 0xe9e5dc));
      floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true; st.world.add(floor);
      var TONE = { green: "ok", red: "bad", orange: "ask", grey: "off" };
      L.zones.forEach(function (z, i) {
        var tone = TONE[z.dep.light] || "off";
        var rugc = new T.Color(st.dark ? 0x262a32 : 0xfbfaf7).lerp(new T.Color(COL[tone]), tone === "off" ? 0.06 : 0.16);
        var rug = new T.Mesh(new T.PlaneGeometry(z.w, z.dz), mat(rugc));
        rug.rotation.x = -Math.PI / 2; rug.position.set(z.x, 0.01, z.z); rug.receiveShadow = true; st.world.add(rug);
        var edge = new T.Mesh(new T.PlaneGeometry(z.w, 0.4), new T.MeshBasicMaterial({ color: COL[tone] }));
        edge.rotation.x = -Math.PI / 2; edge.position.set(z.x, 0.02, z.z - z.dz / 2 + 0.14); st.world.add(edge);
        var name = opts.deptName ? opts.deptName(z.dep.id) : z.dep.id;
        var sign = label(name, opts.deptStatus ? opts.deptStatus(z.dep) : "", tone, 1.9);
        // pinned by its left edge to the back-left corner of the zone, clear of the desks
        sign.center.set(0, 0.5); sign.position.set(z.x - z.w / 2 + 0.3, 0.3, z.z - z.dz / 2 + 0.5); st.world.add(sign);
        z.desks.forEach(function (dk) { desk(dk, z, ACCENT[i % ACCENT.length]); });
      });
      // the owner stands at the front edge: work the owner hands out starts here
      var owner = person(0xfccb1d);
      owner.position.set(0, 0, L.d / 2 + 1.2); owner.scale.setScalar(1.4); st.world.add(owner);
      st.workers.owner = owner;
      var otag = label(opts.ownerName ? opts.ownerName() : "owner", null, null, 1.0);
      otag.position.set(0, 2.9, L.d / 2 + 1.2); st.world.add(otag);
      if (fit) {
        var span = Math.max(L.w, L.d);
        // a narrow (phone) screen backs the camera off so every department still fits
        var f = Math.max(1, 1.4 / (st.cam.aspect || 1));
        st.cam.position.set(span * 0.18 * f, (span * 0.82 + 4) * f, (span * 0.5 + 4) * f);
        st.ctl.target.set(0, 0, 0);
        st.ctl.update();
      }
      clock("");
      st.runTags = {};
      applyRunning();
    }

    // ---- live: a job running at this second gets a blue lamp, a "running" tag and a worker who keeps typing ----
    function applyRunning() {
      if (!st.R || st.replay) return;
      var on = st.running || {};
      Object.keys(st.lamps).forEach(function (k) {
        var L = st.lamps[k];
        if (on[k]) setLamp(k, "run", false);
        else if (L.lamp === "run") setLamp(k, L.base, L.baseBlink);
      });
      Object.keys(st.runTags || {}).forEach(function (k) {
        if (on[k]) return;
        var s = st.runTags[k];
        st.world.remove(s); s.material.map.dispose(); s.material.dispose();
        var w = st.workers[k];
        if (w && w.userData.head.userData.y0 != null) w.userData.head.position.y = w.userData.head.userData.y0;
        delete st.runTags[k];
      });
      Object.keys(on).forEach(function (k) {
        var w = st.workers[k];
        if (!w || st.runTags[k]) return;
        var s = label(tw("office.running"), null, "run", 1.3);
        var p = new st.T.Vector3(); w.getWorldPosition(p);
        s.position.set(p.x, 3.35, p.z); st.world.add(s);
        st.runTags[k] = s;
      });
    }

    // ---- real events: a worker types and a mark rises ----
    function act(jobId, mark) {
      var w = st.workers[jobId];
      if (!w) return;
      var T = st.T;
      var sym = mark === "ok" ? tw("office.mark_ok") : (mark === "bad" ? tw("office.mark_bad") : "...");
      var s = label(sym, null, mark === "run" ? "off" : mark, 1.1);
      var p = new T.Vector3(); w.getWorldPosition(p);
      s.position.set(p.x, 2.6, p.z);
      st.world.add(s);
      st.fx.push({ sprite: s, t0: performance.now(), worker: w });
    }
    // a sheet of paper flies in an arc from the giver to the receiver, who then types
    function arcAt(a, b, t, out) {
      var e = t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
      var h = 3.2 + a.distanceTo(b) * 0.12;
      return out.set(a.x + (b.x - a.x) * e, 1.8 + Math.sin(Math.PI * t) * h, a.z + (b.z - a.z) * e);
    }
    function hand(from, to, status, title) {
      var a = st.workers[from] || st.workers.owner, b = st.workers[to];
      if (!a || !b || a === b) return;
      var T = st.T, pa = new T.Vector3(), pb = new T.Vector3();
      a.getWorldPosition(pa); b.getWorldPosition(pb);
      var tone = status === "failed" ? "bad" : "run";
      var paper = new T.Mesh(new T.BoxGeometry(1.0, 0.06, 1.3),
        new T.MeshStandardMaterial({ color: 0xffffff, emissive: COL[tone], emissiveIntensity: 0.35 }));
      paper.castShadow = true;
      st.world.add(paper);
      // the whole route, dashed, so the eye sees who gives to whom before the sheet lands
      var pts = [];
      for (var i = 0; i <= 32; i++) pts.push(arcAt(pa, pb, i / 32, new T.Vector3()));
      var line = new T.Line(new T.BufferGeometry().setFromPoints(pts),
        new T.LineDashedMaterial({ color: COL[tone], dashSize: 0.5, gapSize: 0.3, transparent: true, opacity: 0.9 }));
      line.computeLineDistances();
      st.world.add(line);
      var tag = title ? label(short(title, 26), null, tone, 0.9) : null;
      if (tag) st.world.add(tag);
      st.flights.push({ mesh: paper, line: line, tag: tag, a: pa, b: pb, t0: performance.now(), to: to, status: status });
    }

    function setLamp(jobId, lamp, blink) {
      var L = st.lamps[jobId];
      if (!L) return;
      L.lamp = lamp; L.blink = !!blink;
      L.mesh.material.color.setHex(COL[lamp]); L.mesh.material.emissive.setHex(COL[lamp]);
      L.glow.color.setHex(COL[lamp]); L.glow.intensity = lamp === "off" ? 0 : 1.4;
    }

    function loop() {
      if (!st.alive) return;
      st.raf = requestAnimationFrame(loop);
      if (document.hidden) return;
      var now = performance.now();
      st.ctl.update();
      var on = Math.floor(now / 550) % 2 === 0;
      Object.keys(st.lamps).forEach(function (k) {
        var L = st.lamps[k];
        if (L.blink) { L.mesh.visible = on; L.glow.intensity = on ? 1.6 : 0; }
        else L.mesh.visible = true;
        if (L.lamp === "run") L.glow.intensity = 1.2 + Math.sin(now / 160) * 0.9;
      });
      if (!st.replay) Object.keys(st.runTags || {}).forEach(function (k) {
        var w = st.workers[k];
        if (!w) return;
        var h = w.userData.head;
        if (h.userData.y0 == null) h.userData.y0 = h.position.y;
        h.position.y = h.userData.y0 + Math.abs(Math.sin(now / 1000 * Math.PI * 3)) * 0.06;   // typing while it runs
      });
      st.fx = st.fx.filter(function (f) {
        var t = (now - f.t0) / 1800;
        var h = f.worker.userData.head;
        if (h.userData.y0 == null) h.userData.y0 = h.position.y;
        if (t >= 1) {
          st.world.remove(f.sprite); f.sprite.material.map.dispose(); f.sprite.material.dispose();
          h.position.y = h.userData.y0;
          return false;
        }
        f.sprite.position.y = 2.6 + t * 1.4;
        f.sprite.material.opacity = 1 - t * t;
        h.position.y = h.userData.y0 + Math.abs(Math.sin(t * Math.PI * 6)) * 0.06;   // typing
        return true;
      });
      st.flights = (st.flights || []).filter(function (f) {
        var t = (now - f.t0) / 2400;
        if (t >= 1.35) {
          [f.mesh, f.line, f.tag].forEach(function (o) {
            if (!o) return;
            st.world.remove(o);
            if (o.geometry) o.geometry.dispose();
            if (o.material.map) o.material.map.dispose();
            o.material.dispose();
          });
          return false;
        }
        if (t >= 1) {
          // landed: the receiver gets to work, the route fades
          if (!f.landed) { f.landed = true; act(f.to, f.status === "failed" ? "bad" : (f.status === "done" ? "ok" : "run")); }
          f.line.material.opacity = 0.9 * (1.35 - t) / 0.35;
          if (f.tag) f.tag.material.opacity = (1.35 - t) / 0.35;
          return true;
        }
        arcAt(f.a, f.b, t, f.mesh.position);
        f.mesh.rotation.y = t * Math.PI * 2;
        if (f.tag) f.tag.position.set(f.mesh.position.x, f.mesh.position.y + 1.0, f.mesh.position.z);
        return true;
      });
      st.R.render(st.scene, st.cam);
    }

    // ---- tapping a desk ----
    function wire() {
      var T = st.T, ray = new T.Raycaster(), v = new T.Vector2(), down = null;
      var el = st.R.domElement;
      el.addEventListener("pointerdown", function (e) { down = [e.clientX, e.clientY]; });
      el.addEventListener("pointerup", function (e) {
        if (!down || Math.hypot(e.clientX - down[0], e.clientY - down[1]) > 6) return;
        var r = el.getBoundingClientRect();
        v.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
        ray.setFromCamera(v, st.cam);
        var hit = ray.intersectObjects(st.picks, false)[0];
        var card = stage.querySelector(".o3-card");
        if (!hit) { card.hidden = true; return; }
        var html = opts.describe ? opts.describe(hit.object.userData.pick) : "";
        if (!html) { card.hidden = true; return; }
        card.innerHTML = '<button type="button" class="o3-x" aria-label="' + tw("office.close") + '">×</button>' + html;
        card.hidden = false;
      });
      stage.addEventListener("click", function (e) {
        if (e.target.closest(".o3-x")) stage.querySelector(".o3-card").hidden = true;
        if (e.target.closest(".o3Replay")) { if (st.replay) stopReplay(); else startReplay(); }
      });
    }

    function clock(text) {
      var c = stage.querySelector(".o3-clock");
      if (c) c.textContent = text;
      var b = stage.querySelector(".o3Replay");
      if (b) b.textContent = st.replay ? tw("office.replay_stop") : tw("office.replay");
    }

    // ---- replay of the chosen day ----
    function startReplay() {
      var d = st.data, steps = replaySteps(d);
      if (!steps.length) { clock(tw("office.replay_none")); return; }
      Object.keys(st.lamps).forEach(function (k) { setLamp(k, "off", false); });
      var i = 0;
      var wait = 0;
      st.replay = setInterval(function () {
        if (wait > 0) { wait--; return; }
        if (i >= steps.length) { stopReplay(true); return; }
        var s = steps[i++];
        if (s.hand) { hand(s.hand.from, s.hand.to, s.hand.status, s.name); wait = steps.length > 40 ? 2 : 1; }
        else { setLamp(s.job, s.lamp, false); act(s.job, s.mark); }
        clock(tw("office.replay_at", { at: s.hm, n: i, total: steps.length }));
      }, steps.length > 40 ? 600 : 1100);
      clock(tw("office.replay_at", { at: steps[0].hm, n: 0, total: steps.length }));
    }
    function stopReplay(finished) {
      clearInterval(st.replay); st.replay = null;
      // back to the real state now; a job that stopped itself blinks red again
      if (st.data) draw(st.data, false);
      clock(finished ? tw("office.replay_done") : "");
    }

    return {
      update: function (d) {
        var first = !st.data;
        var newest = ((d && d.feed) || []).reduce(function (m, f) { return Math.max(m, f.ts || 0); }, 0);
        var fresh = first ? [] : ((d && d.feed) || []).filter(function (f) { return f.ts > st.seen; });
        st.seen = Math.max(st.seen, newest);
        var hs = (d && d.handoffs) || [];
        var hNew = hs.reduce(function (m, h) { return Math.max(m, h.ts || 0); }, 0);
        var freshH = first || !st.seenH ? [] : hs.filter(function (h) { return h.ts > st.seenH; });
        st.seenH = Math.max(st.seenH || 0, hNew);
        var sameDay = st.data && st.data.day === d.day;
        st.data = d;
        if (!st.R) return;
        if (st.replay) return;   // a running replay keeps the stage; it redraws when it ends
        draw(d, !sameDay);
        freshH.forEach(function (h) { hand(h.from, h.to, h.status, h.title); });
        fresh.forEach(function (f) {
          act(f.job, f.result === "ok" || f.result === "verified_ok" ? "ok" : (f.result === "fail" || f.result === "verified_fail" ? "bad" : "run"));
        });
      },
      // ids: {job id: true} of what runs right now (GET /office/live)
      running: function (ids) { st.running = ids || {}; applyRunning(); },
      ready: function () { return ready; },
      destroy: function () {
        st.alive = false;
        cancelAnimationFrame(st.raf);
        clearInterval(st.replay);
        if (st.ro) st.ro.disconnect();
        if (st.R) { try { clear(); } catch (e) { /* already gone */ } st.R.dispose(); }
        host.innerHTML = "";
      },
    };
  }

  var api_ = { supported: supported, create: create, layout: layout, zoneDesks: zoneDesks, replaySteps: replaySteps };
  if (typeof window !== "undefined") window.VanhanhOffice3D = api_;
  if (typeof module !== "undefined" && module.exports) module.exports = api_;
})();
