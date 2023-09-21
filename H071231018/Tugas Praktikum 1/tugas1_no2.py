# Rumus C>F; Tf=9/5Tc +32
# Rumus C>R; Tr=4/5Tc
# Rumus C>K; Tk=Tc+273

Tc = float (input("Masukkan Suhu dalam Celcius= "))
Tf = int (9 / 5 * Tc + 32)
Tr = int (4 / 5 * Tc)
Tk = int (Tc + 273)

print(f'Hasil konversi dari suhu 50 derajat Celcius ke Kelvin adalah  {Tk}K')
print(f'Hasil konversi dari suhu 50 derajat Celcius ke Reamur adalah = {Tr}R')
print(f'Hasil konversi dari suhu 50 derajat Celcius ke Fahrenheit adalah : {Tf}F')