# BAB 1 PENDAHULUAN

---

## 1.1 Latar Belakang

---

Dalam teori graf dan optimasi kombinatorial, *minimum spanning tree* (MST) merupakan salah satu masalah paling mendasar. Diberikan graf tak berarah, terhubung, dan berbobot, MST adalah himpunan sisi yang menghubungkan seluruh simpul tanpa membentuk siklus dengan total bobot sekecil mungkin. Masalah ini dibahas dalam bab tersendiri pada buku teks algoritma, misalnya Bab 11 pada Sanders *et al.* (2019).

Kegunaan MST sudah tampak sejak algoritmanya dirumuskan. Prim (1957) menyebut bahwa masalah ini muncul dalam perencanaan jaringan komunikasi, distribusi, dan transportasi berskala besar. Hingga kini, MST menjadi komponen dasar pada analisis jaringan, dan juga dipakai pada desain *chip*, pelacakan mata (*eye tracking*), perencanaan rute, serta diagnostik medis seperti pengenalan tumor (Fallin *et al.*, 2023). Di luar bidang tersebut, MST menjadi representasi data pada banyak tugas pengenalan pola dan relatif cepat dihitung (Gagolewski *et al.*, 2025). Penerapannya mencakup *clustering*, segmentasi citra, dan desain jaringan (Sanders dan Schimek, 2023), serta deteksi anomali dan optimasi jaringan pada data berukuran besar (Almansoori *et al.*, 2025).

Dua solusi klasik untuk MST adalah algoritma Kruskal dan algoritma Prim. Kruskal (1956) mengusulkan algoritma untuk menemukan MST pada suatu graf, dan setahun kemudian Prim (1957) menerbitkan algoritma yang kini membawa namanya. Algoritma ini juga dikenal sebagai Jarník-Prim (Osipov *et al.*, 2009), dan selanjutnya laporan ini menyebutnya Prim. Keduanya tergolong algoritma *greedy* (Fallin *et al.*, 2023), tetapi cara kerjanya berbeda. Kruskal menumbuhkan sebuah hutan dengan memindai sisi, sedangkan Prim menumbuhkan satu pohon mulai dari simpul sembarang (Osipov *et al.*, 2009).

Meskipun keduanya menghasilkan MST, biaya komputasinya tidak sama pada setiap graf. Misalkan graf memiliki *n* simpul dan *m* sisi. Prim dengan antrean prioritas yang efisien berjalan dalam waktu *O*(*m* + *n* log *n*), sedangkan Kruskal berjalan dalam waktu *O*((*m* + *n*) log *m*) (Osipov *et al.*, 2009). Batas untuk Prim dicapai, misalnya, dengan *Fibonacci heap* (Sanders *et al.*, 2019, Bagian 11.2). Implementasi dalam laporan ini memakai *binary heap*, sehingga batas yang berlaku untuk Prim adalah *O*(*m* log *n*), dan penurunannya dibahas di Bab 3. Karena itu, kepadatan graf dan pilihan struktur data menjadi penentu. Percobaan Osipov *et al.* (2009) dengan implementasi C++ pada graf acak berbobot acak menunjukkan bahwa Kruskal bekerja baik hingga sekitar 8*n* sisi, sedangkan Prim lebih unggul pada graf yang cukup padat untuk ukuran graf yang diuji. Hasil ini belum tentu berlaku untuk implementasi dalam laporan ini.

Batas asimtotik saja belum cukup untuk menentukan algoritma yang lebih baik dalam praktik, sebab waktu eksekusi nyata juga dipengaruhi detail implementasi. Penelitian pada GPU menunjukkan hal ini: ECL-MST, yang memparalelkan algoritma Kruskal, dilaporkan lebih dari 8 kali lebih cepat daripada versi dasarnya tanpa delapan optimasi yang dievaluasi (Fallin *et al.*, 2023). Konteks paralel itu berbeda dari implementasi sekuensial dalam laporan ini, tetapi menunjukkan bahwa detail implementasi dapat memengaruhi kinerja secara nyata. Karena itu, analisis teoretis perlu dilengkapi pengukuran empiris yang dibandingkan langsung dengan kurva kompleksitasnya.

Berdasarkan uraian tersebut, laporan ini menganalisis algoritma Kruskal dan Prim secara formal, mencakup bukti kebenaran serta penurunan kompleksitas waktu dan ruang pada kasus terbaik, rata-rata, dan terburuk. Analisis itu kemudian diuji melalui eksperimen pada graf jarang dan padat dengan ukuran input bervariasi, lalu hasilnya dibandingkan dengan satu algoritma pembanding ketiga, yaitu algoritma Borůvka (Nešetřil *et al.*, 2001).

---

## 1.2 Definisi Formal Masalah

---

Secara sederhana, masalah MST dapat dibayangkan sebagai mencari cara termurah untuk menghubungkan sejumlah kota dengan jalur kabel. Kota berperan sebagai simpul, jalur kabel yang mungkin dibangun sebagai sisi, dan biaya pembangunan sebagai bobot.

Secara formal, diberikan graf tak berarah dan terhubung *G* = (*V*, *E*), dengan *V* himpunan simpul, *E* himpunan sisi, dan *w* : *E* → ℝ fungsi yang memberi setiap sisi *e* sebuah bobot bilangan real *w*(*e*). *Spanning tree* dari *G* adalah himpunan sisi *T* ⊆ *E* yang menghubungkan seluruh simpul tanpa membentuk siklus, dan *minimum spanning tree* adalah *spanning tree* dengan total bobot terkecil (Sanders *et al.*, 2019, Bab 11; Nešetřil *et al.*, 2001). Total bobot sebuah *spanning tree* adalah

*w*(*T*) = Σ *w*(*e*), dengan penjumlahan atas semua *e* ∈ *T*. (1)

*Minimum spanning tree* adalah *spanning tree* *T*\* yang memenuhi

*w*(*T*\*) ≤ *w*(*T*), untuk setiap *spanning tree* *T* dari *G*. (2)

Dengan notasi tersebut, masalah MST dirumuskan sebagai berikut.

**Masukan:** graf tak berarah dan terhubung *G* = (*V*, *E*) dengan fungsi bobot *w* : *E* → ℝ.

**Keluaran:** sebuah *spanning tree* *T*\* dari *G* dengan *w*(*T*\*) minimum.

Ukuran input dinyatakan dengan *n* = |*V*| dan *m* = |*E*|. Setiap *spanning tree* memiliki tepat *n* − 1 sisi, dan *m* ≤ *n*(*n* − 1)/2 untuk graf tanpa sisi ganda dan tanpa *loop*. Selain itu, *m* ≥ *n* − 1 karena *G* terhubung. Graf disebut jarang jika *m* = Θ(*n*), padat jika *m* = Θ(*n*²), dan berkepadatan menengah jika *m* = Θ(*n* log *n*). Ketiga tingkat kepadatan ini dipakai pada subbab 2.3 untuk mendefinisikan kasus terbaik, rata-rata, dan terburuk.

Karena *G* terhubung, *G* memiliki sedikitnya satu *spanning tree*, sehingga MST selalu ada. Bobot sisi boleh bernilai sama. Dalam kasus ini MST dapat lebih dari satu, tetapi seluruhnya memiliki total bobot yang sama.

---

## 1.3 Tujuan

---

Berdasarkan latar belakang dan definisi masalah di atas, tujuan kajian ini adalah sebagai berikut.

1. Menjelaskan prinsip kerja algoritma Kruskal dan Prim beserta *pseudocode* dan contoh perhitungan manualnya sebagai penerapan paradigma *greedy* pada masalah MST.
2. Membuktikan bahwa algoritma Kruskal dan Prim selalu menghasilkan *minimum spanning tree* pada graf tak berarah, terhubung, dan berbobot.
3. Menurunkan kompleksitas waktu dan ruang kedua algoritma secara formal pada kasus terbaik, rata-rata, dan terburuk.
4. Mengimplementasikan algoritma Kruskal dan Prim serta algoritma Borůvka sebagai pembanding, memvalidasi kebenarannya melalui kasus uji kecil yang hasilnya dapat diperiksa secara manual, serta menerapkannya pada satu studi kasus jaringan kabel antar gedung di Fakultas Teknik Universitas Hasanuddin.
5. Mengukur waktu eksekusi ketiga algoritma pada graf jarang dan padat dengan berbagai ukuran input, lalu membandingkan hasilnya satu sama lain dan dengan kurva kompleksitas teoretis.
6. Mengevaluasi kelebihan, keterbatasan, kesesuaian, dan alternatif algoritma berdasarkan hasil analisis dan eksperimen.

---

## 1.4 Batasan Penelitian

---

Ruang lingkup kajian ini dibatasi sebagai berikut.

1. Masalah yang dikaji adalah MST pada graf tak berarah, terhubung, dan berbobot bilangan real, tanpa sisi ganda dan tanpa *loop*. Graf tak terhubung, yang menghasilkan *minimum spanning forest*, tidak dibahas.
2. Algoritma yang dianalisis secara formal dan diimplementasikan adalah Kruskal dengan struktur data *disjoint set* dan Prim dengan antrean prioritas berbasis *binary heap* yang menyimpan sisi kandidat. Borůvka, satu-satunya pembanding yang ditulis sendiri, hanya diimplementasikan dan dibandingkan secara empiris. Batas kompleksitasnya dikutip dari literatur dan diturunkan secara singkat untuk keperluan kurva teoretis, tanpa bukti kebenaran formal. Varian lain seperti Filter-Kruskal, serta versi paralel dan dinamis tidak dibahas.
3. Implementasi ditulis dalam Python dan berjalan secara sekuensial. Logika inti Kruskal, Prim, dan Borůvka serta *disjoint set* ditulis sendiri, sedangkan fungsi pengurutan bawaan dan modul `heapq` hanya dipakai sebagai alat bantu. Pustaka yang langsung menghasilkan MST hanya dipakai untuk verifikasi hasil.
4. Graf masukan untuk Kruskal dan Borůvka direpresentasikan sebagai daftar sisi, sedangkan untuk Prim sebagai daftar ketetanggaan.
5. Data uji pengukuran waktu berupa graf acak sintetis yang dibangkitkan dengan *seed* tetap dan dijamin terhubung, pada kondisi jarang, padat, dan jarang berbobot kembar dengan minimal lima ukuran input per kondisi. Rentang ukuran ditetapkan di Bab 4 dengan mempertimbangkan bahwa jumlah sisi graf padat tumbuh sebesar Θ(*n*²). Studi kasus berupa satu graf kecil jaringan kabel antar lima gedung dengan data tetap, sehingga tidak memakai *seed* dan tidak dipakai untuk mengukur waktu.
6. Pengukuran empiris terbatas pada waktu eksekusi, diulang minimal lima kali per percobaan pada graf yang sama, dan dilaporkan sebagai rata-rata dan simpangan baku pada satu lingkungan perangkat keras dan perangkat lunak. Kompleksitas ruang hanya dianalisis secara teoretis.
7. Ketiga algoritma memakai aturan pemutus seri yang sama untuk sisi berbobot sama, yaitu membandingkan bobot, lalu nomor simpul ujung terkecil, lalu nomor simpul ujung terbesar, dengan simpul diberi nomor bulat tetap. Dengan aturan ini MST yang dihasilkan unik, sehingga keluaran ketiga algoritma dapat dibandingkan.

---

# Daftar Pustaka

[1] P. Sanders, K. Mehlhorn, M. Dietzfelbinger, and R. Dementiev, *Sequential and Parallel Algorithms and Data Structures: The Basic Toolbox*, 2nd ed. Cham, Switzerland: Springer, 2019, doi: 10.1007/978-3-030-25209-0.

[2] R. C. Prim, "Shortest connection networks and some generalizations," *Bell Syst. Tech. J.*, vol. 36, no. 6, pp. 1389-1401, Nov. 1957, doi: 10.1002/j.1538-7305.1957.tb01515.x.

[3] A. Fallin, A. Gonzalez, J. Seo, and M. Burtscher, "A high-performance MST implementation for GPUs," in *Proc. Int. Conf. High Perform. Comput., Netw., Storage Anal. (SC '23)*, Denver, CO, USA, Nov. 2023, doi: 10.1145/3581784.3607093.

[4] M. Gagolewski, A. Cena, M. Bartoszuk, and Ł. Brzozowski, "Clustering with minimum spanning trees: How good can it be?," *J. Classif.*, vol. 42, no. 1, pp. 90-112, 2025, doi: 10.1007/s00357-024-09483-1.

[5] P. Sanders and M. Schimek, "Engineering massively parallel MST algorithms," in *Proc. IEEE Int. Parallel Distrib. Process. Symp. (IPDPS)*, St. Petersburg, FL, USA, May 2023, pp. 691-701, doi: 10.1109/IPDPS54959.2023.00075.

[6] J. B. Kruskal, "On the shortest spanning subtree of a graph and the traveling salesman problem," *Proc. Amer. Math. Soc.*, vol. 7, no. 1, pp. 48-50, 1956, doi: 10.1090/S0002-9939-1956-0078686-7.

[7] V. Osipov, P. Sanders, and J. Singler, "The Filter-Kruskal minimum spanning tree algorithm," in *Proc. Workshop Algorithm Eng. Exp. (ALENEX)*, 2009, pp. 52-61, doi: 10.1137/1.9781611972894.5.

[8] J. Nešetřil, E. Milková, and H. Nešetřilová, "Otakar Borůvka on minimum spanning tree problem: Translation of both the 1926 papers, comments, history," *Discrete Math.*, vol. 233, no. 1-3, pp. 3-36, 2001, doi: 10.1016/S0012-365X(00)00224-7.

[9] M. K. M. Almansoori, A. Meszaros, and M. Telek, "Fast and memory-efficient approximate minimum spanning tree generation for large datasets," *Arab. J. Sci. Eng.*, vol. 50, no. 2, pp. 1233-1246, 2025, doi: 10.1007/s13369-024-08974-y.
