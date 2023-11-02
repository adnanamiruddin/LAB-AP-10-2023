input_str = input("Masukkan beberapa angka: ")
angka = list(map(int, input_str.split()))

angka_nol= []
ganjil = []
genap = []
habis_dibagi_5 = []

for number in angka:
    if number == 0:
        angka_nol.append(number)
    if number % 2 == 1:  # ganjil
        ganjil.append(number)
    if number % 2 == 0 and number != 0:  # genap
        genap.append(number)
    if number % 5 == 0 and number != 0:  #habis dibagi 5
        habis_dibagi_5.append(number)

print("Angka nol:", angka_nol)
print("Angka Genap:", genap)
print("Angka Ganjil:", ganjil)
print("Angka yang Habis Dibagi 5:", habis_dibagi_5)
