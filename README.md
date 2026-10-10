# Tugas Besar Algoritma Komputasi: Minimum Spanning Tree

Implementasi dan analisis algoritma Kruskal dan Prim untuk *Minimum Spanning Tree* (MST), dengan Borůvka sebagai pembanding.

- Nama: Muhammad Alif Qadri
- NIM: D082261018
- Program studi: Magister Teknik Informatika
- Mata kuliah: Algoritma Komputasi

## Algoritma

| Algoritma | Ringkasan implementasi |
|---|---|
| Kruskal | Sisi diurutkan, lalu diterima jika tidak membentuk siklus. Memakai *disjoint set* dengan *union by rank* dan *path halving*. |
| Prim | Daftar ketetanggaan dan antrean prioritas `heapq` yang menyimpan sisi (versi *lazy*, tanpa *decrease-key*). |
| Borůvka (pembanding) | Setiap putaran, setiap komponen memilih sisi keluar termurah, lalu komponen digabung. Sekuensial. |

Ketiganya memakai kunci pemutus seri yang sama, yaitu (bobot, simpul terkecil, simpul terbesar). Kode inti ditulis sendiri. `networkx` hanya dipakai sebagai pembanding verifikasi.

## Struktur

```text
CODING/
  Contoh_Dasar/  Kruskal/, Prim/, Borůvka/ (kode .py + visualisasi .html)
  Uji_Kecil/     uji_kecil.py, PENJELASAN_UJI_KECIL.md
  Studi_Kasus/   studi_kasus.py, studi_kasus_gedung_unhas.csv, PENJELASAN_STUDI_KASUS.md
  Eksperimen/    Tugas_MST_Lokal.ipynb (graf acak ber-seed, waktu, grafik), PENJELASAN_NOTEBOOK.md
  bantu_mst.py   alat bantu bersama Uji_Kecil dan Studi_Kasus
  README.md      petunjuk teknis rinci
DRAF/        naskah laporan (BAB 1 sampai BAB 5) dan gambar/
REFERENSI/   salinan referensi dan daftar DOI
LAPORAN/     laporan akhir (PDF)
```

## Menjalankan

Contoh dasar, uji kasus kecil, dan studi kasus (Python 3.9 atau lebih baru, tanpa pustaka tambahan):

```bash
cd CODING/Contoh_Dasar/Kruskal && python kruskal.py     # juga prim.py dan boruvka.py di folder masing-masing
cd CODING/Uji_Kecil && python uji_kecil.py
cd CODING/Studi_Kasus && python studi_kasus.py
```

Notebook eksperimen (graf acak ber-seed dan pengukuran waktu):

```bash
cd CODING
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cd Eksperimen
python -m notebook Tugas_MST_Lokal.ipynb
```

Di Windows, `CODING\jalankan_notebook.bat` melakukan langkah notebook di atas. Petunjuk Google Colab ada di `CODING/README.md`.

## Hasil eksperimen

- Skenario: graf jarang (*m* = 3*n*), graf padat (*m* = *n*(*n* − 1)/4), dan graf jarang berbobot kembar. Masing-masing lima ukuran.
- Setiap ukuran diukur lima kali pada satu graf dengan *seed* 2026. Hasil dilaporkan sebagai rata-rata dan simpangan baku.
- Dijalankan di Google Colab versi gratis, sehingga waktu bergantung pada mesin dan hasil di komputer lain akan berbeda.
- Grafik waktu terhadap kurva teori ada di `DRAF/gambar/`. Berkas `hasil/` dan `grafik/` dibuat otomatis saat notebook dijalankan dan tidak disimpan di repositori ini.

## Penggunaan AI

Kecerdasan buatan (AI) dipakai sebagai alat bantu pada tiga bagian berikut. Keputusan isi, arah, dan pemeriksaan akhir tetap dilakukan sendiri oleh penulis.

| Bagian | Dikerjakan sendiri | Dibantu AI |
|---|---|---|
| Kode | Kode inti algoritma Kruskal, Prim, dan Borůvka | Bagian eksperimen pada notebook `.ipynb`, yaitu pembangkitan graf acak ber-*seed* |
| Laporan | Penentuan isi dan pembahasan, verifikasi referensi, dan perhitungan manual | *Brainstorming*, pencarian jurnal atau artikel, perbaikan penulisan yang belum baku, dan perhitungan matematis yang sulit |
| Presentasi | Penentuan isi dan rancangan desain tiap slide, serta pemeriksaan dan revisi | Pembuatan slide sesuai arahan penulis |

Cara kerja pada tiap bagian:

- **Kode.** Kode inti algoritma ditulis sendiri oleh penulis. AI hanya dipakai pada bagian eksperimen di notebook, yaitu pembangkitan graf acak dengan *seed*.
- **Laporan.** AI tidak diminta menulis seluruh laporan. Isi dan pembahasan didiskusikan terlebih dahulu, kemudian AI mencari jurnal atau artikel yang sesuai. Penulis memverifikasi setiap referensi secara manual, dan referensi yang belum sesuai diganti dengan hasil pencarian lain. AI juga membantu memperbaiki penulisan yang belum baku serta perhitungan matematis yang sulit, sedangkan perhitungan manual tetap dikerjakan penulis sendiri.
- **Presentasi.** Penulis menentukan isi dan desain, lalu AI membuat slide satu per satu, bukan seluruhnya sekaligus. Setiap slide diperiksa dan direvisi oleh penulis bila diperlukan.

## Status

- Naskah Abstrak, Bab 1 sampai 5, dan Lampiran tersedia di `DRAF/`.
- Studi kasus jaringan kabel antar lima gedung memakai biaya bersih ilustrasi (juta rupiah, memuat bobot 0 dan negatif), bukan data keuangan sesungguhnya (Bab 4.1).
