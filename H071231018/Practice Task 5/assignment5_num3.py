def anagram(word1, word2):
    return sorted(word1.replace(" ", "").lower()) == sorted(word2.replace(" ", "").lower())

word1 = input("Masukkan Kata Pertama: ")
word2 = input("Masukkan Kata Kedua: ")

if anagram(word1, word2):
    print(True)
else:
    print(False)
