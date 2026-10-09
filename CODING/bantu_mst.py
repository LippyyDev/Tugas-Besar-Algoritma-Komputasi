"""Alat bantu bersama untuk Uji_Kecil/uji_kecil.py dan Studi_Kasus/studi_kasus.py.

Mengimpor tiga algoritma dari folder Contoh_Dasar (kode yang sama dengan yang divisualisasikan),
lalu menyediakan dua fungsi bantu: menjalankan ketiganya pada graf yang sama dan merapikan sisi.
"""

import os
import sys

_DASAR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Contoh_Dasar")
for _folder in ("Kruskal", "Prim", "Borůvka"):
    sys.path.insert(0, os.path.join(_DASAR, _folder))

from kruskal import kruskal  # noqa: E402
from prim import buat_daftar_tetangga, prim  # noqa: E402
from boruvka import boruvka  # noqa: E402


def jalankan_tiga_algoritma(jumlah_simpul, daftar_sisi):
    """Menjalankan ketiga algoritma pada graf yang sama. Mengembalikan {nama: (sisi_mst, total)}."""
    return {
        "Kruskal": kruskal(jumlah_simpul, daftar_sisi),
        "Prim": prim(jumlah_simpul, buat_daftar_tetangga(jumlah_simpul, daftar_sisi)),
        "Borůvka": boruvka(jumlah_simpul, daftar_sisi),
    }


def rapikan(sisi_mst):
    """Ubah sisi menjadi (kecil, besar, bobot) supaya arah sisi tidak memengaruhi perbandingan."""
    return {(min(a, b), max(a, b), w) for a, b, w in sisi_mst}
