print("Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit")

x = int(input("Masukkan suhu dalam Celcius = "))

k = x + 273
r = int(4/5 * x) 
f = int((9/5* x) + 32)

print(f'Nilai suhu {x} celcius setelah dikonversi adalah = {k}K')
print(f'Nilai suhu {x} celcius setelah dikonversi adalah = {r}R')
print(f'Nilai suhu {x} celcius setelah dikonversi adalah = {f}F')