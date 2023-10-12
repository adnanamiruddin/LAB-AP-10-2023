def singkatan(nama):
    a = len(nama)
    tengah = a//2
    singkat = nama[0]+ nama[tengah] + nama[-1]
    print(singkat)

singkatan(input ("Masukkan Kata: ") )