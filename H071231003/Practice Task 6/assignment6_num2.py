angka1= input("Input array ke-1: ")
angka2= input("Input array ke-2: ")

a1= set(map(int, angka1.split())) # set menjalankan operasi himpunan matematika
a2= set(map(int, angka2.split()))

x = tuple (a1 & a2) #tdk bisa dijalankan tanpa menggunakan set, tuple agar outputnya dlm kurung
p = len(x)
if p > 1:
    print(f"Terdapat {p} buah duplikat yaitu {x}")
elif p == 1:
    print(f"Terdapat {p} buah duplikat yaitu ({x[0]})")
else:
    print(f"Tidak ada duplikasi ditemukan.")