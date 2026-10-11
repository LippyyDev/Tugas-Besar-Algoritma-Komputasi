# STUDI_KASUS

Jaringan kabel 5 gedung Fakultas Teknik Unhas (kampus Gowa), dipasang dengan biaya bersih minimum. Data tetap (daftar `data_jalur` di `STUDI_KASUS.py`), tanpa *seed*, hasil sama setiap dijalankan.

```
python STUDI_KASUS.py     # Python 3.9+, tanpa pustaka tambahan
```

| Hal | Isi |
|---|---|
| Data | 5 gedung, 6 jalur kandidat (gedung A, gedung B, biaya dalam juta rupiah) |
| Bobot | Biaya bersih: positif = fakultas bayar, 0 = gratis, negatif = insentif sebesar nilai mutlaknya |
| Simpul | Dinomori menurut abjad nama gedung |
| Pemutus seri | Tidak dipakai, karena semua biaya berbeda |

Keluaran: jalur terpilih Kruskal, Prim, dan Borůvka sama, yaitu Arsitektur–Sipil (−5), Sipil–Elektro (−2), Elektro–Geologi (0), Sipil–Industri (15). **Total 8 juta.** Tabel lengkap ada di Bab 4.1 (Tabel 4.1 dan 4.2).
