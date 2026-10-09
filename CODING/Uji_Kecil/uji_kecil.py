"""Uji kasus kecil: empat graf dengan jawaban yang bisa dihitung dengan tangan.

Setiap kasus dijalankan pada Kruskal, Prim, dan Borůvka. Data tetap, tanpa seed.
Jalankan dari folder ini:  python uji_kecil.py
Hitungan tangan tiap kasus ada di PENJELASAN_UJI_KECIL.md.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from bantu_mst import boruvka, buat_daftar_tetangga, jalankan_tiga_algoritma, kruskal, prim, rapikan  # noqa: E402

# Sisi ditulis (simpul_a, simpul_b, bobot). Simpul bernomor 0, 1, 2, dan seterusnya.

# Kasus 1: 4 simpul, bobot berbeda. Sisi (0, 2) bobot 3 harus ditolak karena membentuk siklus. (Tabel 3.1)
KASUS_1 = {"nama": "Kasus 1: 4 simpul biasa (satu sisi ditolak)", "jumlah_simpul": 4,
           "daftar_sisi": [(2, 3, 4), (0, 2, 3), (1, 3, 5), (0, 1, 1), (1, 2, 2)],
           "total_benar": 7,
           "sisi_benar": {(0, 1, 1), (1, 2, 2), (2, 3, 4)}}

# Kasus 2: 5 simpul, ada bobot 0 dan negatif. Hanya urutan bobot yang menentukan.
KASUS_2 = {"nama": "Kasus 2: 5 simpul, bobot 0 dan negatif", "jumlah_simpul": 5,
           "daftar_sisi": [(0, 1, 0), (1, 2, -2), (0, 2, 1), (2, 3, 3), (0, 4, 4), (1, 3, 5), (4, 1, 6)],
           "total_benar": 5,
           "sisi_benar": {(0, 1, 0), (1, 2, -2), (2, 3, 3), (0, 4, 4)}}

# Kasus 3: bobot kembar. Aturan pemutus seri (bobot, simpul terkecil, simpul terbesar) membuat hasilnya tunggal. (Tabel 3.4)
KASUS_3 = {"nama": "Kasus 3: bobot kembar (total dan himpunan sisi)", "jumlah_simpul": 4,
           "daftar_sisi": [(0, 1, 2), (1, 2, 2), (2, 3, 2), (3, 0, 2), (1, 3, 5)],
           "total_benar": 6,
           "sisi_benar": {(0, 1, 2), (0, 3, 2), (1, 2, 2)}}

# Kasus 4: graf tak terhubung. Ketiga algoritma harus melempar ValueError.
KASUS_4 = {"nama": "Kasus 4: graf tak terhubung (harus ValueError)", "jumlah_simpul": 4,
           "daftar_sisi": [(0, 1, 1), (2, 3, 2)]}


def uji_graf_terhubung(kasus):
    """Jalankan satu kasus graf terhubung pada ketiga algoritma. Periksa total, jumlah sisi, dan himpunan sisi."""
    hasil = jalankan_tiga_algoritma(kasus["jumlah_simpul"], kasus["daftar_sisi"])
    for algoritma, (sisi_mst, total) in hasil.items():
        assert total == kasus["total_benar"], f"{kasus['nama']}: total {algoritma} = {total}, seharusnya {kasus['total_benar']}"
        assert len(sisi_mst) == kasus["jumlah_simpul"] - 1, f"{kasus['nama']}: jumlah sisi {algoritma} salah"
        assert rapikan(sisi_mst) == rapikan(kasus["sisi_benar"]), f"{kasus['nama']}: himpunan sisi {algoritma} salah"
    print(f"[LOLOS] {kasus['nama']} | total = {kasus['total_benar']} | Kruskal, Prim, Borůvka sama")


def uji_graf_tak_terhubung(kasus):
    """Ketiga algoritma harus menolak graf tak terhubung dengan ValueError."""
    for algoritma, fungsi in [("Kruskal", lambda n, s: kruskal(n, s)),
                              ("Prim", lambda n, s: prim(n, buat_daftar_tetangga(n, s))),
                              ("Borůvka", lambda n, s: boruvka(n, s))]:
        try:
            fungsi(kasus["jumlah_simpul"], kasus["daftar_sisi"])
            raise AssertionError(f"{algoritma} seharusnya melempar ValueError")
        except ValueError:
            pass
    print(f"[LOLOS] {kasus['nama']} | ketiganya melempar ValueError")


if __name__ == "__main__":
    for kasus in (KASUS_1, KASUS_2, KASUS_3):
        uji_graf_terhubung(kasus)
    uji_graf_tak_terhubung(KASUS_4)
    print("Semua 4 kasus uji lolos pada ketiga algoritma (3 kasus graf terhubung dan 1 kasus galat).")
