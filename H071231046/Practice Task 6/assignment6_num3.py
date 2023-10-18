number = list(map(int, input("Masukkan beberapa angka: ").split()))

nol = [i for i in number if i==0]
genap  = [i for i in number if i % 2 ==0 and i != 0]
ganjil = [i for i in number if i % 2 != 0]
bagi5  = [i for i in number if i % 5 == 0 and i != 0]

print(f"Angka nol: {nol}")
print(f"Angka Genap: {genap}")
print(f"Angka Ganjil: {ganjil}")
print(f"Angka yang habis dibagi 5: {bagi5}")