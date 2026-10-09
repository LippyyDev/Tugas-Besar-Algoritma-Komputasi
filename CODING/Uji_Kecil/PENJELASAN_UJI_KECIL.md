# Penjelasan Uji Kasus Kecil (`uji_kecil.py`)

Empat graf kecil dengan data tetap (tanpa seed) yang jawabannya bisa dihitung dengan tangan. Kode ada di `uji_kecil.py`, dan tiap kasus dijalankan pada Kruskal, Prim, dan Borůvka dari `../Contoh_Dasar/` lewat `../bantu_mst.py`.

**Menjalankan** (Python 3.9 atau lebih baru, tanpa pustaka tambahan):
```
cd Uji_Kecil
python uji_kecil.py
```

**Contoh keluaran:**
```
[LOLOS] Kasus 1: 4 simpul biasa (satu sisi ditolak) | total = 7 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 2: 5 simpul, bobot 0 dan negatif | total = 5 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 3: bobot kembar (total dan himpunan sisi) | total = 6 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 4: graf tak terhubung (harus ValueError) | ketiganya melempar ValueError
Semua 4 kasus uji lolos pada ketiga algoritma (3 kasus graf terhubung dan 1 kasus galat).
```
Jika satu kasus gagal, program berhenti dengan `AssertionError` yang menyebut kasus dan algoritmanya.

## Hitungan tangan

Syarat dosen: **minimal 3 kasus uji kecil yang bisa dicek manual.** Ada 3 kasus graf terhubung dan 1 kasus graf tak terhubung. **Setiap kasus dijalankan pada ketiga algoritma**, sehingga syaratnya terpenuhi baik jika dosen memaksudkan 3 kasus total maupun 3 kasus per algoritma. Jawaban benar ditulis dari hitungan tangan, bukan dari keluaran program.

> **PENTING: ini draf hitungan tangan. Hitung ulang sendiri di kertas sebelum dikumpulkan**, lalu pastikan kamu bisa menjelaskan tiap langkahnya saat tanya jawab. Simpul diberi nomor 0, 1, 2, dan seterusnya. Bagian A murni contoh graf, belum terkait data nyata.

**Kasus 1 (4 simpul biasa, ada satu sisi yang ditolak).** Sisi: (2, 3) bobot 4, (0, 2) bobot 3, (1, 3) bobot 5, (0, 1) bobot 1, (1, 2) bobot 2.
Urut menaik: (0, 1) 1, (1, 2) 2, (0, 2) 3, (2, 3) 4, (1, 3) 5.
Ambil 1 (terima). Ambil 2 (terima). Sisi (0, 2) bobot 3: simpul 0 dan simpul 2 sudah satu komponen lewat simpul 1, jadi **ditolak (siklus)**. Sisi (2, 3) bobot 4: simpul 3 baru, terima. Sudah 3 sisi = n − 1, selesai.
**Total = 1 + 2 + 4 = 7.**

**Kasus 2 (5 simpul, ada bobot 0 dan negatif).** Sisi: (0, 1) bobot 0, (1, 2) bobot -2, (0, 2) bobot 1, (2, 3) bobot 3, (0, 4) bobot 4, (1, 3) bobot 5, (4, 1) bobot 6.
Urut menaik: (1, 2) -2, (0, 1) 0, (0, 2) 1, (2, 3) 3, (0, 4) 4, (1, 3) 5, (1, 4) 6.
Ambil -2 (terima). Ambil 0 (terima). Sisi (0, 2) bobot 1: simpul 0 dan simpul 2 sudah satu komponen lewat simpul 1, jadi **ditolak (siklus)**. Sisi (2, 3) bobot 3: simpul 3 baru, terima. Sisi (0, 4) bobot 4: simpul 4 baru, terima. Sudah 4 sisi = n − 1, selesai, dua sisi terakhir tidak diperiksa.
**Total = -2 + 0 + 3 + 4 = 5.** Bobot 0 dan -2 diperlakukan seperti bobot lain: algoritma hanya membandingkan urutan bobot, bukan tanda atau besarnya (sejalan dengan bobot real pada Bab 1). Prim dari simpul 0 memberi total yang sama: ambil 0 (simpul 1 masuk), ambil -2 (simpul 2 masuk), buang entri usang bobot 1, ambil 3 (simpul 3), ambil 4 (simpul 4). Borůvka selesai dalam satu putaran: simpul 0 memilih sisi bobot 0, simpul 1 dan simpul 2 memilih sisi bobot -2, simpul 3 memilih sisi bobot 3, simpul 4 memilih sisi bobot 4.

**Kasus 3 (bobot kembar).** Sisi: (0, 1) bobot 2, (1, 2) bobot 2, (2, 3) bobot 2, (0, 3) bobot 2, dan diagonal (1, 3) bobot 5. Empat sisi bobot 2 membentuk lingkaran, jadi hanya tiga yang boleh diterima.
Urutan pemeriksaan menurut aturan pemutus seri (bobot, lalu simpul terkecil, lalu simpul terbesar): (0, 1), (0, 3), (1, 2), (2, 3), lalu diagonal 5. Tiga yang pertama diterima. Jika sisi (2, 3) diperiksa, ia **ditolak** karena simpul 2 dan simpul 3 sudah satu komponen lewat simpul 1 dan simpul 0. Catatan: kode Kruskal berhenti setelah 3 sisi diterima, jadi program tidak pernah memeriksa sisi itu. Penolakan ini hanya ada di hitungan tangan, jangan diklaim sebagai keluaran program. Diagonal bobot 5 tidak diperlukan.
**Total = 2 + 2 + 2 = 6**, dengan MST unik {(0, 1), (0, 3), (1, 2)}. Karena aturan pemutus seri sama pada ketiga algoritma, **total dan himpunan sisi** dicek.

**Kasus 4 (graf tak terhubung).** Sisi: (0, 1) bobot 1 dan (2, 3) bobot 2. Simpul 0 dan simpul 1 tidak punya lintasan ke simpul 2 dan simpul 3, jadi **tidak ada MST**: ketiga algoritma harus menolak dengan `ValueError`.
