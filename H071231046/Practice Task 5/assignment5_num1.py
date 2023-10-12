s1 = input("S1 = ")
s2 = input("S2 = ")
# untuk mengubah hasil reversed awalnya tipe data list 
# menjadi tipe data string 
s3 = "".join(reversed(s2)) 
new_word = ""

for i in range(max(len(s1),len(s2))):
    if i < len(s1):
        new_word += s1[i]
    if i < len(s3):
        new_word += s3[i]

print("Hasil mixed =", new_word)