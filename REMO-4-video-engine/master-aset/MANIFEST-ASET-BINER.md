# MANIFEST ASET BINER — REMO 4

**Tanggal inventaris:** 3 November 2026

**Repo:** https://github.com/evercosu75-netizen/Remo-4 — branch `main`

**Status ringkas (diperbarui 3 Nov 2026, 12:44 WIB):** 29 file biner master (Tabel 1) **SUDAH ADA di GitHub** — di-upload lewat website github.com dalam 5 commit (a2f0d98 renders, 08172ca raw, eee4101 outro, 5960139 gaya-flat, eab8059 contact-sheet-kostum). 37 file studio (Tabel 2) tetap **lokal saja** — itu screenshot pengujian, bukan bahan produksi, sengaja tidak di-upload.
(Folder `template/cek/` dan `template/parts/` dapat berisi artefak render sementara
— JPG/MP4 hasil frame-check — yang bukan aset dan tidak dicakup manifest ini.)

## Kenapa file biner sempat tidak ada di GitHub?

Konektor GitHub yang dipakai untuk push repo ini hanya mendukung file teks (UTF-8).
File biner (PNG, WebP, MP4) tidak bisa di-push lewat konektor tersebut — percobaan
push biner akan gagal / file ditolak. Ini batasan alat, bukan keputusan desain.
Karena itu 29 file biner master sempat hanya ada lokal, lalu di-upload manual lewat
website github.com pada 3 Nov 2026 (lihat Status ringkas di atas). Clone baru dari
GitHub kini mendapat file biner master itu langsung — tidak perlu salin manual lagi.

> ⚠️ **Peringatan — Tabel 1 sudah ada di GitHub, Tabel 2 tetap lokal saja.** Produksi video WAJIB memeriksa keberadaan file sebelum memakai aset (jalankan `python3 scripts/check-assets.py`). Kalau file HILANG, laporkan dan jangan diam-diam menggantinya dengan gambar generik.

## File teks besar yang ADA di GitHub (sering disangka hilang)

File ini berukuran besar sehingga kadang gagal dibaca sebagai teks oleh alat audit,
tetapi file-nya **ada** di GitHub dan isinya identik antara lokal dan staging:

- `karakter-3d/vendor/three.module.js` — 1.272.972 byte,
  md5 `a762b8588c6abf23cb87624360d014c4` — teks JavaScript (Three.js), ada di GitHub.
  md5 lokal = md5 staging, terverifikasi 3 Nov 2026.

## Tabel 1 — Aset biner master (wajib untuk produksi)

**29 file, total 3,260,998 byte (~3.11 MiB).**
Path relatif terhadap `master-aset/` — di repo:
`REMO-4-video-engine/master-aset/<path>`, lokal: `~/workspace/master-aset/<path>`.

| File | Ukuran (byte) | MD5 | Status |
|---|---|---|---|
| `brand/outro-referensi-ayraku-3detik.mp4` | 1494662 | `e66ad9d9655b17a0d13a45e70e1857f3` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/contact-sheet-kostum.png` | 273536 | `a2f0d83b662ed3233b73208d0e1214ce` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/contact-sheet.png` | 306636 | `2f4a233967735e36865311bf581fefda` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/nelayan.png` | 25645 | `0280c64856871fb085de903ef46a0e34` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/orang-daratan-cewek.png` | 32688 | `f4e8ec52324bbb6c8ce5e3c75667e7f8` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/orang-daratan-cowok.png` | 26447 | `f8b750a43ebe9375b2a91c52a5098e77` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/pekerja-helm-kuning.png` | 30227 | `4a0bc9ffe50eb53e98f86af4b16e9c75` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/penyelam-cewek.png` | 20530 | `f01e9dd6e4ddc50266665ce531571693` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/penyelam-cowok.png` | 17722 | `09c34afac892ab0f38ba1bda1f97447c` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/penyelam-shrug.png` | 33322 | `6838e553b8ea09c822e23ab20c31cc73` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/perenang-aqua.png` | 32676 | `503c4e131ccbfb4ce625159b22d49398` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/perenang-oranye.png` | 27475 | `bd1c99b4df6f0cf81e2d210d06de77b5` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/perenang-pink.png` | 32267 | `5c29639b8bcb4bb9de350b7542c31494` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/perenang-teal.png` | 27227 | `939326359dcdcce6aae664a2203d1edf` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/diver_f.png` | 28186 | `b390cac4b642753899e0c871be26fda6` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/diver_m.png` | 25067 | `3bfeb1a53cc156b33f76208cbb5f094b` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/diver_shrug.png` | 39915 | `d801c08ccf9b2b2a5b43ee199ec8bcd2` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/fisherman.png` | 33193 | `8f760cba7710a8db2672b50209b6cb2e` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/land_f.png` | 41782 | `ae166cecbcb400ead29be980ee470e03` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/land_m.png` | 34434 | `823ec1dedd8a3cccade725b577607203` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/miner.png` | 38194 | `f81704eefa1e04fa139112f14d459a44` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/swim_aqua.png` | 41453 | `da6430839d1e8a32b70a6d91702843c1` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/swim_orange.png` | 35517 | `345b854a335167ac907c6f9ad37ef375` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/swim_pink.png` | 40721 | `ab9f2918008739d156f4268673b98c15` | ADA di GitHub (web upload 3 Nov 2026) |
| `karakter-3d/renders/raw/swim_teal.png` | 35204 | `ef8573dbbc0e20675610c17b6380cec5` | ADA di GitHub (web upload 3 Nov 2026) |
| `visual/contoh-gaya-flat/hari-01-hook.webp` | 69030 | `4e094bc64d3a28d17f4161488d3b5550` | ADA di GitHub (web upload 3 Nov 2026) |
| `visual/contoh-gaya-flat/hari-02-miliaran.webp` | 175626 | `4b5a721b2189670a16fa08855de4ed59` | ADA di GitHub (web upload 3 Nov 2026) |
| `visual/contoh-gaya-flat/hari-03-tangkap-keruk.webp` | 133566 | `d1dc4b4f009233be82532d0bc9ba353c` | ADA di GitHub (web upload 3 Nov 2026) |
| `visual/contoh-gaya-flat/hari-04-karang.webp` | 108050 | `f53fc92a95adc2a51119e950b989326e` | ADA di GitHub (web upload 3 Nov 2026) |

Catatan tabel 1:

- `karakter-3d/renders/*.png` (11 file) adalah PNG kostum **hasil trim** (transparan,
  siap tempel ke adegan). `karakter-3d/renders/raw/*.png` (11 file) adalah versi
  **mentah sebelum trim** (viewport 800×1000) — arsip / bahan trim ulang.
- `karakter-3d/contact-sheet-kostum.png` (273.536 byte) dan
  `karakter-3d/renders/contact-sheet.png` (306.636 byte) adalah **dua file berbeda**
  (md5 dan ukuran berbeda) — jangan tertukar.
- `brand/outro-referensi-ayraku-3detik.mp4` adalah video **referensi outro 3 detik**,
  bukan outro final yang wajib dipakai di semua video.
- `visual/contoh-gaya-flat/*.webp` (4 file) adalah contoh gaya flat Hari — referensi
  visual, bukan aset adegan.

## Tabel 2 — Aset studio (opsional, lokal saja)

**37 file, total 10,506,519 byte (~10.02 MiB).**
Path relatif terhadap `~/workspace/remo-4/` — di repo (bila sudah di-upload):
`REMO-4-video-engine/<path>`. File-file ini adalah **screenshot pengujian dan
contoh ekspor studio, BUKAN bahan produksi video**. Video tetap bisa di-render
tanpa file-file ini; mereka hanya bukti bahwa studio sudah diuji.

| File | Ukuran (byte) | MD5 | Status |
|---|---|---|---|
| `alam-studio/shots/01-default.png` | 467182 | `c98b4b9d33da762f710e5bbf2805d3f0` | lokal saja — TIDAK ada di GitHub |
| `alam-studio/shots/02-filter-laut.png` | 476030 | `0241f844401c270cba1d53c47b48f66b` | lokal saja — TIDAK ada di GitHub |
| `alam-studio/shots/03-modal.png` | 241222 | `178b16ab1f6bb6641b7c5e7be79fb8cf` | lokal saja — TIDAK ada di GitHub |
| `barang-studio/shots/01-default.png` | 139269 | `a89c419029dcefea6f739f44068cbad5` | lokal saja — TIDAK ada di GitHub |
| `barang-studio/shots/02-search-tumbler.png` | 70494 | `e3513d8e90c4e4d7b3ae10a3ef324ecc` | lokal saja — TIDAK ada di GitHub |
| `barang-studio/shots/03-modal.png` | 213336 | `2e6a33f16791adc5a15906316ba5f784` | lokal saja — TIDAK ada di GitHub |
| `barang-studio/shots/04-lucide-blocked.png` | 134926 | `2009ad6592b3109741ad8b029174b86a` | lokal saja — TIDAK ada di GitHub |
| `barang-studio/shots/05-final-tanpa-pagar.png` | 143258 | `6c535b84c7d90b7539b19d07e56e5a6e` | lokal saja — TIDAK ada di GitHub |
| `fauna-studio/final-01-default.png` | 183659 | `64eb2e07c3f948a6e50208705b5a5124` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/exports/export-pose_female_indonesia_1793641998747.png` | 348418 | `e5e9f66882e79ea7519edb365e584531` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/exports/export-pose_female_indonesia_1793642032384.png` | 348418 | `e5e9f66882e79ea7519edb365e584531` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/01-default-pria-batik-senyum.png` | 266046 | `45bf6ab73130d95bac6f7c0ff640747c` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/02-preset-salam-santun.png` | 270462 | `c3061b4fde4b34228c1d5b7e26255ec3` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/03-preset-tolak-pinggang.png` | 282211 | `a076aa9a73b9b5c590d2fc99e17db02e` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/04-wanita-kebaya-semangat.png` | 263418 | `05f9ca93c2718aeba650dc05bcc39c9f` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/05-toggle-anatomi-otot.png` | 254035 | `cea3b90d72e8343d454addb4c74ca4b9` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/06-toggle-garis-titik-berat.png` | 249661 | `52a1e5787c7b4574a8888f789236948d` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/07-preset-berpikir.png` | 273973 | `d6e21ad02b94c425ab33ee8a04b5dd3e` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/08-tanpa-lucide-cdn.png` | 258001 | `92463bd0c8689fad50c344a02b5be169` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/09-latar-sawah-dof-aktif.png` | 336026 | `a25d6779d5d76c76d4475bf798df348b` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/10-latar-candi-senja.png` | 304915 | `dc0b540138427ce4b9ada62ac337501f` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/11-preset-salam-di-latar-candi.png` | 321063 | `fee19dd2c84faa2082aae42bad72caa6` | lokal saja — TIDAK ada di GitHub |
| `pose-studio/shots/12-latar-pantai-malam.png` | 298161 | `9f670bcf7a367520f9d942c8c423996f` | lokal saja — TIDAK ada di GitHub |
| `staging-background/exports/pose_male_transparan_senja_1793642038411.png` | 418400 | `0d21cb6f8754da6d416ebe43192a473b` | lokal saja — TIDAK ada di GitHub |
| `staging-background/shots/01-default.png` | 322317 | `3366fc5994538bdc1cdf9c4e28201895` | lokal saja — TIDAK ada di GitHub |
| `staging-background/shots/02-preset-salam.png` | 319248 | `b165f9e4893a48c3757f9decd1abdb00` | lokal saja — TIDAK ada di GitHub |
| `staging-background/shots/03-preset-tolak-pinggang.png` | 319974 | `3a299704a5fde6b2c06bddb96ccd2a9d` | lokal saja — TIDAK ada di GitHub |
| `staging-background/shots/bg-candi.png` | 326204 | `73b5ad903569edaa65a3460a26fcc793` | lokal saja — TIDAK ada di GitHub |
| `staging-background/shots/bg-sawah-dof-off.png` | 341017 | `db36c61bf4d97866d4638c6c62dedf6f` | lokal saja — TIDAK ada di GitHub |
| `staging-background/shots/bg-sawah-dof-on.png` | 355749 | `3b51f4bc3f1aa3857bde429a528abf67` | lokal saja — TIDAK ada di GitHub |
| `staging-background/shots/bg-sawah.png` | 337740 | `acda3bea8e53d47810a3f323117c3f50` | lokal saja — TIDAK ada di GitHub |
| `staging-background/shots/bg-transparan.png` | 282359 | `6ec7b37264b841e7be6a50bcbf9023b1` | lokal saja — TIDAK ada di GitHub |
| `staging-hewan/exports/fauna_badak_jawa_2x_1793642061876.png` | 428998 | `2a09865d7a1070dafd5d40b37d43bf90` | lokal saja — TIDAK ada di GitHub |
| `staging-hewan/shots/01-default.png` | 232257 | `4b159b6d096e3b2321576ff4f7c1ef55` | lokal saja — TIDAK ada di GitHub |
| `staging-hewan/shots/02-komodo-detail.png` | 229503 | `c16f3f07d3236df022f55362b4a14a03` | lokal saja — TIDAK ada di GitHub |
| `staging-hewan/shots/03-search-harimau.png` | 183547 | `d35e9ff7d0fb1bc3075aded5f467754b` | lokal saja — TIDAK ada di GitHub |
| `staging-hewan/shots/04-harimau-skeleton.png` | 265022 | `1419ecc4edd0703b26cdc8c7b757eda9` | lokal saja — TIDAK ada di GitHub |

Catatan tabel 2:

- `pose-studio/exports/export-pose_female_indonesia_1793641998747.png` dan
  `export-pose_female_indonesia_1793642032384.png` isinya **identik** (md5 sama) —
  dua ekspor dari pengujian yang sama, bukan dua pose berbeda.
- `staging-background/` dan `staging-hewan/` adalah folder kerja lokal di
  `~/workspace/remo-4/` dan **tidak ada dalam struktur repo GitHub** (repo hanya
  berisi `pose-studio/`, `fauna-studio/`, `alam-studio/`, `barang-studio/`).
  Isi `shots/`/`exports/`-nya dicatat di sini supaya tidak dikira hilang tanpa jejak.
- `alam-studio/exports/` dan `barang-studio/exports/` hanya berisi JSON/CSV (teks),
  jadi tidak masuk tabel biner ini.

## Total keseluruhan: 66 file biner, 13,767,517 byte (~13.13 MiB)

## Cara mendapatkan aset (bagi yang hanya clone dari GitHub)

1. Clone repo seperti biasa:
   `git clone https://github.com/evercosu75-netizen/Remo-4.git`
2. Aset biner master (Tabel 1) **ikut ter-clone** sejak 3 Nov 2026. Aset studio (Tabel 2) **tidak ikut ter-clone**. Dapatkan salinan studio dari salah satu sumber:
   - salinan lokal workspace Muse (`~/workspace/master-aset/` + `~/workspace/remo-4/`),
     lalu letakkan di `REMO-4-video-engine/master-aset/` (dan studio di
     `REMO-4-video-engine/<nama-studio>/`) dengan struktur path yang sama persis; atau
   - unduh dari GitHub Releases / LFS setelah aset di-upload ke sana (lihat bawah); atau
   - render ulang PNG kostum dari `master-aset/karakter-3d/` dengan
     `python3 render_chars.py` + `python3 trim.py` (butuh `vendor/three.module.js`,
     yang sudah ada di GitHub).
3. Verifikasi setelah menyalin:
   `python3 REMO-4-video-engine/scripts/check-assets.py` — harus `OK` semua
   (untuk aset master; lihat `--master-only`).

## Cara upload aset yang disarankan

Semua file biner di manifest ini berukuran < 2 MB (terbesar: MP4 outro 1.494.662
byte), jadi semuanya memenuhi batas upload web GitHub (< 25 MB per file).
Pilih **satu** cara — jangan campur tanpa mencatatnya:

### Opsi A — GitHub LFS (disarankan bila aset akan sering berubah)

- File `.gitattributes` di root repo sudah berisi aturan LFS untuk `*.png`,
  `*.webp`, `*.mp4`, `*.jpg`, `*.jpeg`, `*.gif` di bawah `master-aset/` dan studio.
- Upload **harus lewat git LFS di command line** (`git lfs install`, `git lfs track`,
  `git add`, `git commit`, `git push`) — **bukan** lewat konektor teks Muse, karena
  LFS hanya berlaku bila di-upload via git LFS.
- Setelah push LFS, clone baru tetap mendapat pointer LFS; jalankan
  `git lfs pull` lalu `python3 scripts/check-assets.py` untuk verifikasi.

### Opsi B — Upload manual via web github.com (paling sederhana)

- Buka repo di github.com → masuk ke folder tujuan → Add file → Upload files,
  lalu upload file biner sesuai path di tabel di atas. Semua file < 25 MB.
- Cocok untuk sekali upload; tidak perlu install LFS.

### Opsi C — GitHub Releases (bila tidak mau membesarkan repo)

- Bungkus aset biner menjadi arsip (mis. `master-aset-biner-2026-11-03.zip`),
  upload sebagai aset Release, dan cantumkan link + md5 di sini / di README.
- Repo tetap ringan; pengguna mengunduh arsip lalu mengekstraknya ke path yang benar.

Setelah aset berhasil di-upload dengan cara apa pun, perbarui kolom Status di tabel
di atas (mis. “ada di GitHub via LFS”) dan jalankan `check-assets.py` dari hasil
clone bersih sebagai bukti.

## Cara memperbarui manifest ini

Manifest dan `scripts/check-assets.py` harus selalu sinkron (keduanya memakai daftar
path + ukuran + md5 yang sama, dibuat 3 Nov 2026 dari inventaris lokal). Kalau ada
aset baru / berubah, ulangi inventarisasi:

```bash
find ~/workspace/master-aset -type f \( -iname '*.png' -o -iname '*.webp' -o -iname '*.mp4' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.gif' \) -exec md5sum {} +
find ~/workspace/remo-4 -type f \( -iname '*.png' -o -iname '*.webp' -o -iname '*.mp4' -o -iname '*.jpg' -o -iname '*.jpeg' -o -iname '*.gif' \) -exec md5sum {} +
```

lalu perbarui tabel di atas **dan** daftar `EXPECTED_MASTER` / `EXPECTED_STUDIO` di
`scripts/check-assets.py`, dan jalankan script dari staging dan dari lokal untuk
membuktikan kedua hasil itu.
