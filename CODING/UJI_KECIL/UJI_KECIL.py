import heapq

# BAGIAN 1: FUNGSI DASAR TIGA ALGORITMA MST
#--------------------------------------------------------------------------------------------------------------------

def cari_akar(induk, x):
    # Cari representasi akar himpunan
    if induk[x] == x:
        return x
    induk[x] = cari_akar(induk, induk[x])
    return induk[x]


def rapikan(daftar_sisi):
    # Samakan format arah sisi (u, v) agar mudah divalidasi
    return {(min(u, v), max(u, v), w) for u, v, w in daftar_sisi}


def kruskal(n, sisi_kasus):
    # Pada langkah pertama, siapkan himpunan terpisah untuk n titik
    induk_kruskal = list(range(n))
    # Aturan pemutus seri: urutkan menurut (bobot w, simpul kecil, simpul besar)
    sisi_urut = sorted(sisi_kasus, key=lambda s: (s[2], min(s[0], s[1]), max(s[0], s[1])))
    A_kruskal = []
    total_kruskal = 0

    # Selanjutnya, periksa sisi satu per satu
    for u, v, w in sisi_urut:
        akar_u = cari_akar(induk_kruskal, u)
        akar_v = cari_akar(induk_kruskal, v)
        if akar_u != akar_v:
            induk_kruskal[akar_u] = akar_v
            A_kruskal.append((u, v, w))
            total_kruskal += w
            if len(A_kruskal) == n - 1:
                break

    # Jika sisi terpilih kurang dari n - 1, berarti graf tidak terhubung
    if len(A_kruskal) < n - 1:
        raise ValueError("Graf tidak terhubung!")
    return A_kruskal, total_kruskal


def prim(n, sisi_kasus, s=0):
    # Pada langkah pertama, siapkan daftar tetangga untuk tiap titik
    adj = {i: [] for i in range(n)}
    for u, v, w in sisi_kasus:
        adj[u].append((w, min(u, v), max(u, v), v))
        adj[v].append((w, min(u, v), max(u, v), u))

    masuk = [False] * n
    masuk[s] = True
    Q = []
    for item in adj[s]:
        heapq.heappush(Q, item)

    A_prim = []
    total_prim = 0

    # Selanjutnya, keluarkan sisi termurah dari antrean Q selama belum n - 1 sisi
    while Q and len(A_prim) < n - 1:
        w, u_simpul, v_simpul, tujuan = heapq.heappop(Q)
        if masuk[tujuan]:
            continue

        masuk[tujuan] = True
        A_prim.append((u_simpul, v_simpul, w))
        total_prim += w

        for w_baru, u_b, v_b, tetangga in adj[tujuan]:
            if not masuk[tetangga]:
                heapq.heappush(Q, (w_baru, u_b, v_b, tetangga))

    # Jika sisi terpilih kurang dari n - 1, berarti graf tidak terhubung
    if len(A_prim) < n - 1:
        raise ValueError("Graf tidak terhubung!")
    return A_prim, total_prim


def boruvka(n, sisi_kasus):
    # Pada langkah pertama, siapkan himpunan terpisah dan jumlah komponen c = n
    induk_boruvka = list(range(n))
    A_boruvka = []
    total_boruvka = 0
    c = n

    # Kunci pemutus seri standar: (bobot w, simpul kecil, simpul besar)
    def kunci_sisi(s):
        return (s[2], min(s[0], s[1]), max(s[0], s[1]))

    # Selanjutnya, ulangi selama jumlah komponen c masih lebih dari 1
    while c > 1:
        termurah = {}
        for u, v, w in sisi_kasus:
            akar_u = cari_akar(induk_boruvka, u)
            akar_v = cari_akar(induk_boruvka, v)
            if akar_u != akar_v:
                sisi_sekarang = (u, v, w)
                if akar_u not in termurah or kunci_sisi(sisi_sekarang) < kunci_sisi(termurah[akar_u]):
                    termurah[akar_u] = sisi_sekarang
                if akar_v not in termurah or kunci_sisi(sisi_sekarang) < kunci_sisi(termurah[akar_v]):
                    termurah[akar_v] = sisi_sekarang

        if not termurah:
            break

        # Urutkan sisi termurah agar konsisten
        sisi_terpilih = sorted(termurah.values(), key=kunci_sisi)
        for u, v, w in sisi_terpilih:
            akar_u = cari_akar(induk_boruvka, u)
            akar_v = cari_akar(induk_boruvka, v)
            if akar_u != akar_v:
                induk_boruvka[akar_u] = akar_v
                A_boruvka.append((u, v, w))
                total_boruvka += w
                c -= 1

    # Jika sisi terpilih kurang dari n - 1, berarti graf tidak terhubung
    if len(A_boruvka) < n - 1:
        raise ValueError("Graf tidak terhubung!")
    return A_boruvka, total_boruvka


# BAGIAN 2: DATA EMPAT KASUS UJI GRAF KECIL
#--------------------------------------------------------------------------------------------------------------------
# Kasus 1: 4 simpul biasa (satu sisi ditolak)
KASUS_1 = {
    "nama": "Kasus 1: 4 simpul biasa (satu sisi ditolak)",
    "jumlah_simpul": 4,
    "daftar_sisi": [(2, 3, 4), (0, 2, 3), (1, 3, 5), (0, 1, 1), (1, 2, 2)],
    "total_benar": 7,
    "sisi_benar": {(0, 1, 1), (1, 2, 2), (2, 3, 4)},
}

# Kasus 2: 5 simpul, bobot 0 dan negatif
KASUS_2 = {
    "nama": "Kasus 2: 5 simpul, bobot 0 dan negatif",
    "jumlah_simpul": 5,
    "daftar_sisi": [(0, 1, 0), (1, 2, -2), (0, 2, 1), (2, 3, 3), (0, 4, 4), (1, 3, 5), (4, 1, 6)],
    "total_benar": 5,
    "sisi_benar": {(0, 1, 0), (1, 2, -2), (2, 3, 3), (0, 4, 4)},
}

# Kasus 3: bobot kembar dengan aturan pemutus seri
KASUS_3 = {
    "nama": "Kasus 3: bobot kembar (total dan himpunan sisi)",
    "jumlah_simpul": 4,
    "daftar_sisi": [(0, 1, 2), (1, 2, 2), (2, 3, 2), (3, 0, 2), (1, 3, 5)],
    "total_benar": 6,
    "sisi_benar": {(0, 1, 2), (0, 3, 2), (1, 2, 2)},
}

# Kasus 4: graf tidak terhubung (harus melempar ValueError)
KASUS_4 = {
    "nama": "Kasus 4: graf tak terhubung (harus ValueError)",
    "jumlah_simpul": 4,
    "daftar_sisi": [(0, 1, 1), (2, 3, 2)],
}

# BAGIAN 3: FUNGSI PENGUJIAN DAN VALIDASI
#--------------------------------------------------------------------------------------------------------------------

def uji_graf_terhubung(kasus):
    # Pada langkah pertama, siapkan simpul dan sisi dari kasus uji
    n = kasus["jumlah_simpul"]
    sisi_kasus = kasus["daftar_sisi"]

    # Selanjutnya, jalankan masing-masing algoritma secara mandiri
    A_kruskal, total_kruskal = kruskal(n, sisi_kasus)
    A_prim, total_prim = prim(n, sisi_kasus)
    A_boruvka, total_boruvka = boruvka(n, sisi_kasus)

    hasil = {
        "Kruskal": (A_kruskal, total_kruskal),
        "Prim": (A_prim, total_prim),
        "Borůvka": (A_boruvka, total_boruvka),
    }

    # Selanjutnya, periksa apakah total bobot dan himpunan sisi ketiga algoritma sudah sesuai
    for nama_algo, (sisi_mst, total) in hasil.items():
        assert total == kasus["total_benar"], f"{kasus['nama']}: total {nama_algo} = {total}, seharusnya {kasus['total_benar']}"
        assert len(sisi_mst) == n - 1, f"{kasus['nama']}: jumlah sisi {nama_algo} salah"
        assert rapikan(sisi_mst) == rapikan(kasus["sisi_benar"]), f"{kasus['nama']}: himpunan sisi {nama_algo} salah"

    print(f"[LOLOS] {kasus['nama']} | total = {kasus['total_benar']} | Kruskal, Prim, Borůvka sama")


def uji_graf_tak_terhubung(kasus):
    # Pada kasus graf tidak terhubung, pastikan ketiganya melempar ValueError
    n = kasus["jumlah_simpul"]
    sisi_kasus = kasus["daftar_sisi"]

    for nama_algo, fungsi in [("Kruskal", kruskal), ("Prim", prim), ("Borůvka", boruvka)]:
        try:
            fungsi(n, sisi_kasus)
            raise AssertionError(f"{nama_algo} seharusnya melempar ValueError")
        except ValueError:
            pass

    print(f"[LOLOS] {kasus['nama']} | ketiganya melempar ValueError")


# Terakhir, jalankan semua pengujian kasus kecil saat berkas dieksekusi langsung
if __name__ == "__main__":
    for kasus in (KASUS_1, KASUS_2, KASUS_3):
        uji_graf_terhubung(kasus)
    uji_graf_tak_terhubung(KASUS_4)
    print("Semua 4 kasus uji lolos pada ketiga algoritma (3 kasus graf terhubung dan 1 kasus galat).")