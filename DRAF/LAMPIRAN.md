# LAMPIRAN

---

## Lampiran A. Repositori dan Struktur Berkas

---

Seluruh kode, data, dan hasil eksperimen laporan ini tersimpan pada repositori publik berikut.

**Tautan repositori:** https://github.com/LippyyDev/Tugas-Besar-Algoritma-Komputasi

**Tabel A.1** Berkas yang dirujuk laporan

| Berkas atau folder | Isi | Dirujuk di |
|---|---|---|
| `CODING/Contoh_Dasar/Kruskal/kruskal.py` | `HimpunanTerpisah` dan `kruskal()` | Kode 4.1, Kode 4.2 |
| `CODING/Contoh_Dasar/Prim/prim.py` | `buat_daftar_tetangga()` dan `prim()` | Kode 4.3 |
| `CODING/Contoh_Dasar/Borůvka/boruvka.py` | `boruvka()`, memakai `HimpunanTerpisah` dari `kruskal.py` | Subbab 4.2 |
| `CODING/Contoh_Dasar/*/visualisasi-*.html` | Visualisasi langkah tiap algoritma pada graf 5 simpul | Pendukung presentasi, tidak dirujuk di teks |
| `CODING/Uji_Kecil/uji_kecil.py` | Empat kasus uji kecil | Subbab 4.3, Lampiran B |
| `CODING/Studi_Kasus/studi_kasus.py` dan `studi_kasus_gedung_unhas.csv` | Studi kasus lima gedung | Subbab 4.1, Lampiran C |
| `CODING/Eksperimen/Tugas_MST_Lokal.ipynb` | Pembangkit graf acak ber-*seed*, pengukuran waktu, grafik | Subbab 4.4 dan 4.5 |
| `CODING/Eksperimen/hasil/` | `eksperimen_mentah.csv`, `ringkasan.csv`, `rasio_terhadap_teori.csv` | Tabel 4.6 sampai 4.9 |
| `CODING/Eksperimen/lingkungan_dan_log.txt` | Spesifikasi mesin dan seluruh keluaran sesi Colab | Tabel 4.3, subbab 4.3 |
| `DRAF/gambar/` | Gambar 4.1 sampai 4.3 | Subbab 4.5 |
| `REFERENSI/` | Salinan PDF referensi yang dikutip | Daftar Pustaka |

---

## Lampiran B. Data Empat Kasus Uji Kecil

---

Sisi ditulis (simpul, simpul, bobot) dengan simpul bernomor mulai dari 0. Seluruh kasus dijalankan pada Kruskal, Prim, dan Borůvka oleh `uji_kecil.py`, dan ketiganya lolos pada keempat kasus. Total yang benar pada Kasus 1 sampai 3 dihitung tangan terlebih dahulu.

**Tabel B.1** Data dan hasil kasus uji kecil

| Kasus | *n* | Daftar sisi | Total MST | Sisi MST | Tujuan pemeriksaan |
|---|---|---|---|---|---|
| 1 | 4 | (2,3,4), (0,2,3), (1,3,5), (0,1,1), (1,2,2) | 7 | (0,1,1), (1,2,2), (2,3,4) | Sisi (0,2,3) harus ditolak karena membentuk siklus |
| 2 | 5 | (0,1,0), (1,2,−2), (0,2,1), (2,3,3), (0,4,4), (1,3,5), (4,1,6) | 5 | (1,2,−2), (0,1,0), (2,3,3), (0,4,4) | Bobot nol dan negatif |
| 3 | 4 | (0,1,2), (1,2,2), (2,3,2), (3,0,2), (1,3,5) | 6 | (0,1,2), (0,3,2), (1,2,2) | Bobot kembar, hasil tunggal berkat aturan pemutus seri |
| 4 | 4 | (0,1,1), (2,3,2) | tidak ada | tidak ada | Graf tak terhubung, ketiga algoritma harus melempar `ValueError` |

Keluaran program:

```text
[LOLOS] Kasus 1: 4 simpul biasa (satu sisi ditolak) | total = 7 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 2: 5 simpul, bobot 0 dan negatif | total = 5 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 3: bobot kembar (total dan himpunan sisi) | total = 6 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 4: graf tak terhubung (harus ValueError) | ketiganya melempar ValueError
```

Pada Kasus 3, aturan pemutus seri (bobot, simpul terkecil, simpul terbesar) mengurutkan sisi bobot 2 menjadi (0,1), (0,3), (1,2), lalu (2,3). Tiga sisi pertama diterima dan sisi (2,3) menutup siklus, sehingga MST yang dihasilkan tunggal. Hitungan tangan lengkap tiap kasus ada di `CODING/Uji_Kecil/PENJELASAN_UJI_KECIL.md`.

---

## Lampiran C. Data Studi Kasus

---

Isi `studi_kasus_gedung_unhas.csv` sama dengan Tabel 4.1. Seluruh biaya adalah nilai ilustrasi karangan, bukan data keuangan sesungguhnya.

**Tabel C.1** Berkas data studi kasus

| gedung_a | gedung_b | biaya_juta |
|---|---|---|
| Sipil | Industri | 15 |
| Elektro | Geologi | 0 |
| Arsitektur | Sipil | −5 |
| Arsitektur | Elektro | 18 |
| Sipil | Elektro | −2 |
| Industri | Geologi | 25 |

Keluaran `studi_kasus.py` memuat empat jalur terpilih, yaitu Arsitektur dan Sipil (−5), Elektro dan Sipil (−2), Elektro dan Geologi (0), serta Industri dan Sipil (15), dengan total biaya bersih minimum 8 juta rupiah, sama untuk ketiga algoritma.

---

## Lampiran D. Cara Mengulang Pengujian dan Eksperimen

---

Contoh dasar, uji kecil, dan studi kasus memakai Python 3.9 atau lebih baru tanpa pustaka tambahan.

```bash
cd CODING/Contoh_Dasar/Kruskal && python kruskal.py
cd CODING/Uji_Kecil && python uji_kecil.py
cd CODING/Studi_Kasus && python studi_kasus.py
```

Notebook eksperimen memerlukan pustaka pada `CODING/requirements.txt` (`numpy`, `pandas`, `matplotlib`, `networkx`, dan `notebook`). `networkx` hanya dipakai untuk verifikasi, bukan di dalam algoritma.

```bash
cd CODING
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cd Eksperimen
python -m notebook Tugas_MST_Lokal.ipynb
```

Parameter eksperimen yang dipakai pada laporan adalah *seed* 2026, lima ulangan per ukuran, dan `MODE_CEPAT = False`. Seluruh pengukuran di Bab 4 dijalankan pada Google Colab versi gratis dalam satu sesi selama 149,2 detik, dengan spesifikasi pada Tabel 4.3. Waktu eksekusi bergantung pada mesin, sehingga hasil di perangkat lain akan berbeda dalam nilai mutlak. Total bobot ketiga algoritma pada setiap graf eksperimen tidak bergantung pada mesin dan harus sama.

---

## Lampiran E. Berkas Hasil Eksperimen

---

**Tabel E.1** Kolom berkas hasil

| Berkas | Kolom utama |
|---|---|
| `eksperimen_mentah.csv` | Waktu setiap ulangan untuk setiap skenario, ukuran, dan algoritma |
| `ringkasan.csv` | `skenario`, `n`, `m`, `algoritma`, `rata_rata` (detik), `simpangan_baku` (detik), `jumlah_ulangan` |
| `rasio_terhadap_teori.csv` | Rasio waktu terhadap suku teoretis per skenario dan ukuran |

Tabel 4.6 sampai 4.8 diambil dari `ringkasan.csv` setelah dikonversi ke milidetik. Rasio pada Tabel 4.9 dihitung ulang dari Tabel 4.6 sampai 4.8 dengan suku *m* log₂ *n* untuk ketiga algoritma, sehingga rasio Kruskal dapat berbeda dari `rasio_terhadap_teori.csv`, yang memakai *m* log₂ *m* untuk Kruskal (subbab 4.5).
