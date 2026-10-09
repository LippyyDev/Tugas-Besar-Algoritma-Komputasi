# BAB 5 KESIMPULAN

---

## 5.1 Kesimpulan

---

Kruskal menumbuhkan hutan dengan memeriksa sisi menurut urutan bobot, sedangkan Prim menumbuhkan satu pohon dari simpul awal dengan sisi termurah yang keluar dari pohon (3.1 dan 3.2). Keduanya terbukti benar, yaitu selalu menghasilkan *minimum spanning tree* (Teorema 3.1 dan 3.2), dan dengan aturan pemutus seri yang sama keduanya menghasilkan MST yang sama (Teorema 3.3).

Waktu Kruskal dan Prim sama-sama *O*(*m* log *n*), sedangkan Borůvka pada kode ini *O*(*m* log² *n*). Ruang tambahannya *O*(*n* + *m*) untuk Kruskal dan Prim, dan *O*(*n*) untuk Borůvka. Dengan kasus dibagi menurut kepadatan graf (2.3), batas Kruskal dan Prim adalah *O*(*n* log *n*) pada kasus terbaik, *O*(*n* log² *n*) pada kasus rata-rata, dan *O*(*n*² log *n*) pada kasus terburuk. Teori tidak membedakan Kruskal dan Prim, sehingga pembedanya dilihat dari pengukuran.

Ketiga algoritma diimplementasikan dalam Python, lolos empat kasus uji kecil, memberi total bobot yang sama dengan `networkx` pada 300 graf acak kecil, dan memberi hasil yang sama pada studi kasus jaringan kabel lima gedung Fakultas Teknik Universitas Hasanuddin, yaitu total biaya bersih 8 juta rupiah (biaya ilustrasi, memuat bobot 0 dan negatif).

Pengukuran pada graf jarang, padat, dan jarang berbobot kembar menunjukkan bahwa Kruskal memiliki rata-rata waktu terendah pada graf jarang (empat dari lima ukuran) dan graf jarang berbobot kembar (kelima ukuran), dan Prim terendah pada graf padat (empat dari lima ukuran) jika daftar ketetanggaan sudah tersedia. Borůvka paling lambat pada semua ukuran, yaitu 3,34 sampai 4,72 kali waktu Kruskal pada ukuran terbesar. Selisih Kruskal dan Prim sering masih berada di dalam simpangan baku, sehingga tidak ada satu algoritma yang terbaik pada semua kondisi. Terhadap kurva teoretis, waktu Kruskal dan Prim naik lebih cepat daripada *m* log *n* (rasio pada ukuran terbesar 1,29 sampai 2,19 kali nilai ukuran terkecil). Ini tidak membantah batas atas asimtotik karena rentang yang diukur terbatas, dan penyebabnya tidak diuji.

---

## 5.2 Kelebihan, Keterbatasan, dan Kesesuaian

---

Kruskal sederhana dan langsung memproses daftar sisi, tetapi seluruh sisi harus diurutkan lebih dulu. Prim alami dipakai pada daftar ketetanggaan, tetapi `heapq` tidak menyediakan *decrease-key*, sehingga batasnya *O*(*m* log *n*), bukan *O*(*m* + *n* log *n*). Borůvka hemat ruang, tetapi kode ini memindai seluruh sisi pada setiap putaran dan kebenarannya tidak dibuktikan formal. Pada studi kasus lima gedung, ketiganya sesuai dan menghasilkan himpunan sisi yang sama, sehingga pilihan di antaranya ditentukan oleh bentuk data.

Hasil ini terbatas pada rentang ukuran yang jauh di bawah 10⁶, satu graf per ukuran pada Colab versi gratis, dua kepadatan saja sehingga titik silang Kruskal dan Prim tidak ditetapkan, dan studi kasus berbiaya ilustrasi yang tidak memperhitungkan cadangan jalur.

---

## 5.3 Peluang Pengembangan

---

Pengembangan yang dapat dilakukan adalah memperlebar rentang ukuran dan kepadatan dengan beberapa graf per ukuran untuk menguji penyebab pertumbuhan yang lebih cepat daripada *m* log *n*, mengganti antrean Prim dengan struktur yang mendukung *decrease-key* (Osipov *et al.*, 2009; Sanders *et al.*, 2019), menambahkan kontraksi graf pada Borůvka dan menguji Filter-Kruskal (Osipov *et al.*, 2009), mengimplementasikan ketiganya dalam bahasa selain Python atau versi paralel (Fallin *et al.*, 2023; Sanders dan Schimek, 2023), serta mengganti jarak ilustrasi dengan hasil pengukuran lapangan.
