a1 = list(map(int,(input("Masukkan array ke-1: ").split())))
a2 = list(map(int,(input("Masukkan array ke-2: ").split())))

a1 = set(a1) # menjalankan operasi himpunan matematika
a2 = set(a2)

x = (a1&a2) # bisa menggunakan fungsi intersection  # Tidak bisa di jalankan tanpa menggunakan set
xtuple = tuple(x)
p = len(xtuple)
if p > 1:
    print(f"Terdapat {p} buah duplikat yaitu {xtuple}")
elif p == 1:
    print(f"Terdapat {p} buah duplikat yaitu ({xtuple[0]})")
else:
    print(f"Tidak ada duplikasi ditemukan.")