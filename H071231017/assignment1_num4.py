# buatlah program untuk menentukan karakter huruf kapital, huruf kecil dan angka dari inputan yang dilemparkan

print("Pengujian jenis karakter\n---------------")

k = input("Karakter =")

print ("Huruf kapital?",k.isupper())
print ("Huruf kecil?",k.islower())
print ("Angka?",k.isdigit())