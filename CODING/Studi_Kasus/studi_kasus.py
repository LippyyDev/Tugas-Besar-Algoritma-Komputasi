"""Studi kasus: jaringan kabel lima gedung Fakultas Teknik Unhas (bobot = biaya bersih, juta rupiah).

Bobot positif: fakultas memakai dana sendiri. Nol: gratis (ditanggung universitas, tanpa insentif).
Negatif: ditanggung universitas dan fakultas menerima insentif sebesar nilai mutlaknya.
Data dibaca dari studi_kasus_gedung_unhas.csv (tetap, tanpa seed). Bukan untuk mengukur waktu.
Jalankan dari folder ini:  python studi_kasus.py
"""

import csv
import os
import sys

_FOLDER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_FOLDER, ".."))
from bantu_mst import jalankan_tiga_algoritma, rapikan  # noqa: E402

BERKAS_KASUS = os.path.join(_FOLDER, "studi_kasus_gedung_unhas.csv")


def main():
    with open(BERKAS_KASUS, newline="", encoding="utf-8") as berkas:
        baris_kasus = list(csv.DictReader(berkas))

    nama_gedung = sorted({b[k] for b in baris_kasus for k in ("gedung_a", "gedung_b")})
    nomor_gedung = {nama: i for i, nama in enumerate(nama_gedung)}  # nomor tetap menurut abjad
    sisi_kasus = [(nomor_gedung[b["gedung_a"]], nomor_gedung[b["gedung_b"]], int(b["biaya_juta"])) for b in baris_kasus]

    hasil_kasus = jalankan_tiga_algoritma(len(nama_gedung), sisi_kasus)
    total_kasus = {a: t for a, (_, t) in hasil_kasus.items()}
    assert len(set(total_kasus.values())) == 1, f"total bobot berbeda: {total_kasus}"
    himpunan_kasus = {a: rapikan(s) for a, (s, _) in hasil_kasus.items()}
    assert len({frozenset(h) for h in himpunan_kasus.values()}) == 1, "himpunan sisi ketiga algoritma berbeda"

    sisi_mst_kasus, total_mst_kasus = hasil_kasus["Kruskal"]
    print(f"Studi kasus: {len(nama_gedung)} gedung, {len(sisi_kasus)} jalur kabel yang mungkin")
    for a, b, w in sorted(rapikan(sisi_mst_kasus), key=lambda s: (s[2], s[0], s[1])):
        print(f"  {nama_gedung[a]} - {nama_gedung[b]}: {w} juta")
    print(f"Total biaya bersih minimum: {total_mst_kasus} juta (Kruskal, Prim, dan Borůvka sama)")
    if any(b["keterangan"].upper().startswith("ILUSTRASI") for b in baris_kasus):
        print("PERINGATAN: data masih berlabel ILUSTRASI. Ganti dengan data biaya sebenarnya sebelum disebut data nyata.")


if __name__ == "__main__":
    main()
