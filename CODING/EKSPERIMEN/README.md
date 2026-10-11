# EKSPERIMEN

Notebook `TUGAS_MST_LOKAL.ipynb`: Kruskal, Prim, dan Borůvka pada graf acak ber-*seed* (2026), pengukuran waktu, grafik, dan perbandingan dengan kurva teori. Uji kecil dan studi kasus ada di `../UJI_KECIL/` dan `../STUDI_KASUS/`.

## Menjalankan

| Cara | Langkah |
|---|---|
| Colab | Unggah notebook ke Drive, **Runtime > Run all**, izinkan akses Drive di Sel 2. Hasil di `My Drive/TUGAS BESAR PAK ABDI/HASIL_EKSPERIMEN` (ubah lewat `NAMA_FOLDER_DRIVE`) |
| Komputer + Drive for Desktop | Isi `FOLDER_DRIVE_LOKAL` di Sel 2 |
| Lokal / VS Code | `pip install -r REQUIREMENTS.txt`, jalankan semua sel dari folder ini |

Penuh sekitar 1 sampai 3 menit. `MODE_CEPAT = True` (Sel 1, sekitar 15 detik) hanya uji coba; hasilnya jangan dipakai di laporan. Di Colab, waktu adalah waktu mesin Google bersama, jadi catat spesifikasinya (Sel 3) di Bab 4.1.

Pustaka: bawaan Python, `pandas`, `numpy`, `matplotlib`. `networkx` hanya untuk verifikasi (Sel 10), bukan di dalam algoritma.

## Keluaran

| Berkas | Isi |
|---|---|
| `HASIL/EKSPERIMEN_MENTAH.csv` | Waktu tiap ulangan |
| `HASIL/RINGKASAN.csv` | Rata-rata dan simpangan baku sampel (n − 1) per ukuran |
| `HASIL/RASIO_TERHADAP_TEORI.csv` | Waktu ÷ kurva teori, dinormalkan ke ukuran terkecil |
| `GRAFIK/WAKTU_<SKENARIO>.png` | Titik ukur dengan kurva teori (linear dan log-log) |
| `LINGKUNGAN_DAN_LOG.txt` | Spesifikasi mesin, versi pustaka, log keluaran |

## Isi sel

| Sel | Isi |
|---|---|
| 1 | Pengaturan: `SEED`, tiga skenario (jarang, padat, jarang bobot kembar) |
| 2, 3 | Folder hasil dan log; lingkungan uji |
| 4 | Kruskal + `HimpunanTerpisah` (*union by rank*, *path halving*); `sorted()` O(m log m) |
| 5 | Prim *lazy* dengan `heapq` (tanpa *decrease-key*), O(m log n) |
| 6 | Borůvka, paling banyak log₂ n putaran |
| 7 | `jalankan_tiga_algoritma` |
| 8, 9 | Pembuat graf: pohon acak (pasti terhubung) + sisi acak tanpa sisi ganda dan *loop*; pemeriksaannya |
| 10 | Verifikasi total bobot dengan `networkx` pada 300 graf acak kecil |
| 11 | Pengukuran: `time.perf_counter()`, pemanasan sekali, hanya algoritma yang diukur, graf sama untuk ketiganya, total bobot harus sama |
| 12, 13 | Eksperimen ke CSV; rata-rata dan simpangan baku |
| 14, 15 | Kurva teori dan grafik; pemeriksaan rasio |
| 16 | Pemeriksaan kelengkapan syarat |
| 17 | Catatan metodologi (di bawah) |
| 18 | Simpan hasil; jalankan paling akhir |

Kurva teori: Kruskal c·m·log₂ m, Prim dan Borůvka c·m·log₂ n. Konstanta c dicocokkan dengan kuadrat terkecil lewat titik asal; yang diuji adalah bentuk, bukan waktu mutlak. Bila turunan di Bab 3 berubah, sesuaikan `KURVA_TEORI`.

## Keputusan desain dan batasan (Sel 17)

| Keputusan | Pilihan | Alasan |
|---|---|---|
| Alat bantu bawaan | `sorted()` (Kruskal), `heapq` (Prim) | Bukan pembangkit MST; logika memilih sisi dan deteksi siklus ditulis sendiri |
| Representasi graf | Daftar sisi (Kruskal, Borůvka), daftar ketetanggaan (Prim) | Batasan Bab 1 |
| Waktu Prim | Dilaporkan dua kali: "Prim" dan "Prim (+konversi)" | Agar adil terhadap dua algoritma lain |
| Arti "ulangan" | Mengulang pengukuran pada graf yang sama (`ULANG_GRAF_BARU = False`) | Simpangan baku mengukur gangguan waktu, bukan variasi antar-graf; tulis di Bab 4 |
| Pemutus seri | Bobot, lalu simpul terkecil, lalu terbesar, di ketiga algoritma | MST unik, himpunan sisi bisa dibandingkan |

Batasan: satu lingkungan perangkat keras dan lunak (hasil mutlak berbeda di komputer lain, yang dibandingkan adalah bentuk pertumbuhan); ruang hanya dianalisis secara teoretis; Python murni sehingga konstanta jauh di atas C++ dan hanya relatif.

Sumber: P. Sanders *et al.*, *Sequential and Parallel Algorithms and Data Structures: The Basic Toolbox*, 2nd ed., Springer, 2019, Bab 11 (*union by rank*, kompresi lintasan; *path halving* adalah varian pilihan penulis); Kruskal (1956), Prim (1957), Nešetřil *et al.* (2001). Tidak ada kode yang disalin dari repositori, buku, atau forum.

## Laporan penggunaan AI (draf)

Ringkasan lengkap ada di bagian "Penggunaan AI" pada `../../README.md`. Tulis ulang dengan kata sendiri sebelum dikumpulkan.

| Butir | Isi |
|---|---|
| Alat | Claude (Anthropic) |
| Ditulis sendiri | Kode inti Kruskal, Prim, Borůvka |
| Dibantu AI | Bagian eksperimen notebook (pembangkit graf acak ber-*seed*) |
| Verifikasi | (1) Uji kecil dengan hitungan tangan; (2) total bobot dibandingkan `networkx` pada 300 graf; (3) total bobot ketiga algoritma sama di tiap ulangan |
| Referensi | AI membantu mencari; penulis memverifikasi manual |
