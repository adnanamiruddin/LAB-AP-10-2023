#Program Mengubah Sebuah String, dan diambil hanya string pertama, tengah, dan terakhirnya
kata = input("Masukkan Kata : ") #inputan berupa string
y = len(kata) #Variabel disini yaitu untuk menentukan panjang dari kata yang kita input

x = kata[0] + kata[y//2] + kata[-1]
    #kata[0] berarti mengambil indeks pertamanya dari variabel kata, misal "James", yang diambil "J"
    #kata[y//2] berarti mengambil indeks ditengah dari variabel kata, misal "James", yang diambil yaitu "m"
    #kata[-1] berarti mengambil indeks terakhir dari variabel kata, misal "James", yang diambil yaitu "s"
    #maksud dari kata[-1] itu diambil 1 namun dari kanan

    
print(x) 





