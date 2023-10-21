angka = list(map(int, input("Masukkan beberapa angka: ").split()))

angkaNol = []
angkaGanjil = []
angkaGenap = []
kelipatan5 = []

def kelompok():
    for i in angka:
        if i == 0:
            angkaNol.append(i)
        if i % 2 == 1 and i != 0 :
            angkaGanjil.append(i)
        if i % 2 == 0 and i != 0:
            angkaGenap.append(i)
        if i % 5 == 0 and i != 0:
            kelipatan5.append(i)
            print("")
kelompok()
print(f"Angka Nol: {angkaNol}\nAngka Genap: {angkaGenap}\nAngka Ganjil: {angkaGanjil}\nAngka yang habis dibagi 5: {kelipatan5}")            