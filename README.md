# Tugas Besar Algoritma Komputasi

> **Implementasi, Visualisasi Interaktif, dan Analisis Komparatif Algoritma Minimum Spanning Tree (MST): Kruskal, Prim, dan Borůvka**

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![HTML5 Visualizer](https://img.shields.io/badge/Visualization-HTML5%20Canvas-E34F26?style=for-the-badge&logo=html5&logoColor=white)](#visualisasi-interaktif)

---

## 👤 Informasi Mahasiswa

- **Nama:** Muhammad Alif Qadri
- **NIM:** D082261018
- **Program Studi:** Magister Teknik Informatika
- **Mata Kuliah:** Algoritma Komputasi

---

## 📌 Deskripsi Proyek

Repositori ini memuat pengerjaan Tugas Besar mata kuliah Algoritma Komputasi yang berfokus pada penyelesaian masalah **Minimum Spanning Tree (MST)**. Tiga algoritma klasik diimplementasikan dan dibandingkan secara teoritis maupun empiris:

1. **Algoritma Kruskal**: Menggunakan struktur data *Disjoint-Set Union* (DSU / Himpunan Terpisah) dengan optimasi *path compression* dan *union by rank*.
2. **Algoritma Prim**: Menggunakan representasi graf *adjacency list* dan prioritas penelusuran simpul tetangga terdekat.
3. **Algoritma Borůvka**: Pendekatan paralel/komponen dengan menghubungkan setiap komponen terhubung ke tetangga termurah pada setiap iterasi.

Proyek ini mencakup kode sumber Python murni, visualisasi interaktif berbasis HTML/JavaScript yang dapat dijalankan langsung di peramban, serta notebook Jupyter untuk pengujian benchmark dan pembuatan grafik perbandingan performa.

---

## 📁 Struktur Repositori

```text
├── CODING/
│   ├── README.md                      # Dokumentasi teknis folder CODING
│   ├── requirements.txt               # Daftar pustaka Python yang dibutuhkan
│   ├── jalankan_notebook.bat          # Script otomatisasi lingkungan & notebook (Windows)
│   ├── Kruskal/
│   │   ├── kruskal.py                 # Implementasi Algoritma Kruskal & Disjoint Set
│   │   └── visualisasi-kruskal.html   # Visualisasi interaktif langkah-demi-langkah Kruskal
│   ├── Prim/
│   │   ├── prim.py                    # Implementasi Algoritma Prim
│   │   └── visualisasi-prim.html      # Visualisasi interaktif langkah-demi-langkah Prim
│   ├── Borůvka/
│   │   ├── boruvka.py                 # Implementasi Algoritma Borůvka
│   │   └── visualisasi-boruvka.html   # Visualisasi interaktif langkah-demi-langkah Borůvka
│   └── Eksperimen/
│       └── Tugas_MST_Lokal.ipynb      # Notebook eksperimen, benchmark waktu, CSV, & grafik
├── LAPORAN/
│   └── .gitkeep                       # Direktori untuk laporan tugas besar
└── README.md
```

---

## 🚀 Panduan Menjalankan

### 1. Eksekusi Script Algoritma Satuan (Python CLI)

Setiap algoritma dapat dijalankan langsung secara mandiri tanpa dependensi eksternal (cukup Python 3.9+ bawaan):

```bash
# Algoritma Kruskal
cd CODING/Kruskal
python kruskal.py

# Algoritma Prim
cd ../Prim
python prim.py

# Algoritma Borůvka
cd ../Borůvka
python boruvka.py
```

### 2. Menjalankan Notebook Eksperimen & Benchmark

#### Metode Cepat (Windows)
Cukup jalankan berkas batch otomatis:
```cmd
CODING\jalankan_notebook.bat
```
Script akan otomatis membuat *virtual environment* (`.venv`), memasang dependensi dari `requirements.txt`, dan membuka notebook di browser.

#### Metode Manual (Windows / macOS / Linux)
```bash
cd CODING
python -m venv .venv

# Aktivasi virtual environment:
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
cd Eksperimen
python -m notebook Tugas_MST_Lokal.ipynb
```

> **Tips:** Buka notebook dan pilih **Run > Run All Cells**. Hasil eksekusi berupa tabel CSV di `Eksperimen/hasil/` dan grafik perbandingan performa di `Eksperimen/grafik/` akan digenerate secara otomatis.

---

## 🎨 Visualisasi Interaktif

Tersedia aplikasi web visualisasi interaktif untuk masing-masing algoritma di dalam foldernya:
- `CODING/Kruskal/visualisasi-kruskal.html`
- `CODING/Prim/visualisasi-prim.html`
- `CODING/Borůvka/visualisasi-boruvka.html`

**Fitur Visualisasi:**
- Animasi langkah demi langkah (Step-by-step trace).
- Indikasi sisi yang dievaluasi, diterima (MST), atau ditolak (membentuk siklus).
- Tampilan kode yang sinkron dengan proses eksekusi graf.
- Berjalan sepenuhnya secara lokal di browser modern tanpa perlu server atau koneksi internet.

---

## 📊 Hasil Eksperimen

Hasil eksekusi notebook akan menghasilkan berkas analisis sebagai berikut:
- `Eksperimen/hasil/eksperimen_mentah.csv`: Catatan waktu setiap iterasi pengujian graf acak.
- `Eksperimen/hasil/ringkasan.csv`: Rata-rata dan standar deviasi waktu eksekusi.
- `Eksperimen/hasil/rasio_terhadap_teori.csv`: Analisis perbandingan empiris terhadap kompleksitas teoritis.
- `Eksperimen/grafik/`: Visualisasi grafik kurva waktu komputasi.
