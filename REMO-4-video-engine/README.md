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
├── template/                     # template bersih Remo-4 (isi placeholder, wajib diganti total tiap produksi)
│   ├── animatic.html             # adegan, animasi, transisi, subtitle, timing
│   ├── karakter.js               # generator karakter SVG (5 tokoh, diwarisi dari remo-3)
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
├── alam-studio/                  # Katalog Aset Alam — 135 entri (emoji, bukan gambar)
│   ├── aset_alam.html            # 8 kategori alam, search/filter, ekspor JSON/Node.js
│   └── CATATAN.md                # katalog referensi + modul data, bukan sumber gambar
├── barang-studio/                # Katalog Aset & Inventaris — 120 item (emoji, bukan gambar)
│   ├── aset_barang.html          # 5 kategori × 24, search/filter, favorit, ekspor JSON/CSV
│   └── CATATAN.md                # daftar referensi properti; spesifikasi bukan fakta terverifikasi
└── master-aset/                  # paket aset yang dipakai ulang di semua video
    ├── README.md / PANDUAN.md / template-referensi.md
    ├── karakter-3d/              # pipeline render Three.js + 11 PNG kostum (lihat catatan biner)
    ├── karakter-svg/             # karakter.js — 5 tokoh (diwarisi dari remo-3)
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
   Untuk daftar properti/latar, cek `alam-studio/` (elemen alam) dan
   `barang-studio/` (properti harian/elektronik/kendaraan/dapur/kantor) —
   keduanya katalog referensi ber-emoji: jangan tempel emoji ke video, dan
   jangan kutip spesifikasi barang sebagai fakta tanpa verifikasi.
3. Jangan gambar karakter baru dari nol tanpa alasan — pakai master aset dulu.

## Catatan tentang file biner

File biner master aset — 29 file: render PNG karakter 3D
(`master-aset/karakter-3d/renders/` + `renders/raw/` + contact sheet),
contoh gaya flat WebP (`master-aset/visual/contoh-gaya-flat/`), dan video
referensi outro (`master-aset/brand/outro-referensi-ayraku-3detik.mp4`) —
**sudah ada di GitHub sejak 3 Nov 2026**, di-upload lewat website github.com
(konektor GitHub hanya mendukung file teks UTF-8, jadi biner tidak bisa
di-push lewat konektor). Screenshot pengujian pose/fauna studio (37 file)
tetap **lokal saja** — itu bukti pengujian, bukan bahan produksi.
Daftar lengkap + md5 ada di `master-aset/MANIFEST-ASET-BINER.md` — periksa
manifest itu sebelum memakai aset apa pun, dan laporkan kalau ada file yang
hilang. `.gitattributes` di root repo berisi aturan LFS untuk biner bila
nanti dipakai.

## Prinsip utama

SAME ENGINE, DIFFERENT VISUAL IDENTITY. Sistem timing, subtitle, audio,
rendering, dan komponen teknis dipakai ulang; desain visual setiap video
dikembangkan berdasarkan karakter topiknya.
