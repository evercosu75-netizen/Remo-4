# CATATAN — Fauna Studio REMO 4 (Ensiklopedia & Anatomi 50+ Fauna)

## Asal file
- File asli: `~/workspace/user/files/aset_50_hewan_5_cjo0.html` (TIDAK diubah, md5 `31eb4a7a43eb7bf80236ff7bfc45dd4b`)
- Salinan final: `~/workspace/remo-4/fauna-studio/aset_50_hewan.html` (102.494 byte)
- Perbaikan final (3 Nov 2026 ~01:00 WIB, hanya pada salinan final):
  1. Pagar markdown ```` ```html ```` di awal dan ```` ``` ```` di akhir dibuang
     (sebelumnya teks "html" nyasar tampil di pojok kiri atas layar).
  2. `lucide.createIcons()` dibungkus `safeCreateIcons()` (try/catch + cek
     `window.lucide`) — kalau CDN Lucide gagal, aplikasi tetap jalan.
- Dievaluasi headless sebelum finalisasi: `~/workspace/remo-4/staging-hewan/`
  (test-report.json + shots/ + exports/). Folder staging tetap sebagai bukti uji.

## Isi
- **Database 52 hewan** (klaim "50+" akurat): mamalia 14, aves 10, reptil 9,
  pisces 10, serangga 9. Per hewan: id, nama, nama latin, kelas, ikon, endemik,
  status IUCN, panjang, bobot, diet, sebaran, habitat default, deskripsi,
  3 fitur adaptasi, tipe SVG, warna, data organ.
- **Fitur yang teruji jalan**: filter per kelas (hitungan kartu cocok),
  search ("komodo" → 1, "harimau" → 1, "xyzqq" → 0), panel detail/inspector
  (nama, nama latin, badge kelas + IUCN, panjang, bobot, diet, sebaran,
  deskripsi, 3 fitur adaptasi), tombol pose (Santai/Gerak-Lari/Siaga/Tidur
  mengubah SVG), 6 pilihan habitat, ekspor SVG + PNG.
- **Gambar per hewan = template SVG per TIPE (36 svgType untuk 52 hewan)**,
  bukan ilustrasi per spesies; warna disesuaikan per spesies.

## Batasan — baca sebelum dipakai di video
1. **Gambar hewan sangat sederhana** (siluet datar bentuk dasar; komodo =
   pil abu-abu berkaki batang, harimau = gumpalan oranye bergaris loreng).
   Gaya flat-nya sejiwa dengan remo-3, tapi detail jauh di bawah Budi/Siti
   maupun render 3D. **Cocok sebagai ilustrasi kecil / ikon, BUKAN karakter
   hero tampil besar.**
2. **Overlay "Rangka & Sendi" generik dan tidak sejajar** dengan bentuk hewan
   (garis tulang biru melayang di luar badan harimau). Jangan dipakai sebagai
   referensi anatomi presisi.
3. **Data organ vital hanya ada di 1 dari 52 hewan** (harimau sumatera) — dan
   untuk harimau pun marker-nya nyaris tidak terlihat. Untuk 51 hewan lain
   toggle "Organ Vital" praktis tidak menampilkan apa-apa. **Ini ensiklopedia
   + ilustrasi, BUKAN atlas anatomi organ — jangan klaim begitu di video.**
4. **Fakta: hanya 4 dari 52 hewan yang dicek satu per satu** (komodo, harimau
   sumatera, buaya muara, orangutan — semuanya lolos, tanpa kesalahan
   mencolok). **48 hewan lain belum diverifikasi faktual.** Sebelum memakai
   angka/fakta satu hewan di narasi video, cek dulu sumbernya (seperti biasa
   di workflow remo: riset bersumber).
5. Toggle "Hanya Endemik" dan "Skala Manusia" ada di UI tapi belum diuji mendalam.

## Aturan pakai di video REMO 4
- **Kartu fakta** (deskripsi, fitur adaptasi, panjang/bobot, IUCN) → bahan
  kartu sumber / popup "INFO TAMBAHAN" di layar, setelah dicek sumbernya.
- **SVG hewan** (template svgType + warna spesies) → ilustrasi kecil/ikon di
  adegan, diekspor dari studio ini. Jangan dibesarkan jadi hero.
- **JANGAN** klaim studio ini sebagai atlas anatomi organ.
- **JANGAN** pakai gambar hewan sebagai karakter hero tampil besar — untuk
  itu pakai render 3D (`master-aset/karakter-3d/`) atau karakter SVG
  (`master-aset/karakter-svg/`, pose studio Budi/Siti).
