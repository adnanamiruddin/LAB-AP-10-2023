s1 = input("s1: ")
s2 = input("s2: ")[::-1]
hasil = ""

if len(s1) >= len(s2):
     lenMax = len(s1)
else:
     lenMax = len(s2)

for i in range(lenMax):
    if i < len(s1):
        hasil += s1[i]
    if i < len(s2):
        hasil += s2[i]
        
print(f"Hasil mixed: {hasil}")

# s1 = input("s1: ")
# s2 = input("s2: ")
# hasil = ""

# minim=min((s1),(s2))

# for i in range(len(minim)):
#     balik="".join(reversed(s2))
#     hasil += s1[i] + balik[i]

# print(hasil)
