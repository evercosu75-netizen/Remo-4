# template-referensi.md

Jangan salin skill remo-3 ke folder master. Yang dipakai untuk video baru:

## Engine / template kerja

- **Skill:** `~/workspace/custom-skills/remo-3/` (`SKILL.md`, panggil `/remo 3`).
  Dibaca saja — JANGAN diubah. Aturan yang sudah disepakati dengan Manggala:
  kalau dia memanggil skill + mengirim VO MP3, langsung ke animasi +
  penggabungan dengan VO, lewati riset/naskah/TTS, kecuali dia minta
  sebaliknya. Tetap lakukan per-word timestamps, frame check, verifikasi
  render penuh, dan SFX sebelum MP4 final. Jangan minta persetujuan di
  tiap tahap kecuali ada error.
- **Repo template:** https://github.com/evercosu75-netizen/Remo-3
  (`REMO-3-video-engine/template/`). Salinan lokal:
  `~/workspace/remo-3-github/REMO-3-video-engine/template/`
  (jangan edit salinan ini — salin ke folder proyek baru tiap video).
- **File kunci template:** `animatic.html` (adegan/animasi/subtitle/timing),
  `karakter.js` (generator karakter SVG — salinannya ada di
  `master-aset/karakter-svg/karakter.js`), `words.js` (timestamp kata),
  `frames.py` (cek frame), `render.py` (render MP4 via Playwright +
  ffmpeg, 540×960 @30fps lalu upscale 1080×1920), `sfx.py` (SFX sintetis —
  salinannya ada di `master-aset/audio/sfx.py`).

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

## Alur render standar (remo-3)

1. Salin template ke folder proyek baru → 2. isi `words.js` + `animatic.html`
   → 3. `python3 frames.py <detik terpadat + transisi>` → lihat hasilnya,
   perbaiki → 4. `NAME=<judul> python3 render.py narasi.mp3` → 5.
   `python3 sfx.py narasi.mp3` → gabung ffmpeg ke `*-final-sfx.mp4` →
   6. ffprobe + QA frame dari MP4 final → 7. tulis `.srt` per kalimat.
