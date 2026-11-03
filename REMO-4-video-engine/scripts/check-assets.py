#!/usr/bin/env python3
"""Cek kelengkapan + integritas aset biner REMO 4.

Memeriksa tiap file biner master-aset (wajib) dan studio (opsional) apakah
ada di lokasi yang benar, lalu memverifikasi ukuran dan md5-nya.

SUMBER DAFTAR EKSPEKTASI -- dibaca dulu sebelum mengubah file ini
---------------------------------------------------------------
Cara yang dipakai script ini: DAFTAR EKSPEKTASI TERTANAM (embedded list).
`EXPECTED_MASTER` dan `EXPECTED_STUDIO` di bawah disalin dari inventaris
lokal 3 Nov 2026 dan HARUS identik dengan tabel di
`REMO-4-video-engine/master-aset/MANIFEST-ASET-BINER.md`. Manifest adalah
dokumen yang dibaca manusia; daftar di sini adalah yang dieksekusi mesin.
Kalau manifest berubah, perbarui kedua tempat sekaligus.

Pengecualian: bila flag --manifest diberikan, script MEM-PARSE tabel
markdown manifest tersebut (tabel di bawah heading yang mengandung kata
"master" -> aset master, heading yang mengandung kata "studio" -> aset
studio) dan memakai hasil parse itu MENGANTIKAN daftar tertanam. Ini
berguna untuk memeriksa manifest hasil edit tanpa mengubah script dulu.
Tabel yang di-parse harus berformat:
    | `path/relatif` | <ukuran byte> | `<md5>` | <status> |

LOKASI YANG DIPERIKSA
---------------------
--root <dir>  : root master-aset, mis. .../REMO-4-video-engine/master-aset
                atau ~/workspace/master-aset. Bila tidak diberikan, script
                menebak urutan berikut:
                  1. cwd bila cwd adalah folder master-aset,
                  2. <lokasi script>/../master-aset (saat script dijalankan
                     dari repo/staging -- ini yang membuat jalan dari
                     staging memeriksa STAGING, bukan workspace lokal),
                  3. <cwd>/REMO-4-video-engine/master-aset,
                  4. <cwd>/master-aset,
                  5. ~/workspace/master-aset.
                Jadi: jalan dari staging -> memeriksa staging (biner HILANG
                adalah HASIL YANG BENAR, karena staging memang teks saja).
                Jalan dengan --root ~/workspace/master-aset -> memeriksa
                workspace lokal (seharusnya OK semua).
--studio-root <dir>: root studio (folder yang berisi pose-studio/ dll).
                Bila tidak diberikan: bila <root>/../pose-studio ada, pakai
                <root>/.. ; bila tidak, pakai ~/workspace/remo-4 bila ada.

STATUS PER FILE: OK (ada + ukuran + md5 cocok), HILANG (file tidak ada),
RUSAK (ada tapi ukuran dan/atau md5 berbeda).
EXIT CODE: 0 bila semua file yang diperiksa OK, 1 bila ada yang HILANG/RUSAK,
2 bila argumen/lokasi tidak valid (mis. manifest tidak bisa di-parse).

Hanya memakai Python stdlib (argparse, pathlib, hashlib, sys).
"""

import argparse
import hashlib
import sys
from pathlib import Path

EXPECTED_MASTER = [
    ("brand/outro-referensi-ayraku-3detik.mp4", 1494662, "e66ad9d9655b17a0d13a45e70e1857f3"),
    ("karakter-3d/contact-sheet-kostum.png", 273536, "a2f0d83b662ed3233b73208d0e1214ce"),
    ("karakter-3d/renders/contact-sheet.png", 306636, "2f4a233967735e36865311bf581fefda"),
    ("karakter-3d/renders/nelayan.png", 25645, "0280c64856871fb085de903ef46a0e34"),
    ("karakter-3d/renders/orang-daratan-cewek.png", 32688, "f4e8ec52324bbb6c8ce5e3c75667e7f8"),
    ("karakter-3d/renders/orang-daratan-cowok.png", 26447, "f8b750a43ebe9375b2a91c52a5098e77"),
    ("karakter-3d/renders/pekerja-helm-kuning.png", 30227, "4a0bc9ffe50eb53e98f86af4b16e9c75"),
    ("karakter-3d/renders/penyelam-cewek.png", 20530, "f01e9dd6e4ddc50266665ce531571693"),
    ("karakter-3d/renders/penyelam-cowok.png", 17722, "09c34afac892ab0f38ba1bda1f97447c"),
    ("karakter-3d/renders/penyelam-shrug.png", 33322, "6838e553b8ea09c822e23ab20c31cc73"),
    ("karakter-3d/renders/perenang-aqua.png", 32676, "503c4e131ccbfb4ce625159b22d49398"),
    ("karakter-3d/renders/perenang-oranye.png", 27475, "bd1c99b4df6f0cf81e2d210d06de77b5"),
    ("karakter-3d/renders/perenang-pink.png", 32267, "5c29639b8bcb4bb9de350b7542c31494"),
    ("karakter-3d/renders/perenang-teal.png", 27227, "939326359dcdcce6aae664a2203d1edf"),
    ("karakter-3d/renders/raw/diver_f.png", 28186, "b390cac4b642753899e0c871be26fda6"),
    ("karakter-3d/renders/raw/diver_m.png", 25067, "3bfeb1a53cc156b33f76208cbb5f094b"),
    ("karakter-3d/renders/raw/diver_shrug.png", 39915, "d801c08ccf9b2b2a5b43ee199ec8bcd2"),
    ("karakter-3d/renders/raw/fisherman.png", 33193, "8f760cba7710a8db2672b50209b6cb2e"),
    ("karakter-3d/renders/raw/land_f.png", 41782, "ae166cecbcb400ead29be980ee470e03"),
    ("karakter-3d/renders/raw/land_m.png", 34434, "823ec1dedd8a3cccade725b577607203"),
    ("karakter-3d/renders/raw/miner.png", 38194, "f81704eefa1e04fa139112f14d459a44"),
    ("karakter-3d/renders/raw/swim_aqua.png", 41453, "da6430839d1e8a32b70a6d91702843c1"),
    ("karakter-3d/renders/raw/swim_orange.png", 35517, "345b854a335167ac907c6f9ad37ef375"),
    ("karakter-3d/renders/raw/swim_pink.png", 40721, "ab9f2918008739d156f4268673b98c15"),
    ("karakter-3d/renders/raw/swim_teal.png", 35204, "ef8573dbbc0e20675610c17b6380cec5"),
    ("visual/contoh-gaya-flat/hari-01-hook.webp", 69030, "4e094bc64d3a28d17f4161488d3b5550"),
    ("visual/contoh-gaya-flat/hari-02-miliaran.webp", 175626, "4b5a721b2189670a16fa08855de4ed59"),
    ("visual/contoh-gaya-flat/hari-03-tangkap-keruk.webp", 133566, "d1dc4b4f009233be82532d0bc9ba353c"),
    ("visual/contoh-gaya-flat/hari-04-karang.webp", 108050, "f53fc92a95adc2a51119e950b989326e"),
]

EXPECTED_STUDIO = [
    ("alam-studio/shots/01-default.png", 467182, "c98b4b9d33da762f710e5bbf2805d3f0"),
    ("alam-studio/shots/02-filter-laut.png", 476030, "0241f844401c270cba1d53c47b48f66b"),
    ("alam-studio/shots/03-modal.png", 241222, "178b16ab1f6bb6641b7c5e7be79fb8cf"),
    ("barang-studio/shots/01-default.png", 139269, "a89c419029dcefea6f739f44068cbad5"),
    ("barang-studio/shots/02-search-tumbler.png", 70494, "e3513d8e90c4e4d7b3ae10a3ef324ecc"),
    ("barang-studio/shots/03-modal.png", 213336, "2e6a33f16791adc5a15906316ba5f784"),
    ("barang-studio/shots/04-lucide-blocked.png", 134926, "2009ad6592b3109741ad8b029174b86a"),
    ("barang-studio/shots/05-final-tanpa-pagar.png", 143258, "6c535b84c7d90b7539b19d07e56e5a6e"),
    ("fauna-studio/final-01-default.png", 183659, "64eb2e07c3f948a6e50208705b5a5124"),
    ("pose-studio/exports/export-pose_female_indonesia_1793641998747.png", 348418, "e5e9f66882e79ea7519edb365e584531"),
    ("pose-studio/exports/export-pose_female_indonesia_1793642032384.png", 348418, "e5e9f66882e79ea7519edb365e584531"),
    ("pose-studio/shots/01-default-pria-batik-senyum.png", 266046, "45bf6ab73130d95bac6f7c0ff640747c"),
    ("pose-studio/shots/02-preset-salam-santun.png", 270462, "c3061b4fde4b34228c1d5b7e26255ec3"),
    ("pose-studio/shots/03-preset-tolak-pinggang.png", 282211, "a076aa9a73b9b5c590d2fc99e17db02e"),
    ("pose-studio/shots/04-wanita-kebaya-semangat.png", 263418, "05f9ca93c2718aeba650dc05bcc39c9f"),
    ("pose-studio/shots/05-toggle-anatomi-otot.png", 254035, "cea3b90d72e8343d454addb4c74ca4b9"),
    ("pose-studio/shots/06-toggle-garis-titik-berat.png", 249661, "52a1e5787c7b4574a8888f789236948d"),
    ("pose-studio/shots/07-preset-berpikir.png", 273973, "d6e21ad02b94c425ab33ee8a04b5dd3e"),
    ("pose-studio/shots/08-tanpa-lucide-cdn.png", 258001, "92463bd0c8689fad50c344a02b5be169"),
    ("pose-studio/shots/09-latar-sawah-dof-aktif.png", 336026, "a25d6779d5d76c76d4475bf798df348b"),
    ("pose-studio/shots/10-latar-candi-senja.png", 304915, "dc0b540138427ce4b9ada62ac337501f"),
    ("pose-studio/shots/11-preset-salam-di-latar-candi.png", 321063, "fee19dd2c84faa2082aae42bad72caa6"),
    ("pose-studio/shots/12-latar-pantai-malam.png", 298161, "9f670bcf7a367520f9d942c8c423996f"),
    ("staging-background/exports/pose_male_transparan_senja_1793642038411.png", 418400, "0d21cb6f8754da6d416ebe43192a473b"),
    ("staging-background/shots/01-default.png", 322317, "3366fc5994538bdc1cdf9c4e28201895"),
    ("staging-background/shots/02-preset-salam.png", 319248, "b165f9e4893a48c3757f9decd1abdb00"),
    ("staging-background/shots/03-preset-tolak-pinggang.png", 319974, "3a299704a5fde6b2c06bddb96ccd2a9d"),
    ("staging-background/shots/bg-candi.png", 326204, "73b5ad903569edaa65a3460a26fcc793"),
    ("staging-background/shots/bg-sawah-dof-off.png", 341017, "db36c61bf4d97866d4638c6c62dedf6f"),
    ("staging-background/shots/bg-sawah-dof-on.png", 355749, "3b51f4bc3f1aa3857bde429a528abf67"),
    ("staging-background/shots/bg-sawah.png", 337740, "acda3bea8e53d47810a3f323117c3f50"),
    ("staging-background/shots/bg-transparan.png", 282359, "6ec7b37264b841e7be6a50bcbf9023b1"),
    ("staging-hewan/exports/fauna_badak_jawa_2x_1793642061876.png", 428998, "2a09865d7a1070dafd5d40b37d43bf90"),
    ("staging-hewan/shots/01-default.png", 232257, "4b159b6d096e3b2321576ff4f7c1ef55"),
    ("staging-hewan/shots/02-komodo-detail.png", 229503, "c16f3f07d3236df022f55362b4a14a03"),
    ("staging-hewan/shots/03-search-harimau.png", 183547, "d35e9ff7d0fb1bc3075aded5f467754b"),
    ("staging-hewan/shots/04-harimau-skeleton.png", 265022, "1419ecc4edd0703b26cdc8c7b757eda9"),
]

# File teks besar yang ADA di GitHub (bukan biner -- tidak diperiksa di sini,
# hanya dicatat supaya tidak disangka hilang):
#   karakter-3d/vendor/three.module.js -- 1272972 byte,
#   md5 a762b8588c6abf23cb87624360d014c4


def md5_of(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_manifest(manifest_path):
    """Parse tabel markdown manifest -> (master_rows, studio_rows).

    rows: list of (rel_path, size:int, md5:str). Hanya baris tabel di bawah
    heading yang mengandung 'master' atau 'studio' yang diambil.
    """
    text = Path(manifest_path).read_text(encoding="utf-8")
    master_rows, studio_rows = [], []
    kind = None
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("#"):
            low = s.lower()
            if "studio" in low:
                kind = "studio"
            elif "master" in low:
                kind = "master"
            else:
                kind = None
            continue
        if kind is None or not s.startswith("|"):
            continue
        cells = [c.strip().strip("`") for c in s.strip("|").split("|")]
        if len(cells) < 3:
            continue
        if cells[0].lower().startswith("file") or set(cells[0]) <= set("-: "):
            continue
        if cells[1].startswith("-"):
            continue
        try:
            size = int(cells[1].replace(",", ""))
        except ValueError:
            continue
        md5 = cells[2].strip("`").lower()
        if len(md5) != 32 or any(c not in "0123456789abcdef" for c in md5):
            continue
        (master_rows if kind == "master" else studio_rows).append(
            (cells[0], size, md5)
        )
    return master_rows, studio_rows


def resolve_master_root(explicit):
    if explicit:
        return Path(explicit).expanduser()
    cwd = Path.cwd()
    # 1. cwd adalah folder master-aset
    if (cwd / "karakter-3d").is_dir() or cwd.name == "master-aset":
        return cwd
    # 2. relatif terhadap lokasi script (repo/staging)
    try:
        from_script = Path(__file__).resolve().parent.parent / "master-aset"
        if from_script.is_dir():
            return from_script
    except Exception:
        pass
    # 3. cwd/REMO-4-video-engine/master-aset
    cand = cwd / "REMO-4-video-engine" / "master-aset"
    if cand.is_dir():
        return cand
    # 4. cwd/master-aset
    cand = cwd / "master-aset"
    if cand.is_dir():
        return cand
    # 5. ~/workspace/master-aset
    cand = Path.home() / "workspace" / "master-aset"
    if cand.is_dir():
        return cand
    return cand


def resolve_studio_root(master_root, explicit):
    if explicit:
        return Path(explicit).expanduser()
    engine = master_root.parent
    if (engine / "pose-studio").is_dir():
        return engine
    cand = Path.home() / "workspace" / "remo-4"
    if cand.is_dir():
        return cand
    return engine


def check_one(base, rel, size, md5):
    path = base / rel
    if not path.is_file():
        return "HILANG", f"tidak ada: {path}"
    actual_size = path.stat().st_size
    if actual_size != size:
        return "RUSAK", f"ukuran {actual_size} != {size} (md5 tidak diperiksa)"
    actual_md5 = md5_of(path)
    if actual_md5 != md5:
        return "RUSAK", f"md5 {actual_md5} != {md5}"
    return "OK", ""


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Cek kelengkapan + integritas aset biner REMO 4."
    )
    ap.add_argument("--manifest", default=None,
                    help="path manifest markdown lain untuk di-parse "
                         "(tanpa flag ini memakai daftar tertanam).")
    ap.add_argument("--root", default=None,
                    help="root master-aset (default: ditebak, lihat docstring).")
    ap.add_argument("--studio-root", default=None,
                    help="root studio (default: ditebak dari --root).")
    ap.add_argument("--master-only", action="store_true",
                    help="hanya periksa aset master (wajib), lewati studio.")
    args = ap.parse_args(argv)

    if args.manifest:
        mpath = Path(args.manifest).expanduser()
        if not mpath.is_file():
            print(f"ERROR: manifest tidak ditemukan: {mpath}", file=sys.stderr)
            return 2
        expected_master, expected_studio = parse_manifest(mpath)
        if not expected_master and not expected_studio:
            print(f"ERROR: tidak ada baris ekspektasi yang bisa di-parse dari {mpath}",
                  file=sys.stderr)
            return 2
        print(f"Ekspektasi di-parse dari manifest: {mpath}")
    else:
        expected_master, expected_studio = EXPECTED_MASTER, EXPECTED_STUDIO

    master_root = resolve_master_root(args.root)
    studio_root = resolve_studio_root(master_root, args.studio_root)
    print(f"Master root : {master_root}")
    print(f"Studio root : {studio_root}" + (" (dilewati --master-only)" if args.master_only else ""))
    print()

    counts = {"OK": 0, "HILANG": 0, "RUSAK": 0}
    groups = [("MASTER (wajib)", master_root, expected_master)]
    if not args.master_only:
        groups.append(("STUDIO (opsional)", studio_root, expected_studio))

    for label, base, rows in groups:
        print(f"== {label} -- {len(rows)} file, base {base} ==")
        for rel, size, md5 in rows:
            status, detail = check_one(base, rel, size, md5)
            counts[status] += 1
            line = f"[{status}] {rel} ({size} byte, md5 {md5})"
            if detail:
                line += f" -- {detail}"
            print(line)
        print()

    total = sum(counts.values())
    print(f"Ringkasan: {counts['OK']} OK / {counts['HILANG']} HILANG / "
          f"{counts['RUSAK']} RUSAK dari {total} file yang diperiksa.")
    if counts["HILANG"] or counts["RUSAK"]:
        print("Hasil: GAGAL -- ada aset hilang/rusak. Jangan klaim aset lengkap; "
              "lihat MANIFEST-ASET-BINER.md untuk cara mendapatkan aset.")
        return 1
    print("Hasil: OK -- semua aset yang diperiksa ada dan md5/ukuran cocok.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
