kata1 = input('Masukan kata1: ')
kata2 = input ("Masukan kata2: ")
kata3 = ""

minimal = min(kata1,kata2)

for i in range(len(minimal)):
    balik ="".join(reversed(kata2)) #bisa menggunakan balik = kata2 [::-1]
    kata3 += kata1[i] + balik[i]

print(kata3)