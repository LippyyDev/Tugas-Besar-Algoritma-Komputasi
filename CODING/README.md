# CODING

Kode tugas besar: Kruskal, Prim, dan Borůvka (MST). Python 3.9+.

| Folder | Isi | Cara jalan |
|---|---|---|
| `UJI_KECIL/` | 4 graf kecil, ketiga algoritma dicocokkan | `python UJI_KECIL.py` |
| `STUDI_KASUS/` | Jaringan kabel 5 gedung FT Unhas (data tetap) | `python STUDI_KASUS.py` |
| `EKSPERIMEN/` | Graf acak (seed 2026), waktu, grafik, CSV | Buka `TUGAS_MST_LOKAL.ipynb`, **Run All** (lokal atau Colab) |

Dua skrip pertama tanpa pustaka tambahan. Notebook butuh `pip install -r REQUIREMENTS.txt` (pandas, numpy, matplotlib; `networkx` hanya untuk verifikasi).

Eksperimen penuh sekitar 1 sampai 3 menit. `MODE_CEPAT = True` di Sel 1 hanya untuk uji coba, hasilnya jangan dipakai di laporan.

Hasil eksperimen yang dipakai laporan ada di `EKSPERIMEN/HASIL/` (CSV), `EKSPERIMEN/GRAFIK/` (gambar), dan `EKSPERIMEN/LINGKUNGAN_DAN_LOG.txt` (spesifikasi mesin dan log). Di Colab, hasil baru tersimpan di `My Drive/TUGAS BESAR PAK ABDI/HASIL_EKSPERIMEN`; waktunya adalah waktu mesin Google, jadi catat spesifikasinya di Bab 4.

Detail per folder ada di `README.md` masing-masing.
