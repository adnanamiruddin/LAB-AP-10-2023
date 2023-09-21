# buatlah program yang bisa secara otomatis mengonversi suhu dari skala celcius ke beberapa skala lain seperti kelvin, reamur, farenheit

c = int(input("masukkan nilai celcius:"))

k = c+273
r = (c*4//5)
f = (c*9//5+32)

print(f"hasil konversi dari suhu {c} derajat celcius ke kelvin adalah :{k}K")
print(f"hasil konversi dari suhu {c} derajat celcius ke reamur adalah :{r}R")
print(f"hasil konversi dari suhu {c} derajat celcius ke fahrenheit adalah :{f}F")