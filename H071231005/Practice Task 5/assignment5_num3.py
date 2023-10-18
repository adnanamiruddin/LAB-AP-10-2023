def anagram (kata1, kata2):
    ganti1 = kata1.replace(" ", "").lower()
    ganti2 = kata2.replace(" ", "").lower()
    print(sorted(ganti1) == sorted(ganti2))

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
anagram(kata1,kata2)
