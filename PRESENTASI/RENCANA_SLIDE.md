# Rencana Presentasi Tugas Besar Analisis Algoritma

Analisis Perbandingan Algoritma Kruskal, Prim, dan Borůvka pada *Minimum Spanning Tree* (MST).
Penyaji: Muhammad Alif Qadri. Durasi rencana: 14,5 menit (batas tugas 10 sampai 15 menit).

Status: slide 1 sampai 6 sudah jadi. Slide 7 sampai 12 masih rencana.

## 1. Struktur dan Alokasi Waktu

| No | Slide | Waktu | Status |
|----|-------|-------|--------|
| 1 | Judul | 0,5 mnt | Jadi |
| 2 | Masalah MST dan ide dasar *greedy* (*cut property*) | 2 mnt | Jadi |
| 3 | Algoritma yang dibahas | 0,5 mnt | Jadi |
| 4 | Kruskal | 1,5 mnt | Jadi |
| 5 | Prim | 1,5 mnt | Jadi |
| 6 | Borůvka | 1,5 mnt | Jadi |
| 7 | Contoh manual tiga algoritma | 1,5 mnt | Rencana |
| 8 | Kompleksitas teoretis | 1,5 mnt | Rencana |
| 9 | Implementasi (struktur data, potongan kode inti, verifikasi) | 1 mnt | Rencana |
| 10 | Metode eksperimen | 1 mnt | Rencana |
| 11 | Hasil dan analisis | 1,5 mnt | Rencana |
| 12 | Kesimpulan | 0,5 mnt | Rencana |

Slide 3 menambah 0,5 menit sehingga total menjadi 14,5 menit, masih di dalam batas 10 sampai 15 menit. Bila perlu dipangkas, ambil dari slide 7 atau 8.

Pengelompokan pada bar progres di bawah slide: Pembuka (1), Konsep (2), Algoritma (3 sampai 7), Teori (8), Eksperimen (9 sampai 11), Penutup (12).

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

Kompleksitas tidak dicantumkan di slide ini, karena dibahas di slide 8 setelah diverifikasi.

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

## 6. Slide 7 sampai 12 (Rencana)

Belum dikerjakan (slide 3 sampai 6 dijelaskan di bagian 5, 5b, 5c, dan 5d). Alokasi waktu mengikuti tabel di bagian 1. Isi di bawah adalah arah yang direncanakan dan masih bisa berubah.

| Slide | Arah isi |
|-------|----------|
| 5 Prim | Ide tumbuh dari satu titik dengan sisi termurah yang menyeberang. Animasi serupa dengan Kruskal |
| 6 Borůvka | Ide tiap gugus memilih sisi termurahnya lalu digabung. Alasan ikut dibahas: algoritma pembanding ketiga, tidak ada ketentuan tertulis dari dosen |
| 7 Contoh manual tiga algoritma | Satu graf kecil dijalankan dengan ketiga algoritma, hasil MST yang sama dibandingkan |
| 8 Kompleksitas teoretis | Ringkasan batas waktu ketiga algoritma. Analisis formal hanya untuk Kruskal dan Prim, Borůvka dikutip singkat |
| 9 Implementasi | Struktur data yang dipakai, potongan kode inti, dan cara verifikasi hasil |
| 10 Metode eksperimen | Cara graf acak dibuat, ukuran, pengulangan, dan alat ukur waktu |
| 11 Hasil dan analisis | Grafik hasil eksperimen dan penjelasan sesuai kondisi graf (jarang dan padat) |
| 12 Kesimpulan | Ringkas, bahasa sederhana |

Aturan yang dijaga di seluruh slide: bahasa mudah dipahami, istilah asing ditulis miring, tanpa tanda pisah panjang, dan hanya angka yang bisa dipertanggungjawabkan dari laporan.

## 7. Hal yang Masih Terbuka

- NIM dan nama dosen di slide 1 belum diisi.
- Slide 7 sampai 12 belum dibuat.
- Sitasi untuk rumus Cayley dan *cut property* belum diverifikasi.
- Pengujian slide dilakukan di Chromium. Perilaku di layar sentuh belum dicoba.

## 8. Panduan Belajar: Penjelasan Mudah Slide 4 sampai 6

Bagian ini untuk dipelajari penyaji, bukan untuk dibacakan. Semua angka memakai graf yang sama dengan slide: titik A sampai E, sisi A–B 5, A–C 8, B–C 11, B–D 3, C–D 6, D–E 4, C–E 9. MST yang benar berisi 4 sisi dengan total 18. Pseudocode di slide 5 dan 6 adalah ringkasan dari Bab 3 (lihat 5c dan 5d), jadi bila ada selisih kata, rujukan resminya tetap Pseudocode 3.2 sampai 3.4.

### 8.1 Dasar yang Sama untuk Ketiganya

- **Spanning tree**: sekumpulan sisi yang menghubungkan semua titik tanpa ada lingkaran. Untuk 5 titik, jumlah sisinya selalu 4, yaitu n − 1.
- **MST** adalah *spanning tree* dengan jumlah bobot terkecil.
- **Siklus** adalah lingkaran. Sisi yang membuat lingkaran tidak pernah berguna, karena dua titik itu sudah tersambung lewat jalan lain.
- Ketiga algoritma bersifat *greedy*: di setiap langkah mengambil pilihan yang paling murah dan aman, lalu tidak pernah menarik kembali pilihan itu. Alasan aman: sisi termurah yang menyeberangi sebuah pembagian titik (*cut property*, slide 2) selalu boleh masuk MST.
- Bila ada dua sisi berbobot sama, urutannya ditentukan kunci κ: bobot dulu, lalu simpul terkecil, lalu simpul terbesar. Pada graf contoh tidak ada bobot kembar, jadi aturan ini tidak terlihat.
- Beda cara berpikir: **Kruskal** melihat seluruh sisi dari termurah, **Prim** menumbuhkan satu pohon dari satu titik, **Borůvka** membuat semua titik atau kelompok memilih sisinya sekaligus.

### 8.2 Slide 4: Kruskal

**Ide satu kalimat.** Urutkan semua sisi dari yang termurah, lalu ambil satu per satu asalkan tidak membuat lingkaran.

**Analogi.** Membangun jalan antar desa. Anda mulai dari rencana jalan paling murah. Jalan baru dibangun hanya bila menghubungkan dua kelompok desa yang belum tersambung. Jalan yang menghubungkan dua desa yang sudah tersambung dibatalkan, karena sia-sia.

**Alat bantu: kelompok (himpunan).** Awalnya tiap titik adalah kelompok sendiri: {A} {B} {C} {D} {E}. Fungsi `GABUNG(u, v)` bekerja dua hal sekaligus: mengecek apakah u dan v sudah satu kelompok, dan bila belum, menggabungkan kedua kelompoknya. Hasilnya BENAR bila berhasil digabung dan SALAH bila sudah satu kelompok (artinya akan membuat lingkaran).

**Pseudocode baris demi baris** (Pseudocode 3.2).

| Baris | Arti dalam bahasa biasa |
|-------|--------------------------|
| 1 | Urutkan semua sisi dari bobot terkecil (E′ adalah E yang sudah urut) |
| 2 | Siapkan kelompok (tiap titik sendiri), daftar sisi terpilih A kosong, total biaya 0 |
| 3 | Untuk setiap sisi dari yang termurah, kerjakan baris 4 sampai 6 |
| 4 | Bila ujung sisi (u dan v) beda kelompok, gabungkan |
| 5 | Sisi masuk ke A, tambahkan bobotnya ke total |
| 6 | Bila A sudah berisi n − 1 sisi, berhenti |
| 7 | Bila setelah semua sisi habis A belum n − 1, graf tidak terhubung (galat) |
| 8 | Kembalikan A dan total |

**Jalannya pada graf contoh.** Urutan sisi: B–D 3, D–E 4, A–B 5, C–D 6, A–C 8, C–E 9, B–C 11.

| Sisi | Kelompok sebelum | Hasil | Total |
|------|------------------|-------|-------|
| B–D 3 | B dan D beda | diterima, jadi {B, D} | 3 |
| D–E 4 | D di {B, D}, E sendiri | diterima, jadi {B, D, E} | 7 |
| A–B 5 | A sendiri, B di {B, D, E} | diterima, jadi {A, B, D, E} | 12 |
| C–D 6 | C sendiri, D di {A, B, D, E} | diterima, jadi {A, B, C, D, E} | 18 |

Setelah C–D, A berisi 4 sisi = n − 1, jadi perulangan berhenti. Sisa A–C 8, C–E 9, B–C 11 tidak pernah diperiksa.

**Mengapa klik terakhir bertuliskan "seandainya".** Pada graf ini kode berhenti sebelum ada sisi yang ditolak. Klik terakhir hanya memperlihatkan apa yang akan terjadi bila A–C 8 diperiksa: A dan C sudah satu kelompok (tersambung lewat A–B, B–D, C–D), jadi `GABUNG` gagal dan sisi ditolak karena membuat lingkaran.

**Panel Arti simbol.** E semua sisi, E′ sisi yang sudah urut, κ aturan urut, himpunan kelompok tiap titik, A sisi MST terpilih, total jumlah bobot di A, (u, v, w) ujung dan bobot sisi yang sedang diperiksa, n jumlah titik.

**Hal yang paling sering salah paham.**
- Kruskal tidak menumbuhkan satu pohon. Selama berjalan, sisi terpilih bisa membentuk beberapa potongan terpisah (hutan), dan baru menyatu di akhir. Pada contoh ini potongannya langsung {B, D}, lalu membesar.
- Berhenti di n − 1 sisi, bukan setelah semua sisi diperiksa.

### 8.3 Slide 5: Prim

**Ide satu kalimat.** Mulai dari satu titik, lalu terus perluas satu pohon dengan sisi termurah yang menghubungkan pohon itu ke titik di luarnya.

**Analogi.** Membangun jaringan listrik dari satu gardu. Setiap kali, tarik kabel termurah dari jaringan yang sudah ada menuju rumah yang belum teraliri.

**Alat bantu: antrean Q.** Antrean prioritas yang menyimpan sisi calon. Yang termurah selalu keluar lebih dulu. Q berisi sisi yang menyentuh pohon. Sisi lama yang kedua ujungnya sudah di pohon bisa tertinggal di Q, lalu dibuang saat keluar (baris 5 di slide).

**Pseudocode (ringkasan Pseudocode 3.3).**

| Baris | Arti dalam bahasa biasa |
|-------|--------------------------|
| 1 | Tandai semua titik belum masuk, lalu masukkan titik awal s ke pohon. A kosong, total 0 |
| 2 | Masukkan sisi dari s ke tetangganya ke dalam Q |
| 3 | Selama Q tidak kosong dan A belum n − 1 sisi, ulangi baris 4 sampai 8 |
| 4 | Keluarkan sisi termurah dari Q. Sisi ditulis (w, k, b): bobot, dan dua ujungnya |
| 5 | Bila kedua ujungnya sudah di pohon, sisi dilewati (akan membuat lingkaran) |
| 6 | Ujung yang belum masuk disebut tujuan. Tandai tujuan sebagai masuk pohon |
| 7 | Sisi masuk ke A, tambahkan bobotnya ke total |
| 8 | Masukkan ke Q sisi dari tujuan ke titik yang belum masuk |
| 9 | Bila A belum n − 1 sisi, graf tidak terhubung (galat) |
| 10 | Kembalikan A dan total |

**Jalannya pada graf contoh, mulai dari A.**

| Putaran | Isi Q sebelum keluar | Sisi keluar | Tujuan | Total | Sisi baru masuk Q |
|---------|----------------------|-------------|--------|-------|--------------------|
| awal | A–B 5, A–C 8 | | | 0 | |
| 1 | A–B 5, A–C 8 | A–B 5 | B | 5 | B–D 3, B–C 11 |
| 2 | B–D 3, A–C 8, B–C 11 | B–D 3 | D | 8 | C–D 6, D–E 4 |
| 3 | D–E 4, C–D 6, A–C 8, B–C 11 | D–E 4 | E | 12 | C–E 9 |
| 4 | C–D 6, A–C 8, C–E 9, B–C 11 | C–D 6 | C | 18 | tidak ada |

Setelah putaran 4, A berisi 4 sisi, perulangan berhenti. Sisa Q (A–C 8, C–E 9, B–C 11) tidak diproses. Hasil sama dengan Kruskal (A–B, B–D, D–E, C–D, total 18), hanya urutan terpilihnya berbeda.

**Panel Arti simbol.** s titik awal (A), n jumlah titik, masuk titik yang sudah di pohon, Q antrean sisi, (w, k, b) sisi yang baru keluar dari Q, asal dan tujuan ujung lama dan ujung baru, A sisi terpilih, total jumlah bobot.

**Mengapa Q berisi sisi, bukan titik.** Rumusan Prim yang berbasis titik membutuhkan operasi menurunkan nilai kunci titik di antrean, yang tidak disediakan `heapq` Python. Karena itu implementasi ini menyimpan sisi di Q (alasan ini tertulis di Bab 3, subbab 3.2.3).

**Klik terakhir "seandainya".** Sama seperti Kruskal: bila A–C 8 keluar dari Q, kedua ujungnya sudah di pohon sehingga dilewati (baris 5). Pada kode sebenarnya perulangan sudah berhenti sebelum itu.

**Beda utama dengan Kruskal.** Prim selalu satu pohon yang membesar dari A. Kruskal boleh punya beberapa potongan lebih dulu. Prim memeriksa sisi lewat Q, Kruskal lewat daftar terurut.

### 8.4 Slide 6: Borůvka

**Ide satu kalimat.** Bekerja dalam putaran: di tiap putaran, setiap kelompok sekaligus memilih sisi termurah yang keluar darinya, lalu semua pilihan digabung.

**Analogi.** Setiap desa menunjuk jalan termurah ke desa tetangga. Semua penunjukan dikerjakan serentak, lalu jalan-jalan itu dibangun. Desa yang tersambung membentuk kelompok baru, dan putaran berikutnya diulang antar kelompok.

**Istilah.** *Komponen* adalah kelompok titik yang sudah tersambung. Awalnya tiap titik adalah komponen sendiri (c = n = 5). Tabel T menyimpan pilihan: komponen → sisi termurah yang keluar darinya.

**Pseudocode (ringkasan Pseudocode 3.4).**

| Baris | Arti dalam bahasa biasa |
|-------|--------------------------|
| 1 | Siapkan kelompok, A kosong, total 0, jumlah komponen c = n |
| 2 | Selama komponen lebih dari satu, kerjakan satu putaran (baris 3 sampai 11) |
| 3 | Kosongkan tabel T |
| 4 | Periksa setiap sisi (u, v, w) pada graf |
| 5 | Bila u dan v satu komponen, lewati sisi itu |
| 6 | Bila sisi ini lebih murah dari pilihan yang tersimpan, jadikan pilihan untuk kedua komponen ujungnya |
| 7 | Bila T kosong padahal komponen masih banyak, graf tidak terhubung (galat) |
| 8 | Ambil pilihan di T satu per satu |
| 9 | Bila `GABUNG(u, v)` berhasil |
| 10 | Sisi masuk ke A, tambahkan bobotnya ke total |
| 11 | Kurangi c satu |
| 12 | Kembalikan A dan total |

**Jalannya pada graf contoh (hanya 1 putaran).** Pilihan tiap komponen, dari sisi yang keluar darinya:

| Komponen | Sisi keluar (bobot) | Pilihan termurah |
|----------|---------------------|-------------------|
| A | A–B 5, A–C 8 | A–B 5 |
| B | A–B 5, B–D 3, B–C 11 | B–D 3 |
| C | A–C 8, C–D 6, C–E 9, B–C 11 | C–D 6 |
| D | B–D 3, C–D 6, D–E 4 | B–D 3 |
| E | D–E 4, C–E 9 | D–E 4 |

Sisi B–D 3 dipilih dua komponen sekaligus (B dan D). Pada kode, T berurutan C, D, A, B, E (urutan sisi pertama kali ditemui), sehingga pemasangannya:

| Pilihan | Hasil | c | Total |
|---------|-------|---|-------|
| C: C–D 6 | berhasil | 4 | 6 |
| D: B–D 3 | berhasil | 3 | 9 |
| A: A–B 5 | berhasil | 2 | 14 |
| B: B–D 3 | gagal, B dan D sudah satu komponen (sisi sudah dipasang dari pilihan D) | 2 | 14 |
| E: D–E 4 | berhasil | 1 | 18 |

Setelah c = 1, perulangan berhenti. Total 18, sama dengan Kruskal dan Prim.

**Panel Arti simbol.** E semua sisi, n jumlah titik, c jumlah komponen, himpunan komponen tiap titik, T sisi termurah tiap komponen, (u, v, w) sisi yang sedang diproses, A sisi terpilih, total jumlah bobot.

**Mengapa B–D tidak dipasang dua kali.** Dua komponen bisa memilih sisi yang sama. `GABUNG` kedua kalinya mengembalikan SALAH, sehingga sisi itu tidak masuk A dua kali. Pada slide ini penolakan itu benar-benar terjadi di kode, sehingga tidak diberi kata "seandainya".

**Mengapa hanya 1 putaran.** Pada graf kecil ini pilihan semua komponen sudah cukup untuk menyambung seluruh titik. Menurut dokumentasi di `boruvka.py`, jumlah komponen menyusut sedikitnya separuh per putaran. Pada graf lain bisa dibutuhkan lebih dari satu putaran, lalu pilihan diulang antar komponen yang lebih besar.

### 8.5 Perbandingan Singkat Ketiganya

| | Kruskal | Prim | Borůvka |
|---|---------|------|---------|
| Unit yang diproses | Sisi, urut dari termurah | Titik baru lewat sisi termurah di Q | Seluruh komponen serentak |
| Bentuk selama berjalan | Beberapa potongan bergabung | Satu pohon membesar | Banyak komponen bergabung per putaran |
| Alat bantu | Himpunan terpisah (*disjoint set*) | Antrean prioritas Q | Himpunan terpisah dan tabel T |
| Cara mendeteksi lingkaran | `GABUNG` gagal | Kedua ujung sudah masuk pohon | `GABUNG` gagal |
| Berhenti saat | A berisi n − 1 sisi | A berisi n − 1 sisi | Komponen tinggal satu |
| Urutan sisi pada contoh | B–D, D–E, A–B, C–D | A–B, B–D, D–E, C–D | C–D, B–D, A–B, D–E |
| Total | 18 | 18 | 18 |

Ketiganya menghasilkan total yang sama karena semuanya benar. Bila bobot semua sisi berbeda, MST-nya tunggal. Perbedaan baru terasa pada kecepatan, yang dibahas di slide 8 dan 11, bukan di bagian ini.

### 8.6 Kemungkinan Pertanyaan Penguji

1. *Mengapa Kruskal berhenti sebelum semua sisi diperiksa?* Karena MST dari n titik selalu n − 1 sisi. Setelah terkumpul, sisa sisi pasti hanya membuat lingkaran.
2. *Apa bedanya Kruskal dan Prim?* Kruskal memilih dari seluruh sisi yang terurut dan boleh membentuk potongan terpisah dulu. Prim selalu memperbesar satu pohon dari titik awal.
3. *Apa gunanya `GABUNG`?* Satu operasi yang mengecek dan menggabung sekaligus. Hasil SALAH berarti akan membuat lingkaran.
4. *Mengapa Prim di sini memakai antrean berisi sisi?* Karena `heapq` tidak punya operasi menurunkan kunci. Entri usang di Q dibuang saat keluar.
5. *Mengapa Borůvka dibahas?* Sebagai algoritma pembanding tambahan di eksperimen. Ini bukan ketentuan tertulis dari dosen, melainkan tafsiran (lihat 5).
6. *Mengapa hasil ketiganya sama padahal urutannya beda?* Semuanya mengikuti prinsip *cut property*, sehingga tiap sisi yang diambil aman masuk MST.
7. *Mengapa ada klik "seandainya"?* Karena pada graf contoh, kode Kruskal dan Prim berhenti sebelum sisi bermasalah diperiksa. Klik itu hanya ilustrasi, dan diberi label jelas.
8. *Bagaimana bila graf tidak terhubung?* Ketiga kode melaporkan galat "Graf tidak terhubung". Pemeriksaan ini hanya pengaman, karena masukan diasumsikan terhubung (butir 1 subbab 1.4 laporan).

Kompleksitas waktu sengaja tidak dibahas di bagian ini, karena akan dibahas di slide 8 setelah diverifikasi dengan literatur.
