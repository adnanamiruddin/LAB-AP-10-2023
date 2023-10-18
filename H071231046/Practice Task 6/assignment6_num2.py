array1 = list(map(int, input("Input array ke-1: ").split()))
array2 = list(map(int, input("Input array ke-2: ").split()))
# array1 = set(array1)
# array2 = set(array2)
array = set(array1) & set(array2)

if len(array) == 1:
    print(f"Terdapat {len(array)} buah duplikat yaitu ({array.pop()})")
elif len(array) > 1:
    array = tuple(array)
    print(f"Terdapat {len(array)} buah duplikat yaitu {array}")
else:
    print("Tidak ada duplikasi ditemukan")