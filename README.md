# REMO 4 — Video Explainer Studio V3

**REMO 4 = REMO 3 + master aset.**

Engine produksi video explainer animasi vertikal 9:16 (45–60 detik) untuk
Instagram Reels, YouTube Shorts, dan TikTok, dengan Dynamic Visual
Storytelling: engine yang sama, identitas visual berbeda tiap topik —
ditambah satu paket master aset yang dipakai ulang di semua video supaya
karakter dan hasil konsisten.

Dipanggil dengan **`/remo 4`** (skill `remo-4`). Remo-3 tetap ada sebagai
skill/repo terpisah dan tidak diubah oleh repo ini.

## Struktur folder

```
Remo-4/
├── README.md                     # file ini
└── REMO-4-video-engine/
    ├── README.md                 # dokumentasi engine (baca ini dulu)
    ├── LICENSE
    ├── skill/
    │   └── produksi-video-explainer/
    │       ├── SKILL.md          # skill Remo 4 (panggil /remo 4)
    │       └── skill.yaml
    ├── template/                 # template bersih Remo-4 (isi placeholder,
    │                             # wajib diganti total tiap produksi)
    ├── pose-studio/              # Studio Anatomi & Pose (Budi/Siti)
    ├── fauna-studio/             # Ensiklopedia 52 hewan
    ├── alam-studio/              # Katalog 135 entri alam (referensi)
    ├── barang-studio/            # Katalog 120 item (referensi properti)
    └── master-aset/              # paket aset reusable (karakter 3D/SVG,
                                  # brand, komponen visual, audio, panduan)
```

## Instalasi

```bash
git clone https://github.com/evercosu75-netizen/Remo-4.git
cd Remo-4/REMO-4-video-engine
```

Kebutuhan:

- Python 3.10+
- Node.js 18+
- FFmpeg
- Chromium + Playwright

Instalasi dependensi (dari folder `template/`):

```bash
cd template
npm install
pip install -r requirements.txt
python -m playwright install chromium
```

Periksa versi dengan `python --version`, `node --version`, dan
`ffmpeg -version` sebelum produksi.

## Cara pakai (singkat)

1. Panggil skill **`/remo 4`** dan kirim VO (WAV maupun MP3).
2. VO dipakai apa adanya — durasi video mengikuti durasi VO aktual.
3. Salin `REMO-4-video-engine/template/` ke folder proyek baru, tulis
   `words.js` baru dari transkripsi aktual (atau estimasi yang dilabeli
   ESTIMASI), isi `animatic.html` untuk topik itu, lalu frame check,
   render MP4, SFX, dan QA akhir.
4. Ikuti alur lengkap di
   [`REMO-4-video-engine/skill/produksi-video-explainer/SKILL.md`](REMO-4-video-engine/skill/produksi-video-explainer/SKILL.md)
   dan dokumentasi engine di
   [`REMO-4-video-engine/README.md`](REMO-4-video-engine/README.md).

Aturan yang mengikat: cek aset dulu sebelum bikin sendiri (lihat bagian 13
SKILL.md), jangan pernah pakai `words.js` dari proyek sebelumnya, dan
laporkan aset yang hilang — jangan diam-diam menggantinya dengan gambar
generik.

## Catatan jujur tentang file biner

File biner master aset (29 file: render PNG karakter 3D, contoh gaya flat
WebP, video referensi outro) **sudah ada di GitHub sejak 3 Nov 2026**,
di-upload lewat website github.com — konektor push hanya mendukung file
teks (UTF-8), jadi biner tidak bisa di-push lewat konektor. Screenshot
pengujian studio (37 file) tetap lokal saja — itu bukti pengujian, bukan
bahan produksi. Daftar lengkap + md5 ada di
[`REMO-4-video-engine/master-aset/MANIFEST-ASET-BINER.md`](REMO-4-video-engine/master-aset/MANIFEST-ASET-BINER.md).
Aturan LFS untuk biner ada di `.gitattributes` bila nanti dipakai.

## Remo-3 tetap terpisah

Engine Remo-4 diwarisi dari Remo-3, tapi Remo-3 tetap ada sebagai skill
dan repo terpisah (`evercosu75-netizen/Remo-3`) dan tidak diubah oleh repo
ini. Semua video baru memakai template Remo-4 di repo ini — jangan pakai
template Remo-3 untuk video baru.
