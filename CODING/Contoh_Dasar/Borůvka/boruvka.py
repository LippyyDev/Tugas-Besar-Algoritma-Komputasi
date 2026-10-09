"""Algoritma Borůvka untuk MST (pembanding), memakai HimpunanTerpisah dari kruskal.py.

Graf: daftar sisi, satu sisi ditulis (simpul_a, simpul_b, bobot).
Tiap putaran, setiap komponen memilih sisi termurah yang keluar darinya,
lalu semua pilihan digabung. Jumlah komponen menyusut sedikitnya separuh per putaran.
"""

import os
import sys

# Folder Kruskal ada di samping folder ini; tambahkan ke jalur impor agar kruskal.py ditemukan.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Kruskal"))
from kruskal import HimpunanTerpisah


def kunci_sisi(sisi):
    """Kunci pembanding sisi: bobot, lalu simpul terkecil, lalu simpul terbesar (sama seperti Kruskal)."""
    return (sisi[2], min(sisi[0], sisi[1]), max(sisi[0], sisi[1]))


def boruvka(jumlah_simpul, daftar_sisi):
    """Mengembalikan (sisi_mst, total_bobot). ValueError jika graf tidak terhubung."""
    himpunan = HimpunanTerpisah(jumlah_simpul)
    sisi_mst = []
    total_bobot = 0
    jumlah_komponen = jumlah_simpul  # awalnya tiap simpul adalah satu komponen

    while jumlah_komponen > 1:
        termurah = {}  # akar komponen -> sisi termurah yang keluar dari komponen itu
        for simpul_a, simpul_b, bobot in daftar_sisi:
            akar_a = himpunan.cari_akar(simpul_a)
            akar_b = himpunan.cari_akar(simpul_b)
            if akar_a == akar_b:  # sisi di dalam satu komponen, abaikan
                continue
            sisi = (simpul_a, simpul_b, bobot)
            for akar in (akar_a, akar_b):  # sisi ini calon pilihan kedua komponen
                if akar not in termurah or kunci_sisi(sisi) < kunci_sisi(termurah[akar]):
                    termurah[akar] = sisi

        if not termurah:  # tidak ada sisi keluar: graf terpisah
            raise ValueError("Graf tidak terhubung")

        for simpul_a, simpul_b, bobot in termurah.values():  # gabungkan semua pilihan
            if himpunan.gabung(simpul_a, simpul_b):  # False jika sisi itu sudah dipasang
                sisi_mst.append((simpul_a, simpul_b, bobot))
                total_bobot += bobot
                jumlah_komponen -= 1

    return sisi_mst, total_bobot


if __name__ == "__main__":
    # Contoh 5 simpul (sama dengan kruskal.py). Butuh 1 putaran.
    # Hasil yang benar: total bobot 18.
    contoh = [
        (2, 3, 6),
        (0, 2, 8),
        (1, 3, 3),
        (0, 1, 5),
        (3, 4, 4),
        (2, 4, 9),
        (1, 2, 11),
    ]
    sisi_mst, total_bobot = boruvka(5, contoh)
    for simpul_a, simpul_b, bobot in sisi_mst:
        print(f"Simpul {simpul_a} ke simpul {simpul_b}, bobot {bobot}")
    print("Total bobot:", total_bobot)
