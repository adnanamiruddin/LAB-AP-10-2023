angka = input("Masukkan Beberapa Angka : ").split() #fungsi split() untuk memisahkan angka2 yang telah di input berdasarkan spasi dan mengubahnya menjadi list.
angka = list(map(int, angka)) #baris ini mengubah setiap bagian dalam list angka menjadi integer.fungsi map() untuk menerapkan fungsi int() ke setiap bagian dalam list
nol, genap, ganjil, habis5 = [], [], [], [] #baris ini menyatakan 3 list kosong:genap untuk menyimpan angka genap, ganjil untuk menyimpan angka ganjil dan habis5 untuk menyimpan angka yang habis di bagi 5
for i in angka:
    if i == 0:
        nol.append(i)
    if i % 2 == 0 and i != 0: 
        genap.append(i)
    if i % 2 != 0: 
        ganjil.append(i)
    if i % 5 == 0 and i != 0: 
        habis5.append(i)
print(f"\n0 : {nol}\nAngka Genap : {genap}\nAngka Ganjil : {ganjil}\nAngka yang habis dibagi 5 : {habis5}")