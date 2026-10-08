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

Seluruh panjang pada Tabel 4.1 berbeda, sehingga MST pada graf ini tunggal dan kunci pemutus seri pada Persamaan (6) tidak pernah dipakai. Kruskal mengurutkan sisi secara menaik lalu menerima sisi Sipil dan Industri (20), Elektro dan Geologi (30), serta Arsitektur dan Sipil (40). Sisi Arsitektur dan Elektro (50) juga diterima karena menghubungkan dua komponen yang berbeda, yaitu {Arsitektur, Sipil, Industri} dan {Elektro, Geologi}. Sisi Sipil dan Elektro (60) serta Industri dan Geologi (80) ditolak karena menutup siklus.

**Tabel 4.2** Hasil ketiga algoritma pada studi kasus

| Algoritma | Jumlah sisi | Total (m) |
|---|---|---|
| Kruskal | 4 | 140 |
| Prim | 4 | 140 |
| Borůvka | 4 | 140 |

Ketiga algoritma menghasilkan empat sisi, sesuai banyaknya sisi pohon rentang untuk lima simpul, dengan total 140 m. Karena MST pada graf ini tunggal, total yang sama berarti himpunan sisinya juga sama.

Dengan hanya lima simpul, studi kasus ini membuktikan kebenaran keluaran dan kegunaan MST, tetapi tidak dapat dipakai menilai efisiensi. Perbandingan waktu terhadap ukuran masukan dibahas pada eksperimen sintetis di subbab berikutnya.

---

## 4.2 Lingkungan dan Rancangan Eksperimen

---

Seluruh pengukuran dijalankan pada satu sesi Google Colab versi gratis (*free tier*), yaitu mesin virtual yang dipakai bersama pengguna lain. Spesifikasinya dicatat oleh program pada awal sesi dan disajikan pada Tabel 4.3. Kapasitas memori tidak dicatat dan karena itu tidak dilaporkan. Spesifikasi mesin virtual dapat berbeda antar sesi, sehingga seluruh angka pada laporan ini berasal dari satu sesi yang sama dan tidak dicampur dengan sesi lain.

**Tabel 4.3** Lingkungan uji

| Komponen | Keterangan |
|---|---|
| Platform | Google Colab versi gratis (mesin virtual bersama) |
| Prosesor | Intel(R) Xeon(R) CPU @ 2.20GHz, 2 CPU |
| Sistem operasi | Linux 6.6.122+ |
| Python | 3.13.16 |
| Pustaka | pandas 2.2.3, numpy 2.1.3 |
| Pengukur waktu | `time.perf_counter()` |
| Eksekusi | sekuensial |

Pengukuran memakai tiga skenario graf (Tabel 4.4). Graf padat diberi ukuran lebih kecil karena jumlah sisinya tumbuh sebesar Θ(*n*²) (butir 5 subbab 1.4), sehingga jumlah sisi pada kedua kepadatan berada pada rentang yang sebanding, yaitu sekitar 10⁴ sampai 2,5 × 10⁵. Skenario ketiga memakai bentuk graf yang sama dengan skenario pertama, tetapi bobotnya hanya bilangan bulat 1 sampai 5 sehingga banyak sisi berbobot sama.

**Tabel 4.4** Skenario pengukuran

| Skenario | Jumlah sisi *m* | Ukuran *n* | Rentang *m* | Bobot |
|---|---|---|---|---|
| jarang | 3*n* | 4000, 8000, 16000, 32000, 64000 | 12000 sampai 192000 | bilangan bulat acak 1 sampai 1000000 |
| padat | *n*(*n* − 1)/4 (separuh sisi maksimum) | 200, 400, 600, 800, 1000 | 9950 sampai 249750 | bilangan bulat acak 1 sampai 1000000 |
| jarang_kembar | 3*n* | 4000, 8000, 16000, 32000, 64000 | 12000 sampai 192000 | bilangan bulat acak 1 sampai 5 |

Graf dibangkitkan dengan `random.Random` ber-*seed* 2026. Pembangkit membentuk pohon acak terlebih dahulu, dengan setiap simpul dihubungkan ke satu simpul bernomor lebih kecil, sehingga graf pasti terhubung. Sisi acak lalu ditambahkan tanpa sisi ganda dan tanpa *loop* sampai jumlah sisi terpenuhi. Pemeriksaan pada ukuran terkecil tiap skenario menunjukkan graf terhubung, tanpa sisi ganda, dan tanpa *loop*.

Untuk setiap pasangan skenario dan ukuran, satu graf dibangkitkan dan ketiga algoritma dijalankan pada graf yang sama. Satu putaran pemanasan dijalankan lebih dahulu dan tidak dicatat, lalu pengukuran diulang lima kali pada graf yang sama. Waktu diambil dengan `time.perf_counter()` hanya di sekitar pemanggilan algoritma, setelah `gc.collect()`, dan pengumpul sampah tetap aktif selama pengukuran. Kruskal dan Borůvka menerima daftar sisi, sedangkan Prim menerima daftar ketetanggaan (butir 4 subbab 1.4). Waktu Prim dicatat dua kali, yaitu waktu inti dan waktu yang ditambah pembuatan daftar ketetanggaan. Pada setiap ulangan, total bobot ketiga algoritma dibandingkan dan program berhenti jika ada yang berbeda. Hasil dilaporkan sebagai rata-rata dan simpangan baku sampel (pembagi *n* − 1).

Kebenaran kode diperiksa sebelum pengukuran. Empat kasus uji kecil lolos pada ketiga algoritma, yaitu tiga graf terhubung dengan total 7, 3, dan 6 serta satu graf tak terhubung yang harus menghasilkan `ValueError`. Total bobot ketiga algoritma juga sama dengan `networkx` pada 300 graf acak kecil, dan `networkx` hanya dipakai sebagai pembanding, tidak di dalam algoritma (butir 3 subbab 1.4).

Rancangan ini memiliki beberapa keterbatasan. Pertama, kelima ulangan memakai graf yang sama, sehingga simpangan baku hanya mengukur gangguan waktu pada mesin, bukan variasi antar graf. Kedua, mesin virtual dipakai bersama sehingga gangguan itu besar. Simpangan baku mencapai sekitar 57% dari rata-rata pada satu titik (Borůvka, skenario jarang, *n* = 16000) dan 20% sampai 30% pada banyak ukuran dengan *n* ≥ 16000, sehingga selisih waktu yang kecil tidak ditafsirkan. Ketiga, urutan eksekusi dalam setiap ulangan tetap, yaitu pembuatan daftar ketetanggaan, Kruskal, Prim, lalu Borůvka. Keempat, pencocokan berkas `.py` dengan kode notebook dilewati di Colab, sehingga kode yang diukur adalah kode di dalam notebook.
