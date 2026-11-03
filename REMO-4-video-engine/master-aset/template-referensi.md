# template-referensi.md

Jangan salin skill remo-4 ke folder master. Yang dipakai untuk video baru
adalah **REMO 4** — sumber resmi di bawah ini.

## Engine / template kerja (RESMI REMO 4)

- **Skill:** `~/workspace/custom-skills/remo-4/` (`SKILL.md`, panggil `/remo 4`).
  Dibaca saja — JANGAN diubah. Aturan yang sudah disepakati dengan Manggala:
  kalau dia memanggil skill + mengirim VO (WAV maupun MP3), langsung ke
  animasi + penggabungan dengan VO, lewati riset/naskah/TTS, kecuali dia
  minta sebaliknya. Tetap lakukan per-word timestamps, frame check,
  verifikasi render penuh, dan SFX sebelum MP4 final. Jangan minta
  persetujuan di tiap tahap kecuali ada error.
- **Repo template:** https://github.com/evercosu75-netizen/Remo-4
  (`REMO-4-video-engine/template/`). Salinan lokal:
  `~/workspace/remo-4-github/REMO-4-video-engine/template/`
  (jangan edit salinan ini — salin ke folder proyek baru tiap video).
- **File kunci template:** `animatic.html` (adegan/animasi/subtitle/timing),
  `karakter.js` (generator karakter SVG — salinannya ada di
  `master-aset/karakter-svg/karakter.js`), `words.js` (timestamp kata),
  `frames.py` (cek frame), `render.py` (render MP4 via Playwright +
  ffmpeg, 540×960 @30fps lalu upscale 1080×1920), `sfx.py` (SFX sintetis —
  salinannya ada di `master-aset/audio/sfx.py`).

## Tentang Remo-3 (asal engine — BUKAN sumber kerja)

Engine Remo-4 diwarisi dari Remo-3 (repo `evercosu75-netizen/Remo-3`,
salinan lokal `~/workspace/remo-3-github/`). Remo-3 hanya disebut di sini
sebagai **asal engine / referensi kompatibilitas**.

**JANGAN pakai template Remo-3 untuk video baru.** Semua video baru
wajib memakai template Remo-4 di atas. Remo-3 tetap ada sebagai
skill/repo terpisah dan **TIDAK BOLEH diubah** — jangan edit file apapun
di `~/workspace/custom-skills/remo-3/` atau `~/workspace/remo-3-github/`.
Kalau ada dokumen lain yang masih menunjuk Remo-3 sebagai sumber kerja,
abaikan dokumen itu dan ikuti dokumen ini + `SKILL.md` Remo-4.

## Template lain yang pernah dipakai (referensi saja)

- **remo-1** (`~/workspace/custom-skills/remo-1/`): gaya kliping berita,
  template lama `utama-wira/template-video-explainer`. Dipakai untuk
  bakso, Soekarno, air tawar.
- **remo-2** (`~/workspace/custom-skills/remo-2/`): Remotion (React,
  frame-accurate). Dipakai untuk Soekarno v2.
- **Gaya Hari** (bukan skill): assembly ffmpeg sederhana dari gambar flat
  + slow zoom + crossfade + caption per kalimat. Skrip contoh:
  `~/workspace/bernafas-air-hari-style/build.py` (baca-saja, jangan salin
  mentah — pola assembly-nya yang dipakai ulang). Contoh gambarnya ada di
  `master-aset/visual/contoh-gaya-flat/`.

## Alur render standar (remo-4)

0. Jalankan check-assets untuk memeriksa keberadaan setiap aset yang
   akan dipakai — kalau ada aset yang hilang, LAPORKAN ke Manggala,
   jangan diam-diam mengganti dengan gambar generik/emoji.
1. Salin template Remo-4 ke folder proyek baru → 2. **wajib ganti total**
   `words.js` + `animatic.html` untuk topik/VO baru (JANGAN PERNAH pakai
   `words.js` atau adegan dari proyek sebelumnya) → 3.
   `python3 frames.py <detik terpadat + transisi>` → lihat hasilnya,
   perbaiki → 4. `NAME=<judul> python3 render.py narasi.mp3` (atau
   `narasi.wav` — VO diterima WAV maupun MP3, durasi video mengikuti
   durasi VO aktual) → 5. `python3 sfx.py narasi.mp3` → gabung ffmpeg ke
   `*-final-sfx.mp4` → 6. ffprobe + QA frame dari MP4 final → 7. tulis
   `.srt` per kalimat.
