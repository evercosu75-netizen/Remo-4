# Audio — SFX & SRT

## `sfx.py` (salinan)

Sumber: `bernafas-air-combined/template/sfx.py` (identik dengan versi v4).
Cara pakai: `python3 sfx.py [narasi.mp3]` → menghasilkan `sfx.wav`
(+ `mix.wav` bila ada narasi). Daftar momen SFX dibaca dari halaman
animatic (`window.SFX` + `window.DURATION`), jadi SFX terikat cue
adegan — bukan ditempel sembarangan.

SFX yang tersedia (semuanya sintetis, bebas hak cipta, dibuat dengan
numpy/scipy — bukan rekaman):

| Nama | Bunyi |
|---|---|
| `whoosh`, `blurwhoosh`, `zoom`, `boom`, `slices` | desing/sapuan transisi |
| `impact`, `stamp` | hentakan / stempel |
| `pop`, `tick`, `click` | letupan / ketukan kecil |
| `ding`, `chime` | lonceng penutup |
| `scratch`, `rise`, `swish` | gesek / naik / kibas |

Catatan: `sfx.py` butuh `scipy` + Playwright (membuka `animatic.html`
untuk membaca `window.SFX`). Di proyek v3/v4, SFX lalu digabung dengan
VO via ffmpeg menjadi `*-final-sfx.mp4`.

## Aturan audio di semua video

- VO dipakai apa adanya (tidak dipercepat/diperlambat), tanpa TTS berbayar baru.
- SFX sintetis saja, **tanpa musik latar** (kecuali diminta eksplisit).
  Pengecualian yang pernah ada: CTA Ayraku 3 detik pakai musik ceria
  sintetis 120 BPM C mayor + SFX — itu untuk @AyraKu, bukan standar
  Ternyata Begitu.
- Jangan menutupi narasi dengan SFX. Volume narasi tetap dominan.

## Patokan loudness (yang pernah terukur — sementara, bukan target resmi)

- v1 bernafas-air (remo-3): **-16,5 LUFS**
- CTA Ayraku 3 detik: **-14,0 LUFS**, peak -2,9 dBFS
- v3/v4 bernafas-air: level mentah mean -19,7 dB, max -3,1 dB
  (tidak clipping; nilai ini BUKAN LUFS, jangan dibandingkan langsung
  dengan dua angka di atas)
- Belum ada target loudness resmi channel — kalau Manggala menetapkan
  (mis. -14 LUFS seperti CTA), catat di sini dan normalisasi semua video
  ke target itu.

## Format SRT (`contoh.srt`)

Salinan dari `bernafas-air-combined.srt` (11 cue, 1 cue per kalimat).
Aturan SRT yang dipakai:

- 1 cue = 1 kalimat, maksimal 2 baris per cue.
- Format waktu `HH:MM:SS,mmm`, cue berurutan tanpa overlap.
- Timing dari word timing yang sama dengan video (estimasi silence
  detection, ±0,3 dtk — bukan transkripsi layanan).
- Kata yang diucapkan ditulis seperti ucapan ("dua puluh empat", bukan "24").
- Validasi sebelum serah: baca kembali file, cek penomoran + tidak ada
  cue yang tumpang tindih.
