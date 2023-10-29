try:
    arr1 = [int(i) for i in input('\nMasukkan angka untuk array ke-1 (pisahkan dengan spasi): ').split(' ')]
    arr2 = [int(i) for i in input('Masukkan angka untuk array ke-2 (pisahkan dengan spasi): ').split(' ')]

    arrDuplikat = set()   #utk menyimpan angka2 duplikat

    for i in arr1:   #iterasi melalui angka2 dalam array ke
        if i in arr2 and i not in arrDuplikat:  #Jika angka tersebut ada di arr2 dan belum ada di arrDuplikat, maka angka tersebut ditambahkan ke dalam arrDuplikat
            arrDuplikat.add(i)
    if len(arrDuplikat) == 0:
        print('\nTidak ditemukan duplikasi.\n')
    else:
        print(f"\nTerdapat {len(arrDuplikat)} buah duplikat, yaitu {tuple(arrDuplikat)}\n")
except ValueError:
    print('\nInputan invalid.')