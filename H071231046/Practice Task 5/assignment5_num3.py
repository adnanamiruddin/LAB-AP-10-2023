def anagram(word1,word2):
    
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ","").lower()

    # Memeriksa apakah jumlah huruf sama
    if len(word1) != len(word2):
        return False
    # jika False maka program berhenti dan tidak dijalankan 
    # kode yang dibawah
    # sorted() digunakan untuk mengurutkan elemen dalam string/list
    word_sort1 = "".join(sorted(word1))
    word_sort2 = "".join(sorted(word2))
    # print(word_sort1, word_sort2)

    # Membandingkan kedua kata yang sudah diurutkan
    if word_sort1 == word_sort2:
        return True
    else:
        return False

word1 = input("Masukkan kata pertama : ")
word2 = input("Masukkan kata kedua : ")

print(anagram(word1, word2))
