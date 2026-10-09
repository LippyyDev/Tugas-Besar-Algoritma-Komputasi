# Rencana Presentasi Tugas Besar Analisis Algoritma

Analisis Perbandingan Algoritma Kruskal, Prim, dan Borůvka pada *Minimum Spanning Tree* (MST).
Penyaji: Muhammad Alif Qadri. Durasi rencana: 14,5 menit (batas tugas 10 sampai 15 menit).

Status: slide 1 sampai 3 sudah jadi. Slide 4 sampai 12 masih rencana.

## 1. Struktur dan Alokasi Waktu

| No | Slide | Waktu | Status |
|----|-------|-------|--------|
| 1 | Judul | 0,5 mnt | Jadi |
| 2 | Masalah MST dan ide dasar *greedy* (*cut property*) | 2 mnt | Jadi |
| 3 | Algoritma yang dibahas | 0,5 mnt | Jadi |
| 4 | Kruskal | 1,5 mnt | Rencana |
| 5 | Prim | 1,5 mnt | Rencana |
| 6 | Borůvka | 1,5 mnt | Rencana |
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
- `slide1.html`, `slide2.html`: slide yang sudah jadi.
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

Gerak (4 langkah): (1) jaringan titik kecil yang melayang mewakili algoritma *greedy* lain; (2) sampai (4) satu kartu muncul per klik, ditarik oleh garis cahaya dari satu titik di jaringan itu. Setiap kartu menjalankan animasi algoritmanya sendiri secara berulang pada graf yang sama dengan slide 2: Kruskal menguji sisi dari bobot terkecil dan menolak yang membentuk siklus, Prim tumbuh dari titik A, Borůvka memilih sisi termurah tiap titik serentak.

Aliran dari slide 2: langkah terakhir slide 2 menutup dengan "semua titik tersambung, MST berbiaya 18" dan kalimat jembatan pada catatan penyaji nomor 7. Slide 3 menjawab pertanyaan yang muncul setelahnya, yaitu algoritma *greedy* yang mana yang akan dipakai. Setelah itu slide 4 langsung masuk ke Kruskal.

Catatan penyaji (sekitar 30 detik): sebut bahwa *greedy* adalah keluarga algoritma yang besar, lalu sebut dua yang akan dijelaskan (Kruskal dan Prim) dan satu pembanding (Borůvka). Alasan Borůvka dibahas: pembanding tambahan dalam eksperimen, bukan ketentuan tertulis dari dosen (tafsiran penyaji).

## 6. Slide 4 sampai 12 (Rencana)

Belum dikerjakan (slide 3 dijelaskan di bagian 5). Alokasi waktu mengikuti tabel di bagian 1. Isi di bawah adalah arah yang direncanakan dan masih bisa berubah.

| Slide | Arah isi |
|-------|----------|
| 4 Kruskal | Ide urut sisi dari termurah dan tolak yang membentuk siklus. Animasi langkah demi langkah dengan tombol maju dan reset |
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
- Slide 4 sampai 12 belum dibuat.
- Sitasi untuk rumus Cayley dan *cut property* belum diverifikasi.
- Pengujian slide dilakukan di Chromium. Perilaku di layar sentuh belum dicoba.
