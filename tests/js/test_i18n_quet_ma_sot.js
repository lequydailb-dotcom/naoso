/* Chữ vẽ TRƯỚC khi từ điển về không được kẹt ở dạng mã khoá.
 *
 *     python tests/run.py i18n_quet_ma_sot
 *
 * Trên naota.vuong.ai, khoảng 50 chỗ in nguyên mã khoá: chú thích menu trái (`page.chat.label`), nút trong cây file
 * (`common.delete`), dòng dưới file đang ghim ở ô chat (`app.pin_meta`). Các phần đó gọi t() khi từ điển chưa tới
 * và không vẽ lại. i18n/index.js nay rà cả trang khi từ điển về. Test dựng một trang giả, nạp index.js THẬT với
 * từ điển vi.json thật, rồi xem các mã khoá đã thành chữ chưa và chữ thường có bị đụng không.
 */
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const D = path.resolve(__dirname, "../../dashboard");

let loi = 0;
function check(ten, ok, chi_tiet = "") {
  console.log(`${ok ? "ok  " : "FAIL"} ${ten}${ok ? "" : "  " + chi_tiet}`);
  if (!ok) loi++;
}

const VI = JSON.parse(fs.readFileSync(path.join(D, "i18n", "vi.json"), "utf8"));
const EN = JSON.parse(fs.readFileSync(path.join(D, "i18n", "en.json"), "utf8"));

// ---- trang giả: đủ cho querySelectorAll("[title],[aria-label],[placeholder]") và createTreeWalker ----
function el(attrs, texts) {
  const a = Object.assign({}, attrs);
  return {
    attrs: a,
    texts: (texts || []).map((s) => ({ nodeValue: s })),
    getAttribute: (k) => (k in a ? a[k] : null),
    setAttribute: (k, v) => { a[k] = String(v); },
  };
}
const nutMenu = el({ title: "page.chat.label" });
const nutXoa = el({ title: "common.delete", "aria-label": "common.delete" });
const dongGhim = el({}, ["app.pin_meta"]);
const tenFile = el({ title: "note.md" }, ["note.md", "usage_index.db"]);
const coThamSo = el({ "aria-label": "cmark.question_n" });
const chuThuong = el({ title: "Trò chuyện" }, ["Xin chào"]);
const ALL = [nutMenu, nutXoa, dongGhim, tenFile, coThamSo, chuThuong];

const body = {
  querySelectorAll: () => ALL.filter((e) => ["title", "aria-label", "placeholder"].some((k) => e.getAttribute(k) !== null)),
};
const document = {
  body,
  documentElement: { setAttribute() {} },
  cookie: "",
  getElementById: () => null,
  querySelectorAll: () => [],
  createTreeWalker: () => {
    const nodes = ALL.flatMap((e) => e.texts);
    let i = 0;
    return { nextNode: () => (i < nodes.length ? nodes[i++] : null) };
  },
};
const hen = [];
const win = {
  document,
  navigator: { languages: ["vi"] },
  localStorage: { getItem: () => "vi", setItem() {} },
  sessionStorage: { getItem: () => null, setItem() {} },
  fetch: (url) => Promise.resolve({ ok: true, json: () => Promise.resolve(url.includes("/en.json") ? EN : VI) }),
  setTimeout: (f) => { hen.push(f); return hen.length; },
  clearTimeout() {},
  dispatchEvent() {},
  CustomEvent: function CustomEvent() {},
  location: { reload() {} },
  Date,
  Promise,
  JSON,
  Object,
};
win.window = win;
vm.createContext(win);
vm.runInContext(fs.readFileSync(path.join(D, "i18n", "index.js"), "utf8"), win);

const src = fs.readFileSync(path.join(D, "i18n", "index.js"), "utf8");
check("index.js có lượt rà mã khoá còn sót", src.includes("function quetMaSot("));
check("lượt rà chạy sau khi báo naota:i18n", /dispatchEvent\(new CustomEvent\("naota:i18n"[\s\S]{0,200}_quetHenGio\(\)/.test(src));

setImmediate(() => setImmediate(() => {
  while (hen.length) hen.shift()();
  check("NaotaI18n đã sẵn sàng", win.NaotaI18n && win.NaotaI18n.ready());
  check("chú thích menu trái thành chữ", nutMenu.attrs.title === VI["page.chat.label"], nutMenu.attrs.title);
  check("nút xoá: cả title lẫn aria-label thành chữ",
        nutXoa.attrs.title === VI["common.delete"] && nutXoa.attrs["aria-label"] === VI["common.delete"],
        JSON.stringify(nutXoa.attrs));
  check("dòng dưới file đang ghim thành chữ", dongGhim.texts[0].nodeValue === VI["app.pin_meta"], dongGhim.texts[0].nodeValue);
  check("tên file giống mã khoá (note.md) KHÔNG bị đụng",
        tenFile.attrs.title === "note.md" && tenFile.texts[0].nodeValue === "note.md" && tenFile.texts[1].nodeValue === "usage_index.db");
  check("khoá cần tham số không bị điền bừa", coThamSo.attrs["aria-label"] === "cmark.question_n");
  check("chữ thường giữ nguyên", chuThuong.attrs.title === "Trò chuyện" && chuThuong.texts[0].nodeValue === "Xin chào");
  check("hàm rà trả về số chỗ đã sửa (lượt hai: 0)", win.NaotaI18n.quetMaSot() === 0);
  console.log(loi ? `\n${loi} FAIL` : "\nOK");
  process.exit(loi ? 1 : 0);
}));
