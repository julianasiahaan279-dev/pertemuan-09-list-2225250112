# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Angelita Juliana Siahaan
NIM: 2225250112
Kelas: 3B

## Tujuan
Mengolah kumpulan data numerik dengan list Python.

## Struktur Program
- `latihan/01_buat_list.py` : membuat dan membaca list
- `latihan/02_indeks_slicing.py` : indeks dan slicing
- `latihan/03_manipulasi_list.py` : mengubah, menambah, menyisipkan, menghapus elemen
- `latihan/04_agregasi_nilai.py` : total, rata-rata, minimum, maksimum
- `latihan/05_filter_kelulusan.py` : menyaring nilai lulus (batas 60)
- `latihan/06_fungsi_statistik.py` : fungsi rata-rata
- `praktik/analisis_nilai_mahasiswa.py` : analisis nilai mahasiswa

## Cara Menjalankan
python praktik/analisis_nilai_mahasiswa.py

## Test Case
| Data | Yang diperiksa | Hasil diharapkan | Hasil aktual | Status |
|------|----------------|------------------|--------------|--------|
| [60, 70, 80] | Rata-rata | 70.00 | 70.00 | Lulus |
| [60, 70, 80] | Minimum / maksimum | 60 / 80 | 60 / 80 | Lulus |
| [60, 70, 80] | Jumlah lulus | 3 | 3 | Lulus |
| [59, 60, 61] | Batas kelulusan | 2 lulus | 2 lulus | Lulus |
| [] | Fungsi rata_rata | Tidak error | 0 (tidak error) | Lulus |

## Refleksi
Satu hal yang saya pahami: indeks list Python dimulai dari 0, sehingga elemen pertama adalah `nilai[0]` dan elemen terakhir bisa diambil dengan `nilai[-1]`. Pada slicing seperti `nilai[1:4]`, batas akhirnya tidak ikut diambil, jadi hasilnya hanya indeks 1, 2, dan 3.

## Refleksi
Satu hal yang saya pahami: indeks list Python dimulai dari 0, sehingga elemen pertama adalah `nilai[0]` dan elemen terakhir bisa diambil dengan `nilai[-1]`. Pada slicing seperti `nilai[1:4]`, batas akhirnya tidak ikut diambil, jadi hasilnya hanya indeks 1, 2, dan 3.