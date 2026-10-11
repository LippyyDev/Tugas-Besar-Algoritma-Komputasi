# PRESENTASI

Slide web 12 halaman untuk Tugas Besar Analisis Algoritma (Kruskal, Prim, Borůvka pada MST). Penyaji: Muhammad Alif Qadri. Batas tugas 10 sampai 15 menit.

## Cara pakai

Buka `INDEX.html` (daftar slide dan pratinjau) atau langsung `SLIDE1.html`. Tanpa internet pun jalan (KaTeX ada di `ASET/KATEX/`).

| Aksi | Fungsi |
|---|---|
| Panah kiri/kanan, Spasi, PageUp/PageDown, klik tepi kiri/kanan layar | Mundur atau maju |
| Kursor ke bawah layar | Kotak navigasi |
| `R` / `F` / `T` / `I` | Reset animasi / layar penuh / mode terang atau gelap / ke `INDEX.html` |

Maju di langkah terakhir pindah ke slide berikutnya, mundur di langkah pertama ke slide sebelumnya. Panggung tetap 1920 × 1080 dan diskalakan otomatis. Tema dan transisi tirai ada di `ASET/tema.css` dan `ASET/tema.js`. Aturan desain ada di `DESIGN.md`. PDF semua slide: `Presentasi_Slide.pdf`.

Menambah slide: buat `SLIDEN.html`, set `ready:true` di `INDEX.html`, isi `NEXT_SLIDE` pada slide sebelumnya.

## Isi per slide

| No | Slide | Waktu | Klik | Isi utama | Sumber di laporan |
|---|---|---|---|---|---|
| 1 | Judul | 0,5 mnt | - | Judul, tiga algoritma, penyaji, NIM, dosen | |
| 2 | Apa itu MST | 2 | 9 | Graf 5 titik (MST 18 dari total 46), 21 pohon rentang, *cut property* | Bab 2 |
| 3 | Algoritma yang dibahas | 0,5 | 4 | Kruskal dan Prim (utama), Borůvka (pembanding) | |
| 4 | Kruskal | 1,5 | 7 | Pseudocode 3.2, hasil B–D, D–E, A–B, C–D = 18 | Bab 3 |
| 5 | Prim | 1,5 | 21 | Pseudocode 3.3, urutan A–B, B–D, D–E, C–D = 18 | Bab 3 |
| 6 | Borůvka | 1,5 | 16 | Pseudocode 3.4, 1 putaran, total 18 | Bab 3 |
| 7 | Studi kasus 5 gedung | 1 | 5 | Adegan 3D, tiga metode sama: 8 juta | Bab 4.1 (Tabel 4.1, 4.2) |
| 8 | Kompleksitas teoretis | 3 | 11 | Kruskal dan Prim *O*(m log n), Borůvka *O*(m log² n) | Bab 3.2, 3.4 |
| 9 | Metode eksperimen | 1 | 4 | Tiga skenario, pembangkit graf, *seed* 2026, 225 pengukuran | Bab 4.4 (Tabel 4.5) |
| 10 | Hasil dan analisis | 1,5 | 3 | Pemenang per skenario, Borůvka 3,3 sampai 4,7 kali Kruskal | Bab 4.6 (Tabel 4.6 sampai 4.10) |
| 11 | Tanya jawab | 0,25 | - | Kutipan Mayer, grafik tanda tanya | |
| 12 | Kesimpulan | 0,5 | 5 | Ringkasan Bab 5, batas hasil, terima kasih | Bab 5 |

Total 14,75 menit. Bila perlu dipangkas, ambil dari slide 4 sampai 6.
