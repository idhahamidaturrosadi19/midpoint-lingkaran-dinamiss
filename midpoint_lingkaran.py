import matplotlib.pyplot as grafik

def kalkulasi_titik_oktan(x_pusat, y_pusat, x, y, daftar_x, daftar_y):
    # Menyebar 8 titik simetris ke dalam list
    daftar_x.extend([x_pusat + x, x_pusat - x, x_pusat + x, x_pusat - x, x_pusat + y, x_pusat - y, x_pusat + y, x_pusat - y])
    daftar_y.extend([y_pusat + y, y_pusat + y, y_pusat - y, y_pusat - y, y_pusat + x, y_pusat + x, y_pusat - x, y_pusat - x])

def generate_lingkaran_midpoint(x_pusat, y_pusat, jari2):
    koordinat_x = []
    koordinat_y = []

    # Set nilai awal
    titik_x = 0
    titik_y = jari2
    batas_keputusan = 1 - jari2 

    # Titik mula-mula
    kalkulasi_titik_oktan(x_pusat, y_pusat, titik_x, titik_y, koordinat_x, koordinat_y)

    # Proses iterasi algoritma
    while titik_x < titik_y:
        titik_x += 1
        if batas_keputusan < 0:
            batas_keputusan += 2 * titik_x + 1
        else:
            titik_y -= 1
            batas_keputusan += 2 * titik_x - 2 * titik_y + 1
            
        kalkulasi_titik_oktan(x_pusat, y_pusat, titik_x, titik_y, koordinat_x, koordinat_y)

    return koordinat_x, koordinat_y

# --- Blok Eksekusi ---
print("=== GENERATOR LINGKARAN MIDPOINT ===")
input_x = int(input("Ketik titik pusat X: "))
input_y = int(input("Ketik titik pusat Y: "))
input_r = int(input("Ketik nilai radius : "))

# Panggil fungsi
hasil_x, hasil_y = generate_lingkaran_midpoint(input_x, input_y, input_r)

# Tampilkan di Colab
grafik.figure(figsize=(6, 6))
grafik.plot(hasil_x, hasil_y, 'ro') # 'ro' artinya titik warna merah (Red)
grafik.title(f'Hasil Algoritma Midpoint | Pusat({input_x},{input_y}), Radius: {input_r}')
grafik.xlabel('Koordinat X')
grafik.ylabel('Koordinat Y')
grafik.grid(color='gray', linestyle='--', linewidth=0.5)
grafik.axis('equal') 
grafik.show()
