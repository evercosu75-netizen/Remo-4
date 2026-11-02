# Visual — contoh gaya flat & art direction

## Contoh gaya flat Hari (`contoh-gaya-flat/`)

4 ilustrasi dari tes gaya Hari untuk topik bernafas-air
(sumber: `bernafas-air-hari-style/assets/`, dibuat dengan
`media.generate_image`):

| File | Adegan |
|---|---|
| `hari-01-hook.webp` | Satu orang bernapas di dalam air, gelembung naik (adegan hook) |
| `hari-02-miliaran.webp` | Kerumunan / miliaran orang |
| `hari-03-tangkap-keruk.webp` | Tangkap ikan + keruk dasar laut |
| `hari-04-karang.webp` | Terumbu karang |

Ciri gaya: latar beige polos **#F0E7D8** (diukur dari piksel gambar),
bentuk sederhana, warna muted, tenang, tanpa teks di dalam gambar
(label adegan ditambahkan saat assembly, bukan di gambar).

**Batasan (jujur):** ini gambar diam — di video hanya bisa slow zoom +
crossfade, bukan animasi gerak penuh per elemen. Di tes Hari, kotak
caption adegan 03/04 menutupi sebagian visual. Pakai gaya ini untuk
explainer tenang; untuk adegan yang butuh gerak (ikan berenang, gelembung
naik, karang memudar), pakai animasi kode remo-3.

## Contoh dokumen art direction

- `contoh-art-direction-gabungan.md` — salinan dari v3 bernafas-air:
  contoh lengkap (konsep, identitas visual, palet, tipografi, gaya
  ilustrasi, komposisi, motion language, transisi, scene-by-scene,
  sumber, yang sengaja TIDAK diklaim). Ikuti strukturnya untuk video baru.
- `contoh-art-direction-remo3.md` — salinan dari v1 bernafas-air (remo-3):
  contoh art direction "TURUN KE LAUT" dengan 5 adegan.

## Komponen reusable

Lihat `komponen.css` — potongan CSS dari animatic v3: variabel palet,
label `// NN`, caption `#cap`, kartu, stempel, chip, popup, gelembung,
sinar, latar gradien laut. Detail pemakaian ada di komentar file itu
dan di `../brand/gaya.md`.
