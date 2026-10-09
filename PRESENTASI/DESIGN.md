# DESIGN.md: Panduan Gaya Presentasi Web

Dokumen ini adalah konteks gaya untuk membuat slide baru (slide 4 sampai 12) agar seragam dengan slide 1 sampai 3. Nilai di bawah diambil dari kode yang sudah jadi. Bila berbeda dengan kode, kode yang benar.

## 1. Prinsip

- Tema hitam bergaya Palantir: latar gelap, garis tipis, huruf mono kapital untuk label, satu warna aksen biru, satu warna pendamping kuning.
- Layar bukan tempat membaca. Teks sedikit, gerak yang menjelaskan.
- Satu klik maju satu ide. Tidak ada animasi satu kali yang berjalan sendiri lalu hilang tanpa bisa diulang; animasi penjelas boleh berulang (loop) bila fungsinya memperlihatkan cara kerja.
- Satu gambar tidak boleh memuat dua pesan. Bila perlu dua pesan, pecah jadi dua langkah.
- Warna selalu bermakna, bukan hiasan (lihat bagian 3).
- Aturan tulis: Bahasa Indonesia, istilah asing miring (`<em>`), tanpa tanda pisah panjang (em dash), tanpa tanda hubung sebagai pemisah kalimat, tidak ada angka atau sitasi yang tidak bisa dipertanggungjawabkan.

## 2. Struktur Berkas

- Satu slide satu berkas `slideN.html` berisi HTML, CSS, dan JS sendiri (tanpa pustaka luar; hanya Google Fonts dengan cadangan).
- `index.html`: daftar slide dengan pratinjau (iframe skala), daftar `SLIDES` berisi judul, menit, nama berkas, dan `ready`.
- `aset/logo-unhas.png`: logo.
- `RENCANA_SLIDE.md`: rencana dan penjelasan tiap slide. `DESIGN.md`: dokumen ini.
- Slide baru: salin `slide3.html` sebagai dasar (paling lengkap dan terbaru), ganti `PREV_SLIDE`, `NEXT_SLIDE`, `SLIDE_NO`, judul, dan isi. Lalu set `ready:true` di `index.html` dan isi `NEXT_SLIDE` pada slide sebelumnya.

## 3. Token Desain

| Token | Nilai | Makna |
|-------|-------|-------|
| `--bg` | `#050507` | latar |
| `--panel` | `#0a0b0f` | permukaan kartu dan dock |
| `--line` / `--line2` | `rgba(255,255,255,.13)` / `.07` | garis utama / garis halus |
| `--text` | `#f1f2f6` | teks utama dan judul |
| `--body` | `#c4c7d4` | teks isi |
| `--mute` | `#80849a` | label, keterangan |
| `--accent` | `#7db4ff` | biru: hal yang dibahas, sisi MST, status aktif |
| `--accent-bright` | `#c4dcff` | biru terang: sorotan, sisi yang sedang dipilih |
| `--amber` | `#ffc266` | kuning: kandidat, perbandingan, pembanding (Borůvka), peringatan |

Makna warna di grafik: abu = belum diproses, kuning = kandidat yang sedang dibandingkan, putih tebal = pilihan saat ini, biru = sudah masuk MST.

Huruf: `Space Grotesk` (isi dan judul, bobot 400 sampai 700, judul `letter-spacing:-.03em`) dan `JetBrains Mono` (label, angka, bobot sisi, penanda). Cadangan: `Segoe UI`, `Cascadia Mono`, `Consolas`.

Latar panggung: gradasi radial biru samar di kiri atas, bayangan biru di kanan bawah, dan titik-titik grid 32px (`radial-gradient(rgba(255,255,255,.055) 1px, transparent 1.2px)`).

## 4. Panggung dan Tata Letak

- Panggung tetap 1920 × 1080, diskalakan ke jendela dengan `transform: translate() scale(min(w/1920, h/1080))` dan ditengahkan (fungsi `fit()`). Semua ukuran di CSS memakai piksel panggung.
- Margin kiri dan kanan 96px. Header: top 52, tinggi 76, logo 60px, nama universitas 28px, program studi 19px, penanda "Tugas Besar Analisis Algoritma" di kanan (mono 16px kapital). Garis bawah header `--line2`.
- Judul slide: `h1` 56px bold di left 96, top 158 (slide dengan kartu penuh) atau top 236 (slide dengan teks kiri dan panel kanan).
- Pola A (teks kiri, grafik kanan): kolom teks left 96, top 322, lebar 740. Panel grafik left 880, top 236, 944 × 716.
- Pola B (kartu penuh): kartu mulai top 430, tinggi 520, tiga kolom sama lebar 1728 total, jarak 36.
- Footer: bilah progres di bottom 44, lebar penuh 96 sampai 96. Enam kelompok: Pembuka (1), Konsep (1), Algoritma (5), Teori (1), Eksperimen (3), Penutup (1). Garis 3px, label mono 13px kapital, kelompok berjalan berwarna biru.
- Jangan menaruh elemen penting di bawah y = 1000 (area bilah progres dan dock).

## 5. Komponen

**Panel grafik (Pola A).** Bingkai 1px `--line`, gradasi tipis, empat sudut siku biru 16px (tebal 2px). Kepala panel 76px: kiri "Fig. NN · judul" (mono 15px kapital), kanan readout (label mono 13px, nilai mono 32px). Dasar panel 112px berisi keterangan satu kalimat (23px) atau legenda.

**Kartu (Pola B).** Radius 6px, bingkai `--line`, gradasi biru (atau kuning untuk pembanding) dari atas. Saat tampil: bingkai berwarna 55% dan bayangan lembut 14%, garis atas 3px menyapu dari kiri ke kanan. Isi: baris kepala mono (nomor kiri, penanda kanan berwarna), nama algoritma 56px bold, grafik mini, keterangan satu frasa di dasar dengan kata kunci tebal berwarna.

**Teks bertahap (Pola A).** Blok `.blk` bertingkat: label mono kapital (`01 · Definisi`) dan paragraf 30 sampai 40px. Blok aktif terang, blok sebelumnya redup (`.seen`, opacity .5). Blok tersembunyi runtuh (`max-height:0`) agar teks tidak melompat.

**Graf.** Titik: lingkaran r 25 sampai 34 dengan halo, huruf mono. Sisi: garis dasar 2 sampai 3px abu, garis sorot 5 sampai 9px; label bobot di tengah sisi (kotak mono kecil). Graf contoh standar (5 titik, bobot unik, MST tunggal biaya 18):

- Titik: A (140,260), B (340,100), C (340,420), D (580,260), E (820,260) pada viewBox 960 × 520.
- Sisi: AB 5, AC 8, BC 11, BD 3, CD 6, DE 4, CE 9. MST: BD 3, DE 4, AB 5, CD 6.
- Semua slide algoritma memakai graf ini agar penonton tidak perlu belajar graf baru.

**Dock navigasi.** Kotak mengambang di bawah tengah (bottom 78). Muncul bila kursor berada di 15% bagian bawah layar atau di atas dock, hilang 1 detik setelah kursor pergi. Isi: penghitung langkah, tombol Sebelumnya, Reset, Berikutnya (teks saja, tanpa simbol), baris petunjuk tombol. Latar `#0a0b0f` pekat (tidak transparan).

**Zona tepi layar.** 7% lebar di kiri dan kanan berfungsi seperti Canva: kursor berubah menjadi panah bulat, klik mundur atau maju. Zona kiri dimatikan bila tidak ada slide sebelumnya.

## 6. Gerak (Motion Graph)

Prinsip: gerak harus menjelaskan urutan sebab akibat, bukan sekadar menghibur.

| Kebutuhan | Teknik |
|-----------|--------|
| Sisi tergambar | `pathLength="1"`, `stroke-dasharray:1`, animasikan `stroke-dashoffset` 1 ke 0 (0,6 sampai 0,9 detik, `cubic-bezier(.3,.7,.2,1)`) |
| Berurutan (stagger) | variabel CSS `--d` (ms) dipakai sebagai `transition-delay` |
| Titik muncul | skala 0 ke 1 dengan `cubic-bezier(.2,1.5,.4,1)` (pantulan kecil), 0,55 sampai 0,8 detik |
| Kartu masuk | `translateY(46px) scale(.97)` dan opacity 0 ke normal, 0,8 detik, `cubic-bezier(.2,.9,.2,1)` |
| Idle (hidup terus) | titik melayang `translate` bolak balik 7 detik `ease-in-out alternate` dengan jeda negatif berbeda; berkedip lewat `stroke` 4 detik; cahaya kecil berjalan di garis lewat `animateMotion` (SMIL) dengan `begin` bertingkat |
| Garis putus berjalan | `stroke-dasharray` lalu animasikan `stroke-dashoffset` (`linear infinite`) |
| Denyut | cincin yang membesar dan memudar (`scale` 1 ke 2,3, opacity .55 ke 0) |
| Pindai | pita gradien tipis yang bergeser vertikal perlahan sebagai latar hidup |
| Berpindah slide | `body.leaving` memudar 0,25 detik sebelum `location.href` berubah; slide baru memudar masuk 0,5 detik |

Aturan:

- Durasi transisi 0,4 sampai 0,9 detik. Hindari yang lebih cepat dari 0,3 detik kecuali penanda pengujian sisi (`try`).
- Semua animasi berulang disimpan di daftar `runs` (id `setTimeout`) dan dibersihkan lewat `clearRuns()` setiap berganti langkah atau reset, supaya tidak menumpuk.
- Elemen yang dianimasikan dengan CSS `transform` tidak boleh juga memakai atribut SVG `transform` untuk posisi. Bungkus: `<g transform="translate(x,y)">` di luar, elemen beranimasi di dalam.
- Elemen SMIL yang baru mulai di tengah jalan harus tersembunyi sampai `begin` (pakai `<animate attributeName="opacity" begin=...>`), kalau tidak titik tampak diam di pojok.
- Pengujian: render dengan `?step=N` (loncat ke langkah N) dan ambil tangkapan layar di Chromium/Playwright pada 1920 × 1080 sebelum dianggap selesai.

### Animasi algoritma standar (dipakai ulang di slide 4 sampai 7)

- **Kruskal:** sisi diuji dari bobot terkecil. Penguji menyala putih sebentar (`try`), lalu menjadi biru (diterima) atau meredup (ditolak karena siklus).
- **Prim:** tiap putaran: sisi yang menyeberang dari pohon ke luar menyala kuning (`cand`) dengan label bobot ikut kuning, yang kalah memudar (`rej`), yang termurah menyala putih tebal (`pick`) lalu menjadi biru dan titik baru masuk.
- **Borůvka:** semua titik menyala bersamaan, tiap titik menandai sisi termurahnya serentak (kuning), lalu semuanya menjadi biru dalam satu putaran.
- **Cut property:** garis putus bergerak membatasi kelompok titik (dibangun dari cangkang cembung titik kelompok), sisi termurah yang menyeberang diberi tanda AMAN.

## 7. Kerangka Dasar Satu Slide

```
<div id="stage">                      // 1920x1080, diskalakan fit()
  .header                             // logo, nama kampus, penanda tugas
  .kicker h1                          // judul slide
  [Pola A] .copy (blok bertahap) + .panel (svg graf, readout, keterangan)
  [Pola B] .cards (grid 3 kolom)
  .footer .prog                       // bilah progres 6 kelompok
  #dock                               // navigasi pop up
</div>
<script>
  const PREV_SLIDE, NEXT_SLIDE, SLIDE_NO
  STEPS = [ ()=>{...}, ... ]          // satu fungsi per klik, idempoten
  render() progress() next() prev() reset() leave(url) fit()
  keyboard, dock, edge zone
</script>
```

Kontrol (seragam di semua slide): panah kiri/kanan, Spasi, PageUp, PageDown, Backspace, Enter = mundur atau maju; `R` reset; `F` layar penuh; `I` indeks; `?step=N` lompat langkah. Maju di langkah terakhir pindah ke slide berikutnya, mundur di langkah pertama pindah ke slide sebelumnya.

## 8. Struktur Presentasi (PPT)

Total rencana 14,5 menit (batas tugas 10 sampai 15 menit). Rincian ada di `RENCANA_SLIDE.md`.

| No | Slide | Waktu | Pola |
|----|-------|-------|------|
| 1 | Judul | 0,5 | khusus (latar jaringan hidup) |
| 2 | Apa itu MST (definisi, masalah, solusi *greedy*, *cut property*) | 2 | A |
| 3 | Algoritma yang dibahas | 0,5 | B |
| 4 | Kruskal | 1,5 | A |
| 5 | Prim | 1,5 | A |
| 6 | Borůvka | 1,5 | A |
| 7 | Contoh manual tiga algoritma | 1,5 | B |
| 8 | Kompleksitas teoretis | 1,5 | A |
| 9 | Implementasi | 1 | A |
| 10 | Metode eksperimen | 1 | A |
| 11 | Hasil dan analisis | 1,5 | A (grafik hasil) |
| 12 | Kesimpulan | 0,5 | khusus |

Pola isi tiap slide algoritma (4 sampai 6): judul, satu kalimat ide, graf contoh beranimasi dengan langkah bertahap, readout (total biaya atau jumlah sisi), keterangan satu kalimat per langkah, ditutup pernyataan kompleksitas hanya bila sudah diverifikasi.

Slide hasil memakai data nyata dari eksperimen laporan; jangan menaruh angka yang belum diukur. Bila ada grafik data, warna seri mengikuti makna warna di bagian 3 (Kruskal biru, Prim biru terang, Borůvka kuning) dan sumbu diberi satuan.

## 9. Daftar Periksa Sebelum Slide Dianggap Selesai

- [ ] Memakai token warna dan huruf di bagian 3, tanpa warna baru.
- [ ] Teks di layar singkat; penjelasan panjang dipindah ke catatan penyaji di `RENCANA_SLIDE.md`.
- [ ] Setiap langkah bisa dimundurkan dan Reset mengembalikan ke awal tanpa sisa animasi.
- [ ] `clearRuns()` dipanggil pada setiap perpindahan langkah.
- [ ] Tidak ada em dash, tidak ada tanda hubung pemisah kalimat, istilah asing miring.
- [ ] Tangkapan layar pada 1920 × 1080 untuk tiap langkah, tidak ada teks bertabrakan atau terpotong.
- [ ] Judul sejajar dengan slide lain, tidak ada elemen di bawah y = 1000.
- [ ] `index.html` diperbarui (`ready:true`), `NEXT_SLIDE` slide sebelumnya terisi, `RENCANA_SLIDE.md` disesuaikan.
- [ ] Commit dan push ke `main`.
