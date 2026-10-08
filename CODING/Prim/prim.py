"""Algoritma Prim untuk MST (varian lazy, antrean prioritas binary heap).

Graf: daftar ketetanggaan, daftar_tetangga[simpul] = [(simpul_tetangga, bobot), ...].
heapq dipakai sebagai alat bantu antrean prioritas, biaya O(log m) per operasi.
Isi antrean (bobot, simpul_kecil, simpul_besar): bila bobot sama, simpul terkecil diambil dulu,
lalu simpul terbesar (aturan yang sama dengan Kruskal dan Borůvka).
"""

import heapq


def buat_daftar_tetangga(jumlah_simpul, daftar_sisi):
    """Ubah daftar sisi (simpul_a, simpul_b, bobot) menjadi daftar ketetanggaan."""
    daftar_tetangga = [[] for _ in range(jumlah_simpul)]
    for simpul_a, simpul_b, bobot in daftar_sisi:
        daftar_tetangga[simpul_a].append((simpul_b, bobot))
        daftar_tetangga[simpul_b].append((simpul_a, bobot))  # graf tak berarah
    return daftar_tetangga


def prim(jumlah_simpul, daftar_tetangga, simpul_awal=0):
    """Mengembalikan (sisi_mst, total_bobot). ValueError jika graf tidak terhubung."""
    sudah_masuk = [False] * jumlah_simpul  # simpul yang sudah ada di pohon
    sisi_mst = []
    total_bobot = 0

    # Pohon dimulai dari satu simpul; masukkan semua sisi yang keluar darinya.
    sudah_masuk[simpul_awal] = True
    antrean = []
    for simpul_tetangga, bobot in daftar_tetangga[simpul_awal]:
        heapq.heappush(antrean, (bobot, min(simpul_awal, simpul_tetangga), max(simpul_awal, simpul_tetangga)))

    while antrean and len(sisi_mst) < jumlah_simpul - 1:
        bobot, kecil, besar = heapq.heappop(antrean)  # sisi termurah yang menyentuh pohon
        if sudah_masuk[kecil] and sudah_masuk[besar]:  # kedua ujung sudah di pohon: siklus
            continue
        asal, tujuan = (kecil, besar) if sudah_masuk[kecil] else (besar, kecil)  # tujuan = ujung baru
        sudah_masuk[tujuan] = True  # simpul baru bergabung ke pohon
        sisi_mst.append((asal, tujuan, bobot))
        total_bobot += bobot
        for simpul_tetangga, bobot_baru in daftar_tetangga[tujuan]:
            if not sudah_masuk[simpul_tetangga]:
                heapq.heappush(antrean, (bobot_baru, min(tujuan, simpul_tetangga), max(tujuan, simpul_tetangga)))

    if len(sisi_mst) != jumlah_simpul - 1:
        raise ValueError("Graf tidak terhubung")
    return sisi_mst, total_bobot


if __name__ == "__main__":
    # Contoh 4 simpul (sama dengan kruskal.py). Sisi = (simpul_a, simpul_b, bobot).
    nama_kota = ["Maros", "Makassar", "Gowa", "Takalar"]
    MAROS, MAKASSAR, GOWA, TAKALAR = 0, 1, 2, 3  # nomor simpul tiap kota

    # Hasil yang benar: total 7.
    contoh = [
        (GOWA, TAKALAR, 4),
        (MAROS, GOWA, 3),
        (MAKASSAR, TAKALAR, 5),
        (MAROS, MAKASSAR, 1),
        (MAKASSAR, GOWA, 2),
    ]
    daftar_tetangga = buat_daftar_tetangga(4, contoh)
    sisi_mst, total_bobot = prim(4, daftar_tetangga, simpul_awal=MAROS)
    for simpul_a, simpul_b, bobot in sisi_mst:
        print(f"{nama_kota[simpul_a]} ke {nama_kota[simpul_b]}, biaya {bobot} juta")
    print("Total biaya:", total_bobot, "juta")
