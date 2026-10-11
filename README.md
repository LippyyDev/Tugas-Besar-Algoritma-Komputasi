# Tugas Besar Algoritma Komputasi: Minimum Spanning Tree

Implementasi dan analisis algoritma Kruskal dan Prim untuk _Minimum Spanning Tree_ (MST), dengan Borůvka sebagai pembanding.

- Nama: Muhammad Alif Qadri
- NIM: D082261018
- Program studi: Magister Teknik Informatika
- Mata kuliah: Algoritma Komputasi

## Algoritma

| Algoritma            | Ringkasan implementasi                                                                                                       |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Kruskal              | Sisi diurutkan, lalu diterima jika tidak membentuk siklus. Memakai _disjoint set_ dengan _union by rank_ dan _path halving_. |
| Prim                 | Daftar ketetanggaan dan antrean prioritas `heapq` yang menyimpan sisi (versi _lazy_, tanpa _decrease-key_).                  |
| Borůvka (pembanding) | Setiap putaran, setiap komponen memilih sisi keluar termurah, lalu komponen digabung. Sekuensial.                            |

Ketiganya memakai kunci pemutus seri yang sama, yaitu (bobot, simpul terkecil, simpul terbesar). Kode inti ditulis sendiri. `networkx` hanya dipakai sebagai pembanding verifikasi.

## Struktur

```text
CODING/
  UJI_KECIL/     UJI_KECIL.py, README.md
  STUDI_KASUS/   STUDI_KASUS.py, README.md
  EKSPERIMEN/    TUGAS_MST_LOKAL.ipynb (graf acak ber-seed, waktu, grafik), README.md
  README.md      petunjuk teknis rinci
DRAF/        naskah laporan (BAB 1 sampai BAB 5), abstrak, daftar pustaka, dan lampiran
REFERENSI/   salinan referensi dan daftar DOI
PRESENTASI/  slide web (SLIDE1 sampai SLIDE12), INDEX.html, Presentasi_Slide.pdf, README.md
D082261018__Muhammad Alif Qadri_Laporan Tugas Besar Kruskal Prim.pdf   laporan akhir
D082261018__Muhammad Alif Qadri_PPT Tugas Besar Kruskal Prim.pdf      slide presentasi (PDF)
```

## Hasil eksperimen

- Skenario: graf jarang (_m_ = 3*n*), graf padat (_m_ = _n_(_n_ − 1)/4), dan graf jarang berbobot kembar. Masing-masing lima ukuran.
- Setiap ukuran diukur lima kali pada satu graf dengan _seed_ 2026. Hasil dilaporkan sebagai rata-rata dan simpangan baku.
- Dijalankan di Google Colab versi gratis, sehingga waktu bergantung pada mesin dan hasil di komputer lain akan berbeda.
- Grafik waktu terhadap kurva teori ada di `CODING/EKSPERIMEN/GRAFIK/`, data hasil ukur di `CODING/EKSPERIMEN/HASIL/`, dan log sesi di `CODING/EKSPERIMEN/LINGKUNGAN_DAN_LOG.txt`. Folder `HASIL/` dan `GRAFIK/` dibuat ulang otomatis setiap notebook dijalankan.

## Penggunaan AI

Kecerdasan buatan (AI) dipakai sebagai alat bantu pada beberapa bagian berikut. Keputusan isi, arah, dan pemeriksaan akhir tetap dilakukan sendiri oleh penulis.

| Bagian     | Dikerjakan sendiri                                                                                                   | Dibantu AI                                                                                                                  |
| ---------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Lain-lain  | Keputusan dan pemeriksaan atas setiap perubahan di repositori                                                        | Pembuatan _commit_, penulisan README, dan penamaan berkas                                                                   |
| Kode       | Kode inti algoritma Kruskal, Prim, dan Borůvka                                                                       | Bagian eksperimen pada notebook `.ipynb`, yaitu pembangkitan graf acak ber-_seed_                                           |
| Laporan    | Penentuan isi dan pembahasan, penyimpanan hasil kesepakatan dalam draf, verifikasi referensi, dan perhitungan manual | _Brainstorming_, pencarian jurnal atau artikel, perbaikan penulisan yang belum baku, serta perhitungan matematis yang sulit |
| Presentasi | Seluruh ide, penentuan isi, dan rancangan desain tiap slide, serta pemeriksaan dan revisi                            | Pembuatan slide sesuai arahan penulis                                                                                       |

Cara kerja pada tiap bagian:

- **Lain-lain.** AI membantu membuat _commit_, menulis README, dan menamai berkas. Penulis tetap menentukan isi dan memeriksa setiap perubahan.
- **Kode.** Kode inti algoritma ditulis sendiri oleh penulis. AI hanya dipakai pada bagian eksperimen di notebook, yaitu pembangkitan graf acak dengan _seed_.
- **Laporan.** AI tidak diminta menulis seluruh laporan. Isi dan pembahasan didiskusikan terlebih dahulu, dan hasil _brainstorming_ yang disepakati disimpan dalam draf (folder `DRAF/`). AI kemudian mencari jurnal atau artikel yang sesuai. Penulis memverifikasi setiap referensi secara manual, dan referensi yang belum sesuai diganti dengan hasil pencarian lain. AI juga membantu memperbaiki penulisan yang belum baku serta perhitungan matematis yang sulit, sedangkan perhitungan manual tetap dikerjakan penulis sendiri. Setelah draf selesai dikerjakan, AI membantu menyusunnya menjadi dokumen Word sesuai format IEEE.
- **Presentasi.** Seluruh ide berasal dari penulis, mulai dari isi hingga rancangan desain tiap slide. AI hanya mewujudkannya menjadi slide sesuai arahan, dikerjakan satu per satu dan bukan seluruhnya sekaligus. Setiap slide diperiksa dan direvisi oleh penulis bila diperlukan.

## Status

- Naskah Abstrak, Bab 1 sampai 5, dan Lampiran tersedia di `DRAF/`.
- Studi kasus jaringan kabel antar lima gedung memakai biaya bersih ilustrasi (juta rupiah, memuat bobot 0 dan negatif), bukan data keuangan sesungguhnya (Bab 4.1).
