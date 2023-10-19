a1 = list(map(int, (input("Masukkan array ke-1 : ").split()))) #memetakan semua inputan menjadi integer dalam bentuk list
a2 = list(map(int, (input("Masukkan array ke-2 : ").split()))) #spilt itu memisahkan inputan 
a1 = set(a1) #di gunakan set karena akan menggunakan operasi intersection 
a2 = set(a2)
x = a1.intersection(a2) #dibaris ini akan mencari bagian yang sama antara a1 dan a2
xtuple = tuple(x) #x itu diubah dari set menjadi tupple karena di outputnya berbentuk tupple
p = len(xtuple) #menghitung panjang tuple
if p > 0:
    print(f"Terdapat {p} buah duplikat yaitu {xtuple}")
else:
    print(f"Tidak ada duplikasi ditemukan.")  

    #array itu kumpulan data
    #intersection itu irisan