#Program Menentukan Apakah dari Dua Buah Kata Apakah termasuk anagram
#Anagram adalah salah satu jenis permainan kata di mana huruf-huruf dalam kata atau frasa awal diacak untuk membentuk kata atau frasa baru.
#Namun anagram tanpa menambah huruf baru.

#Logika dari anagram itu
kata1 = input("Masukkan Inputan Pertama : ") #Inputan Kata Pertama
kata2 = input("Masukkan Inputan Kedua : ") #Inputan Kata Kedua
kata1 = kata1.replace(" ", "").lower()#replace untuk menghilangkan spasi
kata2 = kata2.replace(" ", "").lower() 

kata1_sorted = "".join(sorted(kata1))
kata2_sorted = "".join(sorted(kata2))

if len(kata1) == len(kata2):
    if kata1_sorted == kata2_sorted:
        print("True")
    else:
        print("False")
else:
    print("False")

    #suatu kalimat bisa membuat kalimat baru dari huruf2 kalimat itu

    #sorted(kata1) = akan mengurutkan karakter dalam kata1
    #"".join = digunakan untuk menggabungkan kembali karakter-karakter yang sudah di urutkan menjadi satu string tanpa ada pemisah


    