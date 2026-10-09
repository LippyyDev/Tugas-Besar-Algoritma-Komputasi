# Tugas Besar Pak Abdi: Kruskal, Prim, dan Borůvka (MST), versi lokal

Mahasiswa: Muhammad Alif Qadri (D082261018) | Mata kuliah: Algoritma Komputasi, Magister Teknik Informatika

Folder ini siap ditaruh di `D:\TUGAS BESAR PAK ABDI\CODING`. Bisa dijalankan di komputer sendiri atau di Google Colab, dengan hasil disimpan ke folder khusus di Google Drive.

## Isi folder

```
CODING/
├── README.md
├── requirements.txt            # pustaka yang dipakai notebook
├── jalankan_notebook.bat       # Windows: siapkan lingkungan lalu buka notebook
├── bantu_mst.py                # alat bantu bersama untuk Uji_Kecil dan Studi_Kasus
├── Contoh_Dasar/               # contoh dasar tiap algoritma + visualisasi
│   ├── Kruskal/
│   │   ├── kruskal.py          # HimpunanTerpisah + kruskal()
│   │   └── visualisasi-kruskal.html
│   ├── Prim/
│   │   ├── prim.py             # buat_daftar_tetangga() + prim()
│   │   └── visualisasi-prim.html
│   └── Borůvka/
│       ├── boruvka.py          # boruvka() (pembanding), memakai HimpunanTerpisah dari Kruskal
│       └── visualisasi-boruvka.html
├── Uji_Kecil/                  # uji kasus kecil (kode lokal, tanpa seed)
│   ├── uji_kecil.py
│   └── PENJELASAN_UJI_KECIL.md # hitungan tangan keempat kasus
├── Studi_Kasus/                # studi kasus 5 gedung FT Unhas (kode lokal, tanpa seed)
│   ├── studi_kasus.py
│   ├── studi_kasus_gedung_unhas.csv   # data tetap; angka ILUSTRASI
│   └── PENJELASAN_STUDI_KASUS.md
└── Eksperimen/                 # hanya yang berat secara komputasi
    ├── Tugas_MST_Lokal.ipynb   # graf acak ber-seed, pengukuran waktu, grafik, CSV
    └── PENJELASAN_NOTEBOOK.md  # penjelasan rinci tiap sel, keputusan desain, draf laporan AI
```
Folder `hasil/` (CSV), `grafik/` (gambar), dan berkas `lingkungan_dan_log.txt` **dibuat otomatis** saat notebook dijalankan: di samping notebook (lokal) atau di folder Google Drive (Colab). Folder itu tidak disimpan di repositori; grafik yang dipakai laporan ada di `../DRAF/gambar/`.

## Cara menjalankan

Contoh dasar, uji kasus kecil, dan studi kasus berupa skrip Python biasa: butuh Python 3.9 atau lebih baru, **tanpa pustaka tambahan**. Hanya notebook eksperimen yang membutuhkan `requirements.txt`.

### 1. Contoh dasar (satu algoritma, graf 5 simpul)
```
cd Contoh_Dasar\Kruskal
python kruskal.py

cd ..\Prim
python prim.py

cd ..\Borůvka
python boruvka.py
```
Keluarannya berupa sisi MST yang terpilih beserta total bobotnya.
Catatan: `boruvka.py` memakai `HimpunanTerpisah` dari `Kruskal/kruskal.py`, jadi folder `Kruskal` harus tetap berada di samping folder `Borůvka`.

### 2. Uji kasus kecil
```
cd Uji_Kecil
python uji_kecil.py
```
Empat graf kecil (3 terhubung dan 1 tak terhubung) dijalankan pada ketiga algoritma. Contoh keluaran:
```
[LOLOS] Kasus 1: 4 simpul biasa (satu sisi ditolak) | total = 7 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 2: 5 simpul, bobot 0 dan negatif | total = 5 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 3: bobot kembar (total dan himpunan sisi) | total = 6 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 4: graf tak terhubung (harus ValueError) | ketiganya melempar ValueError
```
Hitungan tangan tiap kasus ada di `Uji_Kecil/PENJELASAN_UJI_KECIL.md`.

### 3. Studi kasus (5 gedung FT Unhas)
```
cd Studi_Kasus
python studi_kasus.py
```
Data tetap dari `studi_kasus_gedung_unhas.csv`, jadi **tanpa seed**. Bobot sisi adalah biaya bersih (juta rupiah): positif berarti fakultas memakai dana sendiri, 0 berarti gratis (ditanggung universitas tanpa insentif), negatif berarti ditanggung universitas dan fakultas menerima insentif. Kolom `keterangan` berisi ILUSTRASI: angkanya contoh karangan, bukan data keuangan sesungguhnya, dan Bab 4.1 menyebutnya demikian. Jika kelak diganti dengan data biaya sebenarnya, catat sumbernya dan ubah Bab 4.1. Penjelasan: `Studi_Kasus/PENJELASAN_STUDI_KASUS.md`.

### 4. Notebook eksperimen (graf acak, seed 2026)
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

**Google Colab dan Google Drive:** unggah `Tugas_MST_Lokal.ipynb` ke Google Drive, buka dengan Colab, lalu **Runtime > Run all** dan izinkan akses Drive di Sel 2. Semua hasil disimpan ke `My Drive/TUGAS BESAR PAK ABDI/HASIL_EKSPERIMEN` (nama folder bisa diubah di Sel 2), berisi `hasil/`, `grafik/`, dan `lingkungan_dan_log.txt` (spesifikasi mesin dan seluruh keluaran teks). Sel 18 dijalankan paling akhir supaya semuanya tersinkron. Notebook tidak lagi membutuhkan folder `data/` atau berkas CSV studi kasus. Pencocokan file `.py` dengan kode notebook (Sel 10) dilewati di Colab karena folder `Contoh_Dasar` tidak ada di sana.
Waktu yang terukur di Colab adalah waktu mesin virtual Google yang dipakai bersama, jadi spesifikasinya harus ditulis di Bab 4. Untuk komputer sendiri dengan Google Drive for Desktop, isi `FOLDER_DRIVE_LOKAL` di Sel 2.

### 5. Halaman visualisasi
Klik dua kali berkas `.html` di `Contoh_Dasar/<algoritma>/`. Dibuka di browser, tidak perlu internet (font memakai cadangan sistem bila offline). Tombol **Selanjutnya** menjalankan satu langkah, tombol **Fokus** (atau tombol F) menyembunyikan panel yang tidak perlu. Kode di halaman sama persis dengan file `.py`.

## Pustaka
| Pustaka | Dipakai untuk |
|---|---|
| `random`, `time`, `math`, `heapq`, `csv`, `os`, `sys`, `platform`, `statistics`, `gc` (bawaan Python) | Pembuat graf, pengukuran, antrean prioritas (alat bantu Prim), pembaca CSV studi kasus |
| `pandas`, `numpy` | Ringkasan data, rata-rata dan simpangan baku |
| `matplotlib` | Grafik |
| `networkx` | **Hanya verifikasi** (Sel 10 notebook), tidak dipakai di dalam algoritma |

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
- Hitung ulang sendiri jawaban uji kasus kecil di `Uji_Kecil/uji_kecil.py` (draf perhitungan ada di `Uji_Kecil/PENJELASAN_UJI_KECIL.md`) dan total studi kasus (8 juta rupiah).
- Isi laporan penggunaan AI (draf di `Eksperimen/PENJELASAN_NOTEBOOK.md`, bagian 6.17) dengan kata-katamu sendiri. Kode di folder ini disusun dengan bantuan AI, jadi pelajari dan tulis ulang versimu sendiri sebelum diklaim sebagai karya sendiri.
- Buat repositori GitHub atau GitLab publik untuk tautan di lampiran laporan.
