# BAB 4 HASIL DAN PEMBAHASAN

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
