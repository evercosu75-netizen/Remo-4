# Karakter SVG 2D (alternatif)

File: `karakter.js` — salinan dari `bernafas-air-combined/template/karakter.js`
(template remo-3, MIT). Dipakai dengan `window.characterSVG({tokoh, ekspresi,
pose, mulut, kedip})`, menghasilkan SVG `viewBox="0 0 300 420"`.

## Tokoh (5)

| Tokoh | Kulit | Atasan | Ciri |
|---|---|---|---|
| `host` | #C2805A | merah #D9483B | pembawa acara utama, rambut hitam |
| `nur` | #C98B62 | kuning #E9A23B | pakai rok, bukan celana |
| `yohana` | #7A4A30 | biru #4A6FA5 | — |
| `togar` | #B07650 | biru muda #A9C2DA | — |
| `lina` | #E2B48C | ungu #7B5EA7 | rambut hitam panjang menutupi bahu |

## Ekspresi & pose

- Ekspresi (`ekspresi`): `senyum`, `kaget`, `berpikir` — mengubah alis,
  mata, dan mulut. `mulut` bisa di-override: `senyum` / `bicara` / `kaget` /
  `berpikir`. `kedip: true` untuk mata berkedip.
- Pose tangan kanan (`pose`): `santai`, `pegang-hp`, `kaget`, `berpikir`,
  `menunjuk`. Tangan kiri hanya naik kalau pose `kaget`.

## Kapan pakai SVG vs 3D

- **Pakai SVG** kalau butuh pembawa acara 2D yang ekspresif (bicara,
  kaget, menunjuk) dan konsisten dengan gaya remo-3 sebelumnya. Ringan,
  mudah dianimasikan per frame (kedip, gerak mulut mengikuti kata).
- **Pakai 3D** (`../karakter-3d/`) kalau butuh manusia yang terlihat
  "nyata"/bervolume dan kostum profesi (penyelam, nelayan, pekerja helm).
  Kekurangannya: sprite diam, tanpa ekspresi berubah.
- **Jangan pakai keduanya sekaligus** dalam satu video kecuali ada alasan
  visual yang jelas — campur 2D + 3D dalam satu adegan terlihat tidak konsisten.
