/* Logo VANHANH và màu mặc định của linh vật (VANHANH 1.0.0).

       node tests/js/test_logo_linh_vat.js

   Logo là chữ (cùng kiểu logo ĐẠI LÊ AI): ô đen #0E1116 bo góc, chữ N
   vàng #FCCB1D Montserrat Black nghiêng. Linh
   vật vẫn là ngôi sao nhưng mặc định màu vàng "nắng" theo bộ màu thương hiệu, và không còn thay
   chỗ logo. Logo nằm ở nhiều chỗ (logo.svg, các PNG, MAC_DINH, nút Đặt lại) nên test khoá lại.

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

check("linh vật mặc định là NGÔI SAO", /var MAC_DINH = \{[^}]*shape: "star"/.test(pet));
check("linh vật mặc định màu NẮNG (vàng thương hiệu)", /var MAC_DINH = \{[^}]*palette: "nang"/.test(pet));
check("nút Đặt lại trả về ngôi sao màu nắng",
  /P\.setCfg\(\{ shape: "star", palette: "nang",/.test(read("dashboard/console.js")));
check("logo.svg là logo chữ VANHANH 1.0.0, bọc đúng ảnh PNG", /Logo VANHANH 1\.0\.0/.test(svg) && /href="data:image\/png;base64,/.test(svg));
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
