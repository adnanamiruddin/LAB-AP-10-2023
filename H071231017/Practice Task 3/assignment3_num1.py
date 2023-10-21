try:
    x = int(input("Masukkan Input = "))

    angka0 = 0
    angka1 = 1
    jumlah = 0

    i = 0

    while i < x:
        i += 1
        angka0 = angka1
        angka1 = jumlah
        print(jumlah, end=" ")
        jumlah = angka0 + angka1

except ValueError:
    print("Masukkan harus berupa angka")