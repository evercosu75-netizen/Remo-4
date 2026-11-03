# Karakter SVG 2D (alternatif)

File: `karakter.js` — salinan dari `bernafas-air-combined/template/karakter.js`
(template remo-3, MIT). Dipakai dengan `window.characterSVG({tokoh, ekspresi,
pose, mulut, kedip})`, menghasilkan SVG `viewBox="0 0 300 420"`.

## Tokoh (5)

| Tokoh | Kulit | Atasan | Ciri |
|---|---|---|---|
| `host` | #C2805A | merah #D9483B | pembawa acara utama — cowok dewasa BARU dari GPT (3 Nov 2026), rambut pendek + jambul |
| `nur` | #C98B62 | kuning #E9A23B | pakai rok, bukan celana |
| `yohana` | #7A4A30 | biru #4A6FA5 | — |
| `togar` | #B07650 | biru muda #A9C2DA | — |
| `lina` | #E2B48C | ungu #7B5EA7 | cewek dewasa BARU dari GPT (3 Nov 2026), rambut hitam panjang menutupi bahu |

## Tokoh baru dari GPT (3 Nov 2026)

- `host` (cowok) dan `lina` (cewek) diganti total ke artwork baru dari GPT,
  atas persetujuan Manggala. File sumber: `baru/cowok-dewasa.svg` dan
  `baru/cewek-dewasa.svg` (viewBox 300x420, grup ber-id). `nur`, `yohana`,
  `togar` TIDAK berubah (masih generator lama).
- API-nya sama persis (`{tokoh, ekspresi, pose, mulut, kedip}`): mulut
  bicara/kaget/berpikir dan alis diganti per ekspresi, kedip via scaleY
  grup mata, pose via rotasi lengan (berpikir = tangan ke dagu, pegang-hp =
  HP di tangan kanan, kaget = kedua lengan ke atas, menunjuk = lengan
  kanan ke atas-luar). Dites visual 3 Nov 2026: semua pose x ekspresi
  (host + lina) + kedip bersih, tanpa tangan hilang/lengan putus.
- **ATURAN MENGIKAT (SKILL.md remo-4 bag. 13): gender avatar HARUS cocok
  dengan gender suara VO** — VO cewek → `lina` (atau `nur`/`yohana`),
  VO cowok → `host` (atau `togar`). Kalau gender VO tidak jelas, tanyakan
  ke Manggala sebelum render penuh. Pelajaran dari video medan magnet
  (VO cewek, avatar cowok → revisi v2).

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
