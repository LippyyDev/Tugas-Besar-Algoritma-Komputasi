# BAB 4 IMPLEMENTASI DAN EKSPERIMEN

---

## 4.1 Studi Kasus: Jaringan Kabel antar Gedung Fakultas Teknik

---

Studi kasus memodelkan perencanaan jaringan kabel yang menghubungkan lima gedung di Fakultas Teknik Universitas Hasanuddin, kampus Gowa, yaitu Arsitektur, Elektro, Geologi, Industri, dan Sipil. Setiap gedung menjadi satu simpul (*n* = 5), setiap jalur kabel kandidat menjadi satu sisi (*m* = 6), dan panjang jalur dalam meter menjadi bobot sisi. Persoalannya adalah memilih himpunan jalur yang menghubungkan kelima gedung dengan total panjang terkecil, yaitu MST pada graf tak berarah berbobot.

Panjang jalur pada studi kasus ini merupakan nilai ilustrasi, bukan hasil pengukuran lapangan. Nilai tersebut dipakai untuk memperlihatkan bahwa ketiga algoritma bekerja pada persoalan yang bermakna, bukan untuk menyatakan rancangan jaringan yang optimal bagi kampus yang sesungguhnya. Hanya enam dari sepuluh pasangan gedung yang diperlakukan sebagai jalur kandidat, sedangkan pasangan lainnya diasumsikan tidak layak dibangun.

**Tabel 4.1** Jalur kabel kandidat dan panjangnya (nilai ilustrasi)

| Gedung A | Gedung B | Panjang (m) |
|---|---|---|
| Sipil | Industri | 20 |
| Elektro | Geologi | 30 |
| Arsitektur | Sipil | 40 |
| Arsitektur | Elektro | 50 |
| Sipil | Elektro | 60 |
| Industri | Geologi | 80 |

Seluruh panjang pada Tabel 4.1 berbeda, sehingga MST pada graf ini tunggal dan komponen pemutus seri pada kunci κ (Persamaan (6)) tidak pernah menentukan urutan sisi. Kruskal mengurutkan sisi secara menaik lalu menerima sisi Sipil dan Industri (20), Elektro dan Geologi (30), serta Arsitektur dan Sipil (40). Sisi Arsitektur dan Elektro (50) juga diterima karena menghubungkan dua komponen yang berbeda, yaitu {Arsitektur, Sipil, Industri} dan {Elektro, Geologi}. Sisi Sipil dan Elektro (60) serta Industri dan Geologi (80) ditolak karena menutup siklus.

**Tabel 4.2** Hasil ketiga algoritma pada studi kasus

| Algoritma | Jumlah sisi | Total (m) |
|---|---|---|
| Kruskal | 4 | 140 |
| Prim | 4 | 140 |
| Borůvka | 4 | 140 |

Keluaran ketiga program sama dengan hitungan tangan di atas, yaitu empat sisi, sesuai banyaknya sisi pohon rentang untuk lima simpul, dengan total 140 m. Karena MST pada graf ini tunggal, total yang sama berarti himpunan sisinya juga sama.

Hasil ini memiliki keterbatasan yang berasal dari model, bukan dari algoritma. MST meminimalkan total panjang kabel, tetapi hasilnya berupa pohon, sehingga putusnya satu jalur memutus jaringan. MST juga tidak memperhitungkan syarat lain seperti cadangan jalur atau kondisi medan (lihat 3.5.2).

Dengan hanya lima simpul, studi kasus ini membuktikan kebenaran keluaran dan kegunaan MST, tetapi tidak dapat dipakai menilai efisiensi. Perbandingan waktu terhadap ukuran masukan dibahas pada eksperimen sintetis di subbab berikutnya.

---

## 4.2 Lingkungan Uji dan Implementasi

---

Seluruh pengukuran dijalankan pada satu sesi Google Colab versi gratis (*free tier*), yaitu mesin virtual yang bersifat pribadi bagi akun pengguna dengan sumber daya yang tidak dijamin tetap. Spesifikasinya dicatat oleh program pada awal sesi dan disajikan pada Tabel 4.3.

**Tabel 4.3** Lingkungan uji

| Komponen | Keterangan |
|---|---|
| Platform | Google Colab versi gratis (mesin virtual) |
| Prosesor | Intel(R) Xeon(R) CPU @ 2.20GHz, 2 CPU |
| Sistem operasi | Linux 6.6.122+ |
| Python | 3.13.16 |
| Pustaka | pandas 2.2.3, numpy 2.1.3 |
| *Seed* pengacak | 2026 |
| Pengukur waktu | `time.perf_counter()` |
| Eksekusi | sekuensial |

Waktu diambil dengan `time.perf_counter()` hanya di sekitar pemanggilan algoritma, setelah `gc.collect()`, dan pengumpul sampah tetap aktif selama pengukuran. Ketiga algoritma dijalankan pada graf yang sama. Kruskal dan Borůvka menerima daftar sisi, sedangkan Prim menerima daftar ketetanggaan (butir 4 subbab 1.4). Karena itu waktu Prim dicatat dua kali, yaitu waktu inti tanpa pembuatan daftar ketetanggaan dan waktu yang ditambah konversi daftar sisi menjadi daftar ketetanggaan.

Ketiga algoritma ditulis dalam Python dan berjalan sekuensial (butir 3 subbab 1.4). Kode tersimpan pada tiga berkas di repositori, yaitu `Kruskal/kruskal.py`, `Prim/prim.py`, dan `Borůvka/boruvka.py`. Pemetaan setiap bagian *pseudocode* ke fungsi pada kode ada di Tabel 3.7. Pengurutan memakai `sorted` pada Kruskal, antrean prioritas memakai `heapq` pada Prim, dan keduanya hanya alat bantu. Struktur *disjoint set* ditulis sendiri pada kelas `HimpunanTerpisah` dengan *union by rank* dan *path halving*, dan Borůvka memakai kelas yang sama dari `kruskal.py`. Kode lengkap tersedia di repositori (lihat Lampiran). Berikut kutipan bagian intinya, dengan komentar pada kode asli dihilangkan agar ringkas.

**Kode 4.1** `HimpunanTerpisah` (*Pseudocode* 3.1)

```python
def cari_akar(self, simpul):
    while self.induk[simpul] != simpul:
        self.induk[simpul] = self.induk[self.induk[simpul]]
        simpul = self.induk[simpul]
    return simpul

def gabung(self, simpul_a, simpul_b):
    akar_a = self.cari_akar(simpul_a)
    akar_b = self.cari_akar(simpul_b)
    if akar_a == akar_b:
        return False
    if self.peringkat[akar_a] < self.peringkat[akar_b]:
        akar_a, akar_b = akar_b, akar_a
    self.induk[akar_b] = akar_a
    if self.peringkat[akar_a] == self.peringkat[akar_b]:
        self.peringkat[akar_a] += 1
    return True
```

`cari_akar` memendekkan lintasan menuju akar setiap kali dilalui (*path halving*). `gabung` menggantungkan pohon yang lebih rendah ke pohon yang lebih tinggi (*union by rank*) dan mengembalikan `False` jika kedua simpul sudah berada pada himpunan yang sama, yaitu jika sisi itu akan membentuk siklus.

**Kode 4.2** Kruskal (*Pseudocode* 3.2)

```python
sisi_terurut = sorted(daftar_sisi, key=lambda sisi: (sisi[2], min(sisi[0], sisi[1]), max(sisi[0], sisi[1])))
himpunan = HimpunanTerpisah(jumlah_simpul)
for simpul_a, simpul_b, bobot in sisi_terurut:
    if himpunan.gabung(simpul_a, simpul_b):
        sisi_mst.append((simpul_a, simpul_b, bobot))
        total_bobot += bobot
        if len(sisi_mst) == jumlah_simpul - 1:
            break
```

Kunci pengurutan adalah tripel κ pada Persamaan (6), yaitu bobot, simpul terkecil, lalu simpul terbesar. Sisi diterima hanya jika `gabung` mengembalikan `True`, dan perulangan berhenti segera setelah *n* − 1 sisi terkumpul. Jika setelah perulangan jumlah sisi kurang dari *n* − 1, fungsi melempar `ValueError` karena graf tidak terhubung (bagian ini tidak ditampilkan pada kutipan).

**Kode 4.3** Prim (*Pseudocode* 3.3)

```python
while antrean and len(sisi_mst) < jumlah_simpul - 1:
    bobot, kecil, besar = heapq.heappop(antrean)
    if sudah_masuk[kecil] and sudah_masuk[besar]:
        continue
    asal, tujuan = (kecil, besar) if sudah_masuk[kecil] else (besar, kecil)
    sudah_masuk[tujuan] = True
    sisi_mst.append((asal, tujuan, bobot))
    total_bobot += bobot
    for simpul_tetangga, bobot_baru in daftar_tetangga[tujuan]:
        if not sudah_masuk[simpul_tetangga]:
            heapq.heappush(antrean, (bobot_baru, min(tujuan, simpul_tetangga), max(tujuan, simpul_tetangga)))
```

Antrean berisi sisi dalam bentuk tripel (bobot, simpul kecil, simpul besar), sehingga urutannya memakai kunci κ yang sama dengan Kruskal. Sisi termurah diambil dari antrean. Jika kedua ujungnya sudah berada di pohon, sisi itu sudah usang dan dilewati. Jika tidak, ujung yang belum masuk menjadi simpul baru, lalu semua sisi dari simpul itu ke simpul di luar pohon dimasukkan ke antrean.

**Kode 4.4** Borůvka, satu putaran (*Pseudocode* 3.4)

```python
termurah = {}
for simpul_a, simpul_b, bobot in daftar_sisi:
    akar_a = himpunan.cari_akar(simpul_a)
    akar_b = himpunan.cari_akar(simpul_b)
    if akar_a == akar_b:
        continue
    sisi = (simpul_a, simpul_b, bobot)
    for akar in (akar_a, akar_b):
        if akar not in termurah or kunci_sisi(sisi) < kunci_sisi(termurah[akar]):
            termurah[akar] = sisi
for simpul_a, simpul_b, bobot in termurah.values():
    if himpunan.gabung(simpul_a, simpul_b):
        sisi_mst.append((simpul_a, simpul_b, bobot))
        total_bobot += bobot
        jumlah_komponen -= 1
```

Pada setiap putaran, setiap komponen memilih sisi termurah yang keluar darinya menurut `kunci_sisi`, yaitu κ yang sama. Sisi di dalam satu komponen diabaikan. Setelah semua komponen memilih, pilihan dipasang satu per satu, dan `gabung` yang mengembalikan `False` menandakan sisi itu sudah terpasang oleh komponen lain pada putaran yang sama. Putaran diulang sampai tersisa satu komponen, dan jika tidak ada sisi yang keluar dari komponen mana pun padahal komponen masih lebih dari satu, fungsi melempar `ValueError` (bagian ini dan pembuatan `himpunan` serta `jumlah_komponen` tidak ditampilkan pada kutipan).

---

## 4.3 Verifikasi Kebenaran

---

Kebenaran kode diperiksa sebelum waktu dicatat, karena waktu dari kode yang salah tidak bermakna. Pemeriksaan ini bukti empiris yang menguatkan. Bukti kebenaran formal Kruskal dan Prim ada di Bab 3, sedangkan kebenaran Borůvka tidak dibuktikan secara formal (butir 2 subbab 1.4). Tabel 4.4 merangkum pemeriksaan yang dilakukan beserta batasnya.

**Tabel 4.4** Pemeriksaan kebenaran

| Pemeriksaan | Cara | Yang ditunjukkan | Batas |
|---|---|---|---|
| Kasus uji kecil | Empat graf: tiga graf terhubung dengan total 7, 3, dan 6, serta satu graf tak terhubung yang harus menghasilkan `ValueError` | Ketiga algoritma lolos pada keempat kasus. Total 7 dan 6 sama dengan hitungan tangan di 3.1 | Hanya empat graf |
| Himpunan sisi | Kasus 3 berbobot kembar membandingkan himpunan sisi. Pada studi kasus 4.1, total yang sama berarti himpunan sisi yang sama berdasarkan argumen keunikan MST | Kesamaan himpunan sisi pada graf kecil | Pada graf eksperimen yang dibandingkan hanya total bobot |
| Pembanding `networkx` | Total bobot ketiga algoritma dibandingkan dengan hasil `networkx` pada 300 graf acak kecil | Total bobot sama dengan pustaka standar | `networkx` hanya pembanding, tidak dipakai di dalam algoritma (butir 3 subbab 1.4). Yang dibandingkan total bobot |
| Uji *seed* dan pembangkit graf | Seed yang sama menghasilkan graf yang sama dan seed berbeda menghasilkan graf lain. Pada ukuran terkecil tiap skenario, graf terhubung, tanpa sisi ganda, dan tanpa *loop* | Data uji dapat diulang dan memenuhi syarat graf | Hanya diperiksa pada ukuran terkecil |
| Setiap ulangan pengukuran | Total bobot ketiga algoritma dibandingkan pada setiap ulangan, dan program berhenti jika berbeda | Tidak ada pengukuran dari hasil yang berbeda pada graf besar | Total bobot yang sama belum menjamin himpunan sisi yang sama |

Satu keterbatasan lain menyangkut kode yang diukur. Notebook memiliki langkah pencocokan otomatis antara berkas `.py` dan kode di dalam notebook, tetapi langkah itu dilewati di Colab. Karena itu kode yang diukur adalah kode di dalam notebook.

---

## 4.4 Rancangan Eksperimen

---

Pengukuran memakai tiga skenario graf (Tabel 4.5). Graf padat diberi ukuran lebih kecil karena jumlah sisinya tumbuh sebesar Θ(*n*²) (butir 5 subbab 1.4). Dengan *m* = *n*(*n* − 1)/4, yaitu separuh jumlah sisi maksimum, graf padat berukuran *n* sampai 1000 sudah memiliki sekitar 2,5 × 10⁵ sisi, sehingga jumlah sisi pada kedua kepadatan berada pada rentang yang sebanding, yaitu sekitar 10⁴ sampai 2,5 × 10⁵. Skenario ketiga memakai bentuk graf yang sama dengan skenario pertama, tetapi bobotnya hanya bilangan bulat 1 sampai 5 sehingga banyak sisi berbobot sama.

**Tabel 4.5** Skenario pengukuran

| Skenario | Jumlah sisi *m* | Ukuran *n* | Rentang *m* | Bobot |
|---|---|---|---|---|
| jarang | 3*n* | 4000, 8000, 16000, 32000, 64000 | 12000 sampai 192000 | bilangan bulat acak 1 sampai 1000000 |
| padat | *n*(*n* − 1)/4 (separuh sisi maksimum) | 200, 400, 600, 800, 1000 | 9950 sampai 249750 | bilangan bulat acak 1 sampai 1000000 |
| jarang_kembar | 3*n* | 4000, 8000, 16000, 32000, 64000 | 12000 sampai 192000 | bilangan bulat acak 1 sampai 5 |

Graf dibangkitkan dengan `random.Random` ber-*seed* 2026. Pembangkit membentuk pohon acak terlebih dahulu, dengan setiap simpul dihubungkan ke satu simpul bernomor lebih kecil, sehingga graf pasti terhubung. Sisi acak lalu ditambahkan tanpa sisi ganda dan tanpa *loop* sampai jumlah sisi terpenuhi.

Untuk setiap pasangan skenario dan ukuran, satu graf dibangkitkan. Satu putaran pemanasan dijalankan lebih dahulu dan tidak dicatat, lalu pengukuran diulang lima kali pada graf yang sama (butir 6 subbab 1.4). Karena graf yang sama dipakai pada kelima ulangan, simpangan baku hanya mengukur gangguan waktu pada mesin, bukan variasi antar graf. Hasil setiap kombinasi dilaporkan sebagai rata-rata dan simpangan baku sampel (pembagi *n* − 1).

---

## 4.5 Hasil

---

Hasil pengukuran disajikan per skenario pada Tabel 4.6 sampai 4.8 sebagai rata-rata ± simpangan baku dari lima ulangan, dalam milidetik. Grafik waktu terhadap jumlah sisi beserta kurva teoretis ada pada Gambar 4.1 sampai 4.3, dan rasio waktu terhadap suku teoretis ada pada Tabel 4.9.

**Tabel 4.6** Waktu eksekusi skenario jarang (*m* = 3*n*), rata-rata ± simpangan baku dalam ms

| *n* | *m* | Kruskal | Prim | Prim (+konversi) | Borůvka |
|---|---|---|---|---|---|
| 4000 | 12000 | 17,66 ± 0,19 | 19,91 ± 1,12 | 26,60 ± 1,25 | 83,12 ± 1,11 |
| 8000 | 24000 | 40,43 ± 1,77 | 47,30 ± 7,11 | 60,79 ± 7,22 | 209,63 ± 9,66 |
| 16000 | 48000 | 111,50 ± 31,99 | 133,72 ± 43,62 | 168,61 ± 50,86 | 782,47 ± 446,37 |
| 32000 | 96000 | 265,72 ± 77,28 | 316,61 ± 80,37 | 384,53 ± 88,61 | 1150,53 ± 279,07 |
| 64000 | 192000 | 622,12 ± 138,53 | 754,54 ± 170,75 | 1050,15 ± 223,96 | 2671,35 ± 273,35 |

**Tabel 4.7** Waktu eksekusi skenario padat (*m* = *n*(*n* − 1)/4), rata-rata ± simpangan baku dalam ms

| *n* | *m* | Kruskal | Prim | Prim (+konversi) | Borůvka |
|---|---|---|---|---|---|
| 200 | 9950 | 9,61 ± 2,60 | 6,65 ± 0,49 | 10,55 ± 0,55 | 44,37 ± 1,43 |
| 400 | 39900 | 42,78 ± 1,76 | 32,06 ± 1,06 | 52,23 ± 4,37 | 261,93 ± 8,15 |
| 600 | 89850 | 156,24 ± 34,66 | 112,67 ± 22,07 | 173,70 ± 28,09 | 825,96 ± 248,41 |
| 800 | 159800 | 304,59 ± 87,58 | 197,60 ± 57,90 | 299,85 ± 72,01 | 1638,15 ± 369,76 |
| 1000 | 249750 | 534,56 ± 112,35 | 347,58 ± 69,83 | 518,02 ± 85,95 | 2682,78 ± 658,28 |

**Tabel 4.8** Waktu eksekusi skenario jarang_kembar (*m* = 3*n*, bobot 1 sampai 5), rata-rata ± simpangan baku dalam ms

| *n* | *m* | Kruskal | Prim | Prim (+konversi) | Borůvka |
|---|---|---|---|---|---|
| 4000 | 12000 | 19,41 ± 0,34 | 20,85 ± 1,80 | 28,39 ± 1,90 | 85,24 ± 5,34 |
| 8000 | 24000 | 40,69 ± 1,50 | 43,80 ± 0,77 | 57,29 ± 0,78 | 186,34 ± 8,42 |
| 16000 | 48000 | 116,16 ± 32,99 | 127,78 ± 35,36 | 161,25 ± 42,76 | 531,82 ± 144,01 |
| 32000 | 96000 | 248,12 ± 54,68 | 279,25 ± 65,48 | 349,15 ± 75,85 | 1193,91 ± 305,30 |
| 64000 | 192000 | 625,08 ± 162,42 | 708,80 ± 165,96 | 1007,71 ± 228,62 | 2300,94 ± 251,26 |

**Gambar 4.1** Waktu eksekusi terhadap jumlah sisi pada skenario jarang. Kiri: skala linear. Kanan: skala log-log. Batang galat adalah simpangan baku, dan garis putus-putus adalah kurva teoretis dengan konstanta yang dicocokkan dengan kuadrat terkecil melalui titik asal. (Sisipkan berkas `grafik/waktu_jarang.png`.)

**Gambar 4.2** Waktu eksekusi terhadap jumlah sisi pada skenario padat, dengan keterangan yang sama dengan Gambar 4.1. (Sisipkan berkas `grafik/waktu_padat.png`.)

**Gambar 4.3** Waktu eksekusi terhadap jumlah sisi pada skenario jarang_kembar, dengan keterangan yang sama dengan Gambar 4.1. (Sisipkan berkas `grafik/waktu_jarang_kembar.png`.)

Kurva teoretis pada gambar memakai suku *m* log₂ *m* untuk Kruskal dan *m* log₂ *n* untuk Prim dan Borůvka. Kurva Prim (+konversi) tidak memiliki kurva teoretis sendiri.

**Tabel 4.9** Rasio waktu terhadap suku teoretis, dinormalkan ke ukuran terkecil tiap skenario (= 1,00)

| Skenario | *n* | Kruskal (*m* log *n*) | Prim (*m* log *n*) | Borůvka (*m* log *n*) | Borůvka (*m* log² *n*) |
|---|---|---|---|---|---|
| jarang | 4000 | 1,00 | 1,00 | 1,00 | 1,00 |
| jarang | 8000 | 1,06 | 1,10 | 1,16 | 1,07 |
| jarang | 16000 | 1,35 | 1,44 | 2,02 | 1,73 |
| jarang | 32000 | 1,50 | 1,59 | 1,38 | 1,11 |
| jarang | 64000 | 1,65 | 1,77 | 1,51 | 1,13 |
| padat | 200 | 1,00 | 1,00 | 1,00 | 1,00 |
| padat | 400 | 0,98 | 1,06 | 1,30 | 1,15 |
| padat | 600 | 1,49 | 1,55 | 1,71 | 1,41 |
| padat | 800 | 1,56 | 1,47 | 1,82 | 1,44 |
| padat | 1000 | 1,70 | 1,60 | 1,85 | 1,42 |
| jarang_kembar | 4000 | 1,00 | 1,00 | 1,00 | 1,00 |
| jarang_kembar | 8000 | 0,97 | 0,97 | 1,01 | 0,93 |
| jarang_kembar | 16000 | 1,28 | 1,31 | 1,34 | 1,15 |
| jarang_kembar | 32000 | 1,28 | 1,34 | 1,40 | 1,12 |
| jarang_kembar | 64000 | 1,51 | 1,59 | 1,26 | 0,95 |

Rasio pada Tabel 4.9 dihitung dari rata-rata pada Tabel 4.6 sampai 4.8, dengan suku *m* log₂ *n* untuk ketiga algoritma agar sesuai dengan cara pemeriksaan pada Tabel 3.11. Karena itu rasio Kruskal di sini dapat berbeda dari keluaran notebook, yang memakai *m* log₂ *m* untuk Kruskal. Kolom terakhir adalah rasio Borůvka terhadap suku *m* log² *n*.

Data pada Tabel 4.6 sampai 4.8 menunjukkan hal berikut. Pada skenario jarang dan jarang_kembar, Kruskal memiliki rata-rata terendah pada kelima ukuran. Pada skenario padat, Prim tanpa konversi memiliki rata-rata terendah pada kelima ukuran. Borůvka memiliki rata-rata tertinggi pada semua ukuran di ketiga skenario. Pada ukuran terbesar, waktu Borůvka adalah 4,29 kali waktu Kruskal pada skenario jarang, 5,02 kali pada skenario padat, dan 3,68 kali pada skenario jarang_kembar. Pembuatan daftar ketetanggaan menambah waktu Prim sebesar 39,2% (jarang), 49,0% (padat), dan 42,2% (jarang_kembar) pada ukuran terbesar. Pada skenario padat, Prim (+konversi) lebih lambat daripada Kruskal pada *n* = 200 sampai 600 dan lebih cepat pada *n* = 800 dan 1000, yaitu 518,02 ms dibandingkan 534,56 ms pada *n* = 1000. Simpangan baku berkisar dari 1,1% sampai 57,0% dari rata-rata, dan yang tertinggi terjadi pada Borůvka skenario jarang dengan *n* = 16000.

<!-- CATATAN UNTUK 4.6 (hapus sebelum final): keterbatasan yang belum ditulis. (1) Simpangan baku mencapai sekitar 57% dari rata-rata pada satu titik (Borůvka, skenario jarang, n = 16000), dan 32 dari 60 kombinasi algoritma dan ukuran memiliki simpangan baku sekurang-kurangnya 20% dari rata-rata (dihitung dari ringkasan.csv), sehingga selisih waktu kecil tidak ditafsirkan. (2) Urutan eksekusi dalam setiap ulangan tetap: pembuatan daftar ketetanggaan, Kruskal, Prim, lalu Borůvka. (3) Sumber daya mesin virtual Colab versi gratis tidak dijamin tetap sehingga waktu berfluktuasi. (4) Ukuran n terbesar 64000 (jarang) dan 1000 (padat), jauh di bawah 10^6 pada contoh di slide 10 (contoh, bukan syarat). (5) Rasio waktu terhadap teori pada ukuran terbesar masih naik pada ketiga algoritma. -->
