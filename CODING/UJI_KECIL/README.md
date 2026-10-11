# UJI_KECIL

Empat graf kecil dengan data tetap (tanpa *seed*) yang jawabannya dihitung dengan tangan. Tiap kasus dijalankan pada Kruskal, Prim, dan Borůvka.

```
python UJI_KECIL.py     # Python 3.9+, tanpa pustaka tambahan
```

Keluaran: `[LOLOS]` per kasus, lalu "Semua 4 kasus uji lolos". Bila gagal, program berhenti dengan `AssertionError` yang menyebut kasus dan algoritmanya.

| Kasus | Graf | Hasil benar |
|---|---|---|
| 1 | 4 simpul, 5 sisi, satu sisi ditolak (siklus) | Total 7 |
| 2 | 5 simpul, ada bobot 0 dan negatif | Total 5 |
| 3 | Bobot kembar (4 sisi bobot 2 membentuk lingkaran) | Total 6, MST {(0,1), (0,3), (1,2)}; total dan himpunan sisi dicek |
| 4 | Tak terhubung: (0,1) bobot 1 dan (2,3) bobot 2 | Ketiganya melempar `ValueError` |

## Hitungan tangan

Draf; hitung ulang sendiri di kertas sebelum dikumpulkan. Simpul bernomor 0, 1, 2, dst.

**Kasus 1.** Sisi: (2,3)=4, (0,2)=3, (1,3)=5, (0,1)=1, (1,2)=2. Urut: (0,1)=1, (1,2)=2, (0,2)=3, (2,3)=4, (1,3)=5. Terima 1 dan 2. (0,2) ditolak karena 0 dan 2 sudah satu komponen lewat 1. Terima (2,3)=4, sudah 3 sisi = n − 1. **Total 1 + 2 + 4 = 7.**

**Kasus 2.** Sisi: (0,1)=0, (1,2)=−2, (0,2)=1, (2,3)=3, (0,4)=4, (1,3)=5, (1,4)=6. Urut: −2, 0, 1, 3, 4, 5, 6. Terima −2 dan 0. (0,2)=1 ditolak (siklus). Terima 3 dan 4, sudah 4 sisi. **Total −2 + 0 + 3 + 4 = 5.** Bobot 0 dan negatif diperlakukan sama seperti bobot lain karena algoritma hanya membandingkan urutan. Prim dari simpul 0 dan Borůvka (satu putaran) memberi total sama.

**Kasus 3.** Sisi: (0,1), (1,2), (2,3), (0,3) bobot 2, dan diagonal (1,3) bobot 5. Urutan pemutus seri (bobot, simpul terkecil, simpul terbesar): (0,1), (0,3), (1,2), (2,3), diagonal. Tiga pertama diterima. (2,3) akan ditolak, tetapi kode berhenti setelah 3 sisi sehingga sisi ini tidak pernah diperiksa; penolakan hanya ada di hitungan tangan. **Total 2 + 2 + 2 = 6.**

**Kasus 4.** Simpul 0 dan 1 tidak punya lintasan ke simpul 2 dan 3, jadi tidak ada MST.

Syarat dosen minimal 3 kasus uji kecil terpenuhi (3 kasus terhubung + 1 kasus galat, masing-masing pada tiga algoritma).
