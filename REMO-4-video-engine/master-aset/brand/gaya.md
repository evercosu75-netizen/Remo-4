# Brand — Font, Label, Popup, Stempel

## Font (dari @fontsource, dipakai via `node_modules` template)

File font TIDAK disalin ke master aset — ambil dari `node_modules`
template remo-3 saat render, atau instal paket `@fontsource` yang sama.
Nama + bobot yang dipakai:

| Font | Pakai untuk | Bobot |
|---|---|---|
| Anton | Judul besar per adegan (uppercase) | 400 |
| Plus Jakarta Sans ("Jakarta") | Teks isi, kartu, popup, caption | 500 / 700 / 800 |
| Baloo 2 | Judul ramah / angka besar | 800 |
| Caveat ("hand") | Catatan tangan miring, mis. "bagaimana jika…" | 700 |
| DejaVu Sans Mono | Label adegan `// NN · …` (font sistem, bukan @fontsource) | — |

## Gaya label adegan (gaya Hari, dipakai v3/v4)

- Posisi: kiri atas, `left:28px; top:26px`, z-index 20.
- Font: monospace, 21px, letter-spacing .05em, warna `--foam` (#EAF6F6),
  bayangan teks 0 2px 0 rgba(0,0,0,.35).
- Format: `// 01 · hook`, `// 02 · bukan kabar baik`, dst. — nomor
  berurutan, judul adegan huruf kecil.

## Gaya caption bakar (burned-in, kata-per-kata)

- Posisi: `left:24px; right:24px; top:796px`, tengah, font 30px, bobot 800,
  warna putih, stroke ink 7px (`-webkit-text-stroke`, `paint-order:stroke fill`),
  bayangan 0 5px 0 rgba(0,0,0,.28), z-index 50.
- Kata yang ditekankan dibungkus `<b>` → warna `--aqua2` (#7FE7DC).
- Detail lengkap ada di `visual/komponen.css` (`#cap`).

## Gaya kartu popup INFO TAMBAHAN

- Kotak: `left:28px; top:672px; width:484px`, latar #FFFDF8, border 2.5px
  solid `--ink`, radius 10px, bayangan 5px 5px 0 rgba(6,34,46,.9),
  padding 8px 12px, z-index 45.
- Header: `ⓘ INFO TAMBAHAN`, 13px, bobot 800, letter-spacing .1em,
  warna `--danger` (#FF6B5E).
- Isi: 16px, bobot 700, line-height 1.32, warna `--ink`.
- Sumber: 12px, bobot 700, warna #5A6B70, format `Sumber: Nama, Tahun`.
- Aturan: popup hanya berisi fakta terverifikasi + sumber, muncul-hilang
  halus (pop + fade), jangan menutupi caption. Contoh isi yang pernah
  dipakai (v3): PFC ~1 jam (Kepuchina 2021); ventilasi PFC bayi prematur
  (Univ. Hawai'i 2026); dampak laut 2,2–2,6× 2050 (Halpern, Science 2025).

## Stempel SKENARIO HIPOTETIS — BUKAN FAKTA

- Border 4px solid `--foam`, teks `--foam`, font Anton uppercase,
  padding 6px 16px, radius 8px, rotasi -3deg, latar gelap transparan.
- Dipasang di adegan 01 dan di penutup untuk semua topik "bagaimana jika"
  / legenda yang belum terverifikasi.

## Kartu sumber akhir

- Kartu `.card`: latar `--foam`, border 2.5px solid `--ink`, radius 10px,
  bayangan 5px 5px 0 rgba(6,34,46,.9).
- Isi: daftar sumber yang benar-benar dibuka, singkat (nama + tahun).

## Outro referensi

- File `brand/outro-referensi-ayraku-3detik.mp4` (3,0 detik, 1080×1920):
  CTA "Jangan Lupa Like Subscribe dan Komen — by @AyraKu".
  **Ini untuk @AyraKu, BUKAN outro default Ternyata Begitu.**
  Disimpan di sini hanya sebagai contoh pola outro (kartu aksi + musik
  ceria 120 BPM + SFX). Ternyata Begitu belum punya outro sendiri —
  lihat gap di `PANDUAN.md`.
