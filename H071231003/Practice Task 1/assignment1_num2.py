print ("Konversi Suhu dari Celcius ke Kelvin, Reamur dan Fahrenheit")

c = float(input("Masukkan Suhu dalam Celcius : "))

#Kelvin
K = int(c + 273)
print ("\nHasil konversi dari suhu ",c, "Derajat Celcius ke Kelvin adalah :",str(K),"K" )

#Reamur
R = int((4/5) * c)
print ("Hasil konversi dari suhu ",c, "Derajat Celcius ke Reamur adalah :",str(R),"R")

#Fahrenheit
F = int(((9/5)*c)+32)
print ("Hasil konversi dari suhu ",c, "Derajat Celcius ke Fahrenheit adalah :",str(F),"F")
