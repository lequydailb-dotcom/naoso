/* Logo NAOSO và màu mặc định của linh vật (NAOTA 1.0.0).

       node tests/js/test_logo_linh_vat.js

   Logo là chữ (cùng kiểu logo VUONG.AI): ô đen #0E1116 bo góc, chữ N
   vàng #FCCB1D Montserrat Black nghiêng. Bản 1.0.0 giữ linh vật là ngôi sao màu "nắng".
   Từ 1.60.0 (22/11/2026, chủ: "hình và mọi thứ vẫn còn như cái cũ", "toàn bộ hiển thị trên naota")
   linh vật mặc định mang dáng logo: ô vuông bo góc, màu vàng NAOTA #FCCB1D (bảng màu "naota"). Logo nằm ở nhiều chỗ (logo.svg, các PNG, MAC_DINH, nút Đặt lại) nên test khoá lại.

   KHÔNG dùng ký tự em dash. */
const fs = require("fs");
const path = require("path");
const ROOT = path.resolve(__dirname, "..", "..");
const read = (p) => fs.readFileSync(path.join(ROOT, p), "utf8");
const fails = [];
function check(name, cond, extra) {
  console.log((cond ? "ok   " : "FAIL ") + name + (cond || extra === undefined ? "" : "  [" + extra + "]"));
  if (!cond) fails.push(name);
}

const pet = read("dashboard/pet.js");
const svg = read("dashboard/logo.svg");

check("linh vật mặc định là Ô VUÔNG như logo", /var MAC_DINH = \{[^}]*shape: "square"/.test(pet));
check("linh vật mặc định màu VÀNG NAOTA", /var MAC_DINH = \{[^}]*palette: "naota"/.test(pet) && /naota:\s+\{ key: "pet\.color\.naota",\s+sun: \["#FCCB1D"/.test(pet));
check("nút Đặt lại trả về ô vuông vàng NAOTA",
  /P\.setCfg\(\{ shape: "square", palette: "naota",/.test(read("dashboard/console.js")));
check("trang Việc cần làm không còn ngôi sao cam cũ", !/#fd6100/i.test(read("dashboard/tasks.js")));
check("logo.svg là logo chữ NAOTA 1.0.0, bọc đúng ảnh PNG", /Logo NAOSO 1\.0\.0/.test(svg) && /href="data:image\/png;base64,/.test(svg));
check("logo.svg không còn ngôi sao cam cũ", !/#FD6100/i.test(svg));

// Các PNG phải là ảnh vuông đúng cỡ (đọc thẳng header PNG, khỏi cần thư viện ảnh).
for (const [ten, px] of [["logo.png", 512], ["icon-512.png", 512], ["icon-192.png", 192], ["favicon.png", 64]]) {
  const b = fs.readFileSync(path.join(ROOT, "dashboard", ten));
  const w = b.readUInt32BE(16), h = b.readUInt32BE(20), kieuMau = b[25];
  check(ten + " là PNG " + px + "x" + px + " có kênh trong suốt", b.toString("latin1", 1, 4) === "PNG" && w === px && h === px && kieuMau === 6,
    w + "x" + h + " kieu " + kieuMau);
}

console.log(fails.length ? "\nFAIL: " + fails.join(", ") : "\nTat ca OK");
process.exit(fails.length ? 1 : 0);
