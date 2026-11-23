<!-- translated-from: QUICKSTART.en.md sha256:9f8b8e3a6d68 -->
# NAOSO - Mulai cepat

*[English](../../../QUICKSTART.en.md) · [Tiếng Việt](../../../QUICKSTART.md) · [简体中文](../zh/QUICKSTART.md) · [Español](../es/QUICKSTART.md) · [日本語](../ja/QUICKSTART.md) · [हिन्दी](../hi/QUICKSTART.md) · [Português](../pt-BR/QUICKSTART.md) · [한국어](../ko/QUICKSTART.md) · [Русский](../ru/QUICKSTART.md) · [Deutsch](../de/QUICKSTART.md) · [Français](../fr/QUICKSTART.md) · **Bahasa Indonesia***

> Ini adalah terjemahan otomatis dari panduan mulai cepat berbahasa Inggris.

Jalankan NAOSO dalam beberapa menit. Panduan lengkap: [docs/en/](../../../docs/en/README.md).

## Komputer pribadi (Windows, macOS) - unduh penginstal

Pasang NAOSO seperti aplikasi biasa: unduh satu file, buka, lalu Anda punya ikon NAOSO untuk diklik setiap hari. Penginstal memeriksa apa yang belum ada di komputer (Git, Python, Node, otak AI) dan hanya memasang itu.

- **Windows 10/11:** unduh [Naota-Setup.exe](https://github.com/vuongtex/naota/releases/download/desktop/Naota-Setup.exe), klik dua kali, lalu tekan Next sampai selesai. Kemajuan pemasangan tampil di dalam jendela Setup itu sendiri, langkah demi langkah (beberapa menit), tanpa jendela hitam terpisah. Setelah selesai ada ikon NAOSO di Desktop dan menu Start.
- **macOS 11 atau lebih baru:** buka **Terminal** (Launchpad, ketik Terminal), tempel baris ini lalu tekan Enter. Dengan cara ini macOS tidak menampilkan peringatan:
  ```
  curl -fsSL https://raw.githubusercontent.com/vuongtex/naota/main/packaging/macos/get-naota.sh | bash
  ```
  Perintah ini mengunduh NAOSO, menyalin **NAOSO** ke **Applications**, dan memasangnya langsung di jendela Terminal itu (mungkin meminta Anda membuat akun admin NAOSO dan kata sandi Mac sekali). Setelah itu, buka NAOSO dari Launchpad.

  Lebih suka file? Unduh [Naota-macOS.dmg](https://github.com/vuongtex/naota/releases/download/desktop/Naota-macOS.dmg), buka, seret **NAOSO** ke **Applications**, lalu buka dari Launchpad. File ini belum ditandatangani dengan Apple Developer ID, jadi macOS memblokir saat pertama dibuka: cara mengizinkannya ada di bagian unduhan yang diblokir di bawah.

Mengklik ikon membuka NAOSO di jendelanya sendiri (tanpa bilah alamat), NAOSO berjalan bersama komputer, dan tombol **Update** di aplikasi berfungsi seperti biasa. Data Anda ada di folder `Naota` dalam folder pengguna; mencopot aplikasi tetap menyimpan folder itu.

**Windows: pasang tanpa layar peringatan (disarankan).** Penginstal Windows belum ditandatangani kode, jadi unduhan lewat browser diblokir pada kali pertama. Tempel satu baris saja dan Anda mendapat penginstal yang sama dengan logo NAOSO, tanpa diblokir: tekan Start, ketik `PowerShell`, buka, tempel baris ini lalu tekan Enter:
```
irm https://raw.githubusercontent.com/vuongtex/naota/main/packaging/windows/get-naota.ps1 | iex
```

Jika Anda sudah mengunduh file lewat browser dan diblokir:
- Edge atau Chrome menampilkan "Naota-Setup.exe isn't commonly downloaded" dan tidak menyimpan file: di kotak Downloads, arahkan kursor ke baris itu, klik tiga titik, pilih **Keep**, lalu **Show more** dan **Keep anyway**.
- Windows menampilkan "Windows protected your PC": klik **More info**, lalu **Run anyway**.
- Antivirus menghapus file, atau Windows memblokirnya tanpa tombol **Run anyway** (Smart App Control aktif): pasang tanpa file .exe. Pasang [Git](https://git-scm.com/download/win), buka PowerShell, tempel baris ini lalu tekan Enter. Setelah selesai, NAOSO terbuka di http://localhost:7777 dan berjalan bersama komputer:
  ```
  git clone https://github.com/vuongtex/naota.git "$env:USERPROFILE\NAOSO"; cd "$env:USERPROFILE\NAOSO"; powershell -ExecutionPolicy Bypass -File install.ps1
  ```
- macOS bilang tidak bisa membuka aplikasi: buka **System Settings → Privacy & Security**, gulir ke bawah, klik **Open Anyway**, lalu buka NAOSO lagi.

## Opsi 1 - VPS Hostinger (Docker Manager, sekali klik)

> 🛒 **Belum punya VPS?** [Sewa VPS Hostinger di sini](https://www.hostinger.com?REFERRALCODE=VUONGTEX). Docker Manager sudah tersedia, jadi NAOSO terpasang sekali klik. Setelah siap, kembali ke langkah di bawah.

1. hPanel → VPS → **Docker Manager** → **Compose** → **Compose from URL**.
2. Tempel URL ini:
   ```
   https://raw.githubusercontent.com/vuongtex/naota/main/docker-compose.hostinger.yml
   ```
3. (Opsional, untuk HTTPS + domain) isi ini di kotak **Environment**:
   ```
   DOMAIN_NAME=naota.<vps-hostname>.hstgr.cloud
   ```
   (Hostname ada di hPanel → VPS, contoh `naota.srv1234567.hstgr.cloud`.)
4. **Deploy**. Tunggu 1-3 menit. Buka aplikasi dengan tombol **Open** (atau `https://<DOMAIN_NAME>`).
5. Saat pertama dijalankan, layar akan meminta Anda membuat akun admin. Setelah itu, login ke Claude Code sekali saja dari terminal container: `claude auth login --claudeai`.

Untuk memperbarui: tekan **Redeploy** di Docker Manager (image `:latest`, `pull_policy: always`). Data Brain tetap tersimpan di volume.

## Opsi 2 - Docker di mesin atau VPS apa pun

> 🛒 **Butuh VPS?** [VPS Hostinger](https://www.hostinger.com?REFERRALCODE=VUONGTEX) juga bisa menjalankan opsi ini.

```
docker compose -f docker-compose.yml up -d
```
Buka http://localhost:7777. Untuk HTTPS lewat Caddy, tambahkan `-f docker-compose.https.yml`.

## Opsi 3 - Jalankan langsung (Windows, tanpa Docker)

1. Instal Python 3.12 + Node 22.
2. Di folder proyek, jalankan `setup.bat` sekali: script ini membuat .venv, menginstal dependency, dan menginstalkan dua engine CLI (Claude Code, Codex) untuk Anda.
3. `start-naota.bat` untuk menjalankan di background (`stop-naota.bat` untuk menghentikan).
4. Buka http://localhost:7777.

## Setelah berjalan

- **Pilih engine/model**: halaman **Models** (Claude Code, ChatGPT/Codex, Antigravity CLI, OpenRouter, OpenAI, Google Gemini, Anthropic API, Groq, Ollama).
- **Pasang koneksi** (POS, iklan, kalender, Zalo...) agar laporan memakai angka nyata: halaman **Connections**, lihat [docs/09](../../../docs/en/09-connections-and-business-data.md).
- **Backup Brain ke GitHub** agar data tidak hilang: halaman **Self-learning**, lihat [docs/18](../../../docs/en/18-github-backup.md).
- **Pantau pemakaian token**: halaman **Usage**, lihat [docs/23](../../../docs/en/23-usage-and-cost.md).

## Dokumentasi lengkap

Lihat [docs/en/README.md](../../../docs/en/README.md): satu panduan per fitur (chat/suara, knowledge graph, skill, agent, workflow, job berulang, Kanban, belajar mandiri, koneksi, Telegram, Zalo, plugin, keamanan, backup...). Panduan yang sama dalam bahasa Vietnam: [docs/README.md](../../../docs/README.md).

## Masalah umum

- **Tombol update di aplikasi tidak berfungsi di Hostinger**: memang dirancang begitu; di Hostinger gunakan **Redeploy** di Docker Manager. Tombol di aplikasi butuh Watchtower, dan Hostinger biasanya memblokir Docker socket.
- **ChatGPT/Codex bilang "model not supported"**: pilih model Codex yang valid di halaman Models (contoh `gpt-5.5`). Jangan pakai `gpt-5-mini` atau `gpt-4o`: itu model API dan akun Codex tidak bisa menjalankannya.
- Selengkapnya: [docs/17 - Pemecahan masalah](../../../docs/en/17-troubleshooting.md).
