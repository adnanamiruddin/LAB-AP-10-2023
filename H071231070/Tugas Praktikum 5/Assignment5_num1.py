#Program Mixed Kata
kata1 = input("Masukkan Kata Pertama : ") #Input Kata Pertama, Fungsi .lower() membuat semua karakter pada string menjadi Huruf Kecil (Lowercase)
kata2 = input("Masukkan Kata Kedua : ") #Input Kata Kedua
kata2 = "".join(reversed(kata2)) #Inputan Kata Kedua Dibalik hurufnya, misalnya Abc, jadi cbA
hasil = "" # Variabel hasil disini merupakan string kosong berguna untuk tempat menaruh string yang akan di-mix (dicampur)
x = min(len(kata1), len(kata2))
#variabel x, min disini berfungsi untuk mencari nilai terkecil dari kedua variabel itu, misal len(kata1) = 7, len(kata2) = 3, maka min disini akan mengambil nilai 3, jadinya x = 3
for i in range(x): #i nya akan berulang sebanyak x, disini sudah ditentukan berapa x nya dari variabel x
    hasil += kata1[i] + kata2[i] #disini variabel hasil mengalami perubahan nilai didalamnya yang awalnya string kosong, menjadi ada isinya, diisi atau ditambah oleh kata1[i] dan kata2[i]

print(f"Hasil Mixed kata : {hasil}")




