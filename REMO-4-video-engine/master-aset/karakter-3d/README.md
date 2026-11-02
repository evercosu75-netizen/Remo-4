# Karakter 3D — Cartoon Studio (cowok & cewek)

Sumber: file kiriman Manggala `workspace/user/files/cw_cwo_3d_1_fns0.html`
(Three.js 0.160, 2 karakter, 17 sendi, animasi idle/walk/run/wave/dance).
File asli TIDAK diubah (md5 `35442d8beb7dbbb17450560a6b34a784`).
Salinan mentahnya ada di `sumber-aset-asli.html` (jangan jadikan sumber utama).

## Cara render kostum/pose baru

```bash
cd ~/workspace/master-aset/karakter-3d
python3 render_chars.py [nama-kostum ...]   # render PNG mentah ke renders/raw/
python3 trim.py                              # potong transparan ke renders/
```

Cara kerja: `render.html` (Three.js lokal dari `vendor/three.module.js`,
tanpa CDN) dibuka headless via Playwright + server HTTP lokal
(modul ES tidak bisa dari `file://` karena CORS). Kostum didefinisikan
di `render.html` (objek `C`: ganti warna material + tambah props primitif
— masker, fin, rompi, topi, helm). Pose: `swim` / `shrug` / `wave` /
`stand` (lihat fungsi `applyPose()` di `render.html`).
Untuk kostum baru, tambah entri di `C` + baris di `JOBS`
(`render_chars.py`), lalu render ulang.

## PNG kostum yang sudah jadi (transparan, hasil trim)

| File | Isi | Dipakai di |
|---|---|---|
| `renders/penyelam-cowok.png` | Wetsuit teal gelap + masker + snorkel kuning + fin, pose berenang horizontal | v4 // 01, // 02, // 07, // 10 |
| `renders/penyelam-cewek.png` | Wetsuit ungu + masker + fin, pose berenang | v4 (cadangan kerumunan) |
| `renders/perenang-teal.png` | Swimwear teal, berdiri | v4 // 03 kerumunan |
| `renders/perenang-oranye.png` | Swimwear oranye, berdiri | v4 // 03 kerumunan |
| `renders/perenang-aqua.png` | Swimwear aqua, berdiri | v4 // 03, // 08 panel laut |
| `renders/perenang-pink.png` | Swimwear pink + rok, berdiri | v4 // 03 kerumunan |
| `renders/nelayan.png` | Baju biru + rompi oranye + topi biru | v4 // 05 |
| `renders/pekerja-helm-kuning.png` | Baju kuning + rompi oranye + helm kuning berlampu | v4 // 06 |
| `renders/orang-daratan-cowok.png` | Baju cokelat tanah | v4 // 08 panel daratan |
| `renders/orang-daratan-cewek.png` | Baju cokelat tanah | v4 (cadangan) |
| `renders/penyelam-shrug.png` | Wetsuit + masker, pose mengangkat bahu | v4 // 10 pertanyaan |
| `renders/raw/*.png` | Versi mentah sebelum trim (viewport 800×1000) | arsip / trim ulang |

Lihat `contact-sheet-kostum.png` untuk melihat semua kostum sekaligus.
(`renders/contact-sheet.png` adalah versi contact sheet dari folder render.)

## Batasan yang diketahui (jujur)

- Sprite adalah **gambar diam** — gerak di video hanya bobbing/pop CSS,
  bukan animasi 3D per frame.
- Rambut cowok aset dari depan nyaris tidak menutupi puncak kepala
  (terlihat agak botak). Tutupi dengan topi/helm/masker, atau perbaiki asetnya.
- Snorkel kuning pada pose berenang profil melintang di depan wajah.
- Ukuran sprite harus dicek per adegan (penyelam // 01 di v4 agak
  gelap/kecil; nelayan // 05 agak melayang — kakinya tidak persis di dek).
