# Tugas Besar Pak Abdi: Kruskal, Prim, dan Borůvka (MST), versi lokal

Mahasiswa: Muhammad Alif Qadri (D082261018) | Mata kuliah: Algoritma Komputasi, Magister Teknik Informatika

Folder ini siap ditaruh di `D:\TUGAS BESAR PAK ABDI\CODING`. Semua berjalan di komputer sendiri, tanpa Google Drive.

## Isi folder

```
CODING/
├── README.md
├── requirements.txt            # pustaka yang dipakai
├── jalankan_notebook.bat       # Windows: siapkan lingkungan lalu buka notebook
├── Kruskal/
│   ├── kruskal.py              # HimpunanTerpisah + kruskal()
│   └── visualisasi-kruskal.html
├── Prim/
│   ├── prim.py                 # buat_daftar_tetangga() + prim()
│   └── visualisasi-prim.html
├── Borůvka/
│   ├── boruvka.py              # boruvka() (pembanding), memakai HimpunanTerpisah dari Kruskal
│   └── visualisasi-boruvka.html
└── Eksperimen/
    └── Tugas_MST_Lokal.ipynb   # uji kasus kecil, graf acak, eksperimen, grafik, CSV
```
Folder `Eksperimen/hasil/` (CSV) dan `Eksperimen/grafik/` (gambar) **dibuat otomatis** saat notebook dijalankan.

## Cara menjalankan

### 1. Menjalankan satu algoritma (contoh 4 kota)
Buka terminal di folder algoritmanya, lalu:
```
cd Kruskal
python kruskal.py

cd ..\Prim
python prim.py

cd ..\Borůvka
python boruvka.py
```
Hanya butuh Python 3.9 atau lebih baru (tanpa pustaka tambahan). Keluaran contohnya berupa kabel yang terpilih beserta total biayanya.
Catatan: `boruvka.py` memakai `HimpunanTerpisah` dari `Kruskal/kruskal.py`, jadi folder `Kruskal` harus tetap berada di samping folder `Borůvka`.

### 2. Notebook eksperimen
**Cara termudah (Windows):** klik dua kali `jalankan_notebook.bat`. Berkas itu membuat lingkungan Python (`.venv`), memasang pustaka dari `requirements.txt` (sekali saja, butuh internet), lalu membuka notebook di browser. Di notebook pilih **Run > Run All Cells**.

**Cara manual** (Windows, macOS, atau Linux):
```
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cd Eksperimen
python -m notebook Tugas_MST_Lokal.ipynb
```
Di VS Code: buka `Tugas_MST_Lokal.ipynb`, pilih kernel dari `.venv`, lalu **Run All**.

Lama eksperimen penuh sekitar 1 sampai 3 menit. Untuk uji coba cepat, ubah `MODE_CEPAT = True` di Sel 1 notebook.

### 3. Halaman visualisasi
Klik dua kali berkas `.html` di folder algoritma masing-masing. Dibuka di browser, tidak perlu internet (font memakai cadangan sistem bila offline). Tombol **Selanjutnya** menjalankan satu langkah, tombol **Fokus** (atau tombol F) menyembunyikan panel yang tidak perlu. Kode di halaman sama persis dengan file `.py`.

## Hasil eksperimen yang dihasilkan notebook
| Berkas | Isi |
|---|---|
| `Eksperimen/hasil/eksperimen_mentah.csv` | Waktu setiap ulangan |
| `Eksperimen/hasil/ringkasan.csv` | Rata-rata dan simpangan baku per ukuran |
| `Eksperimen/hasil/rasio_terhadap_teori.csv` | Kesesuaian dengan kurva teori |
| `Eksperimen/grafik/waktu_<skenario>.png` | Grafik waktu dengan kurva teori |

## Pengingat sebelum dikumpulkan
- Hasil waktu dari komputermu sendiri yang dipakai di laporan (Bab 4), bukan angka dari orang lain.
- Hitung ulang sendiri jawaban uji kasus kecil di Sel 7 notebook (draf hitungan ada di sel penjelasannya).
- Isi laporan penggunaan AI di Sel 17 notebook dengan kata-katamu sendiri. Kode di folder ini disusun dengan bantuan AI, jadi pelajari dan tulis ulang versimu sendiri sebelum diklaim sebagai karya sendiri.
- Buat repositori GitHub atau GitLab publik untuk tautan di lampiran laporan.
