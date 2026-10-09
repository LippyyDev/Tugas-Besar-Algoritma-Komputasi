# BAB 3 ANALISIS ALGORITMA

---

## 3.1 Contoh Perhitungan Manual

---

Algoritma Kruskal dan Prim dijalankan langkah demi langkah pada dua graf kecil agar cara kerja keduanya dapat diperiksa dengan perhitungan manual. Graf pertama, empat kota dengan bobot berbeda, memperlihatkan penolakan sisi yang membentuk siklus. Graf kedua memuat sisi berbobot sama dan memperlihatkan peran aturan pemutus seri pada butir 7 subbab 1.4. Kedua graf sama dengan Kasus 1 dan Kasus 3 pada uji kasus kecil di kode program, sehingga hasil perhitungan manual dapat dibandingkan langsung dengan keluaran program (Bab 4).

Simpul diberi nomor tetap, yaitu Maros = 0, Makassar = 1, Gowa = 2, dan Takalar = 3. Bobot sisi menyatakan biaya pemasangan kabel dalam juta rupiah. Biaya ini merupakan angka contoh, bukan data hasil pengukuran. Setiap sisi ditulis sebagai (*u*, *v*) dengan *u* < *v*, dan dalam antrean prioritas Prim ditulis sebagai tripel (*w*, *u*, *v*) sesuai kunci pembanding pada 2.2.3.

---

### 3.1.1 Graf Empat Kota dengan Bobot Berbeda

---

Graf pertama memiliki *n* = 4 simpul dan *m* = 5 sisi, sehingga setiap *spanning tree* memiliki *n* − 1 = 3 sisi (lihat 1.2). Sisi-sisinya tercantum pada Tabel 3.1.

**Tabel 3.1** Graf contoh empat kota (bobot dalam juta rupiah)

| Sisi (*u*, *v*) | Kota | Bobot *w* |
|---|---|---|
| (0, 1) | Maros dan Makassar | 1 |
| (1, 2) | Makassar dan Gowa | 2 |
| (0, 2) | Maros dan Gowa | 3 |
| (2, 3) | Gowa dan Takalar | 4 |
| (1, 3) | Makassar dan Takalar | 5 |

**Algoritma Kruskal.** Sisi diurutkan menurut bobot menaik. Karena seluruh bobot berbeda, urutannya tunggal: (0, 1), (1, 2), (0, 2), (2, 3), (1, 3). Pada awalnya hutan terdiri atas empat pohon, yaitu {0}, {1}, {2}, dan {3}. Setiap sisi diperiksa menurut urutan itu, dan dihentikan setelah tiga sisi diterima (Tabel 3.2).

**Tabel 3.2** Jejak algoritma Kruskal pada graf empat kota

| Langkah | Sisi diperiksa | *w* | Kedua ujung sudah satu pohon? | Keputusan | Pohon sesudahnya | Total bobot |
|---|---|---|---|---|---|---|
| 1 | (0, 1) | 1 | Tidak | Terima | {0, 1}, {2}, {3} | 1 |
| 2 | (1, 2) | 2 | Tidak | Terima | {0, 1, 2}, {3} | 3 |
| 3 | (0, 2) | 3 | Ya, lewat Makassar | Tolak | {0, 1, 2}, {3} | 3 |
| 4 | (2, 3) | 4 | Tidak | Terima | {0, 1, 2, 3} | 7 |

Pada langkah 3, Maros dan Gowa sudah terhubung lewat Makassar, sehingga sisi (0, 2) menutup siklus 0, 1, 2. Bobot sisi itu, yaitu 3, lebih besar daripada kedua sisi lain pada siklus (1 dan 2), sesuai dengan *cycle property* (Teorema 2.2). Setelah langkah 4 terkumpul tiga sisi, yaitu *n* − 1, sehingga pemeriksaan berhenti dan sisi (1, 3) dengan bobot 5 tidak pernah diperiksa. Hasilnya adalah {(0, 1), (1, 2), (2, 3)} dengan total bobot 1 + 2 + 4 = 7.

**Algoritma Prim.** Pohon dimulai dari simpul 0 (Maros), sehingga himpunan simpul pohon *S* = {0}. Semua sisi yang meninggalkan simpul 0 dimasukkan ke antrean, yaitu (1, 0, 1) dan (3, 0, 2). Pada setiap langkah, tripel terkecil dikeluarkan dari antrean. Jika kedua ujungnya sudah berada di *S*, tripel itu dibuang karena sudah usang. Jika tidak, sisi diterima, ujung barunya masuk ke *S*, dan sisi dari ujung baru itu ke simpul di luar *S* dimasukkan ke antrean (Tabel 3.3).

**Tabel 3.3** Jejak algoritma Prim pada graf empat kota, simpul awal 0

| Langkah | Isi antrean sebelum pengambilan (*w*, *u*, *v*) | Tripel diambil | Keputusan | *S* sesudahnya | Total bobot |
|---|---|---|---|---|---|
| 1 | (1, 0, 1), (3, 0, 2) | (1, 0, 1) | Terima, simpul 1 masuk | {0, 1} | 1 |
| 2 | (2, 1, 2), (3, 0, 2), (5, 1, 3) | (2, 1, 2) | Terima, simpul 2 masuk | {0, 1, 2} | 3 |
| 3 | (3, 0, 2), (4, 2, 3), (5, 1, 3) | (3, 0, 2) | Buang, kedua ujung sudah di *S* | {0, 1, 2} | 3 |
| 4 | (4, 2, 3), (5, 1, 3) | (4, 2, 3) | Terima, simpul 3 masuk | {0, 1, 2, 3} | 7 |

Pada langkah 3, tripel (3, 0, 2) sudah usang karena simpul 2 masuk lewat sisi (1, 2) pada langkah 2. Inilah entri usang yang dibiarkan di antrean (lihat 3.2.3). Setelah langkah 4 terkumpul tiga sisi, sehingga perulangan berhenti dan tripel (5, 1, 3) tetap tersisa di antrean tanpa diproses. Hasilnya adalah {(0, 1), (1, 2), (2, 3)} dengan total bobot 7, sama dengan hasil Kruskal.

**Pemeriksaan hasil.** Graf ini memiliki delapan *spanning tree*, yaitu sepuluh kombinasi tiga sisi dikurangi dua kombinasi yang membentuk siklus, yakni {(0, 1), (1, 2), (0, 2)} dan {(1, 2), (2, 3), (1, 3)}. Total bobot kedelapan pohon itu berkisar dari 7 sampai 12, dan hanya satu yang bernilai 7, yaitu pohon di atas. Jadi hasil Kruskal dan Prim memang MST, dan MST-nya unik, sesuai dengan Teorema 2.3 karena seluruh bobot berbeda.

---

### 3.1.2 Graf dengan Sisi Berbobot Sama

---

Graf kedua memiliki *n* = 4 simpul dan *m* = 5 sisi. Empat sisi membentuk siklus 0, 1, 2, 3 dan semuanya berbobot 2, sedangkan diagonal (1, 3) berbobot 5 (Tabel 3.4).

**Tabel 3.4** Graf contoh dengan sisi berbobot sama (bobot dalam juta rupiah)

| Sisi (*u*, *v*) | Kota | Bobot *w* |
|---|---|---|
| (0, 1) | Maros dan Makassar | 2 |
| (1, 2) | Makassar dan Gowa | 2 |
| (2, 3) | Gowa dan Takalar | 2 |
| (0, 3) | Maros dan Takalar | 2 |
| (1, 3) | Makassar dan Takalar | 5 |

Setiap *spanning tree* memiliki tiga sisi dan bobot sisi terkecil adalah 2, sehingga total bobot minimal 6. Membuang salah satu dari empat sisi pada siklus menghasilkan *spanning tree* berbobot 6, sehingga graf ini memiliki empat MST dengan total bobot yang sama. Seperti dibahas pada 2.2.3, himpunan sisi yang dikeluarkan algoritma pada graf semacam ini bergantung pada cara menangani sisi berbobot sama. Laporan ini memakai aturan pemutus seri pada butir 7 subbab 1.4, yaitu membandingkan bobot, lalu simpul ujung bernomor terkecil, lalu simpul ujung bernomor terbesar. Dengan aturan ini urutan seluruh sisi pada Tabel 3.4 menjadi tunggal: (2, 0, 1), (2, 0, 3), (2, 1, 2), (2, 2, 3), (5, 1, 3).

**Algoritma Kruskal.** Sisi diperiksa menurut urutan di atas (Tabel 3.5). Setelah tiga sisi diterima pemeriksaan berhenti, dan sisi (2, 3) tidak diperiksa. Hasilnya {(0, 1), (0, 3), (1, 2)} dengan total bobot 6.

**Tabel 3.5** Jejak algoritma Kruskal pada graf dengan sisi berbobot sama

| Langkah | Sisi diperiksa | *w* | Kedua ujung sudah satu pohon? | Keputusan | Total bobot |
|---|---|---|---|---|---|
| 1 | (0, 1) | 2 | Tidak | Terima | 2 |
| 2 | (0, 3) | 2 | Tidak | Terima | 4 |
| 3 | (1, 2) | 2 | Tidak | Terima | 6 |

**Algoritma Prim.** Pohon dimulai dari simpul 0 (Tabel 3.6).

**Tabel 3.6** Jejak algoritma Prim pada graf dengan sisi berbobot sama, simpul awal 0

| Langkah | Isi antrean sebelum pengambilan (*w*, *u*, *v*) | Tripel diambil | Keputusan | *S* sesudahnya | Total bobot |
|---|---|---|---|---|---|
| 1 | (2, 0, 1), (2, 0, 3) | (2, 0, 1) | Terima, simpul 1 masuk | {0, 1} | 2 |
| 2 | (2, 0, 3), (2, 1, 2), (5, 1, 3) | (2, 0, 3) | Terima, simpul 3 masuk | {0, 1, 3} | 4 |
| 3 | (2, 1, 2), (2, 2, 3), (5, 1, 3) | (2, 1, 2) | Terima, simpul 2 masuk | {0, 1, 2, 3} | 6 |

Pada langkah 3, tripel (2, 1, 2) dan (2, 2, 3) berbobot sama, dan aturan pemutus seri memilih (2, 1, 2). Tanpa aturan itu, Prim dapat memilih (2, 2, 3) dan menghasilkan MST lain dengan total bobot yang sama. Hasilnya {(0, 1), (0, 3), (1, 2)} dengan total bobot 6, sama dengan Kruskal. Tanpa aturan pemutus seri, kedua algoritma tetap menghasilkan total bobot 6 tetapi himpunan sisinya dapat berbeda, sehingga seluruh perbandingan keluaran pada laporan ini memakai aturan yang sama.

---

## 3.2 *Pseudocode*

---

*Pseudocode* disusun menurut kode program yang ditulis sendiri, sehingga setiap baris dapat ditelusuri ke satu baris atau satu blok pada kode. Graf *G* = (*V*, *E*) memiliki *n* simpul bernomor 0 sampai *n* − 1 dan *m* sisi, dan setiap sisi ditulis sebagai (*u*, *v*, *w*) dengan *w* bobotnya. Kruskal dan Borůvka menerima graf sebagai daftar sisi, sedangkan Prim menerima daftar ketetanggaan *Adj*, yaitu *Adj*[*x*] berisi pasangan (*t*, *w*) untuk setiap sisi yang menghubungkan *x* dengan tetangga *t* (butir 4 subbab 1.4).

Ketiga algoritma memakai kunci pembanding sisi yang sama, yaitu aturan pemutus seri pada butir 7 subbab 1.4 dan 2.2.3. Untuk sisi *e* = (*u*, *v*, *w*), kunci ini adalah tripel

κ(*e*) = (*w*, min(*u*, *v*), max(*u*, *v*)), (6)

yang dibandingkan secara leksikografis, yaitu bobot lebih dulu, lalu simpul terkecil, lalu simpul terbesar. Karena graf tidak memiliki sisi ganda, tidak ada dua sisi dengan kunci yang sama, sehingga κ mengurutkan seluruh sisi secara total.

Operasi pengurutan pada Kruskal dan operasi antrean prioritas pada Prim memakai alat bantu bawaan Python, yaitu `sorted` dan `heapq` (butir 3 subbab 1.4). Pada *pseudocode*, alat bantu itu ditulis sebagai "urutkan" dan operasi MASUKKAN serta KELUARKAN-TERKECIL. Biayanya dibahas pada 3.4.

---

### 3.2.1 *Disjoint Set*

---

Kruskal memakai struktur *disjoint set* untuk menjawab apakah dua simpul sudah berada pada pohon yang sama (lihat 2.1.2), dan Borůvka memakai struktur yang sama untuk menentukan komponen setiap simpul. Struktur ini memakai *union by rank* dan kompresi lintasan (Sanders *et al.*, 2019, Bagian 11.4), dengan *path halving* sebagai varian kompresi lintasan yang dipilih pada implementasi ini.

```
Pseudocode 3.1  Disjoint set

BUAT-HIMPUNAN(n)
1  untuk i ← 0 sampai n − 1 lakukan
2      induk[i] ← i ; peringkat[i] ← 0

CARI-AKAR(x)
1  selama induk[x] ≠ x lakukan
2      induk[x] ← induk[induk[x]]
3      x ← induk[x]
4  kembalikan x

GABUNG(a, b)
1  ra ← CARI-AKAR(a) ; rb ← CARI-AKAR(b)
2  jika ra = rb maka kembalikan SALAH
3  jika peringkat[ra] < peringkat[rb] maka tukar ra dan rb
4  induk[rb] ← ra
5  jika peringkat[ra] = peringkat[rb] maka peringkat[ra] ← peringkat[ra] + 1
6  kembalikan BENAR
```

GABUNG mengembalikan SALAH jika kedua simpul sudah berada pada himpunan yang sama. Nilai ini yang dipakai sebagai pendeteksi siklus oleh Kruskal dan sebagai penjaga oleh Borůvka.

---

### 3.2.2 Algoritma Kruskal

---

Kruskal mengurutkan seluruh sisi menurut κ, lalu memeriksanya satu per satu. Sisi diterima jika GABUNG berhasil, dan ditolak jika kedua ujungnya sudah berada pada pohon yang sama. Perulangan dihentikan segera setelah *n* − 1 sisi terkumpul, sehingga sisi terberat tidak selalu diperiksa (lihat contoh pada 3.1.1).

```
Pseudocode 3.2  Kruskal

KRUSKAL(n, E)
1  E′ ← E diurutkan menaik menurut κ
2  himpunan ← BUAT-HIMPUNAN(n) ; A ← ∅ ; total ← 0
3  untuk setiap (u, v, w) pada E′ menurut urutannya lakukan
4      jika GABUNG(u, v) maka
5          A ← A ∪ {(u, v, w)} ; total ← total + w
6          jika |A| = n − 1 maka hentikan perulangan
7  jika |A| ≠ n − 1 maka galat "Graf tidak terhubung"
8  kembalikan (A, total)
```

Jika graf tidak terhubung, sisi yang tersedia habis sebelum *n* − 1 sisi terkumpul, dan baris 7 melaporkan galat. Pemeriksaan ini hanya pengaman, karena graf masukan diasumsikan terhubung (butir 1 subbab 1.4).

---

### 3.2.3 Algoritma Prim

---

Prim tumbuh dari satu simpul awal *s*, dengan *s* = 0 pada implementasi ini. Rumusan Prim berbasis simpul memerlukan operasi *decrease-key* untuk menurunkan kunci simpul di antrean (lihat 2.1.2), tetapi `heapq` tidak menyediakannya. Karena itu antrean prioritas *Q* menyimpan sisi, bukan simpul. Setiap sisi yang menghubungkan pohon dengan simpul di luar pohon dimasukkan ke *Q*, dan sisi yang ujung lainnya sudah berada di pohon dibuang saat dikeluarkan (baris 7), sehingga *Q* dapat memuat entri usang dan hingga *O*(*m*) elemen. Elemen antrean adalah kunci κ dari sisi, sehingga urutan pengeluaran dari *Q* otomatis mengikuti aturan pemutus seri.

```
Pseudocode 3.3  Prim

BUAT-DAFTAR-TETANGGA(n, E)
1  untuk i ← 0 sampai n − 1 lakukan Adj[i] ← daftar kosong
2  untuk setiap (u, v, w) pada E lakukan
3      tambahkan (v, w) ke Adj[u] ; tambahkan (u, w) ke Adj[v]
4  kembalikan Adj

PRIM(n, Adj, s)
1  untuk i ← 0 sampai n − 1 lakukan masuk[i] ← SALAH
2  masuk[s] ← BENAR ; A ← ∅ ; total ← 0 ; Q ← antrean prioritas kosong
3  untuk setiap (t, w) pada Adj[s] lakukan
4      MASUKKAN(Q, (w, min(s, t), max(s, t)))
5  selama Q tidak kosong dan |A| < n − 1 lakukan
6      (w, k, b) ← KELUARKAN-TERKECIL(Q)
7      jika masuk[k] dan masuk[b] maka lanjutkan ke iterasi berikutnya
8      jika masuk[k] maka (asal, tujuan) ← (k, b) selain itu (asal, tujuan) ← (b, k)
9      masuk[tujuan] ← BENAR
10     A ← A ∪ {(asal, tujuan, w)} ; total ← total + w
11     untuk setiap (t, w′) pada Adj[tujuan] lakukan
12         jika tidak masuk[t] maka MASUKKAN(Q, (w′, min(tujuan, t), max(tujuan, t)))
13 jika |A| ≠ n − 1 maka galat "Graf tidak terhubung"
14 kembalikan (A, total)
```

Setiap elemen *Q* memiliki sedikitnya satu ujung di dalam pohon, sehingga pada baris 8 tepat satu ujung bernilai `masuk` dan ujung lainnya menjadi simpul baru. Perulangan berhenti ketika *n* − 1 sisi terkumpul atau *Q* kosong. Pada kasus kedua, graf tidak terhubung dan baris 13 melaporkan galat. Pengukuran di Bab 4 melaporkan waktu Prim tanpa dan dengan pembuatan *Adj*.

---

### 3.2.4 Algoritma Borůvka

---

Borůvka bekerja dalam putaran. Pada setiap putaran, setiap komponen memilih sisi terkecil menurut κ di antara sisi yang keluar dari komponen itu (baris 4 sampai 8), dan baru setelah semua komponen memilih, seluruh pilihan dipasang (baris 10 sampai 13). Seluruh pilihan dalam satu putaran dibuat dari keadaan komponen pada awal putaran yang sama. CARI-AKAR pada baris 5 hanya memendekkan lintasan dan tidak mengubah akar sebuah komponen.

```
Pseudocode 3.4  Borůvka

BORŮVKA(n, E)
1  himpunan ← BUAT-HIMPUNAN(n) ; A ← ∅ ; total ← 0 ; c ← n
2  selama c > 1 lakukan
3      T ← kamus kosong     // akar komponen → sisi terkecil yang keluar darinya
4      untuk setiap e = (u, v, w) pada E lakukan
5          ru ← CARI-AKAR(u) ; rv ← CARI-AKAR(v)
6          jika ru = rv maka lanjutkan ke iterasi berikutnya
7          untuk setiap r ∈ {ru, rv} lakukan
8              jika r ∉ T atau κ(e) < κ(T[r]) maka T[r] ← e
9      jika T kosong maka galat "Graf tidak terhubung"
10     untuk setiap e = (u, v, w) pada nilai T lakukan
11         jika GABUNG(u, v) maka
12             A ← A ∪ {e} ; total ← total + w
13             c ← c − 1
14 kembalikan (A, total)
```

Satu sisi dapat dipilih oleh dua komponen sekaligus, yaitu komponen pada kedua ujungnya. Pada baris 11, GABUNG yang kedua kalinya mengembalikan SALAH, sehingga sisi itu tidak dipasang dua kali. Jika pada suatu putaran tidak ada sisi yang keluar dari komponen mana pun padahal *c* > 1, graf tidak terhubung dan baris 9 melaporkan galat.

---

## 3.3 Bukti Kebenaran

---

Kebenaran Kruskal dan Prim dibuktikan dengan invarian bahwa himpunan sisi *A* yang terkumpul selalu termuat dalam suatu MST, sehingga setiap sisi yang diterima adalah *safe edge* (lihat 2.1.2). Invarian itu dijaga oleh *cut property* (Teorema 2.1), sedangkan *cycle property* (Teorema 2.2) menjelaskan penolakan sisi pada Kruskal. Karena kedua teorema itu baru disketsakan pada Bab 2, buktinya dilengkapi lebih dulu pada 3.3.1 dan 3.3.2. Seluruh pembuktian memakai graf *G* = (*V*, *E*) tak berarah, terhubung, dan berbobot real dengan *n* = |*V*| dan *m* = |*E*| (lihat 1.2), serta istilah potongan, *light edge*, dan menghormati seperti pada 2.2.1.

---

### 3.3.1 Bukti *Cut Property*

---

**Bukti Teorema 2.1.** Misalkan *T* adalah MST yang memuat *A*, (*S*, *V* \ *S*) adalah potongan yang menghormati *A*, dan *e* = (*u*, *v*) adalah *light edge* pada potongan itu. Jika *e* ∈ *T*, maka *A* ∪ {*e*} ⊆ *T* dan pernyataan terbukti.

Jika *e* ∉ *T*, karena *T* adalah *spanning tree*, *T* memuat tepat satu lintasan *p* dari *u* ke *v*. Kedua ujung *e* berada di sisi yang berlawanan pada potongan, sehingga *p* memuat sedikitnya satu sisi *f* = (*x*, *y*) yang melintasi potongan. Karena potongan menghormati *A*, *f* ∉ *A*. Menghapus *f* memutuskan satu-satunya lintasan antara *u* dan *v* di *T*, sehingga *T* − {*f*} terdiri atas dua komponen, yang satu memuat *u* dan yang lain memuat *v*. Sisi *e* menghubungkan kedua komponen itu, sehingga *T'* = (*T* − {*f*}) ∪ {*e*} terhubung dan memiliki *n* − 1 sisi, yaitu sebuah *spanning tree*.

Karena *e* adalah *light edge* dan *f* melintasi potongan yang sama, *w*(*e*) ≤ *w*(*f*). Akibatnya *w*(*T'*) = *w*(*T*) − *w*(*f*) + *w*(*e*) ≤ *w*(*T*). Karena *T* minimum, *w*(*T'*) = *w*(*T*), sehingga *T'* juga MST. Karena *f* ∉ *A*, *A* ⊆ *T* − {*f*}, sehingga *A* ∪ {*e*} ⊆ *T'*. ∎ (Sanders *et al.*, 2019, Lemma 11.1)

---

### 3.3.2 Bukti *Cycle Property*

---

**Bukti Teorema 2.2.** Misalkan *e* = (*u*, *v*) adalah sisi terberat pada siklus *C* dan *G'* = (*V*, *E* \ {*e*}). Graf *G'* terhubung karena *C* − {*e*} adalah lintasan dari *u* ke *v*.

*Langkah 1:* ada MST dari *G* yang tidak memuat *e*. Misalkan *T* adalah MST dari *G*. Jika *e* ∉ *T*, langkah ini selesai. Jika *e* ∈ *T*, menghapus *e* memecah *T* menjadi dua komponen, *T*₁ yang memuat *u* dan *T*₂ yang memuat *v*. Lintasan *C* − {*e*} menghubungkan *u* dan *v*, sehingga memuat sebuah sisi *e'* dengan satu ujung di *T*₁ dan ujung lain di *T*₂. Sisi *e'* berada pada *C* dan *e'* ≠ *e*, sehingga *w*(*e'*) ≤ *w*(*e*). Maka *T'* = (*T* − {*e*}) ∪ {*e'*} adalah *spanning tree* dengan *w*(*T'*) ≤ *w*(*T*), sehingga *T'* adalah MST dari *G* yang tidak memuat *e*.

*Langkah 2:* setiap MST dari *G'* adalah MST dari *G*. Misalkan *T'* adalah MST dari *G* yang tidak memuat *e*. Karena *T'* adalah *spanning tree* dari *G'*, bobot MST dari *G'* paling besar *w*(*T'*), yaitu bobot MST dari *G*. Sebaliknya, setiap *spanning tree* dari *G'* juga *spanning tree* dari *G*, sehingga bobotnya paling kecil sama dengan bobot MST dari *G*. Dengan demikian kedua bobot minimum itu sama, dan setiap MST dari *G'* adalah *spanning tree* dari *G* dengan bobot minimum, yaitu MST dari *G*.

*Langkah 3:* *circuit rule*. Jika *e* adalah satu-satunya sisi terberat pada *C*, maka *w*(*e'*) < *w*(*e*) pada langkah 1. Jika ada MST *T* yang memuat *e*, pertukaran pada langkah 1 menghasilkan *w*(*T'*) < *w*(*T*), yang bertentangan dengan keminimalan *T*. Jadi tidak ada MST dari *G* yang memuat *e*. ∎ (Sanders *et al.*, 2019, Lemma 11.2; Nešetřil *et al.*, 2001, Bagian 8)

---

### 3.3.3 Kebenaran Algoritma Kruskal

---

**Teorema 3.1 (Kebenaran Kruskal).** Pada graf *G* yang tak berarah, terhubung, dan berbobot real, KRUSKAL (*Pseudocode* 3.2) mengembalikan sebuah MST dari *G*, dan galat pada baris 7 tidak pernah terjadi.

**Bukti.** Tiga fakta dipakai. Pertama, himpunan pada *disjoint set* selalu sama dengan komponen terhubung graf (*V*, *A*). Pada awalnya setiap simpul berdiri sendiri, dan *A* bertambah tepat ketika GABUNG mengembalikan BENAR (baris 4 dan 5), yaitu ketika kedua ujung berada pada komponen yang berbeda dan kedua himpunan digabung. Dengan demikian GABUNG mengembalikan SALAH tepat ketika kedua ujung sudah berada pada komponen yang sama, dengan kebenaran struktur *disjoint set* sendiri diasumsikan (Sanders *et al.*, 2019, Bagian 11.4). Kedua, karena *A* hanya bertambah, komponen hanya menyatu dan tidak pernah terpisah. Ketiga, sisi diperiksa menurut κ naik, sehingga bobot sisi yang diperiksa tidak pernah menurun.

*Invarian:* sebelum setiap sisi diperiksa pada baris 3, *A* termuat dalam suatu MST dari *G*.

*Basis.* Pada awalnya *A* = ∅, yang termuat dalam setiap MST, dan MST ada karena *G* terhubung (lihat 1.2).

*Langkah.* Misalkan *e* = (*u*, *v*, *w*) adalah sisi yang sedang diperiksa. Jika *e* ditolak, *A* tidak berubah. Jika *e* diterima, misalkan *C* adalah komponen (*V*, *A*) yang memuat *u*, sehingga *v* ∉ *C*. Potongan (*C*, *V* \ *C*) menghormati *A* karena *C* adalah sebuah komponen, dan *e* melintasinya. Setiap sisi *f* yang sudah diperiksa sebelum *e* tidak melintasi potongan ini. Jika *f* diterima, *f* ∈ *A* sehingga *f* tidak melintasi potongan yang menghormati *A*. Jika *f* ditolak, kedua ujungnya sudah berada pada komponen yang sama saat itu, dan karena komponen hanya menyatu, kedua ujungnya berada pada komponen yang sama sekarang. Jadi setiap sisi yang melintasi potongan belum diperiksa atau adalah *e* sendiri, sehingga bobotnya tidak kurang dari *w*. Dengan demikian *e* adalah *light edge* pada potongan yang menghormati *A*, dan menurut Teorema 2.1, *A* ∪ {*e*} termuat dalam suatu MST. Invarian terjaga.

*Terminasi.* Perulangan berhenti karena *A* mencapai *n* − 1 sisi (baris 6) atau karena seluruh sisi sudah diperiksa. Pada kasus kedua, andaikan (*V*, *A*) memiliki lebih dari satu komponen. Karena *G* terhubung, ada sisi *f* ∈ *E* yang kedua ujungnya berada pada komponen berbeda. Sisi *f* sudah diperiksa, dan saat itu kedua ujungnya juga berada pada komponen berbeda karena komponen hanya menyatu, sehingga *f* diterima dan menjadi anggota *A*, yang bertentangan dengan kedua ujungnya berada pada komponen berbeda. Jadi (*V*, *A*) terhubung. Setiap sisi yang diterima menghubungkan dua komponen berbeda sehingga tidak pernah membentuk siklus, dan dengan demikian *A* adalah *spanning tree* dengan *n* − 1 sisi. Pada kedua kasus *A* memiliki *n* − 1 sisi, sehingga baris 7 tidak pernah melaporkan galat.

*Kesimpulan.* Setelah perulangan, *A* termuat dalam suatu MST *T*\*, dan |*A*| = *n* − 1 = |*T*\*|, sehingga *A* = *T*\*. ∎

Penolakan sisi sesuai dengan Teorema 2.2. Jika sisi *e* = (*u*, *v*) ditolak, *e* menutup siklus bersama lintasan dari *u* ke *v* di (*V*, *A*). Seluruh sisi lintasan itu sudah diperiksa lebih dulu sehingga bobotnya tidak lebih besar daripada *w*(*e*), dan *e* adalah salah satu sisi terberat pada siklus tersebut. Pengamatan ini tidak diperlukan untuk bukti di atas.

---

### 3.3.4 Kebenaran Algoritma Prim

---

**Teorema 3.2 (Kebenaran Prim).** Pada graf *G* yang tak berarah, terhubung, dan berbobot real, untuk sembarang simpul awal *s*, PRIM (*Pseudocode* 3.3) mengembalikan sebuah MST dari *G*, dan galat pada baris 13 tidak pernah terjadi.

**Bukti.** Misalkan *S* adalah himpunan simpul dengan `masuk` bernilai BENAR. Invarian berikut berlaku pada awal setiap iterasi perulangan baris 5:

(a) (*S*, *A*) adalah sebuah pohon, yaitu *A* adalah himpunan sisi pohon dengan himpunan simpul *S*;
(b) *A* termuat dalam suatu MST dari *G*;
(c) kunci κ dari setiap sisi yang tepat satu ujungnya berada di *S* ada di *Q*, dan setiap elemen *Q* adalah kunci κ dari sebuah sisi yang sedikitnya satu ujungnya berada di *S*.

*Basis.* Setelah baris 1 sampai 4, *S* = {*s*} dan *A* = ∅, sehingga (a) dan (b) berlaku. Setiap sisi yang tepat satu ujungnya di *S* adalah sisi yang bersisian dengan *s*, dan baris 3 dan 4 memasukkan kuncinya ke *Q*. Seluruh elemen *Q* adalah kunci sisi yang bersisian dengan *s*, sehingga (c) berlaku.

*Langkah.* Misalkan (*w*, *k*, *b*) adalah elemen terkecil yang dikeluarkan pada baris 6, yaitu kunci κ dari sisi *e* = (*k*, *b*).

*Kasus 1:* kedua ujung *e* berada di *S* (baris 7). Elemen dibuang dan *S* serta *A* tidak berubah, sehingga (a) dan (b) tetap berlaku. Sisi *e* tidak melintasi (*S*, *V* \ *S*), sehingga kehilangan elemen ini tidak melanggar bagian pertama (c), dan bagian kedua (c) tetap berlaku untuk elemen yang tersisa.

*Kasus 2:* tepat satu ujung *e* berada di *S*. Menurut bagian kedua (c), setidaknya satu ujung berada di *S*, sehingga tepat satu ujungnya di *S* jika kasus 1 tidak terjadi. Misalkan *tujuan* adalah ujung yang tidak berada di *S* (baris 8). Potongan (*S*, *V* \ *S*) menghormati *A*, karena menurut (a) kedua ujung setiap sisi *A* berada di *S*, dan *e* melintasinya. Setiap sisi *f* yang melintasi potongan memiliki kunci di *Q* menurut (c), dan κ(*e*) adalah elemen terkecil *Q*, sehingga κ(*e*) ≤ κ(*f*) dan *w*(*e*) ≤ *w*(*f*). Jadi *e* adalah *light edge*, dan menurut Teorema 2.1 serta (b), *A* ∪ {*e*} termuat dalam suatu MST, sehingga (b) berlaku setelah baris 10. Karena *tujuan* ∉ *S* dihubungkan ke pohon oleh *e*, (*S* ∪ {*tujuan*}, *A* ∪ {*e*}) tetap berupa pohon, sehingga (a) berlaku. Untuk (c), sisi yang tepat satu ujungnya di *S* ∪ {*tujuan*} adalah sisi yang sebelumnya tepat satu ujungnya di *S* dan ujung lainnya bukan *tujuan*, yang kuncinya sudah ada di *Q* dan tidak ikut dikeluarkan, atau sisi dari *tujuan* ke simpul di luar *S* ∪ {*tujuan*}, yang kuncinya dimasukkan pada baris 11 dan 12. Setiap elemen *Q* sedikitnya memiliki satu ujung di *S* ∪ {*tujuan*}.

*Terminasi.* Karena (*S*, *A*) adalah pohon, |*A*| = |*S*| − 1. Perulangan berhenti ketika |*A*| = *n* − 1 atau *Q* kosong. Andaikan *Q* kosong dan *S* ≠ *V*. Karena *G* terhubung dan *S* tak kosong, ada sisi yang tepat satu ujungnya di *S*, dan kuncinya ada di *Q* menurut (c), yang bertentangan dengan *Q* kosong. Jadi pada kedua kasus *S* = *V* dan |*A*| = *n* − 1, sehingga baris 13 tidak pernah melaporkan galat.

*Kesimpulan.* Menurut (b), *A* termuat dalam suatu MST *T*\*, dan |*A*| = *n* − 1 = |*T*\*|, sehingga *A* = *T*\*. ∎

Bukti ini berlaku untuk sembarang simpul awal *s* dan menunjukkan mengapa elemen usang pada *Q* boleh dibuang tanpa memeriksa apa pun lagi: sisi dengan kedua ujung di *S* tidak melintasi potongan sehingga tidak diperlukan oleh (c).

---

### 3.3.5 Keunikan MST dan Keluaran Kruskal dan Prim pada Aturan Pemutus Seri

---

Teorema 3.1 dan 3.2 menjamin bahwa keluaran keduanya adalah sebuah MST, padahal pada bobot sama sebuah graf dapat memiliki beberapa MST (lihat 3.1.2). Keunikan MST pada bobot berbeda (Teorema 2.3) dibuktikan lebih dulu, karena menjadi dasar teorema berikutnya.

**Bukti Teorema 2.3.** Buktinya memakai syarat yang lebih umum daripada bobot berbeda, yaitu setiap potongan *G* hanya memiliki satu *light edge*. Misalkan *T*₁ dan *T*₂ adalah MST dengan *e* ∈ *T*₁ tetapi *e* ∉ *T*₂. Menghapus *e* dari *T*₁ memecah *T*₁ menjadi dua komponen, sehingga terbentuk sebuah potongan yang hanya dilintasi *e* dari sisi-sisi *T*₁. Setiap MST memuat sedikitnya satu *light edge* dari setiap potongan (*cut rule*; Nešetřil *et al.*, 2001, Bagian 8), sebab jika semua sisi MST yang melintasi potongan bukan *light edge*, penukaran seperti pada 3.3.1 dengan sebuah *light edge* menghasilkan *spanning tree* yang lebih ringan secara ketat. Jadi *e*, satu-satunya sisi *T*₁ pada potongan itu, adalah *light edge*-nya, dan satu-satunya menurut syarat tersebut. Karena *T*₂ juga MST, *T*₂ memuat *light edge* itu, yaitu *e*, yang bertentangan dengan *e* ∉ *T*₂. Jadi *T*₁ ⊆ *T*₂, dan karena keduanya memiliki |*V*| − 1 sisi, *T*₁ = *T*₂. Bobot sisi yang berbeda membuat *light edge* pada setiap potongan menjadi tunggal, sehingga syarat tersebut terpenuhi dan Teorema 2.3 terbukti. ∎ (Nešetřil *et al.*, 2001, Bagian 7 dan 8; Sanders *et al.*, 2019, Latihan 11.5)

Dengan aturan pemutus seri pada butir 7 subbab 1.4, teorema berikut menunjukkan bahwa keluaran Kruskal dan Prim adalah MST yang sama.

**Teorema 3.3 (Keluaran sama).** Misalkan ρ(*e*) ∈ {1, …, *m*} adalah peringkat sisi *e* menurut κ, dengan peringkat 1 untuk κ terkecil. Karena κ berbeda untuk setiap pasangan sisi (lihat 2.2.3), ρ berbeda untuk setiap sisi, sehingga graf *G* dengan bobot ρ memiliki tepat satu MST *M* menurut Teorema 2.3. Maka KRUSKAL dan PRIM pada *G* dengan bobot *w*, untuk sembarang simpul awal *s*, mengembalikan *M*, dan *M* adalah MST dari *G* menurut bobot *w*.

**Bukti.** Keputusan KRUSKAL pada baris 3 sampai 6 hanya bergantung pada urutan sisi menurut κ dan pada keadaan *disjoint set*, dan keputusan PRIM pada baris 5 sampai 12 hanya bergantung pada perbandingan elemen *Q*, yaitu perbandingan κ. Karena perbandingan κ identik dengan perbandingan ρ, jalannya kedua algoritma dengan bobot *w* identik dengan jalannya dengan bobot ρ. Menurut Teorema 3.1 dan 3.2 pada bobot ρ, keluaran keduanya adalah MST dari *G* menurut ρ, yaitu *M* yang unik. Menurut Teorema 3.1 pada bobot *w*, keluaran KRUSKAL juga MST dari *G* menurut *w*, sehingga *M* adalah MST menurut *w*. ∎

Pada graf 3.1.2, peringkat sisi adalah (0, 1) = 1, (0, 3) = 2, (1, 2) = 3, (2, 3) = 4, dan (1, 3) = 5, sehingga *M* = {(0, 1), (0, 3), (1, 2)}, yang sama dengan keluaran kedua algoritma pada Tabel 3.5 dan 3.6. Teorema ini menjadi dasar perbandingan himpunan sisi antar algoritma pada Bab 4. Borůvka tidak dibuktikan secara formal (butir 2 subbab 1.4), sehingga kesamaan keluarannya dengan *M* hanya diperiksa lewat uji kasus kecil dan graf acak.

---

## 3.4 Analisis Kompleksitas

---

Batas atas waktu dan ruang ketiga algoritma diturunkan dari *pseudocode* pada 3.2, dengan notasi *O* saja (2.3). Batas tersebut berlaku untuk urutan bobot sisi apa pun pada kepadatan yang bersangkutan. Penurunan dilakukan baris demi baris agar setiap suku dapat ditelusuri ke satu blok pada *pseudocode*.

---

### 3.4.1 Asumsi dan Alat Bantu

---

Graf *G* terhubung dan memiliki *n* ≥ 2 simpul (butir 1 subbab 1.4), sehingga *n* − 1 ≤ *m* ≤ *n*(*n* − 1)/2 < *n*². Dua akibatnya dipakai berulang kali:

- *n* = *O*(*m*), sehingga suku *n* selalu terserap oleh suku *m*.
- log *m* < 2 log *n*, sehingga *O*(log *m*) = *O*(log *n*).

Operasi dasar, yaitu perbandingan, penugasan, dan akses larik, dihitung berbiaya *O*(1). Perbandingan dua kunci κ pada persamaan (6) juga *O*(1) karena kunci berupa tripel. Alat bantu bawaan Python diperlakukan menurut biaya standar tumpukan biner dan pengurutan berbasis perbandingan (butir 3 subbab 1.4), yaitu:

- `sorted` atas *k* elemen berbiaya *O*(*k* log *k*) pada kasus terburuk,
- `heapq.heappush` dan `heapq.heappop` pada antrean berisi *k* elemen masing-masing berbiaya *O*(log *k*).

Pengurutan bawaan Python bersifat adaptif, yaitu dapat lebih cepat pada masukan yang sudah hampir terurut. Karena itu laporan ini hanya mengklaim batas atas *O*, bukan Θ.

---

### 3.4.2 *Disjoint Set*

---

**Teorema 3.4.** Pada struktur *disjoint set* *Pseudocode* 3.1 yang berisi *n* elemen, BUAT-HIMPUNAN berbiaya *O*(*n*), serta CARI-AKAR dan GABUNG masing-masing berbiaya *O*(log *n*) pada kasus terburuk.

*Bukti.* BUAT-HIMPUNAN menjalankan satu perulangan sebanyak *n* kali, sehingga berbiaya *O*(*n*). Untuk dua operasi lainnya, dibuktikan dua sifat berikut.

(a) Peringkat simpul selalu lebih kecil daripada peringkat induknya. Pada awalnya setiap simpul adalah akar berperingkat 0 dan belum memiliki induk. Pada GABUNG, baris 3 memastikan peringkat[*ra*] ≥ peringkat[*rb*] sebelum *rb* dipasang di bawah *ra* (baris 4). Jika peringkat keduanya sama, baris 5 menaikkan peringkat[*ra*] sehingga lebih besar. Peringkat simpul yang bukan akar tidak pernah berubah, sedangkan peringkat induknya hanya bisa naik. Pada CARI-AKAR baris 2, induk[*x*] diganti dengan induk dari induk[*x*], yaitu leluhur yang peringkatnya lebih besar lagi. Jadi sifat (a) tetap berlaku setelah setiap operasi.

(b) Akar berperingkat *r* memiliki sedikitnya 2^*r* simpul pada pohonnya. Pernyataan ini benar pada awal (*r* = 0, satu simpul). Peringkat sebuah akar hanya naik pada baris 5 ketika dua akar berperingkat *r* digabung, sehingga pohon baru memuat sedikitnya 2^*r* + 2^*r* = 2^(*r*+1) simpul. Penggabungan dengan peringkat berbeda tidak mengubah peringkat akar dan hanya menambah simpul. Pemendekan lintasan pada baris 2 CARI-AKAR memindahkan simpul di dalam pohon yang sama dan tidak mengeluarkan simpul dari pohonnya.

Dari (b), peringkat setiap akar paling besar log₂ *n*. Dari (a), peringkat sepanjang lintasan menuju akar naik secara ketat, sehingga lintasan dari simpul mana pun memuat paling banyak log₂ *n* sisi. Perulangan baris 1 sampai 3 CARI-AKAR berjalan sebanyak itu paling banyak, sehingga CARI-AKAR berbiaya *O*(log *n*). GABUNG memanggil CARI-AKAR dua kali dan menambah sejumlah langkah berbiaya *O*(1), sehingga berbiaya *O*(log *n*). ∎

Batas *O*(log *n*) pada Teorema 3.4 dapat dibuktikan langsung dari kode yang ditulis, dan cukup untuk Kruskal. Batas yang lebih ketat tidak diturunkan di sini. Pengaruhnya pada Borůvka dibahas pada 3.4.5.

---

### 3.4.3 Algoritma Kruskal

---

**Teorema 3.5.** *Pseudocode* 3.2 berjalan dalam waktu *O*(*m* log *n*).

*Bukti.* Biaya tiap baris pada *Pseudocode* 3.2 adalah sebagai berikut.

| Baris | Pekerjaan | Biaya |
|---|---|---|
| 1 | Mengurutkan *m* sisi menurut κ | *O*(*m* log *m*) = *O*(*m* log *n*) |
| 2 | BUAT-HIMPUNAN dan inisialisasi | *O*(*n*) |
| 3 sampai 6 | Paling banyak *m* iterasi, masing-masing satu GABUNG dan pekerjaan *O*(1) | *m* · *O*(log *n*) = *O*(*m* log *n*) |
| 7 dan 8 | Pemeriksaan dan pengembalian hasil | *O*(1) |

Jumlahnya *O*(*n* + *m* log *n*). Karena *n* = *O*(*m*), jumlah ini adalah *O*(*m* log *n*). ∎

Penghentian dini pada baris 6 tidak menurunkan batas ini. Pengurutan pada baris 1 selalu dikerjakan lebih dulu pada seluruh sisi, dan perulangan tetap dapat memeriksa semua *m* sisi jika sisi terberat adalah satu-satunya jembatan graf. Penghentian dini hanya mengurangi pekerjaan setelah pengurutan.

---

### 3.4.4 Algoritma Prim

---

Pembuktian diawali dengan batas banyaknya masukan ke antrean, karena batas ini yang membedakan analisis Prim berbasis sisi dari rumusan berbasis simpul pada 2.1.2.

**Lemma 3.1.** Pada *Pseudocode* 3.3, setiap sisi dimasukkan ke *Q* paling banyak satu kali. Akibatnya jumlah MASUKKAN paling banyak *m*, jumlah KELUARKAN-TERKECIL paling banyak *m*, dan *Q* tidak pernah memuat lebih dari *m* elemen.

*Bukti.* Sisi (*u*, *v*) dimasukkan hanya pada baris 4 atau baris 12, yaitu ketika salah satu ujungnya, misalnya *u*, baru masuk pohon dan ujung lainnya *v* belum masuk pohon. Sesudah itu *u* sudah masuk pohon. Ketika *v* kelak masuk, baris 12 memeriksa tetangga *u* dan menemukan `masuk[u]` bernilai BENAR, sehingga sisi yang sama tidak dimasukkan lagi. Jadi setiap sisi dimasukkan paling banyak satu kali. Elemen hanya dapat dikeluarkan setelah dimasukkan, dan setiap elemen dikeluarkan paling banyak satu kali. ∎

**Teorema 3.6.** *Pseudocode* 3.3, termasuk BUAT-DAFTAR-TETANGGA, berjalan dalam waktu *O*(*m* log *n*).

*Bukti.* BUAT-DAFTAR-TETANGGA membuat *n* daftar kosong dan memproses setiap sisi dengan dua penambahan, sehingga berbiaya *O*(*n* + *m*). Pada PRIM, baris 1 dan 2 berbiaya *O*(*n*). Setiap simpul masuk pohon paling banyak satu kali (baris 9), dan pada saat itu daftar tetangganya dipindai satu kali (baris 3 atau baris 11). Jumlah panjang seluruh daftar tetangga adalah 2*m*, sehingga seluruh pemindaian berbiaya *O*(*m*) di luar operasi antrean. Menurut Lemma 3.1, antrean menerima paling banyak *m* MASUKKAN dan melayani paling banyak *m* KELUARKAN-TERKECIL, dan setiap operasi berbiaya *O*(log *m*) = *O*(log *n*) karena ukuran antrean paling banyak *m*. Pengeluaran elemen yang sudah usang (baris 7) hanya berbiaya satu KELUARKAN-TERKECIL tanpa pekerjaan lain, sehingga sudah terhitung dalam batas *m* pengeluaran. Jumlah seluruhnya *O*(*n* + *m* + *m* log *n*) = *O*(*m* log *n*). ∎

Batas ini berlaku untuk tumpukan biner dengan antrean berisi sisi (3.2.3). Rumusan berbasis simpul dengan *decrease-key* pada *Fibonacci heap* menghasilkan *O*(*m* + *n* log *n*) (subbab 1.1), tetapi batas tersebut tidak berlaku untuk kode yang ditulis dalam laporan ini.

---

### 3.4.5 Algoritma Borůvka

---

Batas banyaknya putaran dibuktikan lebih dulu, lalu biaya satu putaran.

**Lemma 3.2.** Pada graf terhubung, *Pseudocode* 3.4 berhenti setelah paling banyak ⌈log₂ *n*⌉ putaran.

*Bukti.* Misalkan sebuah putaran dimulai dengan *c* ≥ 2 komponen. Karena graf terhubung, setiap komponen memiliki sedikitnya satu sisi yang keluar dari komponen itu, sehingga *T* memuat satu sisi untuk setiap komponen. Sisi yang dipilih komponen *r* menghubungkan *r* dengan komponen lain *r′*. Pada baris 10 sampai 13, sisi itu diproses oleh GABUNG. GABUNG berhasil menyatukan keduanya, atau mengembalikan SALAH karena keduanya sudah disatukan lebih dulu pada putaran yang sama. Dalam kedua kasus, *r* dan *r′* berakhir pada komponen yang sama. Jadi setiap komponen pada akhir putaran memuat sedikitnya dua komponen awal putaran, sehingga *c* paling banyak menjadi ⌊*c*/2⌋. Setelah *k* putaran, jumlah komponen paling banyak *n*/2^*k*, yang bernilai 1 atau kurang untuk *k* = ⌈log₂ *n*⌉. ∎

**Teorema 3.7.** *Pseudocode* 3.4 berjalan dalam waktu *O*(*m* log² *n*).

*Bukti.* Baris 1 berbiaya *O*(*n*). Satu putaran terdiri atas dua bagian. Bagian pemilihan (baris 4 sampai 8) memproses *m* sisi, masing-masing dengan dua CARI-AKAR berbiaya *O*(log *n*) menurut Teorema 3.4 dan sejumlah perbandingan κ berbiaya *O*(1), sehingga berbiaya *O*(*m* log *n*). Bagian pemasangan (baris 10 sampai 13) memproses paling banyak satu sisi untuk setiap komponen, yaitu paling banyak *n* sisi, masing-masing satu GABUNG berbiaya *O*(log *n*), sehingga berbiaya *O*(*n* log *n*) = *O*(*m* log *n*). Satu putaran berbiaya *O*(*m* log *n*). Menurut Lemma 3.2 terdapat paling banyak ⌈log₂ *n*⌉ = *O*(log *n*) putaran, sehingga totalnya *O*(*m* log² *n*). ∎

Batas ini lebih besar satu faktor log *n* daripada *O*(*m* log *n*) yang disebut pada 2.4. Perbedaannya berasal dari cara komponen ditentukan. Rumusan pada pustaka menganggap komponen setiap simpul tersedia dalam waktu *O*(1), sehingga satu putaran berbiaya *O*(*m*) (subbab 2.4). Kode yang ditulis menentukan komponen dengan CARI-AKAR yang berbiaya *O*(log *n*) menurut batas yang dibuktikan di sini. Jika komponen disimpan sebagai label yang diperbarui pada setiap putaran, batas pustaka *O*(*m* log *n*) dapat dicapai, tetapi itu bukan kode yang diukur pada Bab 4. Batas *O*(*m* log² *n*) adalah batas atas yang dapat dibuktikan untuk kode ini. Kode ini mungkin lebih cepat dalam praktik karena pemendekan lintasan meratakan pohon, tetapi laporan ini tidak membuktikan hal tersebut. Bab 4 membandingkan kurva pengukuran dengan *O*(*m* log *n*) dan *O*(*m* log² *n*).

---

### 3.4.6 Kompleksitas Ruang

---

**Teorema 3.8.** Ruang yang dipakai ketiga algoritma, di luar masukan, adalah *O*(*n* + *m*) untuk Kruskal dan Prim, dan *O*(*n*) untuk Borůvka.

*Bukti.* Kruskal menyimpan salinan terurut *E′* sebanyak *m* elemen (baris 1), struktur *disjoint set* dengan dua larik berukuran *n*, dan *A* dengan paling banyak *n* − 1 elemen, sehingga ruangnya *O*(*n* + *m*). Prim menyimpan *Adj* dengan 2*m* entri dan *n* daftar, larik `masuk` berukuran *n*, *A* dengan paling banyak *n* − 1 elemen, dan *Q* dengan paling banyak *m* elemen (Lemma 3.1), sehingga ruangnya *O*(*n* + *m*). Borůvka menyimpan struktur *disjoint set* berukuran *n*, kamus *T* dengan paling banyak satu entri untuk setiap akar sehingga paling banyak *n* entri, dan *A* dengan paling banyak *n* − 1 elemen, sehingga ruang tambahannya *O*(*n*). Daftar sisi masukan *E* sebanyak *m* tidak disalin. ∎

---

### 3.4.7 Ringkasan dan Substitusi ke Kasus Analisis

---

Hasil 3.4.3 sampai 3.4.6 dirangkum pada Tabel 3.7.

**Tabel 3.7** Ringkasan batas atas kompleksitas (graf terhubung, *n* ≥ 2)

| Algoritma | Waktu | Ruang tambahan | Dasar |
|---|---|---|---|
| Kruskal | *O*(*m* log *n*) | *O*(*n* + *m*) | Teorema 3.5 dan 3.8 |
| Prim (tumpukan biner, antrean berisi sisi) | *O*(*m* log *n*) | *O*(*n* + *m*) | Teorema 3.6 dan 3.8 |
| Borůvka (seperti yang ditulis) | *O*(*m* log² *n*) | *O*(*n*) | Teorema 3.7 dan 3.8 |

Kasus analisis didefinisikan menurut kepadatan graf pada Tabel 2.2, sehingga batas pada Tabel 3.7 dihitung dengan mensubstitusikan nilai *m* ke dalamnya, dan hasilnya disajikan pada Tabel 3.8. Pada kasus rata-rata, *m* = Θ(*n* log *n*) sehingga log *m* = Θ(log *n*), dan substitusi memberi *m* log *n* = *O*(*n* log² *n*). Substitusi ini adalah batas atas kepadatan menengah yang dipilih sebagai wakil (2.3), bukan nilai harapan waktu berjalan.

**Tabel 3.8** Substitusi nilai *m* menurut Tabel 2.2

| Kasus | Nilai *m* | Kruskal | Prim | Borůvka | Ruang Kruskal dan Prim | Ruang Borůvka |
|---|---|---|---|---|---|---|
| Terbaik | *n* − 1 | *O*(*n* log *n*) | *O*(*n* log *n*) | *O*(*n* log² *n*) | *O*(*n*) | *O*(*n*) |
| Rata-rata | Θ(*n* log *n*) | *O*(*n* log² *n*) | *O*(*n* log² *n*) | *O*(*n* log³ *n*) | *O*(*n* log *n*) | *O*(*n*) |
| Terburuk | Θ(*n*²) | *O*(*n*² log *n*) | *O*(*n*² log *n*) | *O*(*n*² log² *n*) | *O*(*n*²) | *O*(*n*) |

Kruskal dan Prim memiliki batas atas yang sama pada ketiga kasus. Notasi *O* tidak membedakan keduanya, dan selisih di antara keduanya baru tampak pada faktor konstanta yang diukur di Bab 4 (lihat 3.5).

---

## 3.5 Perbandingan dan Evaluasi Kritis

---

### 3.5.1 Perbandingan Strategi dan Biaya

---

**Tabel 3.9** Perbandingan Kruskal, Prim, dan Borůvka menurut implementasi dalam laporan ini

| Aspek | Kruskal | Prim | Borůvka |
|---|---|---|---|
| Struktur yang ditumbuhkan | Hutan | Satu pohon dari simpul awal | Hutan, semua komponen tumbuh serentak per putaran |
| Sisi yang dipilih | Sisi terkecil menurut κ yang menghubungkan dua pohon berbeda | Sisi terkecil menurut κ yang meninggalkan pohon | Sisi terkecil menurut κ yang keluar dari setiap komponen |
| Struktur data | *Disjoint set* dan pengurutan seluruh sisi | Antrean prioritas berisi sisi (`heapq`) | *Disjoint set* dan kamus pilihan per komponen |
| Representasi graf | Daftar sisi | Daftar ketetanggaan | Daftar sisi |
| Pekerjaan per sisi | Satu GABUNG pada sisi yang diperiksa | Satu MASUKKAN, dan satu KELUARKAN-TERKECIL bila sisi sampai terambil | Dua CARI-AKAR per sisi pada setiap putaran |
| Waktu (Tabel 3.7) | *O*(*m* log *n*) | *O*(*m* log *n*) | *O*(*m* log² *n*) |
| Ruang tambahan | *O*(*n* + *m*) | *O*(*n* + *m*) | *O*(*n*) |
| Bukti kebenaran | Formal (Teorema 3.1) | Formal (Teorema 3.2) | Tidak formal (butir 2 subbab 1.4) |

Dua fakta tentang jumlah pekerjaan per sisi melengkapi Tabel 3.9 dan menunjukkan mengapa notasi *O* tidak memisahkan Kruskal dari Prim.

**Prim memasukkan tepat *m* entri ke antrean.** Lemma 3.1 menunjukkan bahwa setiap sisi dimasukkan paling banyak satu kali. Pada graf terhubung, seluruh simpul akhirnya masuk pohon, dan ujung sebuah sisi yang masuk lebih dulu memasukkan sisi itu ke antrean. Jadi setiap sisi dimasukkan tepat satu kali, dan jumlah MASUKKAN selalu *m*, sedangkan jumlah KELUARKAN-TERKECIL berada di antara *n* − 1 dan *m*. Selisihnya dengan *n* − 1 adalah jumlah entri usang yang dibuang pada baris 7.

**Kruskal memeriksa sisi sampai sisi terberat MST.** Sisi diterima menurut urutan κ dan perulangan berhenti pada penerimaan sisi ke-(*n* − 1), yaitu sisi MST dengan κ terbesar. Jumlah sisi yang diperiksa pada perulangan sama dengan urutan sisi itu dalam daftar terurut, sehingga berada di antara *n* − 1 dan *m*. Pengurutan pada baris 1 tetap mencakup seluruh *m* sisi.

Akibat kedua fakta ini, pada graf yang mana pun, Kruskal dan Prim sama-sama memproses sisi dalam jumlah yang berorde *m*, dan batas atasnya sama (Tabel 3.7). Selisih waktu di antara keduanya hanya dapat berasal dari faktor konstanta, yaitu biaya satu GABUNG dibandingkan biaya satu MASUKKAN dan KELUARKAN-TERKECIL, serta biaya pembuatan daftar ketetanggaan pada Prim. Faktor konstanta tidak dapat ditentukan dari analisis asimtotik dan diukur pada Bab 4.

---

### 3.5.2 Kelebihan, Keterbatasan, dan Kesesuaian

---

**Kruskal.** Kelebihannya adalah masukan berupa daftar sisi langsung dapat diproses tanpa membangun struktur graf lain, dan algoritmanya sederhana karena seluruh keputusan berada pada satu urutan sisi. Keterbatasannya ada tiga. Seluruh sisi harus tersedia dan diurutkan lebih dulu, sehingga algoritma tidak dapat mulai sebelum semua sisi dikenal. Salinan terurut membuat ruang tambahannya *O*(*n* + *m*). Terakhir, penghentian dini tidak mengurangi biaya pengurutan, sebagaimana dibahas pada 3.4.3. Algoritma ini cocok bila graf sudah berupa daftar sisi, misalnya daftar jalur kabel beserta biayanya, dan bila graf cukup jarang sehingga *m* kecil.

**Prim.** Kelebihannya adalah pohon tumbuh dari satu simpul dan sisi dipilih dari batas pohon, sehingga algoritma ini alami bila graf sudah tersedia sebagai daftar ketetanggaan. Keterbatasannya berasal dari pilihan implementasi. Antrean menyimpan sisi dan memuat entri usang (3.2.3), sehingga ruangnya mencapai *O*(*m*) dan batas waktunya *O*(*m* log *n*), bukan batas rumusan berbasis simpul (3.4.4). Jika graf tersedia sebagai daftar sisi, daftar ketetanggaan harus dibangun lebih dulu dengan biaya *O*(*n* + *m*) dan ruang tambahan 2*m* entri.

**Borůvka.** Kelebihannya adalah strukturnya berputaran, sehingga pemilihan sisi tiap komponen pada satu putaran saling bebas dan secara konsep mudah diparalelkan (subbab 2.4, yang berada di luar batasan laporan ini). Ruang tambahannya paling kecil, yaitu *O*(*n*). Keterbatasan pada implementasi ini ada dua. Pertama, kode tidak melakukan kontraksi (varian pada 2.4), sehingga setiap putaran memindai seluruh *m* sisi termasuk sisi yang kedua ujungnya sudah berada dalam satu komponen (baris 6 pada *Pseudocode* 3.4). Kedua, komponen ditentukan dengan CARI-AKAR, sehingga batas yang dapat dibuktikan adalah *O*(*m* log² *n*), satu faktor log *n* di atas batas pustaka (3.4.5). Algoritma ini dipilih sebagai pembanding karena strateginya berbeda, bukan karena diharapkan lebih cepat pada kode ini.

**Kesesuaian untuk studi kasus.** Studi kasus pada Bab 4 adalah jaringan kabel antar lima gedung, yaitu graf dengan *n* = 5 dan *m* paling banyak 10. Pada ukuran sekecil itu perbedaan orde pertumbuhan tidak berarti, dan ketiga algoritma menghasilkan himpunan sisi yang sama karena memakai aturan pemutus seri yang sama (Teorema 3.3). Pilihan di antara ketiganya ditentukan oleh bentuk data. Daftar jalur beserta biayanya sudah berbentuk daftar sisi, sehingga Kruskal paling langsung dipakai. Ada pula keterbatasan yang berasal dari modelnya, bukan dari algoritmanya. MST meminimalkan total biaya, tetapi hasilnya berupa pohon, sehingga putusnya satu jalur memutus jaringan, dan MST tidak memperhitungkan syarat lain seperti cadangan jalur atau kondisi medan. Jika syarat itu penting, masalahnya bukan lagi MST murni.

---

### 3.5.3 Alternatif

---

Laporan ini membatasi alternatif pada yang sudah dibahas pada subbab sebelumnya. Untuk Prim, rumusan berbasis simpul dengan *Fibonacci heap* memberi batas yang lebih kecil (3.4.4; Osipov *et al.*, 2009; Sanders *et al.*, 2019, Bagian 11.2), tetapi tidak dapat dibangun langsung dari `heapq`. Filter-Kruskal (Osipov *et al.*, 2009) adalah varian Kruskal yang tidak dibahas (butir 2 subbab 1.4). Untuk graf sangat besar, tersedia implementasi paralel dan terdistribusi (Fallin *et al.*, 2023; Sanders dan Schimek, 2023), yang berada di luar batasan laporan ini. Untuk graf kecil seperti studi kasus, tidak ada alasan memakai alternatif tersebut.

---

### 3.5.4 Prediksi Teoretis untuk Bab 4

---

Pengukuran pada Bab 4 hanya mencakup graf jarang, padat, dan jarang berbobot kembar (butir 5 subbab 1.4), dan hanya waktu eksekusi (butir 6), sehingga ruang hanya dianalisis secara teoretis. Karena *O* adalah batas atas (2.3), prediksi pada Tabel 3.10 dirumuskan sebagai hal yang dapat gagal, dan cara membacanya ditetapkan sebelum data diambil. Hasilnya diperiksa dengan membagi waktu terukur *T*(*n*) oleh suku batas, misalnya *T*(*n*)/(*m* log *n*). Nilai yang hampir konstan terhadap *n* berarti batas itu ketat untuk kode ini, nilai yang menurun berarti batas itu longgar, dan nilai yang naik berarti batas itu salah atau ada pengaruh lain yang belum dihitung.

**Tabel 3.10** Prediksi teoretis dan cara pengujiannya pada Bab 4

| No | Pertanyaan | Dasar | Prediksi | Pemeriksaan |
|---|---|---|---|---|
| 1 | Pertumbuhan Kruskal dan Prim | Teorema 3.5 dan 3.6 | *T* tidak tumbuh lebih cepat daripada *m* log *n*, yaitu *n* log *n* pada graf jarang dan *n*² log *n* pada graf padat | *T*/(*m* log *n*) terhadap *n* |
| 2 | Pertumbuhan Borůvka | Teorema 3.7 | *T* tidak tumbuh lebih cepat daripada *m* log² *n*, dan dapat berada di antara *m* log *n* dan *m* log² *n* | *T*/(*m* log *n*) dan *T*/(*m* log² *n*) |
| 3 | Mana yang lebih cepat, Kruskal atau Prim | Tabel 3.7 tidak membedakan | Tidak ada prediksi dari analisis asimtotik. Osipov *et al.* (2009) melaporkan Kruskal baik hingga sekitar 8*n* sisi pada C++, dan hasil itu belum tentu berlaku pada Python | Bandingkan keduanya pada graf jarang dan padat. Dua kepadatan tidak cukup untuk menetapkan titik silang |
| 4 | Biaya daftar ketetanggaan | *Pseudocode* 3.3 | Prim dengan pembuatan *Adj* lebih lambat daripada tanpa pembuatan *Adj* sebesar suku *O*(*n* + *m*) | Ukur Prim tanpa dan dengan pembuatan *Adj* (3.2.3) |
| 5 | Pengaruh bobot kembar | κ mengurutkan seluruh sisi secara total | Batas waktu tidak berubah. Total bobot ketiga algoritma sama | Bandingkan waktu pada graf jarang berbobot kembar, total bobot pada setiap ulangan, dan himpunan sisi pada graf kecil berbobot kembar |
| 6 | Kesamaan keluaran | Teorema 3.3 (Kruskal dan Prim), tanpa bukti untuk Borůvka | Total bobot ketiga algoritma sama pada graf eksperimen, dan himpunan sisi sama pada graf kecil. Kruskal sama dengan Prim menurut Teorema 3.3, dan Borůvka diharapkan sama | Bandingkan total bobot pada setiap ulangan graf eksperimen dan himpunan sisi pada kasus uji kecil. Himpunan sisi pada graf eksperimen tidak dibandingkan. Kesamaan pada data bukan bukti untuk Borůvka |

Jika pengukuran tidak sesuai dengan salah satu prediksi, ketidaksesuaian itu dilaporkan dan dibahas pada Bab 4, bukan disesuaikan.
