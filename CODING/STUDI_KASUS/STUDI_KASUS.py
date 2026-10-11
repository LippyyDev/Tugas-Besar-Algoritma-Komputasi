import heapq


# BAGIAN 1: PERSIAPAN DATA GRAF GEDUNG UNHAS
#--------------------------------------------------------------------------------------------------------------------
# Pada langkah pertama, siapkan data jalur kabel dan biayanya langsung dari tabel
data_jalur = [
    ("Sipil", "Industri", 15),
    ("Elektro", "Geologi", 0),
    ("Arsitektur", "Sipil", -5),
    ("Arsitektur", "Elektro", 18),
    ("Sipil", "Elektro", -2),
    ("Industri", "Geologi", 25),
]

# Selanjutnya, kumpulkan semua nama gedung lalu buat nomor urutnya dari 0 sampai n - 1
nama_gedung = sorted({gedung for g_a, g_b, _ in data_jalur for gedung in (g_a, g_b)})
nomor_gedung = {nama: i for i, nama in enumerate(nama_gedung)}
n = len(nama_gedung)

# Selanjutnya, ubah data setiap jalur kabel jadi format sisi graf (u, v, w)
sisi_kasus = [
    (nomor_gedung[g_a], nomor_gedung[g_b], biaya)
    for g_a, g_b, biaya in data_jalur
]

print(f"Studi kasus: {n} gedung, {len(sisi_kasus)} jalur kabel yang mungkin\n")


# BAGIAN 2: EKSEKUSI ALGORITMA KRUSKAL
#--------------------------------------------------------------------------------------------------------------------
# Pada langkah pertama, siapkan himpunan terpisah untuk n titik
induk_kruskal = list(range(n))

def cari_kruskal(x):
    if induk_kruskal[x] == x:
        return x
    induk_kruskal[x] = cari_kruskal(induk_kruskal[x])
    return induk_kruskal[x]

# Selanjutnya, urutkan semua sisi menaik berdasarkan bobot biaya
sisi_urut = sorted(sisi_kasus, key=lambda x: x[2])
A_kruskal = []
total_kruskal = 0

# Selanjutnya, periksa sisi satu per satu
for u, v, w in sisi_urut:
    akar_u = cari_kruskal(u)
    akar_v = cari_kruskal(v)
    if akar_u != akar_v:
        induk_kruskal[akar_u] = akar_v
        A_kruskal.append((u, v, w))
        total_kruskal += w
        if len(A_kruskal) == n - 1:
            break

# Tampilkan hasil algoritma Kruskal
print("=== HASIL ALGORITMA KRUSKAL ===")
print("Jalur kabel terpilih:")
for u, v, w in sorted(A_kruskal, key=lambda s: (s[2], s[0], s[1])):
    print(f"  {nama_gedung[u]} - {nama_gedung[v]}: {w} juta")
print(f"Total biaya bersih Kruskal: {total_kruskal} juta\n")


# BAGIAN 3: EKSEKUSI ALGORITMA PRIM
#--------------------------------------------------------------------------------------------------------------------
# Pada langkah pertama, siapkan daftar tetangga untuk tiap titik
adj = {i: [] for i in range(n)}
for u, v, w in sisi_kasus:
    adj[u].append((w, u, v))
    adj[v].append((w, v, u))

# Tandai titik awal 0 sudah masuk pohon, siapkan antrean sisi Q
masuk = [False] * n
masuk[0] = True
Q = []
for w, u, v in adj[0]:
    heapq.heappush(Q, (w, u, v))

A_prim = []
total_prim = 0

# Selanjutnya, keluarkan sisi termurah dari antrean Q selama belum n - 1 sisi
while Q and len(A_prim) < n - 1:
    w, k, b = heapq.heappop(Q)
    if masuk[k] and masuk[b]:
        continue

    tujuan = b if not masuk[b] else k
    masuk[tujuan] = True
    A_prim.append((k, b, w))
    total_prim += w

    for w_baru, u_baru, v_baru in adj[tujuan]:
        tetangga = v_baru if u_baru == tujuan else u_baru
        if not masuk[tetangga]:
            heapq.heappush(Q, (w_baru, tujuan, tetangga))

# Tampilkan hasil algoritma Prim
print("=== HASIL ALGORITMA PRIM ===")
print("Jalur kabel terpilih:")
for u, v, w in sorted(A_prim, key=lambda s: (s[2], s[0], s[1])):
    print(f"  {nama_gedung[u]} - {nama_gedung[v]}: {w} juta")
print(f"Total biaya bersih Prim: {total_prim} juta\n")



# BAGIAN 4: EKSEKUSI ALGORITMA BORUVKA
#--------------------------------------------------------------------------------------------------------------------
# Pada langkah pertama, siapkan himpunan terpisah dan jumlah komponen c = n
induk_boruvka = list(range(n))

def cari_boruvka(x):
    if induk_boruvka[x] == x:
        return x
    induk_boruvka[x] = cari_boruvka(induk_boruvka[x])
    return induk_boruvka[x]

A_boruvka = []
total_boruvka = 0
c = n

# Selanjutnya, ulangi selama jumlah komponen c masih lebih dari 1
while c > 1:
    termurah = {}
    for u, v, w in sisi_kasus:
        akar_u = cari_boruvka(u)
        akar_v = cari_boruvka(v)
        if akar_u != akar_v:
            if akar_u not in termurah or w < termurah[akar_u][2]:
                termurah[akar_u] = (u, v, w)
            if akar_v not in termurah or w < termurah[akar_v][2]:
                termurah[akar_v] = (u, v, w)

    if not termurah:
        break

    for u, v, w in termurah.values():
        akar_u = cari_boruvka(u)
        akar_v = cari_boruvka(v)
        if akar_u != akar_v:
            induk_boruvka[akar_u] = akar_v
            A_boruvka.append((u, v, w))
            total_boruvka += w
            c -= 1

# Tampilkan hasil algoritma Boruvka
print("=== HASIL ALGORITMA BORUVKA ===")
print("Jalur kabel terpilih:")
for u, v, w in sorted(A_boruvka, key=lambda s: (s[2], s[0], s[1])):
    print(f"  {nama_gedung[u]} - {nama_gedung[v]}: {w} juta")
print(f"Total biaya bersih Boruvka: {total_boruvka} juta\n")


# BAGIAN 5: VALIDASI KESETARAAN KETIGA ALGORITMA
#--------------------------------------------------------------------------------------------------------------------
# Fungsi bantu untuk menyamakan urutan pasangan sisi
def rapikan(daftar_sisi):
    return {(min(u, v), max(u, v), w) for u, v, w in daftar_sisi}

# Pastikan total biaya ketiga algoritma sama persis
assert total_kruskal == total_prim == total_boruvka, "Total bobot ketiga algoritma berbeda!"

# Pastikan himpunan sisi terpilih ketiga algoritma juga sama persis
assert rapikan(A_kruskal) == rapikan(A_prim) == rapikan(A_boruvka), "Sisi terpilih berbeda!"

# Terakhir, tampilkan kesimpulan
print(f"Kesimpulan: Ketiga algoritma menghasilkan total biaya minimum yang sama, yaitu {total_kruskal} juta.")