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
  Kruskal/  kruskal.py, visualisasi-kruskal.html
  Prim/     prim.py, visualisasi-prim.html
  Borůvka/  boruvka.py, visualisasi-boruvka.html
  Eksperimen/
    Tugas_MST_Lokal.ipynb          notebook uji kasus kecil dan eksperimen waktu
    PENJELASAN_NOTEBOOK.md         penjelasan tiap sel
    data/studi_kasus_gedung_unhas.csv
  README.md                        petunjuk teknis rinci
DRAF/        naskah laporan (BAB 1 sampai BAB 4) dan gambar/
REFERENSI/   salinan referensi dan daftar DOI
LAPORAN/     laporan akhir (PDF)
```

## Menjalankan

Satu algoritma (Python 3.9 atau lebih baru, tanpa pustaka tambahan):

```bash
cd CODING/Kruskal && python kruskal.py
cd ../Prim && python prim.py
cd ../Borůvka && python boruvka.py
```

Notebook eksperimen:

```bash
cd CODING
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cd Eksperimen
python -m notebook Tugas_MST_Lokal.ipynb
```

Di Windows, `CODING\jalankan_notebook.bat` melakukan langkah di atas. Petunjuk Google Colab ada di `CODING/README.md`.

## Hasil eksperimen

- Skenario: graf jarang (*m* = 3*n*), graf padat (*m* = *n*(*n* − 1)/4), dan graf jarang berbobot kembar. Masing-masing lima ukuran.
- Setiap ukuran diukur lima kali pada satu graf dengan *seed* 2026. Hasil dilaporkan sebagai rata-rata dan simpangan baku.
- Dijalankan di Google Colab versi gratis, sehingga waktu bergantung pada mesin dan hasil di komputer lain akan berbeda.
- Grafik waktu terhadap kurva teori ada di `DRAF/gambar/`. Berkas `hasil/` dan `grafik/` dibuat otomatis saat notebook dijalankan dan tidak disimpan di repositori ini.

## Status

- Naskah Bab 1 sampai 4 tersedia di `DRAF/`. Abstrak, Bab 5, dan Lampiran belum ditulis.
- Studi kasus jaringan kabel antar lima gedung memakai biaya bersih ilustrasi (juta rupiah, memuat bobot 0 dan negatif), bukan data keuangan sesungguhnya (Bab 4.1).
