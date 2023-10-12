word = input("Masukkan kata : ")
# Menghapus semua spasi dalam string
word2 = word.replace(" ", "")
word3 = len(word2)//2 # Menentukan indeks tengah dari string
new_word = ""

new_word += word2[0] + word2[word3]  + word2[-1]

print(new_word)

