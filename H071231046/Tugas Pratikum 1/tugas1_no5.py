print("Konversi detik ke jam")
z = int(input("Masukkan Jumlah Detik : "))

jam = z//3600
z %= 3600
menit = z //60
z %= 60
detik = z % 60

print(f"{jam:02d}:{menit:02d}:{detik:02}")