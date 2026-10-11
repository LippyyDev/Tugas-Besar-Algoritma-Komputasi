# LAMPIRAN

---

## Lampiran A. Repositori dan Struktur Berkas

---

Seluruh kode, data, dan hasil eksperimen laporan ini tersimpan pada repositori publik berikut.

**Tautan repositori:** https://github.com/LippyyDev/Tugas-Besar-Algoritma-Komputasi

**Tabel A.1** Berkas yang dirujuk laporan

| Berkas atau folder | Isi | Dirujuk di |
|---|---|---|
| `CODING/UJI_KECIL/UJI_KECIL.py` | Empat kasus uji kecil, berdiri sendiri (memuat ketiga algoritma) | Subbab 4.3, Lampiran B |
| `CODING/STUDI_KASUS/STUDI_KASUS.py` | Studi kasus lima gedung, berdiri sendiri, data ditulis langsung di dalam kode | Subbab 4.1, Lampiran C |
| `CODING/EKSPERIMEN/TUGAS_MST_LOKAL.ipynb` | Implementasi ketiga algoritma, pembangkit graf acak ber-*seed*, pengukuran waktu, grafik | Subbab 4.2, Kode 4.1 sampai 4.3, Subbab 4.4 dan 4.5 |
| `CODING/EKSPERIMEN/HASIL/` | `EKSPERIMEN_MENTAH.csv`, `RINGKASAN.csv`, `RASIO_TERHADAP_TEORI.csv` | Tabel 4.6 sampai 4.9 |
| `CODING/EKSPERIMEN/LINGKUNGAN_DAN_LOG.txt` | Spesifikasi mesin dan seluruh keluaran sesi Colab | Tabel 4.3, subbab 4.3 |
| `CODING/EKSPERIMEN/GRAFIK/` | `WAKTU_JARANG.png`, `WAKTU_PADAT.png`, `WAKTU_JARANG_KEMBAR.png` (Gambar 4.1 sampai 4.3) | Subbab 4.5 |
| `REFERENSI/` | Salinan PDF referensi yang dikutip | Daftar Pustaka |

---

## Lampiran B. Data Empat Kasus Uji Kecil

---

Sisi ditulis (simpul, simpul, bobot) dengan simpul bernomor mulai dari 0. Seluruh kasus dijalankan pada Kruskal, Prim, dan Borůvka oleh `UJI_KECIL.py`, dan ketiganya lolos pada keempat kasus. Total yang benar pada Kasus 1 sampai 3 dihitung tangan terlebih dahulu.

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

Pada Kasus 3, aturan pemutus seri (bobot, simpul terkecil, simpul terbesar) mengurutkan sisi bobot 2 menjadi (0,1), (0,3), (1,2), lalu (2,3). Tiga sisi pertama diterima dan sisi (2,3) menutup siklus, sehingga MST yang dihasilkan tunggal. Hitungan tangan lengkap tiap kasus ada di `CODING/UJI_KECIL/README.md`.

---

## Lampiran C. Data Studi Kasus

---

Data pada daftar `data_jalur` di `STUDI_KASUS.py` sama dengan Tabel 4.1. Seluruh biaya adalah nilai ilustrasi karangan, bukan data keuangan sesungguhnya.

**Tabel C.1** Data jalur studi kasus

| Gedung A | Gedung B | Biaya bersih (juta rupiah) |
|---|---|---|
| Sipil | Industri | 15 |
| Elektro | Geologi | 0 |
| Arsitektur | Sipil | −5 |
| Arsitektur | Elektro | 18 |
| Sipil | Elektro | −2 |
| Industri | Geologi | 25 |

Keluaran `STUDI_KASUS.py` memuat empat jalur terpilih, yaitu Arsitektur dan Sipil (−5), Elektro dan Sipil (−2), Elektro dan Geologi (0), serta Industri dan Sipil (15), dengan total biaya bersih minimum 8 juta rupiah, sama untuk ketiga algoritma.

---

## Lampiran D. Cara Mengulang Pengujian dan Eksperimen

---

Uji kecil dan studi kasus memakai Python 3.9 atau lebih baru tanpa pustaka tambahan.

```bash
cd CODING/UJI_KECIL && python UJI_KECIL.py
cd CODING/STUDI_KASUS && python STUDI_KASUS.py
```

Notebook eksperimen memerlukan pustaka pada `CODING/REQUIREMENTS.txt` (`numpy`, `pandas`, `matplotlib`, `networkx`, dan `notebook`). `networkx` hanya dipakai untuk verifikasi, bukan di dalam algoritma.

```bash
cd CODING
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r REQUIREMENTS.txt
cd EKSPERIMEN
python -m notebook TUGAS_MST_LOKAL.ipynb
```

Parameter eksperimen yang dipakai pada laporan adalah *seed* 2026, lima ulangan per ukuran, dan `MODE_CEPAT = False`. Seluruh pengukuran di Bab 4 dijalankan pada Google Colab versi gratis dalam satu sesi selama 149,2 detik, dengan spesifikasi pada Tabel 4.3. Waktu eksekusi bergantung pada mesin, sehingga hasil di perangkat lain akan berbeda dalam nilai mutlak. Total bobot ketiga algoritma pada setiap graf eksperimen tidak bergantung pada mesin dan harus sama.

---

## Lampiran E. Berkas Hasil Eksperimen

---

**Tabel E.1** Kolom berkas hasil

| Berkas | Kolom utama |
|---|---|
| `EKSPERIMEN_MENTAH.csv` | Waktu setiap ulangan untuk setiap skenario, ukuran, dan algoritma |
| `RINGKASAN.csv` | `skenario`, `n`, `m`, `algoritma`, `rata_rata` (detik), `simpangan_baku` (detik), `jumlah_ulangan` |
| `RASIO_TERHADAP_TEORI.csv` | Rasio waktu terhadap suku teoretis per skenario dan ukuran |

Tabel 4.6 sampai 4.8 diambil dari `RINGKASAN.csv` setelah dikonversi ke milidetik. Rasio pada Tabel 4.9 dihitung ulang dari Tabel 4.6 sampai 4.8 dengan suku *m* log₂ *n* untuk ketiga algoritma, sehingga rasio Kruskal dapat berbeda dari `RASIO_TERHADAP_TEORI.csv`, yang memakai *m* log₂ *m* untuk Kruskal (subbab 4.5).
