# CATATAN — Studio Katalog Barang (120 Item)

## Asal file
- File asli: `~/workspace/user/files/aser_barang_120_item_7_1m2c.html` (TIDAK diubah)
- Salinan final: `~/workspace/remo-4/barang-studio/aset_barang.html`
- md5 asli: `a631b34ac59c8d971c8a663874869573`; md5 final: `91e0595ddaccf54d5a48332509cb7fed`
  (beda karena 2 baris pagar markdown dibuang — satu-satunya perubahan)
- Ukuran: 72.885 byte, 908 baris
- Judul: "Katalog Aset & Inventaris Terpadu (100+ Aset)"
- Dievaluasi headless: 3 Nov 2026 ~01:20 WIB (Playwright + Chromium, CDN diproxy; skrip
  `~/workspace/remo-4/test-batch2.py`)
- Laporan lengkap: `test-report.json` di folder ini; screenshot: `shots/`; ekspor: `exports/`

## Isi terukur
- **120 item, terkonfirmasi** (id unik 1–120), 5 kategori × 24 tepat: Barang Harian, Elektronik &
  Gadget, Kendaraan & Transportasi, Peralatan Rumah & Dapur, Kantor & Belajar.
- Tiap item berisi `{id, name, nameEn, category, icon/emoji, tags, spec}` — **visualnya emoji,
  BUKAN gambar SVG**. Tidak ada item tanpa spec (0 kosong).
- Fitur teruji: filter 5 kategori (elektronik → 24 tepat), search (contoh "tumbler" → 1),
  empty state benar (0 kartu + pesan kosong tampil), modal detail (nama ID + EN + kategori + spec + JSON),
  favorit/bookmark (badge 1, filter "hanya favorit" → 1), salin nama/JSON per item, ekspor JSON
  (120 item) + ekspor CSV (121 baris = header + 120).
- Uji headless: **0 pageerror** (hanya warning Tailwind "should not be used in production").
  Dengan CDN Lucide diblokir total: 0 pageerror, 120 kartu tetap render — pemanggilan
  `lucide.createIcons()` sudah dijaga `if (window.lucide)` di 5 tempat, jadi aplikasi aman dari CDN gagal.
- 377 ikon Lucide UI ter-render saat CDN tersedia.

## Perbaikan yang dilakukan (hanya di salinan final)
- **Pagar markdown dibuang**: file asli diawali ```` ```html ```` dan diakhiri ```` ``` ```` — teks
  "```html" tampil di pojok kiri atas halaman. Setelah dibuang, uji ulang: 0 pageerror, 120 kartu,
  teks halaman diawali "AsetHub Explorer" (bukti: `shots/05-final-tanpa-pagar.png`).

## Batasan jujur
- Visual hanya emoji — BUKAN aset gambar yang bisa ditempel ke adegan video. Peran file ini adalah
  **katalog referensi + inventaris properti** (nama barang, nama Inggris, tag, spesifikasi) untuk
  merancang adegan, bukan sumber gambar. Properti di video tetap digambar SVG mengikuti entri katalog ini.
- 19 emoji dipakai ulang di beberapa item.
- **Spesifikasi adalah teks template generik, BUKAN fakta terverifikasi.** 2 klaim dicek dan memakai
  istilah standar yang benar (UV400 = blokir UV s.d. 400 nm; BFE 99% = tier premium masker bedah
  ASTM F2100/EN 14683) — tapi angka-angka itu milik produk generik imajiner, bukan produk nyata.
  Contoh yang TIDAK BOLEH dikutip sebagai fakta di video: "Sisir kayu cendana meminimalkan
  kerontokan rambut" (klaim kesehatan tak terbukti), "tumbler tahan panas 12 jam / dingin 24 jam"
  (klaim pemasaran generik). Spesifikasi hanya dipakai sebagai inspirasi properti, bukan narasi faktual.

## Aturan pakai
- Pakai sebagai **daftar referensi properti** saat merancang adegan (mis. adegan dapur, kantor, perjalanan
  — cek nama + tag + spek di sini) dan sebagai **data JSON/CSV** (ekspor dari katalog) untuk mesin.
- Jangan tempel emoji dari katalog ini ke dalam video sebagai visual.
- Jangan kutip spesifikasi sebagai fakta di narasi/kartu sumber tanpa verifikasi sumber independen.
