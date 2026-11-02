# TEST-REPORT — Pose Studio REMO 4 (sudah diperbaiki)

**File yang diuji:** `studio-anatomi-pose.html` (salinan dari
`~/workspace/pose-studio-test/studio-anatomi-pose.html`, HANYA salinan ini yang
diubah; file asli tidak disentuh — md5 asli tetap `c994d225871242ce9e760904ec76b1fb`).
**Metode:** headless Chromium + Playwright, CDN diproxy dari curl (sandbox tidak
bisa mencapai CDN langsung), skrip `test-headless.py`, hasil mentah
`test-report.json`, log `test-run.log`.
**Tanggal uji:** 3 Nov 2026 ~00:55 WIB.

## Ringkasan: SEMUA PERBAIKAN WAJIB (a–g) LULUS

| # | Perbaikan | Sebelum | Sesudah (terukur) |
|---|---|---|---|
| a | Proporsi 7,5 kepala | Puncak kepala y=273, karakter 607,7 px (~5,8 kepala) | Puncak kepala y=114,8 (panduan 110), dagu 219,8 (panduan 210), dada 309,8 (310), panggul 510 (510), lutut 709,2 (710), pergelangan kaki 858,7 (860). Total 114,8→860 = 745,2 px ≈ 7,5 kepala |
| b | Preset Salam | Tangan di pinggang (y~481) | Tangan bertemu di tengah dada: kiri (449,8; 386,9), kanan (466,2; 398,6), siku (345, 421)/(571, 433). Bukti: `shots/02-preset-salam-santun.png` |
| b | Preset Tolak Pinggang | Tangan setinggi bahu (shrug) | Tangan di panggul: kiri (395,5; 499,4), kanan (504,5; 499,4), siku mengangkang (319, 420)/(581, 420). Bukti: `shots/03-preset-tolak-pinggang.png` |
| b | Preset Berpikir (bonus) | Tangan di (605, 510), jauh dari dagu | Tangan kiri di dagu (459,1; 213,8), kepala (447,9; 160,6). Bukti: `shots/07-preset-berpikir.png` |
| c | Slider vs preset | 3 pelanggaran (menyapa forearmR −60 vs min −45; tolak pinggang forearmL +90 vs max 45, forearmR −90 vs min −45) | 0 pelanggaran di semua 7 preset (`clamped: []`). Max forearmL 45→90, min forearmR −45→−90. State awal forearmL/R 12/−12 → 10/−10 (sinkron dengan slider) |
| d | Cakram hitam sendi | Cakram hitam besar di tiap siku/lutut | Hilang (terlihat di semua screenshot): ujung kapsul rata + lingkaran sendi sewarna. Jari sederhana di kedua tangan (3 jari + jempol, mengikuti arah lengan bawah). Rambut pria: garis poni diturunkan −30→−16, dahi tidak lagi tampak botak |
| e | Toggle Anatomi Otot | `#layerMuscles` 0 children; toggle menimpa outfit jadi 'anatomy'/kembali 'batik' | Overlay striasi otot sungguhan: 44 elemen (garis + tick di 10 segmen + pektoral/abs). Outfit TIDAK tertimpa (diuji dari 'casual': tetap 'casual' saat ON dan OFF). Bukti: `shots/05-toggle-anatomi-otot.png` |
| f | Ketahanan CDN | `lucide is not defined` → `init()` mati, aplikasi mati total | `lucide.createIcons()` dibungkus `safeCreateIcons()` (try/catch + cek `window.lucide`). Diuji dengan unpkg diblokir total: 0 pageerror, karakter tetap render (15 sendi, 16 grup), 0 ikon — aplikasi hidup |
| g | CoG | Garis x=443,97, titik cx=450 (meleset ~6 px); label tertutup badan | Garis x1=x2=450, titik cx=450, label di (460, 104) — di atas garis, tidak tertutup badan |

## Bukti lain

- **Console:** 0 pageerror, 0 failed request (dengan CDN diproxy). Satu-satunya
  console message: warning Tailwind "should not be used in production".
- **Ekspor:** SVG 27.739 byte (valid, diawali `<svg id="stageSvg" viewBox=...`),
  PNG 348.418 byte, header `89504e47` valid, 1800×2000.
- **Wanita (Siti):** sendi kepala cy=159,8 (sama dengan pria), kebaya brokat +
  sanggul + ekspresi semangat bekerja. Bukti: `shots/04-wanita-kebaya-semangat.png`.
- **Menyapa:** tangan kanan terangkat (669,0; 163,7) di samping kepala — pose
  melambai benar.

## Screenshot

- `shots/01-default-pria-batik-senyum.png` — netral pria, batik
- `shots/02-preset-salam-santun.png` — Salam (tangan menangkup di dada)
- `shots/03-preset-tolak-pinggang.png` — Tolak Pinggang (tangan di panggul)
- `shots/04-wanita-kebaya-semangat.png` — Siti, kebaya, semangat
- `shots/05-toggle-anatomi-otot.png` — overlay otot aktif (outfit kasual utuh)
- `shots/06-toggle-garis-titik-berat.png` — garis + titik CoG satu sumbu
- `shots/07-preset-berpikir.png` — Berpikir (tangan kiri di dagu)
- `shots/08-tanpa-lucide-cdn.png` — halaman tetap jalan tanpa CDN Lucide

## Merge engine background (3 Nov 2026 ~01:00 WIB)

**Yang digabung:** HANYA engine background dari
`remo-4/staging-background/aset_background.html` (fungsi `renderBackground`,
8 latar, 4 waktu, toggle DoF + `dofFilter`, UI pemilih latar) ke pose studio
yang sudah diperbaiki di atas. Konstanta FK / preset lama dari file staging
TIDAK dibawa — diff vs sebelum merge: hanya 1 baris dihapus (nama file PNG
ekspor, sengaja diganti menyertakan latar + waktu); 0 baris kode FK/preset
berubah. Pagar markdown file staging tidak ikut tersalin (ekstraksi per
marker). `lucide.createIcons()` tetap hanya ada 1x, di dalam `safeCreateIcons()`
yang sudah ada. Skrip uji: `test-merge-background.py`, hasil mentah
`test-merge-report.json`, log `test-merge-run.log`.

| # | Yang diuji | Hasil (terukur) |
|---|---|---|
| 1 | Console | 0 pageerror, 0 failed request. Satu-satunya console message: warning Tailwind "should not be used in production" |
| 2 | UI latar | 8 kartu latar (candi, gadang, sawah, pantai, jakarta, blueprint, cyclorama, transparan), 4 tombol waktu, tombol DoF, `layerBackground` + `dofFilter` ada |
| 3 | Siklus 8 latar | Semua latar berganti (`state.background` cocok); isi `layerBackground` berbeda per latar (candi 3053, gadang 3756, sawah 2748, pantai 2529, jakarta 4085, blueprint 2227, cyclorama 1453, transparan 166 karakter); karakter tetap 16 grup |
| 4 | Siklus 4 waktu | Pagi/Siang/Senja/Malam berganti (`state.timeOfDay` cocok); di latar candi, Malam berbeda isinya (3663 karakter, ada bulan sabit) vs Pagi/Siang/Senja ~3052–3053 (hanya warna langit berubah) |
| 5 | DoF di sawah | Sebelum: `filter` null; sesudah klik: `filter="url(#dofFilter)"`, tombol "Aktif". Bukti visual: `shots/09-latar-sawah-dof-aktif.png` — latar blur, karakter tajam |
| 6 | Latar candi senja | Bukti: `shots/10-latar-candi-senja.png` |
| 7 | Kepala vs panduan (setelah merge) | Puncak karakter (bbox) y=114,8 (panduan 110), dagu 219,8 (panduan 210) — SAMA seperti sebelum merge, tidak bergeser |
| 8 | Preset Salam di atas latar candi | Tangan kiri (449,8; 386,9), kanan (466,2; 398,6) — tetap menangkup di dada; `clamped: []`. Bukti: `shots/11-preset-salam-di-latar-candi.png` |
| 9 | Preset Tolak Pinggang di atas latar | Tangan kiri (395,5; 499,4), kanan (504,5; 499,4) — tetap di panggul (panggul y=510); `clamped: []` |
| 10 | Bonus | `shots/12-latar-pantai-malam.png` — pantai + waktu Malam |

## Yang BELUM selesai / cacat kecil yang tersisa

1. **Ekspor karakter-saja belum ada.** Ekspor SVG/PNG masih mengikutkan grid,
   garis panduan, dan skeleton (seperti sebelumnya). Perlu opsi "karakter saja".
2. **Kaki terpotong di viewport 1600×1000 pada screenshot 01** (sudah ada
   sebelum perbaikan; zoom-out / jendela lebih tinggi mengatasinya).
3. **Dagu 219,8 vs panduan 210** (selisih ~10 px, bentuk dagu path +60 dari
   pusat kepala) dan **puncak 114,8 vs 110** (selisih ~5 px) — dalam toleransi
   "≈" dan tidak diperbaiki lebih jauh supaya bentuk kepala tidak berubah.
4. **Sanggul Siti** menjorok ~19 px di atas garis puncak (top −69 relatif) —
   wajar untuk sanggul, bukan cacat.
5. **Aset batch pertama REMO 4 — SELESAI.** File background sudah di-merge
   ke pose studio ini (lihat bagian merge di atas); file hewan sudah
   difinalisasi di `remo-4/fauna-studio/` (pagar markdown dibuang,
   `lucide.createIcons()` dibungkus try/catch; 0 pageerror, 52 kartu, search
   jalan, tetap hidup saat CDN Lucide diblokir). Folder staging
   (`remo-4/staging-background/`, `remo-4/staging-hewan/`) tetap sebagai
   bukti uji.
