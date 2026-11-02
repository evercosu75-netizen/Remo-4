# REMO 4 — Video Explainer Studio V3

**REMO 4 = REMO 3 + master aset.**

Engine produksi video explainer animasi vertikal 9:16 (45–60 detik) untuk
Instagram Reels, YouTube Shorts, dan TikTok, dengan Dynamic Visual
Storytelling: engine sama dengan Remo 3, identitas visual berbeda tiap topik,
ditambah satu paket master aset yang dipakai ulang di semua video supaya
karakter dan hasil konsisten.

Dipanggil dengan **`/remo 4`**. Remo 3 tetap ada sebagai skill/repo terpisah
dan tidak diubah oleh repo ini.

## Isi folder

```
REMO-4-video-engine/
├── README.md                     # file ini
├── LICENSE
├── skill/
│   └── produksi-video-explainer/
│       ├── SKILL.md              # skill Remo 4 (panggil /remo 4)
│       └── skill.yaml
├── template/                     # engine produksi (disalin dari Remo 3, isi tidak diubah)
│   ├── animatic.html             # adegan, animasi, transisi, subtitle, timing
│   ├── karakter.js               # generator karakter SVG (5 tokoh remo-3)
│   ├── words.js                  # timestamp kata narasi
│   ├── frames.py                 # pemeriksaan frame
│   ├── render.py                 # rendering MP4
│   ├── sfx.py                    # pembuatan sound effects
│   └── naskah-contoh.txt
├── pose-studio/                  # Studio Anatomi & Pose Karakter Indonesia (Budi/Siti)
│   ├── studio-anatomi-pose.html  # FK 11 sendi, 7 preset, batik/kebaya, 3 kulit,
│   │                             # 4 ekspresi, 8 latar + 4 waktu + DoF, ekspor SVG/PNG/JSON
│   ├── TEST-REPORT.md            # hasil uji headless + perbaikan (proporsi 7,5 kepala
│   │                             # terverifikasi) + laporan merge background
│   ├── test-report.json
│   ├── test-merge-report.json
│   ├── test-headless.py
│   └── test-merge-background.py
├── fauna-studio/                 # Studio Ensiklopedia & Anatomi 50+ Fauna
│   ├── aset_50_hewan.html        # 52 kartu hewan Nusantara & dunia, search/filter
│   └── CATATAN.md                # batasan jujur (gambar sederhana, 48 hewan belum dicek faktual)
└── master-aset/                  # paket aset yang dipakai ulang di semua video
    ├── README.md / PANDUAN.md / template-referensi.md
    ├── karakter-3d/              # pipeline render Three.js + 11 PNG kostum (lihat catatan biner)
    ├── karakter-svg/             # karakter.js — 5 tokoh remo-3
    ├── brand/                    # palet, gaya label/popup/stempel
    ├── visual/                   # komponen.css + contoh art direction
    └── audio/                    # sfx.py + contoh.srt
```

## Cara pakai

1. Clone repo ini, lalu jalankan sesuai `skill/produksi-video-explainer/SKILL.md`.
2. Untuk video baru: salin `template/` ke folder proyek baru, tulis art direction
   singkat, pilih karakter dari `master-aset/` (3D untuk manusia berkostum,
   SVG untuk host ekspresif), pakai pose dari `pose-studio/` bila butuh pose
   atau latar, dan data/ilustrasi hewan dari `fauna-studio/` untuk topik fauna.
3. Jangan gambar karakter baru dari nol tanpa alasan — pakai master aset dulu.

## Catatan tentang file biner

Repo ini hanya berisi file teks. File biner master aset — render PNG karakter
3D (`master-aset/karakter-3d/renders/`), contoh gaya flat WebP
(`master-aset/visual/contoh-gaya-flat/`), video referensi outro
(`master-aset/brand/outro-referensi-ayraku-3detik.mp4`), serta screenshot
pengujian pose/fauna studio — **tidak ikut ter-push** karena konektor GitHub
yang dipakai hanya mendukung file teks (UTF-8). File-file itu tetap tersimpan
di salinan lokal workspace dan tetap menjadi bagian dari master aset Remo 4.

## Prinsip utama

SAME ENGINE, DIFFERENT VISUAL IDENTITY. Sistem timing, subtitle, audio,
rendering, dan komponen teknis dipakai ulang; desain visual setiap video
dikembangkan berdasarkan karakter topiknya.
