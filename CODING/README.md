# Tugas Besar Pak Abdi: Kruskal, Prim, dan Borůvka (MST), versi lokal

Mahasiswa: Muhammad Alif Qadri (D082261018) | Mata kuliah: Algoritma Komputasi, Magister Teknik Informatika

Folder ini siap ditaruh di `D:\TUGAS BESAR PAK ABDI\CODING`. Bisa dijalankan di komputer sendiri atau di Google Colab, dengan hasil disimpan ke folder khusus di Google Drive.

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
    ├── Tugas_MST_Lokal.ipynb   # uji kasus kecil, studi kasus, graf acak, eksperimen, grafik, CSV
    ├── PENJELASAN_NOTEBOOK.md  # penjelasan rinci tiap sel, perhitungan manual, keputusan desain, draf laporan AI
    └── data/
        └── studi_kasus_gedung_unhas.csv   # data tetap studi kasus (5 gedung); ganti angka ILUSTRASI dengan hasil ukur
```
Folder `hasil/` (CSV), `grafik/` (gambar), dan `data/`, serta berkas `lingkungan_dan_log.txt`, **dibuat otomatis** saat notebook dijalankan: di samping notebook (lokal) atau di folder Google Drive (Colab). Folder itu tidak disimpan di repositori; grafik yang dipakai laporan ada di `../DRAF/gambar/`.

## Cara menjalankan

### 1. Menjalankan satu algoritma (contoh graf 4 simpul)
Buka terminal di folder algoritmanya, lalu:
```
cd Kruskal
python kruskal.py

cd ..\Prim
python prim.py

cd ..\Borůvka
python boruvka.py
```
Hanya butuh Python 3.9 atau lebih baru (tanpa pustaka tambahan). Keluaran contohnya berupa sisi MST yang terpilih beserta total bobotnya.
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

Lama eksperimen penuh sekitar 1 sampai 3 menit. Untuk uji coba cepat, ubah `MODE_CEPAT = True` di Sel 1 notebook (hasilnya jangan dipakai di laporan).

### Google Colab dan Google Drive
Unggah `Tugas_MST_Lokal.ipynb` ke Google Drive, buka dengan Colab, lalu **Runtime > Run all** dan izinkan akses Drive di Sel 2. Semua hasil disimpan ke `My Drive/TUGAS BESAR PAK ABDI/HASIL_EKSPERIMEN` (nama folder bisa diubah di Sel 2), berisi `hasil/`, `grafik/`, `data/`, dan `lingkungan_dan_log.txt` (spesifikasi mesin dan seluruh keluaran teks). Sel 18 dijalankan paling akhir supaya semuanya tersinkron.
Waktu yang terukur di Colab adalah waktu mesin virtual Google yang dipakai bersama, jadi spesifikasinya harus ditulis di Bab 4.1. Untuk komputer sendiri dengan Google Drive for Desktop, isi `FOLDER_DRIVE_LOKAL` di Sel 2.

### Peta bagian notebook
| Bagian | Sel | Isi | Seed |
|---|---|---|---|
| A. Uji kasus kecil | 7 (persiapan), 7.1 Kasus 1, 7.2 Kasus 2, 7.3 Kasus 3, 7.4 Kasus 4 (tak terhubung, harus `ValueError`), 7.5 rekap | Data tetap, bisa dicek tangan | Tidak |
| B. Studi kasus | 7B | 5 gedung FT Unhas | Tidak |
| C. Eksperimen waktu | 8 sampai 18 | Graf acak, 5 ukuran x 5 ulangan | Ya (2026) |

### Studi kasus ilustratif (Sel 7B)
Sel 7B menjalankan ketiga algoritma pada jaringan kabel antar 5 gedung Fakultas Teknik Unhas dari `Eksperimen/data/studi_kasus_gedung_unhas.csv`. Datanya tetap, jadi **tanpa seed**. Kolom `keterangan` berisi ILUSTRASI: jaraknya angka contoh, bukan hasil pengukuran, dan Bab 4.1 menyebutnya demikian. Jika kelak diganti dengan jarak hasil ukur, catat sumbernya dan ubah Bab 4.1 serta judul bagian ini.

### 3. Halaman visualisasi
Klik dua kali berkas `.html` di folder algoritma masing-masing. Dibuka di browser, tidak perlu internet (font memakai cadangan sistem bila offline). Tombol **Selanjutnya** menjalankan satu langkah, tombol **Fokus** (atau tombol F) menyembunyikan panel yang tidak perlu. Kode di halaman sama persis dengan file `.py`.

## Pustaka
| Pustaka | Dipakai untuk |
|---|---|
| `random`, `time`, `math`, `heapq`, `csv`, `os`, `sys`, `platform`, `statistics`, `gc` (bawaan Python) | Pembuat graf, pengukuran, antrean prioritas (alat bantu Prim) |
| `pandas`, `numpy` | Ringkasan data, rata-rata dan simpangan baku |
| `matplotlib` | Grafik |
| `networkx` | **Hanya verifikasi** (Sel 10), tidak dipakai di dalam algoritma |

## Contoh keluaran (uji kasus kecil, Sel 7.1 sampai 7.5)
```
[LOLOS] Kasus 1: 4 simpul biasa (satu sisi ditolak) | total = 7 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 2: 5 simpul, bobot 0 dan negatif | total = 5 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 3: bobot kembar (total dan himpunan sisi) | total = 6 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 4: graf tak terhubung (harus ValueError) | ketiganya melempar ValueError
```
Penjelasan rinci tiap sel, perhitungan manual kasus uji, dan keputusan desain: `Eksperimen/PENJELASAN_NOTEBOOK.md`.

## Hasil eksperimen yang dihasilkan notebook
| Berkas | Isi |
|---|---|
| `Eksperimen/hasil/eksperimen_mentah.csv` | Waktu setiap ulangan |
| `Eksperimen/hasil/ringkasan.csv` | Rata-rata dan simpangan baku per ukuran |
| `Eksperimen/hasil/rasio_terhadap_teori.csv` | Kesesuaian dengan kurva teori |
| `Eksperimen/grafik/waktu_<skenario>.png` | Grafik waktu dengan kurva teori |
| `Eksperimen/lingkungan_dan_log.txt` | Spesifikasi mesin dan seluruh keluaran teks notebook |

## Pengingat sebelum dikumpulkan
- Pakai hasil waktu dari eksperimen yang kamu jalankan sendiri di laporan (Bab 4), bukan angka dari orang lain. Catat mesinnya (Colab atau komputer sendiri) sesuai `lingkungan_dan_log.txt`.
- Hitung ulang sendiri jawaban uji kasus kecil di Sel 7.1 sampai 7.4 notebook (draf perhitungan ada di `Eksperimen/PENJELASAN_NOTEBOOK.md`, bagian 6.7).
- Isi laporan penggunaan AI (draf di `Eksperimen/PENJELASAN_NOTEBOOK.md`, bagian 6.17) dengan kata-katamu sendiri. Kode di folder ini disusun dengan bantuan AI, jadi pelajari dan tulis ulang versimu sendiri sebelum diklaim sebagai karya sendiri.
- Buat repositori GitHub atau GitLab publik untuk tautan di lampiran laporan.
