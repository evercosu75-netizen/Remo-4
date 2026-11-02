# TEST-REPORT — Studio Aset Alam (135)

**File yang diuji:** `aset_alam.html` (salinan verbatim file asli, md5 `f632cc41…`; tidak ada perubahan).
**Metode:** headless Chromium + Playwright, skrip `~/workspace/remo-4/test-batch2.py`, hasil mentah `test-report.json`.
**Tanggal uji:** 3 Nov 2026 ~01:20 WIB.

## Ringkasan: LAYAK (sebagai katalog referensi + modul data)

| Uji | Hasil |
|---|---|
| Console / pageerror / failed request | 0 / 0 / 0 |
| Kartu ter-render | 135 (id unik 1–135) |
| Kategori | 8, hitungan tepat: Laut 28, Sungai & Danau 19, Bumi 18, Hutan 18, Langit 15, Fauna 15, Gunung 12, Elemen 10 |
| Filter "Laut & Samudra" | 28 kartu ✓ |
| Search "gunung" | 12 kartu ✓ (kategori Gunung & Vulkanik) |
| Search tanpa hasil | Empty state benar ("Tidak ada aset yang cocok") |
| Modal detail | Terbuka, nama + kategori + JSON benar |
| Salin | Toast "Tersalin ✓" |
| Ekspor JSON | 135 aset, valid |
| Ekspor Node.js | `module.exports` ada, lolos `node --check` |
| CDN | Tidak ada sama sekali (CSS mandiri) — tidak bisa mati karena CDN |
| Pagar markdown / Lucide | Tidak ada |

## Batasan
- Visual hanya emoji (bukan SVG). Peran: katalog referensi + modul data, bukan sumber gambar.
- 2 nama duplikat (Tanah, Batu), 37 emoji dipakai ulang. Kategori Fauna (15) lebih dangkal dari fauna-studio.

## Screenshot
- `shots/01-default.png` — 135 kartu, 8 chip kategori
- `shots/02-filter-laut.png` — filter Laut & Samudra
- `shots/03-modal.png` — modal detail "Bumi"
