print("Konversi suhu dari celcius ke kelvin, reamur dan fahrenheit")
celcius = float(input("Masukkan Suhu Dalam Celcius = "))

#Rumus
R = int((4/5)*celcius)
F = int(9/5*celcius+32)
K = int(celcius+273)

print(f"hasil konversi dari suhu {celcius} derajat Celcius ke Kelvin adalah = {K}K")
print(f"hasil konversi dari suhu {celcius} derajat celcius ke reamur adalah = {R}R")
print(f"hasil konversi dari suhu {celcius} derajat celcius ke fahrenheit adalah = {F}F")