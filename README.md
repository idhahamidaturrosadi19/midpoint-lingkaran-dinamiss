# 🔵 Implementasi Midpoint Lingkaran Dinamis

## 📝 Deskripsi
Repository ini berisi implementasi algoritma Midpoint untuk membentuk visualisasi lingkaran menggunakan bahasa pemrograman Python. Program ini dirancang secara **dinamis**, yang berarti pengguna dapat menentukan sendiri titik pusat (koordinat X dan Y) serta besaran jari-jari (radius) dari lingkaran dengan angka berapapun.

## ✨ Fitur Utama
* **Input Fleksibel & Dinamis:** Pengguna bebas memasukkan nilai koordinat titik pusat (X, Y) dan nilai radius (r) apa saja via terminal/konsol. Program tidak terpaku (*hardcoded*) pada satu nilai tertentu.
* **Algoritma Midpoint:** Menggunakan perhitungan integer dari parameter keputusan (*decision parameter*) 8 oktan yang efisien tanpa menggunakan fungsi *floating-point*.
* **Visualisasi Matplotlib:** Menampilkan plot titik-titik koordinat dalam bentuk grafik 2D berskala presisi (*equal axis*).

## 🖼️ Hasil Visualisasi (Input: X=5, Y=5, R=10)

![Visualisasi Lingkaran Midpoint](<img width="1017" height="754" alt="image" src="https://github.com/user-attachments/assets/c5f023e9-da8b-4419-8093-ee65c136716e" />
.png)

*Gambar di atas menunjukkan hasil lingkaran dinamis dengan warna titik merah dan latar belakang grid, berpusat di koordinat (5, 5) dan berjari-jari 10.*

## 🚀 Cara Menjalankan Program

Program ini dapat dijalankan langsung di lokal (VS Code/Terminal) maupun di Google Colab.

1. Pastikan *library* `matplotlib` sudah terpasang.
2. Jalankan file `midpoint_lingkaran.py`.
3. Masukkan input saat diminta oleh program. **(Angka disini hanya sebagai contoh, program akan tetap berjalan normal dengan kombinasi angka berapapun!)**
   ```text
   Ketik titik pusat X: 5
   Ketik titik pusat Y: 5
   Ketik nilai radius : 10
