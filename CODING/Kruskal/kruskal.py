"""Algoritma Kruskal untuk MST, beserta Himpunan Terpisah (Disjoint Set).

Graf: simpul bernomor 0..jumlah_simpul-1.
Satu sisi ditulis (simpul_a, simpul_b, bobot).
sorted() dipakai sebagai alat bantu pengurutan, biaya O(m log m).
"""


class HimpunanTerpisah:
    """Disjoint Set (Union-Find) dengan union by rank dan path halving."""

    def __init__(self, jumlah_simpul):
        self.induk = list(range(jumlah_simpul))  # awalnya induk tiap simpul adalah dirinya
        self.peringkat = [0] * jumlah_simpul     # perkiraan tinggi pohon

    def cari_akar(self, simpul):
        """Mencari akar (ketua) himpunan dari simpul."""
        while self.induk[simpul] != simpul:
            self.induk[simpul] = self.induk[self.induk[simpul]]  # path halving
            simpul = self.induk[simpul]
        return simpul

    def gabung(self, simpul_a, simpul_b):
        """Gabungkan himpunan kedua simpul. False jika sudah satu himpunan (siklus)."""
        akar_a = self.cari_akar(simpul_a)
        akar_b = self.cari_akar(simpul_b)
        if akar_a == akar_b:
            return False
        if self.peringkat[akar_a] < self.peringkat[akar_b]:  # pohon pendek digantung ke pohon tinggi
            akar_a, akar_b = akar_b, akar_a
        self.induk[akar_b] = akar_a
        if self.peringkat[akar_a] == self.peringkat[akar_b]:
            self.peringkat[akar_a] += 1
        return True


def kruskal(jumlah_simpul, daftar_sisi):
    """Mengembalikan (sisi_mst, total_bobot). ValueError jika graf tidak terhubung."""
    # Urut menaik menurut bobot (sisi[2]); bila sama, menurut simpul_a lalu simpul_b.
    sisi_terurut = sorted(daftar_sisi, key=lambda sisi: (sisi[2], sisi[0], sisi[1]))

    himpunan = HimpunanTerpisah(jumlah_simpul)
    sisi_mst = []
    total_bobot = 0

    for simpul_a, simpul_b, bobot in sisi_terurut:  # dari sisi paling ringan
        if himpunan.gabung(simpul_a, simpul_b):  # terima jika belum terhubung (tanpa siklus)
            sisi_mst.append((simpul_a, simpul_b, bobot))
            total_bobot += bobot
            if len(sisi_mst) == jumlah_simpul - 1:  # MST sudah lengkap
                break

    if len(sisi_mst) != jumlah_simpul - 1:
        raise ValueError("Graf tidak terhubung")
    return sisi_mst, total_bobot


if __name__ == "__main__":
    # Contoh: 4 kota disambung kabel internet. Bobot = biaya (juta rupiah).
    nama_kota = ["Maros", "Makassar", "Gowa", "Takalar"]
    MAROS, MAKASSAR, GOWA, TAKALAR = 0, 1, 2, 3  # nomor simpul tiap kota

    # Tiap sisi = (kota_a, kota_b, biaya). Hasil yang benar: total 7.
    contoh = [
        (GOWA, TAKALAR, 4),
        (MAROS, GOWA, 3),
        (MAKASSAR, TAKALAR, 5),
        (MAROS, MAKASSAR, 1),
        (MAKASSAR, GOWA, 2),
    ]
    sisi_mst, total_bobot = kruskal(4, contoh)
    for simpul_a, simpul_b, bobot in sisi_mst:
        print(f"{nama_kota[simpul_a]} ke {nama_kota[simpul_b]}, biaya {bobot} juta")
    print("Total biaya:", total_bobot, "juta")
