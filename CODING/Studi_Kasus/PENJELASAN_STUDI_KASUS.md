# Penjelasan Studi Kasus (`studi_kasus.py`)

Jaringan kabel lima gedung Fakultas Teknik Unhas, kampus Gowa. Kode ada di `studi_kasus.py`, dan datanya di `studi_kasus_gedung_unhas.csv` (folder yang sama). Ketiga algoritma diimpor dari `../Contoh_Dasar/` lewat `../bantu_mst.py`.

**Menjalankan** (Python 3.9 atau lebih baru, tanpa pustaka tambahan):
```
cd Studi_Kasus
python studi_kasus.py
```

**Contoh keluaran:**
```
Studi kasus: 5 gedung, 6 jalur kabel yang mungkin
  Arsitektur - Sipil: -5 juta
  Elektro - Sipil: -2 juta
  Elektro - Geologi: 0 juta
  Industri - Sipil: 15 juta
Total biaya bersih minimum: 8 juta (Kruskal, Prim, dan Borůvka sama)
PERINGATAN: data masih berlabel ILUSTRASI. Ganti dengan data biaya sebenarnya sebelum disebut data nyata.
```

Satu contoh penerapan pada **data tetap**, bukan graf acak, sehingga **tidak memakai seed** dan hasilnya sama setiap dijalankan. Data dibaca dari `studi_kasus_gedung_unhas.csv` (kolom: `gedung_a`, `gedung_b`, `biaya_juta`, `keterangan`). Bobot adalah biaya bersih dalam juta rupiah. Positif berarti fakultas memakai dana sendiri, 0 berarti gratis (ditanggung universitas tanpa insentif), dan negatif berarti ditanggung universitas dan fakultas menerima insentif sebesar nilai mutlaknya. Simpul diberi nomor tetap menurut urutan abjad nama gedung, sehingga aturan pemutus seri pada Batasan 7 tetap berlaku.

> **PENTING:** selama kolom `keterangan` masih berisi **ILUSTRASI**, angkanya adalah contoh karangan, bukan hasil ukur. Ganti dengan data biaya sebenarnya, catat sumber dan tanggalnya di Bab 4, lalu hapus kata ILUSTRASI. Graf ini hanya 5 simpul, jadi dipakai untuk menunjukkan kebenaran dan penerapan, **bukan** untuk mengukur waktu.
