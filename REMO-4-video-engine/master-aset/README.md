# MASTER ASET — Ternyata Begitu

Sumber tunggal aset reusable untuk semua video explainer vertikal 9:16
(Reels / Shorts / TikTok). Dibangun 3 Nov 2026 dari aset-aset yang SUDAH ADA
di proyek-proyek sebelumnya — tidak ada aset baru yang diinvent di sini.
Semua file di folder ini adalah SALINAN; file asli di proyek masing-masing
tidak diubah/dipindah.

Aturan utama: **video baru = salin dari sini, jangan bikin ulang dari nol,
jangan ubah file di folder ini tanpa catat di README.**

## Isi folder

| Subfolder / file | Isi | Sumber asal | Dipakai di |
|---|---|---|---|
| `karakter-3d/` | Pipeline render karakter 3D + 11 PNG kostum transparan + contact sheet | `bernafas-air-v4-karakter3d/char3d/` + aset asli `user/files/cw_cwo_3d_1_fns0.html` | v4 bernafas-air |
| `karakter-svg/` | `karakter.js` — generator SVG 5 tokoh (host + lina = artwork baru dari GPT 3 Nov 2026; nur, yohana, togar diwarisi dari remo-3) (host, nur, yohana, togar, lina) | `bernafas-air-combined/template/karakter.js` | template Remo-4 |
| `brand/` | Palet, font, gaya label/popup/stempel, outro referensi | animatic v3, build Hari-style, video CTA Ayraku | v3, v4, CTA |
| `visual/` | `komponen.css` (label/popup/caption/stempel reusable) + 4 contoh gaya flat Hari + 2 contoh dokumen art direction | animatic v3, `bernafas-air-hari-style/` | v3, tes Hari |
| `audio/` | `sfx.py` (SFX sintetis) + `contoh.srt` (format SRT yang benar) + catatan loudness | `bernafas-air-combined/template/sfx.py`, `out/bernafas-air-combined.srt` | v3, v4 |
| `PANDUAN.md` | Cara pakai master aset untuk video baru + checklist QA + daftar kekurangan (gap) | — | — |
| `template-referensi.md` | Template/engine mana yang dipakai, TANPA menyalin skill remo-4 | — | — |

## Yang TIDAK ada di sini (sengaja)

- **Skill remo-4** (`custom-skills/remo-4/`) — tidak disalin ke master-aset,
  hanya dirujuk di `template-referensi.md`. Template kerja tetap diambil
  dari repo `evercosu75-netizen/Remo-4` / salinan lokal
  `workspace/remo-4-github/`.
- **VO per topik** (bakso, Soekarno, urine, dll.) — bukan aset master.
  VO baru disimpan di `workspace/user/files/` per video.
- **Foto produk user** (tumbler, crown cap) — aset per topik, bukan master.
  Tersimpan di `workspace/user/files/` dan folder proyek masing-masing.
- **Video final tiap proyek** — tetap di folder proyeknya (`out/`), bukan di sini.
  Yang disalin ke sini hanya `ayraku-cta-3detik.mp4` sebagai REFERENSI outro.

## Standar yang dijaga di semua video

- Format: **1080×1920, 30 fps, H.264 + AAC**, durasi mengikuti VO apa adanya.
- VO dipakai apa adanya (tidak dipercepat/diperlambat), tanpa TTS berbayar baru.
- SFX sintetis saja, tanpa musik latar (kecuali diminta eksplisit).
- Caption bakar kata-per-kata + file `.srt` eksternal per kalimat (lihat
  `audio/contoh.srt` untuk format yang benar).
- Label **"SKENARIO HIPOTETIS — BUKAN FAKTA"** untuk semua skenario
  "bagaimana jika" / legenda yang belum terverifikasi.
- Popup "INFO TAMBAHAN" hanya berisi fakta terverifikasi + nama sumber.
- QA: frame check sebelum render penuh, ffprobe + lihat frame QA dari MP4
  final sebelum diserahkan.

## Lisensi / catatan

- Template Remo-4 dan `karakter.js` (diwarisi dari Remo-3): MIT License
  (Weyeni.id / repo Remo-3 sebagai asal engine). Distribusi saat ini
  adalah Remo-4. Pertahankan pemberitahuan copyright pada distribusi
  turunannya.
- Three.js `vendor/three.module.js`: MIT License.
- SFX sintetis (`sfx.py`): bebas hak cipta (dibangkitkan dengan numpy/scipy).
- Ilustrasi flat contoh (`visual/contoh-gaya-flat/`): dibuat dengan
  `media.generate_image` untuk tes gaya Hari — contoh gaya, bukan stok bebas pakai
  tanpa cek ulang.
- Aset 3D asli: file kiriman Manggala (`cw_cwo_3d_1_fns0.html`,
  md5 `35442d8beb7dbbb17450560a6b34a784`). Salinannya ada di
  `karakter-3d/sumber-aset-asli.html` — jangan jadikan itu sumber utama;
  sumber utama tetap file di `workspace/user/files/`.
