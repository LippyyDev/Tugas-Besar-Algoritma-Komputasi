# Penjelasan Notebook `Tugas_MST_Lokal.ipynb`

Berkas ini menampung penjelasan rinci yang sengaja dipindahkan dari notebook supaya notebook tetap ringkas. Isi notebook hanya informasi penting per sel. Nomor bagian di sini sama dengan nomor sel di notebook.

**Mahasiswa:** Muhammad Alif Qadri (D082261018) | **Mata kuliah:** Algoritma Komputasi, Magister Teknik Informatika
**Algoritma:** No 10, Kruskal dan Prim (MST). Pembanding ketiga: Borůvka.

---

## 1. Cara menjalankan

| Cara | Langkah |
|---|---|
| **Google Colab** | Unggah notebook ke Google Drive, buka dengan Colab, pilih **Runtime > Run all**, lalu izinkan akses Drive saat diminta di Sel 2. Hasil tersimpan di `My Drive/TUGAS BESAR PAK ABDI/HASIL_EKSPERIMEN` (nama folder bisa diubah lewat `NAMA_FOLDER_DRIVE` di Sel 2). |
| **Komputer sendiri (Windows)** | Klik dua kali `jalankan_notebook.bat` di folder `CODING`, lalu **Run > Run All Cells** di notebook yang terbuka. |
| **Komputer sendiri dengan Google Drive for Desktop** | Isi `FOLDER_DRIVE_LOKAL` di Sel 2 dengan alamat folder Drive yang disinkronkan, misalnya `G:\My Drive\TUGAS BESAR PAK ABDI\HASIL_EKSPERIMEN`. |
| **Manual atau VS Code** | Pasang `requirements.txt`, jalankan notebook dari foldernya sendiri (`CODING/Eksperimen`), lalu jalankan semua sel. |

Untuk uji coba cepat (sekitar 15 detik), ubah `MODE_CEPAT = True` di Sel 1. **Hasil mode cepat tidak boleh dipakai di laporan.** Eksperimen penuh memakan sekitar 1 sampai 3 menit.

Di Colab, waktu yang diukur adalah waktu mesin virtual Google yang dipakai bersama, bukan komputer sendiri. Spesifikasinya dicatat di Sel 3 dan di `lingkungan_dan_log.txt`, dan harus ditulis jujur di Bab 4.1.

## 2. Pustaka yang dipakai

| Pustaka | Dipakai untuk | Catatan |
|---|---|---|
| `random`, `time`, `math`, `heapq`, `csv`, `os`, `sys`, `platform`, `statistics`, `gc` | Pembuat graf, pengukuran, antrean prioritas (alat bantu Prim) | Bawaan Python |
| `pandas`, `numpy` | Ringkasan data, rata-rata dan simpangan baku | Ada di `requirements.txt` |
| `matplotlib` | Grafik | Ada di `requirements.txt` |
| `networkx` | **Hanya verifikasi** (Sel 10), tidak dipakai di dalam algoritma | Opsional, ada di `requirements.txt` |

## 3. Contoh keluaran Sel 7.1 sampai 7.5 (uji kasus kecil)

```
[LOLOS] Kasus 1: 4 simpul biasa (satu sisi ditolak) | total = 7 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 2: 5 simpul, bobot 0 dan negatif | total = 5 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 3: bobot kembar (total dan himpunan sisi) | total = 6 | Kruskal, Prim, Borůvka sama
[LOLOS] Kasus 4: graf tak terhubung (harus ValueError) | ketiganya melempar ValueError

Semua 4 kasus uji lolos pada ketiga algoritma (3 kasus graf terhubung dan 1 kasus galat).
```

## 4. Isi folder hasil

Folder dasar adalah folder Drive (Colab atau `FOLDER_DRIVE_LOKAL`) atau folder tempat notebook dijalankan.

| Berkas | Isi |
|---|---|
| `hasil/eksperimen_mentah.csv` | Waktu setiap ulangan (data mentah) |
| `hasil/ringkasan.csv` | Rata-rata dan simpangan baku per ukuran |
| `hasil/rasio_terhadap_teori.csv` | Pemeriksaan kesesuaian dengan kurva teori |
| `grafik/waktu_<skenario>.png` | Grafik waktu, titik ukur disandingkan dengan kurva teori |
| `data/studi_kasus_gedung_unhas.csv` | Data tetap studi kasus (dibuat otomatis bila belum ada, tidak pernah ditimpa) |
| `lingkungan_dan_log.txt` | Spesifikasi mesin, versi pustaka, dan seluruh keluaran teks notebook |

## 5. Peta syarat tugas ke sel

| Syarat | Sel |
|---|---|
| Kruskal dan Prim ditulis sendiri, tanpa pustaka MST sebagai inti | 4, 5 |
| Pembanding ketiga (Borůvka) | 6 |
| Fungsi atau kelas dengan komentar | 4 sampai 6 |
| Minimal 3 kasus uji kecil yang bisa dicek manual | 7 |
| Pembuat graf acak, *seed* tetap, terhubung, jarang dan padat | 8 dan 9 |
| Minimal 5 ukuran, minimal 5 ulangan, rata-rata dan simpangan baku, CSV | 11 sampai 13 |
| Grafik waktu dengan kurva teori | 14 dan 15 |
| Banyak skenario | 1 (tiga skenario) |
| Pemakaian AI dilaporkan, sumber kode dicantumkan | 17 (bagian 6.17 di bawah) |
| Hasil tersimpan di folder khusus (Drive) untuk dibaca ulang | 2 dan 18 |

---

## 6. Penjelasan per sel

### 6.1 Sel 1. Pengaturan
- **`SEED`** membuat graf acak selalu sama setiap dijalankan, sehingga percobaan bisa diulang oleh orang lain.
- **Tiga skenario** (dosen menyarankan banyak skenario): graf jarang, graf padat, dan graf jarang dengan bobot kembar.
- Graf padat tumbuh seperti n², jadi ukurannya sengaja jauh lebih kecil daripada graf jarang. Ukuran dibuat cukup besar supaya waktu tidak terlalu singkat dan pengukuran tidak berisik.

### 6.2 Sel 2. Folder hasil dan log
Sel ini menentukan `FOLDER_DASAR`: Colab (memasang Drive), `FOLDER_DRIVE_LOKAL` bila diisi, atau folder tempat notebook dijalankan. Di dalamnya dibuat `hasil/`, `grafik/`, dan `data/`. Data studi kasus dibuat dari isi bawaan hanya bila belum ada, jadi angka hasil ukur yang kamu edit langsung di folder ini aman. Semua keluaran `print` juga disalin ke `lingkungan_dan_log.txt` sampai Sel 18 menutupnya.

### 6.3 Sel 3. Pustaka dan lingkungan uji
Informasi lingkungan (Python, sistem, prosesor, jumlah CPU, jenis lingkungan) dipakai untuk bagian "lingkungan uji" di Bab 4.

### 6.4 Sel 4. Kruskal dan Himpunan Terpisah (*Disjoint Set*)
**Gagasan:** urutkan semua sisi dari bobot terkecil, lalu terima sisi satu per satu, kecuali sisi yang membentuk siklus. `HimpunanTerpisah` menjawab satu pertanyaan: "apakah dua simpul sudah satu komponen?"

**Alat bantu bawaan Python:** `sorted()` untuk mengurutkan sisi, biaya O(m log m). Logika memilih sisi dan mendeteksi siklus ditulis sendiri.

**Sumber:** *union by rank* dan kompresi lintasan (*path compression*) dibahas pada Sanders *et al.* (2019, Bagian 11.4). Kode memakai *path halving*, varian kompresi lintasan yang dipilih penulis dan tidak ditemukan pada bagian tersebut. Kode bukan salinan dari repositori atau forum tertentu.

### 6.5 Sel 5. Prim
**Gagasan:** mulai dari satu simpul, lalu tumbuhkan pohon. Setiap kali, ambil sisi **berbobot terkecil** yang keluar dari pohon. Jika simpul di ujungnya sudah ada di pohon, buang (akan membentuk siklus). Jika belum, terima dan masukkan sisi baru dari simpul itu ke antrean.

- **Alat bantu:** `heapq` sebagai antrean prioritas, biaya O(log m) per operasi.
- **Varian *lazy*:** `heapq` tidak punya operasi *decrease-key*, jadi tawaran yang usang dibiarkan di antrean lalu dibuang saat keluar. Antrean bisa berisi sampai O(m) elemen, sehingga waktunya O(m log m), yang sama dengan O(m log n).
- **Pemutus seri:** isi antrean adalah (bobot, simpul_kecil, simpul_besar), jadi tawaran yang sama murah diambil menurut simpul terkecil lalu terbesar, sama dengan Kruskal dan Borůvka. Ujung yang sudah ada di pohon menjadi `asal`, ujung satunya menjadi `tujuan`.
- **Representasi graf:** daftar ketetanggaan (sesuai batasan Bab 1), dibuat oleh `buat_daftar_tetangga`.

### 6.6 Sel 6. Borůvka (pembanding ketiga)
**Gagasan:** semua komponen bergerak **serentak**. Dalam satu putaran, tiap komponen mencatat sisi berbobot terkecil yang keluar darinya, lalu semua pilihan diterima sekaligus. Ulangi sampai tinggal satu komponen. Jumlah komponen menyusut sedikitnya separuh per putaran, sehingga putarannya paling banyak log₂ n.

- **Pemutus seri:** `kunci_sisi` membandingkan bobot, lalu simpul terkecil, lalu simpul terbesar (sama dengan urutan Kruskal dan isi antrean Prim), sesuai batasan Bab 1.
- **Himpunan terpisah:** memakai `HimpunanTerpisah` dari Sel 4 (tidak disalin ulang).

### 6.7 Sel 7 sampai 7.5. Uji kasus kecil (hitungan tangan)

Bagian A notebook dipecah per kasus: Sel 7 = persiapan (fungsi uji), Sel 7.1 = Kasus 1, Sel 7.2 = Kasus 2, Sel 7.3 = Kasus 3, Sel 7.4 = Kasus 4 (graf tak terhubung), Sel 7.5 = rekap. Bagian B (Sel 7B) adalah studi kasus gedung, Bagian C (Sel 8 dan seterusnya) adalah eksperimen waktu dengan seed. Seed hanya dipakai di Bagian C.
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

### 6.8 Sel 7B. Studi kasus: jaringan kabel antar gedung Fakultas Teknik Unhas
Satu contoh penerapan pada **data tetap**, bukan graf acak, sehingga **tidak memakai seed** dan hasilnya sama setiap dijalankan. Data dibaca dari `data/studi_kasus_gedung_unhas.csv` (kolom: `gedung_a`, `gedung_b`, `biaya_juta`, `keterangan`). Bobot adalah biaya bersih dalam juta rupiah (biaya pemasangan dikurangi dana yang diterima), jadi boleh 0 (impas) dan negatif (penerimaan bersih). Simpul diberi nomor tetap menurut urutan abjad nama gedung, sehingga aturan pemutus seri pada Batasan 7 tetap berlaku.

> **PENTING:** selama kolom `keterangan` masih berisi **ILUSTRASI**, angkanya adalah contoh karangan, bukan hasil ukur. Ganti dengan data biaya sebenarnya, catat sumber dan tanggalnya di Bab 4, lalu hapus kata ILUSTRASI. Graf ini hanya 5 simpul, jadi dipakai untuk menunjukkan kebenaran dan penerapan, **bukan** untuk mengukur waktu.

### 6.9 Sel 8. Pembuat graf acak (seed tetap, selalu terhubung)
1. **Pohon acak.** Simpul 1 sampai n−1 masing-masing disambungkan ke satu simpul acak bernomor lebih kecil. Ini menghasilkan n−1 sisi dan graf **pasti terhubung**.
2. **Tambah sisi acak** sampai mencapai jumlah sisi target, dengan melewati pasangan yang sudah ada (**tanpa sisi ganda dan tanpa loop**, sesuai batasan Bab 1).

Pengacak dibuat sendiri dengan `random.Random(seed)`, bukan pengacak global, sehingga seed yang sama selalu menghasilkan graf yang sama. Urutan sisi diacak supaya tidak ada urutan istimewa.

### 6.10 Sel 9. Periksa pembuat graf
Tiga pemeriksaan sebelum graf dipakai: (1) seed yang sama menghasilkan graf yang sama, (2) graf selalu terhubung dan tidak punya sisi ganda atau loop, (3) jumlah sisi sesuai skenario jarang dan padat.

### 6.11 Sel 10. Verifikasi tambahan dengan `networkx` (opsional)
`networkx` **hanya dipakai sebagai pembanding**, tidak di dalam algoritma, sesuai aturan dosen (pustaka boleh sebagai pembanding). Sel ini membandingkan total bobot ketiga algoritma dengan `networkx` pada 300 graf acak kecil. Ini tambahan di luar uji kasus kecil pada Sel 7.1 sampai 7.4, yang jawabannya dari hitungan tangan. Sel ini juga mencocokkan file `.py` di folder `Kruskal`, `Prim`, dan `Borůvka` dengan kode notebook pada 100 graf acak. Pencocokan `.py` dilewati bila folder itu tidak ada di samping folder dasar (normal di Colab).

### 6.12 Sel 11. Fungsi pengukuran waktu
- Waktu diukur dengan `time.perf_counter()` dan **hanya** mengukur pemanggilan algoritma. Waktu membuat graf tidak ikut dihitung.
- Ketiga algoritma dijalankan pada **graf yang sama** supaya perbandingannya adil.
- Setiap algoritma dijalankan sekali **pemanasan** (tidak dicatat) sebelum diukur.
- **Prim** butuh daftar ketetanggaan, sedangkan Kruskal dan Borůvka memakai daftar sisi. Karena itu waktu Prim dicatat dua kali: **"Prim"** (hanya inti algoritma) dan **"Prim (+konversi)"** (ditambah waktu membuat daftar ketetanggaan). Keduanya dilaporkan agar perbandingannya jujur.
- Total bobot ketiga algoritma harus sama pada setiap ulangan. Jika berbeda, program berhenti.

### 6.13 Sel 12. Jalankan eksperimen dan simpan ke CSV
Untuk setiap skenario dan setiap ukuran: buat graf (seed tetap), lakukan pemanasan, lalu ukur sebanyak `ULANGAN` kali. **Data mentah tiap ulangan** disimpan ke `hasil/eksperimen_mentah.csv`, sehingga rata-rata dan simpangan baku bisa dihitung ulang kapan saja. Kemajuan dicetak saat berjalan.

### 6.14 Sel 13. Rata-rata dan simpangan baku
Untuk tiap kombinasi skenario, ukuran, dan algoritma dihitung **rata-rata** dan **simpangan baku sampel** (dibagi n − 1, sama dengan `statistics.stdev`), disimpan ke `hasil/ringkasan.csv`.

**Catatan:** dengan `ULANG_GRAF_BARU = False`, kelima ulangan memakai graf yang sama, sehingga simpangan baku mengukur **gangguan waktu pengukuran**, bukan variasi antar-graf. Tulis arti "ulangan" ini di Bab 4.

### 6.15 Sel 14. Kurva teori dan grafik waktu
Kurva teori berasal dari kompleksitas yang diturunkan di Bab 3 laporan:

| Algoritma | Bentuk teori yang digambar | Alasan singkat |
|---|---|---|
| Kruskal | c · m · log₂ m | Pengurutan sisi O(m log m) mendominasi |
| Prim | c · m · log₂ n | Operasi *heap* O(log) untuk O(m) tawaran |
| Borůvka | c · m · log₂ n | Paling banyak log₂ n putaran, tiap putaran memindai m sisi |

Konstanta **c dicocokkan** dengan metode kuadrat terkecil melalui titik asal, karena teori hanya menyatakan **bentuk** kurva, bukan waktu mutlaknya. Yang diuji adalah apakah **bentuk** titik ukur mengikuti bentuk kurva teori. Jika turunan di Bab 3 berbeda dari tabel ini, ubah isi `KURVA_TEORI` supaya konsisten dengan laporan.

Grafik kiri memakai sumbu linear, grafik kanan sumbu log-log (garis lurus pada log-log menunjukkan pola pangkat). Batang kesalahan menunjukkan satu simpangan baku.

### 6.16 Sel 15. Pemeriksaan kesesuaian dengan teori
Jika waktu mengikuti bentuk teori, maka **waktu ÷ teori(n, m)** kira-kira **konstan** di semua ukuran. Tabel rasio dinormalkan terhadap ukuran terkecil (nilai 1,00). Angka yang menyimpang jauh perlu dijelaskan di pembahasan (misalnya efek *cache*, atau waktu yang terlalu singkat pada ukuran kecil sehingga berisik). Hasil yang kurang bagus **tetap bagian dari penelitian** selama didokumentasikan dan dievaluasi.

### 6.16b Sel 16. Pemeriksaan kelengkapan syarat Tugas 2
Memeriksa otomatis syarat jumlah dan berkas. Tanda **[OK]** berarti terpenuhi.

### 6.17 Sel 17. Catatan metodologi, sumber, dan laporan penggunaan AI

**Keputusan desain (tulis juga di Bab 3 dan Bab 4)**

| Keputusan | Pilihan di notebook ini | Alasan |
|---|---|---|
| Alat bantu bawaan | `sorted()` (Kruskal), `heapq` (Prim) | Alat umum yang tidak menghasilkan MST. Logika memilih sisi dan mendeteksi siklus ditulis sendiri. Biayanya: pengurutan O(m log m), operasi *heap* O(log m) |
| Varian Prim | *Lazy* (tanpa *decrease-key*) | `heapq` tidak punya *decrease-key*. Antrean bisa berisi O(m) elemen, waktunya O(m log m) = O(m log n) |
| Representasi graf | Daftar sisi (Kruskal, Borůvka), daftar ketetanggaan (Prim) | Sesuai batasan Bab 1 |
| Arti "ulangan" | Mengulang pengukuran pada graf yang sama (`ULANG_GRAF_BARU = False`) | Mengukur gangguan waktu. Ubah ke True untuk ikut mengukur variasi antar-graf |
| Waktu konversi Prim | Dilaporkan dua kali (tanpa dan dengan konversi) | Agar perbandingan dengan Kruskal dan Borůvka adil |
| Pemutus seri bobot kembar | Bobot, lalu simpul terkecil, lalu simpul terbesar (`kunci_sisi` di Kruskal dan Borůvka, isi antrean di Prim) | Konsisten di ketiga algoritma, sehingga MST unik dan himpunan sisinya bisa dibandingkan |
| Simpangan baku | Simpangan baku sampel (dibagi n − 1) | Standar untuk sampel kecil |
| Pengukuran | `time.perf_counter()`, pemanasan sekali, hanya mengukur algoritma | Mengurangi derau dan efek pemanasan |
| Lingkungan | Satu mesin, satu proses, Python murni. Bila dijalankan di Colab, mesinnya adalah mesin virtual Google yang dipakai bersama | Batasan Bab 1. Spesifikasi dicatat di Sel 3 dan `lingkungan_dan_log.txt` |

**Batasan**
- Waktu diukur pada satu lingkungan perangkat keras dan perangkat lunak (lihat Sel 3). Hasil mutlak berbeda di komputer lain, sedangkan **bentuk** pertumbuhannya yang dibandingkan dengan teori.
- Kompleksitas ruang hanya dianalisis secara teoretis (batasan Bab 1).
- Waktu Python murni mencakup beban interpreter, jadi konstanta jauh lebih besar daripada implementasi C++ dan sifatnya hanya perbandingan relatif.

**Sumber**
- P. Sanders, K. Mehlhorn, M. Dietzfelbinger, R. Dementiev, *Sequential and Parallel Algorithms and Data Structures: The Basic Toolbox*, edisi ke-2, Springer, 2019, Bab 11: penyajian Kruskal, Prim, Borůvka, dan struktur data *disjoint set* (Bagian 11.2 sampai 11.4 dan 11.6).
- Kruskal (1956), Prim (1957), dan Nešetřil *et al.* (2001) untuk Borůvka, seperti di daftar pustaka Bab 1.
- Tidak ada kode yang disalin dari repositori GitHub, buku, atau forum. Draf kode dibuat dengan bantuan AI (lihat laporan di bawah).

**Laporan penggunaan AI (DRAF, sesuaikan dengan kenyataan sebelum dikumpulkan)**

> **Isi bagian ini dengan jujur dan dengan kata-katamu sendiri.** Dosen mewajibkan pemakaian AI dilaporkan di lampiran, dan kamu harus bisa menjelaskan setiap baris kode serta setiap langkah penurunan kompleksitas saat tanya jawab. Jika kamu menulis ulang bagian kode dengan versimu sendiri, catat itu di sini.

| Butir | Isi (draf) |
|---|---|
| Alat AI yang dipakai | Claude (Anthropic) |
| Tujuan | Memahami konsep Kruskal, Prim, dan Borůvka; contoh penerapan; contoh implementasi; *debugging*; pembuatan kerangka eksperimen |
| Bagian pekerjaan yang dibantu | Draf kode Kruskal, Prim, Borůvka; kerangka notebook, pembuat graf, dan eksperimen; visualisasi HTML untuk belajar |
| Cara verifikasi | (1) Uji kasus kecil dengan hitungan tangan (Sel 7.1 sampai 7.4); (2) perbandingan total bobot dengan `networkx` pada 300 graf acak kecil; (3) pemeriksaan total bobot ketiga algoritma sama pada setiap ulangan eksperimen |
| Referensi | Setiap referensi di laporan sudah dicek keberadaannya ke sumber aslinya (**centang setelah kamu benar-benar memeriksa**) |
| Bagian yang kamu tulis atau ubah sendiri | (isi sendiri) |

### 6.18 Sel 18. Simpan semua hasil
Mendaftar berkas yang tersimpan, menutup `lingkungan_dan_log.txt`, lalu di Colab memaksa Drive menyinkronkan semuanya dan melepasnya. Jalankan paling akhir. Untuk menjalankan ulang, mulai lagi dari Sel 2.
