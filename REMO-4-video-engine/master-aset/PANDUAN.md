# PANDUAN — Cara Pakai Master Aset untuk Video Baru

## Langkah kerja video baru (ringkas)

1. **Terima VO dari Manggala.** Simpan di `workspace/user/files/`.
   Cek durasi + md5 (kalau VO sama dengan video lama, jangan bikin ulang
   tanpa alasan — cek dulu folder proyek lama).
2. **Salin template kerja** dari repo Remo-4 (lihat `template-referensi.md`).
   Kerja di folder proyek BARU (`workspace/<topik>-explainer/`), jangan
   pernah edit template sumber atau proyek video lama.
3. **Tulis art direction singkat** (ikuti contoh di
   `visual/contoh-art-direction-gabungan.md`): konsep, palet, tipografi,
   gaya ilustrasi, komposisi per adegan, transisi.
4. **Pilih karakter** (lihat `karakter-3d/README.md` dan
   `karakter-svg/CATATAN.md`):
   - Butuh manusia yang terlihat "nyata" dan konsisten antar video
     → karakter 3D (PNG transparan dari `karakter-3d/renders/`, atau render
     kostum/pose baru dengan `karakter-3d/render_chars.py`).
   - Butuh pembawa acara 2D dengan ekspresi (senyum/kaget/berpikir) dan
     pose tangan (santai/menunjuk/pegang-hp) → karakter SVG
     (`karakter-svg/karakter.js`: host, nur, yohana, togar, lina).
   - Jangan pakai keduanya sekaligus dalam satu video kecuali ada alasan.
5. **Terapkan komponen visual dari `visual/komponen.css`**: label
   `// NN · …`, caption `#cap`, kartu `.card`, popup `.popup`,
   stempel `.stamp`, gelembung `.bub`, sinar `.ray`.
6. **Isi popup INFO TAMBAHAN hanya dengan fakta terverifikasi + sumber.**
   Jangan invent angka. Kalau belum terverifikasi, beri label
   "konon/legenda" atau jangan masukkan.
7. **Word timing + aturan input audio**: VO diterima WAV maupun MP3 —
   simpan apa adanya, jangan konversi diam-diam tanpa catat. Durasi video
   mengikuti durasi VO aktual (target 45–60 detik di SKILL.md adalah
   target, bukan pemaksaan percepat/perlambat VO — JANGAN percepat/
   perlambat VO kecuali Manggala minta eksplisit). Timing estimasi dari
   silence detection + alokasi proporsional per kalimat harus dilabeli
   ESTIMASI ±0,3 detik dan dibedakan jelas dari timing hasil transkripsi
   aktual — jangan klaim estimasi sebagai hasil transkripsi. JANGAN
   PERNAH pakai `words.js` dari proyek sebelumnya; tiap produksi wajib
   tulis `words.js` baru.
8. **Frame check SEBELUM render penuh**: 4–7 detik terpadat + titik
   transisi + satu frame tiap popup + satu frame tiap kostum. LIHAT
   gambarnya, perbaiki teks terpotong / elemen bertabrakan / karakter
   tertutup, baru render penuh.
9. **Render penuh → SFX (`audio/sfx.py`) → QA akhir**: ffprobe
   (1080×1920, 30 fps, H.264 + AAC, durasi mengikuti VO), lihat frame QA
   dari MP4 final (awal/tengah/akhir + popup), baca kembali file `.srt`.
10. **Serahkan MP4 + SRT + catatan batasan.** Jangan posting/menjadwalkan
    tanpa persetujuan Manggala per publish.

## Checklist QA (wajib sebelum serah)

- [ ] File MP4 ada, ukuran > 0, durasi ≈ durasi VO, 1080×1920, 30 fps, audio AAC
- [ ] VO apa adanya (tidak dipercepat/diperlambat), SFX saja tanpa musik latar
- [ ] Caption terbaca, tidak terpotong, tidak menutupi info utama
- [ ] Label `// NN` bernomor benar dan berurutan
- [ ] Popup (kalau ada) tidak menutupi caption, ada nama sumbernya
- [ ] Stempel SKENARIO HIPOTETIS ada kalau topiknya hipotetis/legenda
- [ ] Kartu sumber akhir ada dan sumbernya benar-benar dibuka
- [ ] File `.srt`: 1 cue per kalimat, maks 2 baris/cue, tanpa overlap,
      format waktu `HH:MM:SS,mmm` benar
- [ ] Karakter tidak terpotong / tidak melayang tanpa alasan / kostum terbaca
- [ ] Skill remo-3 dan remo-4 asli tidak berubah; template sumber tidak diedit, kerja di folder proyek baru

## DAFTAR KEKURANGAN (gap) — jujur, belum lengkap

Master aset ini BELUM lengkap. Yang masih butuh dari Manggala / dicari:

1. **Karakter 3D dengan animasi gerak beneran.** Aset sekarang hanya bisa
   dirender jadi PNG diam (gerak di video hanya bobbing/pop CSS). Belum ada:
   animasi berenang/berjalan/menunjuk per frame, ekspresi wajah berubah,
   sinkron mulut dengan VO. Yang dicari: file `.glb`/`.fbx` rigged dengan
   animasi, atau HTML Three.js lain yang sudah punya animasi swim.
2. **Rambut cowok aset 3D.** Dari depan, rambut aset nyaris tidak menutupi
   puncak kepala (terlihat agak botak). Perlu perbaikan di aset atau
   selalu pakai topi/helm/masker untuk karakter cowok.
3. **Logo Ternyata Begitu (PNG transparan) + warna/font resmi channel.**
   Logo Page sudah ada (lampu + clapper + buku + kaca pembesar), tapi file
   aslinya belum ada di workspace. Tanpa ini, intro/outro/kartu sumber
   belum bisa konsisten penuh.
4. **Musik latar / SFX pilihan.** Sejauh ini SFX sintetis saja
   (lihat `audio/CATATAN.md`). Belum ada musik latar atau pustaka SFX
   rekaman yang dipilih Manggala.
5. **Foto referensi per topik.** Foto asli / referensi visual per topik
   (seperti foto crown cap dan tumbler) sangat membantu akurasi, tapi
   sifatnya per topik — tidak bisa dijadikan master aset.
6. **Karakter SVG: hanya 5 tokoh, pose tangan terbatas** (santai,
   pegang-hp, kaget, berpikir, menunjuk). Belum ada pose berenang,
   memegang alat, atau kostum profesi.
7. **Video generatif (text-to-video) TIDAK tersedia** untuk akun/region ini
   (gagal 403, 2 Nov 2026, batasan permanen). Jalur video di sini tetap:
   ilustrasi/animasi kode + assembly ffmpeg, bukan generate klip AI.
