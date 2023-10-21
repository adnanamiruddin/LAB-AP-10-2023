array1 = list(map(int, input("Input array ke-1: ").split()))
array2 = list(map(int, input("Input array ke-2: ").split()))

a = set(array1)
b = set(array2)

jumlahDuplikat = len(a & b)
angkaDuplikat = tuple(a & b)

if jumlahDuplikat > 1 :
    print(f"Terdapat {jumlahDuplikat} buah duplikat yaitu {angkaDuplikat}")
elif jumlahDuplikat==1:
    print(f"Terdapat {jumlahDuplikat} buah duplikat yaitu ({list(angkaDuplikat)[0]})")    
else:
    print("Tidak ada duplikasi ditemukan.")