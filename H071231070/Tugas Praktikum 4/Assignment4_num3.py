def terbesar(*angka): #diberikan fungsi terbesar dengan pararameter kata
    terbesar = angka[0] #dibuat variabel baru yaitu terbesar dengan kata indeks 0
    for i in angka: #disini perulangan for i in kata
        if terbesar < i: #diberi suatu kondisi dimana jika terbesar lebih kecil dari i maka terbesar adalah i
            terbesar = i  
    return terbesar #lalu return nilai terbesar


# angka = [1, 3, 54, 6, 2, 3, 56, 6, 3, 6, 8, 90, 32, 5] #ini adalah nilai dari list kata
# print(terbesar(angka))

print(terbesar(1, 3, 54, 6, 2, 3, 56, 6, 3, 6, 8, 90, 32, 5, 99999))
 #"*"menyimpan berapapun angka dalam bentuk list