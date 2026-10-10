# Rencana Presentasi Tugas Besar Analisis Algoritma

Analisis Perbandingan Algoritma Kruskal, Prim, dan Borůvka pada *Minimum Spanning Tree* (MST).
Penyaji: Muhammad Alif Qadri. Durasi rencana: 13 menit (batas tugas 10 sampai 15 menit).

Status: slide 1 sampai 10 sudah jadi. Slide 11 (Kesimpulan) masih rencana. Slide Implementasi dihapus atas permintaan pengguna.

## 1. Struktur dan Alokasi Waktu

| No | Slide | Waktu | Status |
|----|-------|-------|--------|
| 1 | Judul | 0,5 mnt | Jadi |
| 2 | Masalah MST dan ide dasar *greedy* (*cut property*) | 2 mnt | Jadi |
| 3 | Algoritma yang dibahas | 0,5 mnt | Jadi |
| 4 | Kruskal | 1,5 mnt | Jadi |
| 5 | Prim | 1,5 mnt | Jadi |
| 6 | Borůvka | 1,5 mnt | Jadi |
| 7 | Kompleksitas teoretis | 1,5 mnt | Jadi |
| 8 | Studi kasus: jaringan kabel lima gedung (adegan 3D) | 1 mnt | Jadi |
| 9 | Metode eksperimen | 1 mnt | Jadi |
| 10 | Hasil dan analisis | 1,5 mnt | Jadi |
| 11 | Kesimpulan | 0,5 mnt | Rencana |

Total 13 menit, di dalam batas 10 sampai 15 menit. Bila perlu dipangkas, ambil dari slide 7 atau 4 sampai 6.

Pengelompokan pada bar progres di bawah slide: Pembuka (1), Konsep (2), Algoritma (3 sampai 6), Teori (7), Eksperimen (8 sampai 10), Penutup (11).

## 2. Gaya dan Cara Pakai

Tema hitam bergaya Palantir: huruf mono kapital untuk label, garis tipis, satu warna aksen biru, dan sudut panel bersiku. Panggung tetap 1920 × 1080 yang otomatis diskalakan ke ukuran layar. Tiap file HTML berisi HTML, CSS, dan JS sendiri.

| Cara | Fungsi |
|------|--------|
| Klik tepi kiri atau kanan layar (sekitar 7% lebar), seperti Canva | Mundur atau maju |
| Tombol panah kiri atau kanan, Spasi, PageUp, PageDown | Mundur atau maju |
| Kursor ke bagian bawah layar | Memunculkan kotak navigasi (Sebelumnya, Reset, Berikutnya, penanda langkah). Hilang 1 detik setelah kursor dilepas |
| R | Reset animasi ke awal |
| F | Layar penuh |
| I | Kembali ke `index.html` |

Maju di langkah terakhir sebuah slide pindah ke slide berikutnya. Mundur di langkah pertama pindah ke slide sebelumnya.

Isi folder `PRESENTASI`:

- `index.html`: daftar slide dengan pratinjau dan total durasi.
- `slide1.html` sampai `slide4.html`: slide yang sudah jadi.
- `aset/logo-unhas.png`: logo.

Menambah slide baru: buat `slideN.html`, ubah `ready:true` pada `index.html`, dan isi `NEXT_SLIDE` pada slide sebelumnya.

## 3. Slide 1: Judul

Tujuan: memperkenalkan topik dan penyaji dalam 30 detik.

Isi:

- Logo dan nama Universitas Hasanuddin, Magister Teknik Informatika.
- Judul: Analisis Perbandingan Algoritma Kruskal, Prim, dan Borůvka pada *Minimum Spanning Tree*.
- Tiga label algoritma: Kruskal, Prim, Borůvka.
- Satu kalimat deskripsi: membandingkan cara kerja, kompleksitas teoretis, dan hasil eksperimen tiga algoritma.
- Nama penyaji. NIM dan nama dosen masih berupa placeholder `[ISI NIM]` dan `[ISI NAMA DOSEN]` yang harus diisi di `slide1.html`.

Visual dan gerak: judul muncul kata demi kata, lalu label algoritma satu per satu. Latar berupa jaringan titik yang bergerak dan menghitung MST secara langsung. Tombol R memutar ulang animasi pembuka.

Catatan penyaji: sebut judul, sebut tiga algoritma yang dibandingkan, lalu langsung masuk ke masalah di slide 2.

## 4. Slide 2: Apa itu MST?

Tujuan: penonton paham apa itu MST, mengapa tidak boleh mencoba semua pohon, dan mengapa pilihan *greedy* itu benar.

Teks di slide:

> **MST (*Minimum Spanning Tree*)** adalah cara menghubungkan semua titik dalam sebuah jaringan dengan total biaya paling kecil.
>
> **Masalahnya:** bagaimana membangun MST tanpa harus mencoba semua kemungkinan pohon?
>
> **Solusinya:** algoritma *greedy*, yaitu pilih sisi termurah yang aman di setiap langkah. Sisi aman adalah sisi yang pasti ada di suatu MST. *Cut property*: bagi titik jadi dua kelompok, sisi termurah yang menyeberanginya pasti aman.

Kata "suatu MST" dipakai sengaja, karena bila ada bobot sisi yang sama, MST bisa lebih dari satu.

Graf contoh: 5 titik (A sampai E) dan 7 sisi dengan bobot tidak ada yang kembar, sehingga MST-nya tunggal. Semua angka di bawah dihitung otomatis oleh kode dari data graf.

| Langkah | Tampilan | Pesan untuk penonton |
|---------|----------|----------------------|
| 1 | Jaringan muncul. Total biaya bila semua sisi dipasang: 46 | Titik adalah lokasi, sisi adalah kabel, angka adalah biaya pasang |
| 2 | MST terbentuk sisi demi sisi: B–D (3), D–E (4), A–B (5), C–D (6). Total 18 | Semua titik tersambung dengan 4 sisi saja, jauh lebih murah dari 46 |
| 3 | Semua pohon rentang dicoba satu per satu (21 pohon pada graf ini), lalu tabel jumlah pohon pada jaringan lengkap | Makin banyak titik, jumlah pohon meledak, jadi tidak mungkin dicoba semua |
| 4 | Contoh *greedy*: A–B dan B–D sudah terpilih, kandidat berwarna kuning, D–E (4) termurah | Di setiap langkah ambil yang termurah, tetapi apakah aman? |
| 5 | Putaran *cut* 1: kelompok 1 = A. Sisi yang menyeberang 5 dan 8. A–B (5) aman | Garis putus-putus memisahkan dua kelompok, sisi termurah yang menyeberang pasti aman |
| 6 | Putaran 2: kelompok 1 = A, B. Menyeberang 8, 11, 3. B–D (3) aman | Kelompok membesar |
| 7 | Putaran 3: kelompok 1 = A, B, D. Menyeberang 8, 11, 6, 4. D–E (4) aman | Alasan yang sama dipakai berulang |
| 8 | Putaran 4: kelompok 1 = A, B, D, E. Menyeberang 8, 11, 6, 9. C–D (6) aman | Titik terakhir bergabung |
| 9 | Semua titik tersambung, MST berbiaya 18 | Hasilnya sama dengan MST di langkah 2 |

Satu klik maju satu langkah. Tidak ada animasi yang berjalan sendiri setelah *cut*, supaya penyaji bisa menjelaskan tiap putaran.

Catatan penyaji (sekitar 2 menit):

1. Mulai dari gambar jaringan: "Bayangkan lima lokasi yang harus disambung kabel. Tiap kabel punya biaya."
2. Tunjukkan MST: "Kita cari susunan kabel termurah yang tetap menyambungkan semuanya."
3. Masalah: "Cara naif adalah mencoba semua susunan. Untuk 10 titik saja ada seratus juta kemungkinan."
4. Solusi: "Algoritma *greedy* memilih yang termurah di tiap langkah, asal aman."
5. *Cut property*: "Aman berarti pasti ada di suatu MST. Buktinya: bagi titik jadi dua kelompok. Dua kelompok itu harus tersambung, jadi minimal satu kabel harus menyeberang. Memilih yang termurah di antara penyeberang tidak pernah merugikan."
6. Putaran: "Ulangi sampai semua titik tersambung."
7. Jembatan ke slide 3: "Pendekatan *greedy* ini tidak hanya satu. Ada banyak algoritma *greedy*, jadi mari kita lihat mana yang akan kita bahas."

Analogi sederhana untuk *cut property*: dua desa di seberang sungai yang harus disambung jembatan. Minimal satu jembatan harus dibangun, dan memilih lokasi jembatan termurah tidak pernah rugi.

Pembagian dua kelompok bebas, asalkan kedua kelompok tidak kosong dan sisi yang diperiksa adalah sisi yang menyeberang. Prim memakai kelompok titik yang sudah terhubung, sedangkan Kruskal dan Borůvka memakai gugus yang sedang terbentuk.

Hal yang perlu diverifikasi sebelum dipakai di laporan: rumus Cayley (jumlah pohon pada jaringan lengkap: 125 untuk 5 titik, 100.000.000 untuk 10 titik, sekitar 2,6 × 10²³ untuk 20 titik) dan *cut property* adalah teori dasar. Sitasi buku teks standar belum diverifikasi, dan judul serta edisinya harus dicek sebelum dicantumkan.

## 5. Slide 3: Algoritma yang Dibahas

Tujuan: menjadi penghubung dari ide *greedy* di slide 2 ke tiga algoritma yang dibahas. Slide ini murni pernyataan, tanpa animasi graf, tanpa rumus, dan tanpa isi tambahan.

Teks di slide: judul "Algoritma yang dibahas", kalimat "Algoritma *greedy* ada banyak jenisnya dan banyak lainnya", lalu tiga kartu berdampingan: **Kruskal** (utama), **Prim** (utama), **Borůvka** (pembanding, berwarna kuning). Tiap kartu hanya memuat nama dan satu frasa pendek: urut sisi dari termurah, tumbuh dari satu titik, serentak semua titik memilih.

Gerak (4 langkah): (1) jaringan titik kecil mewakili algoritma *greedy* lain; titik muncul bergantian dan garisnya tergambar, lalu terus hidup (melayang, berkedip, dan ada cahaya kecil yang berjalan di sepanjang garis); (2) sampai (4) satu kartu muncul per klik, ditarik oleh garis cahaya dari satu titik di jaringan itu. Setiap kartu menjalankan animasi algoritmanya sendiri secara berulang pada graf yang sama dengan slide 2: Kruskal menguji sisi dari bobot terkecil dan menolak yang membentuk siklus, Prim tumbuh dari titik A (tiap putaran: semua sisi yang menyeberang menyala kuning sebagai kandidat, yang kalah meredup, sisi termurah menyala putih lalu menjadi bagian pohon), Borůvka memilih sisi termurah tiap titik serentak.

Aliran dari slide 2: langkah terakhir slide 2 menutup dengan "semua titik tersambung, MST berbiaya 18" dan kalimat jembatan pada catatan penyaji nomor 7. Slide 3 menjawab pertanyaan yang muncul setelahnya, yaitu algoritma *greedy* yang mana yang akan dipakai. Setelah itu slide 4 langsung masuk ke Kruskal.

Catatan penyaji (sekitar 30 detik): sebut bahwa *greedy* adalah keluarga algoritma yang besar, lalu sebut dua yang akan dijelaskan (Kruskal dan Prim) dan satu pembanding (Borůvka). Alasan Borůvka dibahas: pembanding tambahan dalam eksperimen, bukan ketentuan tertulis dari dosen (tafsiran penyaji).

## 5b. Slide 4: Algoritma Kruskal

Tujuan: penonton paham cara Kruskal memilih sisi dan mengapa sisi yang membentuk siklus ditolak, sambil melihat pseudocode yang menyala sinkron dengan gambar. Pola A: pseudocode di kiri, graf di kanan.

Isi layar: pseudocode 8 baris yang sama dengan Pseudocode 3.2 di Bab 3 (urutannya mengikuti fungsi `kruskal()` di `kruskal.py`), graf standar 5 titik, deret sisi terurut (B–D 3, D–E 4, A–B 5, C–D 6, A–C 8, C–E 9, B–C 11), baris kelompok (setara himpunan terpisah pada contoh dasar), pembacaan Sisi MST dan Total biaya, serta panel **Arti simbol** di bawah pseudocode. Panel itu menjelaskan tiap simbol (E, E′, κ, himpunan, A, total, u v w, n) dalam bahasa biasa beserta nilainya saat ini, dan barisnya menyala sesuai baris pseudocode yang sedang berjalan. Semua angka dihitung kode dari data graf, bukan ditulis tangan.

| Langkah | Tampilan | Pesan untuk penonton |
|---------|----------|----------------------|
| 1 | Graf muncul. Ide Kruskal | Urut sisi dari termurah, ambil asal tidak membentuk siklus |
| 2 | Sisi terurut muncul, tiap titik jadi kelompok sendiri, himpunan A kosong (baris 1 dan 2) | Persiapan sebelum perulangan |
| 3 sampai 6 | Satu sisi per klik: B–D 3, D–E 4, A–B 5, C–D 6. Tiap klik: ambil sisi (baris 3), GABUNG berhasil (baris 4), masuk A (baris 5), cek |A| = n − 1 (baris 6). Setelah C–D, baris 6 menghentikan perulangan: 4 dari 4 sisi, total 18 | Sisi diterima bila kedua ujungnya beda kelompok |
| 7 | Contoh sisi A–C 8 diperiksa seandainya proses tidak berhenti: A dan C sudah satu kelompok, GABUNG gagal pada baris 4, ditolak, label SIKLUS | Mengapa sisi ditolak |

Catatan jujur untuk penyaji: pada graf contoh ini sisi yang membentuk siklus tidak pernah sampai diperiksa, karena kode berhenti begitu MST berisi 4 sisi (sesuai `kruskal.py`). Langkah 7 sengaja diberi kata "seandainya" supaya tidak terkesan sisi itu benar-benar diperiksa oleh kode.

Catatan penyaji (sekitar 1,5 menit):

1. "Kruskal bekerja dengan daftar sisi yang diurutkan dari termurah."
2. "Tiap titik mulai sebagai kelompok sendiri."
3. "Ambil sisi termurah. Kalau kedua ujungnya beda kelompok, ambil dan gabungkan kelompoknya."
4. "Kalau sudah satu kelompok, sisi itu hanya membuat lingkaran, jadi dibuang."
5. "Berhenti saat sisi terpilih sudah n dikurangi 1. Di sini 4 sisi, total biaya 18."

Kompleksitas tidak dicantumkan di slide ini, karena dibahas di slide 7 setelah diverifikasi.

## 5c. Slide 5: Algoritma Prim

Tujuan: penonton paham bahwa Prim menumbuhkan satu pohon dari titik awal A dengan selalu mengambil sisi termurah dari antrean Q. Tata letak sama dengan slide 4, dan satu klik hanya menjalankan satu fase.

Isi layar: pseudocode 10 baris yang merupakan **ringkasan** Pseudocode 3.3 (PRIM) di Bab 3, dengan urutan mengikuti fungsi `prim()` di `prim.py`. Pseudocode 3.3 asli 14 baris dan beberapa barisnya terlalu panjang untuk kotak slide, sehingga beberapa baris digabung atau disingkat (misalnya baris 8 dan 12 asli menjadi "masukkan ke Q sisi dari tujuan ke titik baru"). Bagian lain: graf standar 5 titik, deret antrean Q (termurah di kiri), baris Pohon (titik yang sudah masuk), pembacaan Sisi MST dan Total biaya, serta panel Arti simbol (s dan n, masuk, Q, w k b, asal dan tujuan, A, total) dengan nilai saat ini. Semua angka dihitung kode dari simulasi Prim sungguhan (kunci urut bobot, simpul kecil, simpul besar).

Urutan hasil: A–B 5, B–D 3, D–E 4, C–D 6, total 18 (berbeda urutan dengan Kruskal, hasil sama).

| Klik | Tampilan | Pesan |
|------|----------|-------|
| 1 | Graf muncul. Ide Prim | Tumbuh dari satu titik, ambil sisi termurah yang menyeberang |
| 2 sampai 3 | A masuk pohon (baris 1), sisi A–B 5 dan A–C 8 masuk Q (baris 2) | Persiapan |
| 4 sampai 19 | Tiap sisi 4 klik: keluarkan termurah dari Q (baris 3 dan 4), cek ujung dan tujuan masuk pohon (baris 5 dan 6), masuk A (baris 7), tetangga baru masuk Q (baris 8). Pada sisi terakhir C–D ada klik tambahan: |A| = n − 1, berhenti, kembalikan hasil (baris 3, 9, 10) | Q selalu mengeluarkan sisi termurah |
| 20 sampai 21 | "Seandainya" sisi A–C 8 dikeluarkan lagi: kedua ujung sudah di pohon, dilewati (baris 5), label SIKLUS | Mengapa sisi dilewati |

Catatan jujur: seperti Kruskal, pada graf contoh ini sisi yang dilewati tidak pernah dikeluarkan dari Q oleh kode, karena perulangan berhenti saat |A| = n − 1. Dua klik terakhir diberi kata "seandainya".

## 5d. Slide 6: Algoritma Borůvka

Tujuan: penonton paham bahwa Borůvka bekerja dalam putaran, dan di tiap putaran semua komponen memilih sisi termurahnya secara serentak. Tata letak sama dengan slide 4 dan 5, satu klik satu fase.

Isi layar: pseudocode 12 baris yang merupakan **ringkasan** Pseudocode 3.4 (BORŮVKA) di Bab 3, urutannya mengikuti `boruvka()` di `boruvka.py` (baris 5 dan 6 asli digabung sebagai "simpan sisi ini di T jika lebih murah"). Bagian lain: graf 5 titik, deret "Pilihan tiap komponen" dalam urutan kamus T seperti di kode (C, D, A, B, E), baris Komponen, pembacaan Sisi MST dan Total biaya, dan panel Arti simbol (E, n dan c, himpunan, T, u v w, A, total). Simulasi memakai urutan daftar sisi yang sama dengan contoh di `boruvka.py`.

Hasil: 1 putaran. Pilihan: C→C–D 6, D→B–D 3, A→A–B 5, B→B–D 3, E→D–E 4. Pemasangan berurutan: C–D 6, B–D 3, A–B 5, lalu B–D 3 gagal (sudah dipasang dari pilihan D), D–E 4, total 18 dan c = 1.

| Klik | Tampilan | Pesan |
|------|----------|-------|
| 1 | Graf muncul. Ide Borůvka | Bekerja dalam putaran, semua komponen memilih serentak |
| 2 sampai 5 | himpunan dibuat dan c = 5 (baris 1), putaran dimulai dan T kosong (baris 2 dan 3), tiap komponen memilih sisi termurah (baris 4 sampai 6), T tidak kosong (baris 7 dan 8) | Pilihan serentak |
| 6 sampai 15 | Tiap pilihan 2 klik: ambil dan cek GABUNG (baris 8 dan 9), lalu diterima (baris 10 dan 11) atau gagal (baris 9, label SUDAH DIPASANG untuk B–D yang kedua) | Satu sisi bisa dipilih dua komponen |
| 16 | c = 1, perulangan berhenti, kembalikan hasil (baris 2 dan 12) | Selesai dalam 1 putaran |

Catatan: berbeda dengan slide 4 dan 5, penolakan pada slide ini benar-benar terjadi di kode (GABUNG kedua untuk B–D mengembalikan SALAH), jadi tidak memakai kata "seandainya".

## 5e. Slide 7: Kompleksitas Teoretis

Tujuan: penonton yang belum akrab dengan notasi *O* tetap paham dari mana batas waktu dan ruang tiap algoritma berasal. Isi mengikuti Bab 3 subbab 3.4 (Teorema 3.5 sampai 3.8, Tabel 3.7 dan 3.8). Komposisinya sengaja berbeda dari slide 4 sampai 6: tiga kartu lebar penuh dan grafik batang, tanpa panel kiri kanan. Satu klik satu langkah.

Catatan: rencana awal menyebut Borůvka hanya "dikutip singkat", tetapi laporan sudah membuktikan *O*(*m* log² *n*) untuk kode Borůvka (Teorema 3.7), sehingga slide mengikuti laporan.

| Klik | Tampilan | Pesan |
|------|----------|-------|
| 1 | Empat kartu: n (titik), m (sisi), log n (berapa kali n dibelah dua), *O*( ) (batas atas). Strip rumus kunci "banyak pekerjaan × biaya tiap pekerjaan". Deret 1.000, 500, ..., 1 | log n tumbuh sangat lambat, dan *O* adalah batas atas langkah, bukan waktu pasti |
| 2 | Kartu Kruskal dan Prim dengan pola "berapa kali × biaya tiap kali". Prim: ≤ m masuk + ≤ m keluar, angka 2 dibuang di *O*. Keduanya O(m log n) | Sama-sama memproses sekitar m sisi, tiap sisi berbiaya sekitar log n. Batas atas sama belum tentu sama cepat |
| 3 | Kartu Borůvka: putaran paling banyak log n (contoh: 1.000 titik sekitar 10 putaran, graf contoh 1 putaran), tiap putaran m log n. Hasil O(m log² n), label "+1 faktor log n" | Kode ini mencari komponen dengan CARI-AKAR, jadi ada satu faktor log n lebih |
| 4 | Baris "Memori ekstra di luar data" pada tiap kartu, lengkap dengan isi yang disimpan | Kruskal dan Prim O(n + m), Borůvka O(n) |
| 5 | Grafik batang skala logaritmik untuk graf jarang, menengah, padat pada n = 1.000, dengan legenda "batang panjang = langkah lebih banyak = lebih berat" dan dua penanda rasio (padat sekitar 500 kali jarang, Borůvka sekitar 10 kali lebih berat) | Graf padat jauh lebih berat. Kruskal dan Prim berbatas atas sama, jadi pembeda diukur lewat eksperimen |

Angka pada grafik dihitung dari rumus: m = n − 1 (jarang), m = n log₂ n (menengah), m = n(n − 1)/2 (padat), lalu m log₂ n dan m log₂² n dengan n = 1.000. Ini ilustrasi satuan langkah menurut rumus, bukan hasil pengukuran, dan diberi label di slide. Kasus "menengah" memakai konstanta 1 pada Θ(n log n) sebagai asumsi ilustrasi.

## 5f. Slide 8: Studi Kasus

Tujuan: penonton awam melihat MST dipakai pada masalah nyata kecil, dan bahwa ketiga algoritma menghasilkan jawaban sama. Isi mengikuti Bab 4 subbab 4.1 (Tabel 4.1 dan 4.2). Gaya berbeda dari slide lain: adegan 3D layar penuh (lima gedung sebagai balok, jalur kabel sebagai lengkung di atas lantai kampus), tanpa kotak panel. Proyeksi dihitung dengan JavaScript (bukan CSS 3D) sehingga label selalu menghadap layar. Adegan bisa diputar dengan menyeret kursor, klik dua kali mengembalikan sudut. Lima klik.

| Klik | Tampilan | Pesan |
|------|----------|-------|
| 1 | Lima gedung naik, enam jalur kandidat (garis putus), empat pasangan terhalang bertanda ✕ | 5 simpul, 6 sisi, tujuan MST |
| 2 | Jalur diwarnai menurut tanda biaya (biru negatif, putih nol, kuning positif) dengan chip biaya, legenda arti bobot | Bobot nol dan negatif sah. Nilai ilustrasi karangan |
| 3 | Kruskal menerima −5, −2, 0 berurutan (kabel menyala, total berjalan −7) | Terima yang tidak membentuk siklus |
| 4 | Jalur 15 menyambung Industri, total 8, jalur 18 dan 25 dicoret (tidak diperiksa) | Berhenti setelah n − 1 = 4 sisi |
| 5 | Hasil Kruskal, Prim, Borůvka sama (4 sisi, 8), rincian −5 − 2 + 0 + 15 = 8, kotak batas | Kasus kecil menguji kebenaran, bukan efisiensi |

Prim dan Borůvka tidak dianimasikan terpisah di slide ini, hanya hasilnya yang disebut (Tabel 4.2). MST tunggal karena semua biaya berbeda.

## 5g. Slide 9: Metode Eksperimen

Tujuan: penonton awam paham graf apa yang diuji, mengapa ukurannya begitu, dari mana grafnya, dan berapa kali diukur. Isi mengikuti Bab 4 subbab 4.4 (Tabel 4.5). Gaya tanya jawab: judul berupa pertanyaan besar (empat pertanyaan), jawabannya visual. Tujuh klik (tiga klik pertama membangun satu jalur skenario tiap klik, dengan graf mini beranimasi: sisi tergambar satu per satu, pada kembar bobot 2 yang berulang disorot).

| Klik | Pertanyaan dan tampilan | Pesan |
|------|-------------------------|-------|
| 1 | Graf seperti apa yang diuji? Tiga jalur (jarang m = 3n, padat m = n(n − 1)/4, jarang kembar) dengan graf mini, ukuran n, dan bobot | Skenario kembar memakai bobot 1 sampai 5 agar banyak bobot sama |
| 2 | Mengapa graf padat dibuat lebih kecil? Batang rentang jumlah sisi (12.000 sampai 192.000 dan 9.950 sampai 249.750), zona tumpang tindih, hitungan n = 64.000 sekitar 1 miliar sisi | Jumlah sisi padat tumbuh kuadrat n, jadi n dibuat kecil agar jumlah sisi sebanding |
| 3 | Dari mana grafnya? Animasi pohon acak (biru) lalu sisi tambahan (kuning), catatan *seed* 2026 | Pohon dulu agar pasti terhubung, tanpa sisi ganda dan tanpa *loop*, hasil dapat diulang |
| 4 | Berapa kali diukur? 1 pemanasan tidak dicatat, 5 ulangan, 15 graf, 225 pengukuran | Rata-rata dan simpangan baku sampel |
| 5 | Catatan jujur muncul | Graf sama di kelima ulangan, jadi simpangan baku hanya gangguan waktu mesin |

Angka 225 adalah hitungan dari rancangan (15 graf × 3 algoritma × 5 ulangan), diberi label di slide. Angka 1 miliar adalah hitungan n(n − 1)/4 untuk n = 64.000, hanya ilustrasi alasan.

## 5h. Slide 10: Hasil dan Analisis

Satu layar, tiga klik, tiga lapis dari atas ke bawah dengan label di kiri (animasi: panel masuk bertahap, batang tumbuh, angka berhitung naik, pemenang disorot, kartu hasil muncul berurutan): (1) Apa datanya: waktu dalam milidetik, 225 pengukuran, tabel ukuran terbesar tiap skenario dengan sel tercepat disorot. (2) Highlight: Kruskal tercepat di jarang, Prim di padat, Borůvka 3,3 sampai 4,7 kali Kruskal, daftar tetangga menambah Prim 44 sampai 50%. (3) Bagaimana hasilnya: tidak ada satu pemenang, Borůvka paling lambat, Kruskal dan Prim tumbuh lebih cepat dari rumus (Prediksi 1 tidak terpenuhi), dan batas hasil. Kartu hasil 3 menjawab "sesuai rumus?" (Kruskal dan Prim tidak, rasio 1,29 sampai 2,19; Borůvka mendekati) dan kartu 4 menjawab "membuktikan teori?" (belum terbukti dan belum terbantah, karena teorema adalah batas atas untuk n sangat besar dan data hanya ukuran terbatas).

Istilah kasus terbaik, rata-rata, dan terburuk hanya dipakai di slide 7 (kompleksitas waktu teoretis). Di slide 9 dan 10 skenario hanya disebut jarang, padat, dan kembar. Semua angka dari Tabel 4.6 sampai 4.10.

## 6. Slide 11 (Rencana)

Belum dikerjakan (slide 3 sampai 10 dijelaskan di bagian 5 sampai 5h). Alokasi waktu mengikuti tabel di bagian 1. Slide "Contoh manual tiga algoritma" dihapus dari rencana, sehingga nomor slide sesudahnya bergeser satu. Isi di bawah adalah arah yang direncanakan dan masih bisa berubah.

| Slide | Arah isi |
|-------|----------|
| 5 Prim | Ide tumbuh dari satu titik dengan sisi termurah yang menyeberang. Animasi serupa dengan Kruskal |
| 6 Borůvka | Ide tiap gugus memilih sisi termurahnya lalu digabung. Alasan ikut dibahas: algoritma pembanding ketiga, tidak ada ketentuan tertulis dari dosen |
| 11 Kesimpulan | Ringkas, bahasa sederhana |

Aturan yang dijaga di seluruh slide: bahasa mudah dipahami, istilah asing ditulis miring, tanpa tanda pisah panjang, dan hanya angka yang bisa dipertanggungjawabkan dari laporan.

## 7. Hal yang Masih Terbuka

- NIM dan nama dosen di slide 1 belum diisi.
- Slide 11 belum dibuat.
- Sitasi untuk rumus Cayley dan *cut property* belum diverifikasi.
- Pengujian slide dilakukan di Chromium. Perilaku di layar sentuh belum dicoba.

## 8. Panduan Belajar Singkat: Slide 4 sampai 6

Graf: sisi A–B 5, A–C 8, B–C 11, B–D 3, C–D 6, D–E 4, C–E 9. MST: 4 sisi, total 18. Pseudocode slide 5 dan 6 adalah ringkasan dari Bab 3.

### Slide 4: Kruskal

**Ide.** Urutkan sisi dari termurah, ambil satu per satu asal tidak membuat lingkaran.

**Pseudocode.** Baris 1 urutkan sisi. Baris 2 siapkan kelompok (tiap titik sendiri), A kosong, total 0. Baris 3 ambil sisi berikutnya. Baris 4 `GABUNG(u, v)`: bila beda kelompok, digabung (berhasil). Baris 5 sisi masuk A, tambah bobot. Baris 6 berhenti bila A berisi n − 1 sisi. Baris 7 dan 8 cek galat lalu kembalikan hasil.

**Jalannya.** B–D 3 (total 3), D–E 4 (7), A–B 5 (12), C–D 6 (18). A berisi 4 sisi, berhenti. A–C, C–E, B–C tidak diperiksa. Klik terakhir ("seandainya"): A–C 8 akan ditolak karena A dan C sudah satu kelompok.

**Simbol.** E sisi graf, E′ sisi terurut, κ aturan urut, himpunan = kelompok tiap titik, A = sisi terpilih, (u, v, w) = ujung dan bobot sisi, n = jumlah titik.

### Slide 5: Prim

**Ide.** Mulai dari A, perbesar satu pohon dengan sisi termurah yang keluar dari pohon.

**Pseudocode.** Baris 1 A masuk pohon. Baris 2 sisi dari A masuk antrean Q (termurah keluar dulu). Baris 3 ulangi selama Q ada isi dan A belum n − 1 sisi. Baris 4 keluarkan sisi termurah (w, k, b). Baris 5 bila kedua ujung sudah di pohon, lewati. Baris 6 ujung baru (tujuan) masuk pohon. Baris 7 sisi masuk A, tambah bobot. Baris 8 sisi dari tujuan ke titik baru masuk Q.

**Jalannya.** A–B 5 (total 5), B–D 3 (8), D–E 4 (12), C–D 6 (18). Sisa Q tidak diproses. Klik terakhir ("seandainya"): A–C 8 dilewati karena kedua ujung sudah di pohon.

**Simbol.** s titik awal, masuk = titik di pohon, Q antrean, (w, k, b) sisi yang keluar, asal dan tujuan = ujung lama dan baru, A, total.

### Slide 6: Borůvka

**Ide.** Dalam putaran: semua komponen sekaligus memilih sisi termurah yang keluar darinya, lalu semua pilihan digabung.

**Pseudocode.** Baris 1 tiap titik satu komponen, c = n. Baris 2 ulangi selama c > 1. Baris 3 kosongkan tabel T. Baris 4 sampai 6 periksa semua sisi, simpan sisi termurah tiap komponen di T. Baris 7 cek T tidak kosong. Baris 8 ambil pilihan di T satu per satu. Baris 9 sampai 11 bila `GABUNG` berhasil: sisi masuk A, tambah bobot, c berkurang satu. Baris 12 kembalikan hasil.

**Jalannya.** Pilihan: A→A–B, B→B–D, C→C–D, D→B–D, E→D–E. Dipasang berurutan: C–D 6, B–D 3, A–B 5, B–D 3 (gagal, sudah dipasang), D–E 4. Total 18, c = 1, selesai dalam 1 putaran.

**Simbol.** c jumlah komponen, T sisi termurah tiap komponen, himpunan, A, total, (u, v, w).

### Slide 7: Kompleksitas Teoretis

**Ide.** Hitung kira-kira berapa langkah tiap algoritma bila graf membesar. Hasilnya batas atas, bukan waktu pasti.

**Istilah.** n jumlah titik, m jumlah sisi, log n berapa kali n bisa dibelah dua sampai 1 (1.000 sekitar 10 kali).

**Kruskal.** Urutkan m sisi (m log n), lalu tiap sisi satu GABUNG berbiaya log n (m × log n). Total O(m log n). Ruang O(n + m) karena menyimpan salinan sisi terurut.

**Prim.** Tiap sisi masuk lalu keluar antrean paling banyak sekali (≤ 2m operasi), tiap operasi log n. Total O(m log n). Ruang O(n + m).

**Borůvka.** Paling banyak log n putaran, tiap putaran m sisi dengan 2 CARI-AKAR (m log n). Total O(m log² n), satu faktor log n lebih dari Kruskal dan Prim karena kode mencari komponen dengan CARI-AKAR. Ruang O(n).

**Grafik.** Pada n = 1.000, graf padat jauh lebih berat daripada graf jarang untuk ketiganya. Kruskal dan Prim berbatas atas sama, sehingga mana yang lebih cepat baru terlihat di eksperimen.

### Slide 8: Studi Kasus

**Masalah.** Lima gedung Teknik, enam jalur kandidat, empat pasangan terhalang. Cari jalur yang menghubungkan semua gedung dengan biaya bersih paling kecil (MST).

**Biaya bersih.** Positif bayar sendiri, nol gratis, negatif dapat insentif. Sah karena algoritma hanya memakai urutan bobot.

**Kruskal.** Urutkan: −5, −2, 0, 15, 18, 25. Terima empat pertama (tidak membentuk siklus), lalu berhenti. Total −5 − 2 + 0 + 15 = 8 juta. Prim dan Borůvka sama (Tabel 4.2).

**Batas.** Lima gedung hanya menguji kebenaran dan kegunaan, bukan efisiensi.

### Slide 9: Metode Eksperimen

**Skenario.** Jarang (m = 3n, n 4.000 sampai 64.000), padat (m = n(n − 1)/4, n 200 sampai 1.000), jarang kembar (seperti jarang, bobot hanya 1 sampai 5). Bobot lainnya acak 1 sampai 1.000.000.

**Mengapa padat lebih kecil.** Sisi padat tumbuh kuadrat n. Dengan n kecil, jumlah sisi kedua jenis graf sebanding (sekitar 10 ribu sampai 250 ribu).

**Pembangkit.** Pohon acak dulu (tiap titik disambung ke titik bernomor lebih kecil, pasti terhubung), lalu sisi acak tanpa sisi ganda dan tanpa *loop*. *Seed* 2026.

**Pengukuran.** Satu graf per pasangan skenario dan ukuran, 1 putaran pemanasan, 5 ulangan pada graf yang sama, laporan rata-rata dan simpangan baku sampel. Simpangan baku hanya mengukur gangguan mesin, bukan variasi antar graf.

### Slide 10: Hasil dan Analisis

**Siapa tercepat.** Pada ukuran terbesar: Kruskal tercepat di graf jarang, Prim tanpa daftar tetangga tercepat di graf padat. Di jarang kembar selisihnya kurang dari simpangan baku, jadi belum pasti. Borůvka paling lambat di semua.

**Yang menghambat.** Borůvka 3,3 sampai 4,7 kali Kruskal. Membuat daftar tetangga menambah Prim 44 sampai 50%. Dengan daftar dihitung, keunggulan Prim di graf padat hilang (selisih dalam simpangan baku).

**Dibanding teori.** Rasio waktu terhadap rumus naik 1,29 sampai 2,19 kali untuk Kruskal dan Prim, jadi prediksi 1 tidak terpenuhi. Borůvka melampaui m log² n sedikit di 2 dari 3 skenario. Tidak membantah teorema (batas atas untuk graf sangat besar). Penyebab tidak diuji.

**Seberapa yakin.** Simpangan baku sampai sekitar 41%, satu graf per ukuran di Colab gratis, urutan eksekusi tetap, rentang m hanya 16 sampai 25 kali, hanya dua kepadatan dan Python. Jangan diekstrapolasi.
