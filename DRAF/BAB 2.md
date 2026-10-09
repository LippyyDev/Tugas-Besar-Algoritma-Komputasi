# BAB 2 LANDASAN TEORI

---

## 2.1 Paradigma Desain *Greedy*

---

### 2.1.1 Sifat *Greedy-Choice* dan *Optimal Substructure*

Algoritma *greedy* adalah strategi penyelesaian masalah yang memeriksa unsur-unsur masalah dalam suatu urutan, dan keputusan tentang suatu unsur diambil pada saat unsur itu diperiksa. Keputusan yang sudah diambil tidak pernah dibatalkan (Sanders *et al.*, 2019, Bab 12). Pada umumnya strategi ini hanya menghasilkan solusi yang suboptimal. Pada beberapa masalah, termasuk MST dan lintasan terpendek dengan bobot tak negatif, pendekatan *greedy* menghasilkan solusi optimal (Sanders *et al.*, 2019, Bab 12). Masalah yang dapat diselesaikan secara *greedy* memiliki dua sifat utama, yaitu *greedy-choice* dan *optimal substructure* (MIT OpenCourseWare, 2015).

Sifat *greedy-choice* berarti pilihan yang optimal secara lokal menuntun ke solusi yang optimal secara global (MIT OpenCourseWare, 2015). Kebenaran pilihan *greedy* harus dibuktikan. Pada MST, pembuktiannya memakai argumen *cut and paste* yang lazim pada bukti algoritma *greedy* (MIT OpenCourseWare, 2015), yaitu menukar sebagian solusi optimal dengan pilihan *greedy* tanpa menambah biaya. Argumen penukaran yang sama dipakai untuk membuktikan *cut property* (Sanders *et al.*, 2019, Bagian 11.1).

Suatu masalah memiliki *optimal substructure* jika solusi optimalnya tersusun dari solusi optimal submasalahnya. Pada pemrograman dinamis, sifat ini dikenal sebagai prinsip optimalitas, dan algoritmanya menyusun tabel solusi optimal untuk submasalah dari yang terkecil, lalu menggabungkannya menjadi solusi masalah yang lebih besar (Sanders *et al.*, 2019, Bab 12). Sebaliknya, algoritma *greedy* memutuskan setiap unsur saat unsur itu diperiksa dan tidak membatalkannya (Sanders *et al.*, 2019, Bab 12).

Kedua sifat tersebut dapat ditunjukkan pada masalah MST (MIT OpenCourseWare, 2015). Untuk *optimal substructure*, dengan submasalah didefinisikan sebagai graf hasil kontraksi, sisi *e* dari suatu MST dikontraksi dengan menggabungkan kedua simpul ujungnya. Jika *T'* adalah MST dari graf hasil kontraksi, maka *T'* ditambah *e* adalah MST dari graf semula (MIT OpenCourseWare, 2015). Untuk *greedy-choice*, pada setiap potongan (*cut*) graf, sisi berbobot terkecil yang melintasi potongan tersebut termasuk dalam suatu MST (MIT OpenCourseWare, 2015; Sanders *et al.*, 2019, Lemma 11.1). Buktinya dengan argumen *cut and paste*, yaitu menukar sisi lain yang melintasi potongan dengan sisi tersebut tanpa menambah total bobot (MIT OpenCourseWare, 2015). Sifat *greedy-choice* ini menjadi dasar algoritma Prim dan Kruskal, yang menjaga agar himpunan sisi terkumpul selalu menjadi bagian dari suatu MST (MIT OpenCourseWare, 2015; Sanders *et al.*, 2019, Bagian 11.2 dan 11.3). Bukti kebenaran keduanya dibahas di Bab 3.

---

### 2.1.2 Penerapan pada MST: Strategi Kruskal (Hutan) dan Prim (Satu Pohon)

Algoritma Kruskal dan Prim memakai pendekatan *greedy* yang sama untuk masalah MST, tetapi keduanya menerapkannya dengan cara berbeda. Keduanya merupakan kasus khusus dari algoritma generik yang bertumpu pada *cut property*. Algoritma generik dimulai dari himpunan sisi kosong. Selama himpunan itu belum merupakan *spanning tree*, dipilih sebuah potongan yang tidak dilintasi sisi dari himpunan tersebut, lalu sisi berbobot minimum pada potongan itu ditambahkan. Pilihan potongan yang berbeda menghasilkan algoritma yang berbeda (Sanders *et al.*, 2019, Bagian 11.1). Algoritma ini mengelola himpunan sisi *A* yang selalu termuat dalam suatu MST. Sisi yang dapat ditambahkan ke *A* tanpa melanggar sifat tersebut disebut *safe edge* dalam laporan ini.

*Safe edge* dikenali melalui konsep potongan (*cut*) dan *light edge*, yang didefinisikan secara formal pada 2.2.1. Aturannya, jika *A* termuat dalam suatu MST, maka *light edge* yang melintasi potongan yang menghormati *A* adalah *safe edge* untuk *A* (Teorema 2.1). Aturan ini berkaitan erat dengan sifat *greedy-choice* pada MST yang dibahas di 2.1.1.

Selama algoritma generik berjalan, graf (*V*, *A*) selalu berupa hutan, dan setiap komponen terhubungnya adalah sebuah pohon. Pada awalnya *A* kosong, sehingga hutan terdiri atas |*V*| pohon yang masing-masing hanya berisi satu simpul. Setiap sisi yang ditambahkan melintasi potongan yang menghormati *A*, sehingga kedua ujungnya berada pada komponen yang berbeda dan penambahannya tidak membentuk siklus. Dengan demikian, setiap iterasi mengurangi jumlah pohon sebanyak satu dan perulangan berjalan |*V*| − 1 kali. Hasil akhirnya adalah satu pohon dengan |*V*| − 1 sisi, yaitu satu komponen tanpa siklus yang memuat semua simpul. Dari aturan di atas diperoleh akibat berikut. Jika *C* adalah salah satu komponen pada (*V*, *A*) dan (*u*, *v*) adalah sisi berbobot minimum di antara sisi yang meninggalkan *C*, maka (*u*, *v*) adalah *safe edge* untuk *A*. Hal ini mengikuti Teorema 2.1, karena potongan (*C*, *V* \ *C*) menghormati *A* sebab tidak ada sisi *A* yang meninggalkan komponen *C*. Akibat inilah yang dipakai kedua algoritma untuk memilih sisi.

Pada algoritma Kruskal, *A* berupa hutan. Algoritma memindai sisi menurut urutan bobot naik dan menjaga invarian bahwa himpunan sisi yang terkumpul adalah hutan bagian dari suatu MST (Sanders *et al.*, 2019, Bagian 11.3; Kruskal, 1956). Algoritma dimulai dengan |*V*| pohon, satu untuk setiap simpul, lalu mengurutkan seluruh sisi menurut bobot tak menurun. Sisi diperiksa satu per satu. Jika kedua ujungnya sudah berada di pohon yang sama, sisi dibuang karena penambahannya membentuk siklus. Jika tidak, sisi ditambahkan ke *A* sebagai *light edge* pada potongan yang menghormati *A*, sesuai dengan *cut property*. Argumen lengkapnya dibahas pada 3.3.2. Pemeriksaan keanggotaan pohon memakai struktur data *disjoint set* (*union-find*) dengan operasi *find* dan *union* (Sanders *et al.*, 2019, Bagian 11.4). Algoritma ini tidak memerlukan representasi graf yang rumit dan dapat bekerja pada graf yang tersedia sebagai urutan sisi (Sanders *et al.*, 2019, Bagian 11.3).

Pada algoritma Prim, *A* selalu membentuk satu pohon. Pohon tumbuh dari sebuah simpul awal sembarang dengan menambahkan satu simpul demi satu simpul. Misalkan *S* adalah himpunan simpul yang sudah masuk pohon. Pada setiap iterasi, sisi berbobot minimum yang meninggalkan *S*, yaitu sisi dengan tepat satu ujung di *S*, ditambahkan ke pohon (Sanders *et al.*, 2019, Bagian 11.2; Prim, 1957). Berdasarkan akibat di atas, aturan ini hanya menambahkan *safe edge*, sehingga sisi yang terkumpul pada akhirnya membentuk MST. Agar sisi berikutnya mudah dipilih, algoritma menyimpan dalam antrean prioritas, untuk setiap simpul di luar *S*, koneksi termurah antara simpul itu dan *S* (Sanders *et al.*, 2019, Bagian 11.2). Cara kerja ini sangat mirip dengan algoritma Dijkstra untuk lintasan terpendek, dengan perbedaan bahwa antrean menyimpan biaya sisi, bukan panjang lintasan (Sanders *et al.*, 2019, Bagian 11.2). Rumusan tersebut memerlukan operasi *decrease-key* untuk menurunkan kunci simpul. Implementasi dalam laporan ini tidak memakainya dan menyimpan sisi, bukan simpul, di dalam antrean. Alasan dan akibatnya pada kompleksitas dibahas pada 3.2.3 dan 3.4.3. Kedua algoritma termasuk algoritma *greedy* (Sanders *et al.*, 2019, Bab 12) dan menjaga invarian yang sama, yaitu himpunan sisi yang terkumpul selalu merupakan bagian dari suatu MST (MIT OpenCourseWare, 2015).

Perbedaan strategi dan struktur data kedua algoritma inilah yang menentukan biaya komputasi masing-masing, dan penurunannya dibahas di Bab 3.

---

## 2.2 Landasan Matematis MST

---

### 2.2.1 *Cut*, *Light Edge*, dan *Cut Property*

Misalkan *G* = (*V*, *E*) adalah graf tak berarah dan terhubung dengan fungsi bobot *w* seperti pada 1.2. Potongan (*cut*) dari *G* adalah pembagian himpunan simpul *V* menjadi dua himpunan tak kosong (*S*, *V* \ *S*). Sebuah sisi (*u*, *v*) ∈ *E* melintasi potongan jika salah satu ujungnya berada di *S* dan ujung lainnya berada di *V* \ *S*. Himpunan sisi yang melintasi potongan dinotasikan *E*(*S*, *V* \ *S*), dan himpunan ini membentuk *cut* dalam arti himpunan sisi yang jika dihapus memutuskan *G* (Sanders *et al.*, 2019, Bagian 11.1). Karena *G* terhubung dan kedua bagian tidak kosong, himpunan ini memuat setidaknya satu sisi.

Sebuah sisi *e* ∈ *E*(*S*, *V* \ *S*) disebut *light edge* dalam laporan ini jika bobotnya minimum di antara sisi yang melintasi potongan tersebut (Sanders *et al.*, 2019, Bagian 11.1), yaitu

w(e) = min { w(f) : f ∈ E(S, V \ S) }. (3)

Jika beberapa sisi memiliki bobot minimum yang sama, potongan tersebut memiliki lebih dari satu *light edge*. Selanjutnya, suatu potongan dalam laporan ini disebut menghormati (*respects*) himpunan sisi *A* ⊆ *E* jika tidak ada sisi di *A* yang melintasi potongan tersebut, sesuai syarat pada Lemma 11.1 dalam Sanders *et al.* (2019).

Sifat yang mengaitkan potongan dengan MST disebut *cut property* (Sanders *et al.*, 2019, Bagian 11.1) atau *cut rule* (Nešetřil *et al.*, 2001, Bagian 8) dan dinyatakan dalam teorema berikut.

**Teorema 2.1 (*Cut Property*).** Misalkan *G* = (*V*, *E*) graf tak berarah, terhubung, dan berbobot real. Misalkan *A* ⊆ *E* termuat dalam suatu MST dari *G*, (*S*, *V* \ *S*) potongan yang menghormati *A*, dan (*u*, *v*) sebuah *light edge* yang melintasi potongan tersebut. Maka *A* ∪ {(*u*, *v*)} juga termuat dalam suatu MST dari *G*, atau dengan kata lain (*u*, *v*) adalah *safe edge* untuk *A* (Sanders *et al.*, 2019, Lemma 11.1).

Rumusan Teorema 2.1 dan 2.2 memakai bobot real, lebih luas daripada asumsi bobot positif pada buku tersebut. Bukti penukaran keduanya tidak memakai tanda bobot, dan masalah MST dapat diselesaikan untuk fungsi bobot apa pun, termasuk bobot negatif (Nešetřil *et al.*, 2001, Bagian 8).

Untuk *A* = ∅, setiap potongan menghormati *A*. Dalam kasus ini, teorema menyatakan bahwa setiap *light edge* pada setiap potongan termuat dalam suatu MST (Sanders *et al.*, 2019, Lemma 11.1).

Teorema ini dibuktikan dengan argumen *cut and paste*, yaitu menukar sisi pada lintasan di sebuah MST yang melintasi potongan dengan *light edge* tanpa menambah bobot (Sanders *et al.*, 2019, Lemma 11.1). Bukti lengkap dibahas pada 3.3.1.

Jika semua bobot sisi berbeda, setiap potongan hanya memiliki satu *light edge* dan *G* memiliki MST yang unik (Sanders *et al.*, 2019, Latihan 11.5; Nešetřil *et al.*, 2001, Bagian 7). Dalam kasus ini, setiap MST memuat *light edge* dari setiap potongan (Nešetřil *et al.*, 2001, Bagian 8). Pada bobot yang tidak seluruhnya berbeda, teorema hanya menjamin bahwa *light edge* termuat dalam suatu MST. Salah satu cara menangani kondisi ini adalah memakai aturan pemutus seri yang konsisten, sehingga algoritma yang mengandaikan bobot berbeda tetap dapat dijalankan (Nešetřil *et al.*, 2001, Bagian 4, catatan ⟨1⟩, hlm. 23; Sanders dan Schimek, 2023, Bagian II-C). Sifat potongan ini dipakai di Bab 3 untuk membuktikan kebenaran algoritma Kruskal dan Prim.

---

### 2.2.2 *Cycle Property*

Jika *cut property* menunjukkan sisi yang dapat dimasukkan ke dalam MST, *cycle property* menunjukkan sisi yang dapat dikeluarkan dari MST. Sifat ini dinyatakan dalam teorema berikut.

**Teorema 2.2 (*Cycle Property*).** Misalkan *G* = (*V*, *E*) graf tak berarah, terhubung, dan berbobot real. Misalkan *C* adalah sebuah siklus di *G* dan *e* adalah sisi pada *C* dengan bobot maksimum di antara semua sisi *C*. Maka setiap MST dari *G'* = (*V*, *E* \ {*e*}) juga merupakan MST dari *G* (Sanders *et al.*, 2019, Lemma 11.2). Dengan kata lain, ada MST dari *G* yang tidak memuat *e*.

Buktinya memakai argumen penukaran yang serupa dengan *cut property*, yaitu menukar sisi *e* pada sebuah MST dengan sisi lain pada siklus yang tidak lebih berat (Sanders *et al.*, 2019, Lemma 11.2). Bukti itu tidak diulang di Bab 3 karena bukti kebenaran Kruskal dan Prim hanya memakai *cut property*. Pada Kruskal, sisi yang menutup siklus dibuang sesuai dengan *cycle property* dan sisi yang menghubungkan dua komponen ditambahkan sesuai dengan *cut property* (Sanders *et al.*, 2019, Bagian 11.3), sedangkan Prim hanya menambahkan sisi berbobot minimum yang meninggalkan himpunan simpul pohon (Sanders *et al.*, 2019, Bagian 11.2).

---

### 2.2.3 Keunikan MST pada Bobot Berbeda dan Bobot Sama

Seperti disebut pada 1.2, sebuah graf dapat memiliki lebih dari satu MST. Contoh paling sederhana adalah segitiga yang ketiga sisinya berbobot 1. Setiap pasangan dari dua sisinya adalah *spanning tree* berbobot 2, sehingga graf tersebut memiliki tiga MST. Secara umum, jika seluruh sisi suatu graf berbobot 1, setiap *spanning tree* adalah MST dengan bobot |*V*| − 1, karena setiap *spanning tree* memiliki tepat |*V*| − 1 sisi (lihat 1.2). Seluruh MST dari suatu graf memiliki total bobot yang sama, yaitu bobot minimum menurut (2).

Keunikan MST terjamin jika bobot sisi berbeda, sebagaimana dinyatakan dalam teorema berikut.

**Teorema 2.3 (Keunikan MST).** Jika semua bobot sisi pada graf terhubung *G* berbeda, maka *G* memiliki tepat satu MST (Nešetřil *et al.*, 2001, Bagian 7; Sanders *et al.*, 2019, Latihan 11.5).

Teorema ini dibuktikan pada 3.3.4 dengan syarat yang lebih umum daripada bobot berbeda, yaitu setiap potongan hanya memiliki satu *light edge*. Kebalikannya tidak berlaku. Graf dengan bobot berulang tetap dapat memiliki MST yang unik, misalnya jika *G* sendiri berupa sebuah pohon, karena satu-satunya *spanning tree* dari pohon adalah pohon itu sendiri. Pada lintasan tiga simpul *a*, *b*, *c* dengan dua sisi berbobot 1, misalnya, MST-nya unik, tetapi potongan ({*a*, *c*}, {*b*}) memiliki dua *light edge*.

Jika bobot tidak berbeda, keluaran algoritma bergantung pada cara menangani sisi berbobot sama. Algoritma Kruskal dapat mengembalikan MST yang berbeda untuk graf yang sama, bergantung pada urutan sisi berbobot sama saat pengurutan. Pada segitiga berbobot sama di atas, tiga urutan yang berbeda menghasilkan tiga pohon yang berbeda. Ambiguitas ini dapat dihilangkan dengan aturan pemutus seri yang konsisten. Asumsi bobot berbeda mudah dipenuhi dengan prosedur pemutus seri apa pun (Nešetřil *et al.*, 2001, Bagian 4, catatan ⟨1⟩, hlm. 23), misalnya dengan memakai label simpul (Sanders dan Schimek, 2023, Bagian II-C). Aturan yang dipakai laporan ini adalah membandingkan bobot terlebih dahulu, lalu simpul ujung bernomor terkecil, lalu simpul ujung bernomor terbesar. Karena graf tidak memiliki sisi ganda, setiap sisi memiliki tripel (*w*, *u*, *v*) dengan *u* < *v* yang berbeda, sehingga seluruh sisi terurut total, algoritma yang mengandaikan bobot berbeda tetap dapat dijalankan, dan keluaran Kruskal dan Prim menjadi tunggal (dibuktikan pada 3.3.4). Tanpa aturan pemutus seri yang sama, dua algoritma yang benar dapat menghasilkan himpunan sisi yang berbeda dengan total bobot yang sama.

---

## 2.3 Notasi Asimtotik dan Definisi Kasus Analisis

---

Kompleksitas algoritma dinyatakan dengan notasi asimtotik *O*, Ω, dan Θ, yang mengabaikan konstanta pengali dan suku berorde rendah karena yang diperhatikan adalah laju pertumbuhan untuk masukan yang besar. Notasi *O* menyatakan batas atas laju pertumbuhan, Ω batas bawah, dan Θ batas atas dan batas bawah sekaligus (Sanders *et al.*, 2019, Bagian 2.1). Definisi formalnya mengikuti buku tersebut dan tidak diulang di sini.

Pada graf, ukuran masukan lazim dinyatakan dengan jumlah simpul dan jumlah sisi (Sanders *et al.*, 2019, Bagian 2.1), yaitu *n* = |*V*| dan *m* = |*E*| (Sanders *et al.*, 2019, Bagian 2.12) seperti pada 1.2. Karena itu, notasi *O* dipakai untuk fungsi dua peubah, yaitu *f*(*n*, *m*) = *O*(*g*(*n*, *m*)) jika ada konstanta *c* > 0 sehingga *f*(*n*, *m*) ≤ *c*·*g*(*n*, *m*) untuk *n* dan *m* yang cukup besar.

Waktu berjalan suatu algoritma dapat berbeda untuk masukan yang berukuran sama. Misalkan *I*ₙ adalah himpunan hingga masukan berukuran *n* dan *T*(*i*) adalah waktu berjalan pada masukan *i*. Kasus terburuk, terbaik, dan rata-rata didefinisikan sebagai (Sanders *et al.*, 2019, Bagian 2.1)

T_terburuk(n) = max { T(i) : i ∈ I_n }, T_terbaik(n) = min { T(i) : i ∈ I_n }, T_rata-rata(n) = (1 / |I_n|) · Σ T(i) untuk i ∈ I_n. (4)

Kasus terburuk memberikan jaminan kinerja yang paling kuat (Sanders *et al.*, 2019, Bagian 2.1). Kasus rata-rata memerlukan model keacakan, yaitu ruang peluang yang mendasari masukan (Sanders *et al.*, 2019, Bagian 2.9), sehingga hasilnya hanya berlaku jika masukan nyata sesuai dengan model tersebut.

Pada masalah MST, laporan ini membedakan ketiga kasus berdasarkan kepadatan graf. Untuk jumlah simpul *n* tertentu, kasus ditentukan oleh jumlah sisi *m*, dengan batas *n* − 1 ≤ *m* ≤ *n*(*n* − 1)/2 sesuai 1.2. Pembagian ini merupakan definisi yang dipilih dalam laporan ini, dan ditunjukkan pada Tabel 2.1.

**Tabel 2.1** Definisi kasus analisis berdasarkan kepadatan graf

| Kasus | Kepadatan graf (untuk *n* tertentu) | Jumlah sisi |
|---|---|---|
| Terbaik | Graf jarang minimal (berbentuk pohon) | *m* = *n* − 1 |
| Rata-rata | Kepadatan menengah sebagai wakil | *m* = Θ(*n* log *n*) |
| Terburuk | Graf padat | *m* = Θ(*n*²) |

Dengan demikian, ketiga kasus pada Tabel 2.1 adalah klasifikasi berdasarkan kepadatan graf, yang batas waktunya diperoleh dengan mensubstitusikan nilai *m*. Klasifikasi ini tidak sama dengan nilai minimum, rata-rata, dan maksimum waktu berjalan atas seluruh masukan berukuran *n* pada (4), terutama untuk kasus rata-rata.

Kasus terbaik termasuk dalam keluarga graf jarang (*m* = Θ(*n*)), sehingga orde kurva teoretisnya sama dengan graf jarang yang diukur pada eksperimen. Demikian pula kasus terburuk adalah graf padat yang diukur pada eksperimen. Kasus rata-rata pada laporan ini bukan nilai harapan secara probabilistik, melainkan kepadatan menengah yang dipilih sebagai wakil. Kasus ini dianalisis secara teoretis dengan mensubstitusikan nilai *m* ke batas umum, sedangkan pengukuran empiris pada Bab 4 terbatas pada graf jarang dan padat sesuai 1.4.

Hasil analisis pada Bab 3 dinyatakan dengan notasi *O*, yaitu batas atas yang berlaku untuk urutan bobot sisi apa pun pada kepadatan yang bersangkutan. Pernyataan bahwa Θ berlaku memerlukan argumen batas bawah tersendiri. Kompleksitas ruang dianalisis dengan notasi yang sama sebagai fungsi *n* dan *m*.

---

## 2.4 Algoritma Borůvka sebagai Pembanding

---

Algoritma Borůvka dipilih sebagai pembanding karena strateginya berbeda dari Kruskal dan Prim, tetapi tetap bertumpu pada sifat *greedy* yang sama. Borůvka merumuskan solusi pertama masalah MST pada tahun 1926, dan kedua makalah aslinya diterjemahkan serta dikaji oleh Nešetřil *et al.* (2001). Dalam rumusan modern, algoritma ini bekerja dalam putaran. Mula-mula setiap simpul adalah pohon tersendiri. Pada setiap putaran, setiap pohon memilih sisi berbobot minimum yang keluar dari pohon itu, semua sisi terpilih ditambahkan ke hutan, dan pohon-pohon yang terhubung oleh sisi terpilih digabung. Putaran diulang sampai tersisa satu pohon (Nešetřil *et al.*, 2001, Bagian 7). Pada varian dengan kontraksi, setiap pohon yang terbentuk digantikan oleh satu simpul, sisi yang kedua ujungnya berada dalam pohon yang sama dibuang, dan di antara sisi sejajar hanya yang berbobot terkecil dipertahankan (Nešetřil *et al.*, 2001, Bagian 7; Sanders dan Schimek, 2023, Bagian II-C).

Jumlah pohon, atau jumlah simpul pada graf terkontraksi, berkurang paling sedikit setengahnya pada setiap putaran, sehingga banyak putaran paling besar log *n* (Nešetřil *et al.*, 2001, Bagian 8; Sanders *et al.*, 2019, Bagian 11.6). Setiap putaran dapat diimplementasikan dalam waktu linear terhadap *m*, sehingga total waktunya *O*(*m* log *n*) (Nešetřil *et al.*, 2001, Bagian 8; Sanders *et al.*, 2019, Bagian 11.6). Batas ini sama dengan batas pengurutan sisi pada Kruskal, yaitu *O*(*m* log *m*) = *O*(*m* log *n*) (Sanders *et al.*, 2019, Bagian 11.3). Penurunan batas Borůvka disajikan secara singkat di Bab 3 untuk keperluan kurva teoretis, sesuai dengan kode yang ditulis.

Kebenaran algoritma ini dibuktikan dengan asumsi bobot sisi berbeda (Nešetřil *et al.*, 2001, Bagian 7; Sanders *et al.*, 2019, Bagian 11.6), dan asumsi tersebut dipenuhi oleh aturan pemutus seri pada butir 7 subbab 1.4. Tanpa urutan total atas sisi, sisi terpilih dapat membentuk siklus. Pada segitiga dengan tiga bobot sama, misalnya, ketiga simpul dapat memilih tiga sisi yang berbeda.

---

## 2.5 Penelitian Terkait

---

Tiga dari empat penelitian terbaru berikut mengembangkan varian algoritma MST (paralel, terdistribusi, dan aproksimasi), sedangkan satu menerapkan MST pada *clustering*.

Fallin *et al.* (2023) mengembangkan ECL-MST, implementasi MST untuk GPU yang memparalelkan algoritma Kruskal. Hasilnya hampir identik dengan paralelisasi Borůvka karena keduanya memakai struktur data *disjoint set* yang sama. Pada GPU Titan V, ECL-MST dilaporkan rata-rata 4,6 kali lebih cepat daripada kode tercepat berikutnya. Pada sistem kedua (RTX 3080 Ti), penulis juga menunjukkan bahwa delapan optimasi yang dievaluasi, bila digabung, membuat kodenya lebih dari 8 kali lebih cepat daripada versi tanpa optimasi tersebut.

Sanders dan Schimek (2023) mengembangkan varian Borůvka dan Filter-Borůvka untuk memori terdistribusi. Algoritma mereka berskala hingga sedikitnya 65.536 inti dan hingga 800 kali lebih cepat daripada algoritma MST terdistribusi sebelumnya (nilai tertinggi dicapai pada graf grid yang berlokalitas tinggi). Mereka mencatat bahwa Borůvka dapat memproses seluruh sisi sebanyak logaritmik kali, dan Filter-Kruskal dalam banyak hal merupakan algoritma sekuensial praktis terbaik saat ini. Mereka juga menyatakan bahwa label simpul dapat dipakai untuk memutus seri antar bobot sama secara konsisten, sehingga bobot dapat diasumsikan berbeda dan MST menjadi unik. Hal ini sejalan dengan aturan pemutus seri pada subbab 1.4.

Almansoori *et al.* (2025) mengusulkan algoritma pembangkitan MST aproksimasi untuk data berdimensi tinggi dan berukuran besar. Metode ini membangun graf k tetangga terdekat secara aproksimasi, membentuk MST awal darinya, lalu mengoptimalkan MST tersebut. Mereka melaporkan bahwa algoritma yang diusulkan unggul dibandingkan FISHDBC dalam waktu jalan dan galat relatif. Algoritma MST eksak yang dipakai sebagai pembanding lebih cepat pada data berdimensi rendah atau berukuran kecil, sehingga keunggulan metode ini terutama berlaku untuk data besar berdimensi tinggi. Pada pendahuluannya, mereka menyebut *clustering*, desain dan optimasi jaringan, serta deteksi anomali sebagai penerapan MST yang penting.

Gagolewski *et al.* (2025) menempatkan MST sebagai representasi data pada tugas *clustering* berdimensi rendah. Dari batas atas kesesuaian yang dihitung dengan algoritma *oracle*, mereka menyimpulkan bahwa metode berbasis MST berpotensi sangat kompetitif. Di antara metode yang diuji, Genie dan metode berbasis teori informasi sering mengungguli algoritma non-MST seperti *K-means*, *Gaussian mixture*, dan *spectral clustering*. Temuan ini terbatas pada *dataset* uji dengan *n* < 10.000 dan dimensi *d* ≤ 3.

Laporan ini tidak mengusulkan varian baru. Laporan ini menganalisis secara formal dan mengukur secara sekuensial algoritma klasik Kruskal, Prim, dan Borůvka, yang menjadi acuan varian-varian tersebut, pada graf jarang dan padat, lalu membandingkan hasilnya dengan kurva kompleksitas teoretis.

---
