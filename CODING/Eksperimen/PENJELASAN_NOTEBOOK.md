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

## 3. Yang tidak ada di notebook ini

| Bagian | Letak | Menjalankan |
|---|---|---|
| Contoh dasar tiap algoritma dan visualisasinya | `../Contoh_Dasar/` | `python kruskal.py`, `python prim.py`, `python boruvka.py` |
| Uji kasus kecil (4 kasus) | `../Uji_Kecil/` | `python uji_kecil.py` |
| Studi kasus 5 gedung Unhas | `../Studi_Kasus/` | `python studi_kasus.py` |

Notebook ini hanya berisi hal yang berat secara komputasi: graf acak ber-*seed*, pengukuran waktu, grafik, dan analisisnya.

## 4. Isi folder hasil

Folder dasar adalah folder Drive (Colab atau `FOLDER_DRIVE_LOKAL`) atau folder tempat notebook dijalankan.

| Berkas | Isi |
|---|---|
| `hasil/eksperimen_mentah.csv` | Waktu setiap ulangan (data mentah) |
| `hasil/ringkasan.csv` | Rata-rata dan simpangan baku per ukuran |
| `hasil/rasio_terhadap_teori.csv` | Pemeriksaan kesesuaian dengan kurva teori |
| `grafik/waktu_<skenario>.png` | Grafik waktu, titik ukur disandingkan dengan kurva teori |
| `lingkungan_dan_log.txt` | Spesifikasi mesin, versi pustaka, dan seluruh keluaran teks notebook |

## 5. Peta syarat tugas ke sel

| Syarat | Sel |
|---|---|
| Kruskal dan Prim ditulis sendiri, tanpa pustaka MST sebagai inti | 4, 5 |
| Pembanding ketiga (Borůvka) | 6 |
| Fungsi atau kelas dengan komentar | 4 sampai 6 |
| Minimal 3 kasus uji kecil yang bisa dicek manual | di luar notebook: `../Uji_Kecil/uji_kecil.py` |
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
Sel ini menentukan `FOLDER_DASAR`: Colab (memasang Drive), `FOLDER_DRIVE_LOKAL` bila diisi, atau folder tempat notebook dijalankan. Di dalamnya dibuat `hasil/` dan `grafik/`. Semua keluaran `print` juga disalin ke `lingkungan_dan_log.txt` sampai Sel 18 menutupnya.

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

### 6.7 Uji kasus kecil (dipindah ke kode lokal)

Uji kasus kecil **tidak lagi ada di notebook**. Kodenya ada di `../Uji_Kecil/uji_kecil.py`, dan hitungan tangan keempat kasus ada di `../Uji_Kecil/PENJELASAN_UJI_KECIL.md`. Notebook hanya menyisakan Sel 7 (fungsi bantu `jalankan_tiga_algoritma`), karena eksperimen berbasis seed membutuhkannya.

### 6.8 Studi kasus (dipindah ke kode lokal)

Studi kasus gedung Unhas **tidak lagi ada di notebook**. Kodenya ada di `../Studi_Kasus/studi_kasus.py` dengan data `studi_kasus_gedung_unhas.csv`, dan penjelasannya di `../Studi_Kasus/PENJELASAN_STUDI_KASUS.md`.

### 6.9 Sel 8. Pembuat graf acak (seed tetap, selalu terhubung)
1. **Pohon acak.** Simpul 1 sampai n−1 masing-masing disambungkan ke satu simpul acak bernomor lebih kecil. Ini menghasilkan n−1 sisi dan graf **pasti terhubung**.
2. **Tambah sisi acak** sampai mencapai jumlah sisi target, dengan melewati pasangan yang sudah ada (**tanpa sisi ganda dan tanpa loop**, sesuai batasan Bab 1).

Pengacak dibuat sendiri dengan `random.Random(seed)`, bukan pengacak global, sehingga seed yang sama selalu menghasilkan graf yang sama. Urutan sisi diacak supaya tidak ada urutan istimewa.

### 6.10 Sel 9. Periksa pembuat graf
Tiga pemeriksaan sebelum graf dipakai: (1) seed yang sama menghasilkan graf yang sama, (2) graf selalu terhubung dan tidak punya sisi ganda atau loop, (3) jumlah sisi sesuai skenario jarang dan padat.

### 6.11 Sel 10. Verifikasi tambahan dengan `networkx` (opsional)
`networkx` **hanya dipakai sebagai pembanding**, tidak di dalam algoritma, sesuai aturan dosen (pustaka boleh sebagai pembanding). Sel ini membandingkan total bobot ketiga algoritma dengan `networkx` pada 300 graf acak kecil. Ini tambahan di luar uji kasus kecil pada `../Uji_Kecil/uji_kecil.py`, yang jawabannya dari hitungan tangan. Sel ini juga mencocokkan file `.py` di folder `Kruskal`, `Prim`, dan `Borůvka` dengan kode notebook pada 100 graf acak. Pencocokan `.py` dilewati bila folder itu tidak ada di samping folder dasar (normal di Colab).

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
- Tidak ada kode yang disalin dari repositori GitHub, buku, atau forum. Kode inti algoritma ditulis sendiri, dan AI hanya membantu bagian eksperimen pada notebook (lihat laporan di bawah).

**Laporan penggunaan AI**

Ringkasan lengkap ada di bagian "Penggunaan AI" pada `../../README.md`. Dosen mewajibkan pemakaian AI dilaporkan di lampiran.

| Butir | Isi |
|---|---|
| Alat AI yang dipakai | Claude (Anthropic) |
| Bagian kode yang ditulis sendiri | Kode inti algoritma Kruskal, Prim, dan Borůvka |
| Bagian kode yang dibantu AI | Bagian eksperimen pada notebook, yaitu pembangkitan graf acak ber-*seed* |
| Cara verifikasi | (1) Uji kasus kecil dengan hitungan tangan (`../Uji_Kecil/uji_kecil.py`); (2) perbandingan total bobot dengan `networkx` pada 300 graf acak kecil; (3) pemeriksaan total bobot ketiga algoritma sama pada setiap ulangan eksperimen |
| Referensi laporan | AI membantu mencari, lalu penulis memverifikasi keberadaan dan kesesuaian tiap referensi secara manual |

### 6.18 Sel 18. Simpan semua hasil
Mendaftar berkas yang tersimpan, menutup `lingkungan_dan_log.txt`, lalu di Colab memaksa Drive menyinkronkan semuanya dan melepasnya. Jalankan paling akhir. Untuk menjalankan ulang, mulai lagi dari Sel 2.
