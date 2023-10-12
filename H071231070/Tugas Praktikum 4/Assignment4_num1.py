def geser_huruf(n): #Fungsi geser huruf ini menggeser huruf pertama atau karakter pertama ke posisi yang paling terakhir
    for i in range(len(n)): #perulangan for, berulang sebanyak range len(n), len adalah fungsi dimana menentukan banyak karakter dalam variabel tersebut, misalkan len(n), dengan n = "Mobil" maka len(n) = 5
        n = n[1:]+ n[0]     #n yang baru = n[1:] maksudnya adalah diambil karakter mulai dari karakter 1 sampai ke terakhir, lalu ditambah n[0], contohnya : Mobil =  Obil + M
        print(n, end=" | ") #lalu print n yang baru yaitu obilM dan end dengan |
try:
    geser_huruf(input()) #inputannya cuma bisa berupa string, jika memasukkan angka didalam ini maka akan ke except
except TypeError:
    print("Terjadi error, N harus bertipe data string")

#digunakan perulangan for i in range(len(n)) agar huruf atau karakter dalam string dihitung satu persatu