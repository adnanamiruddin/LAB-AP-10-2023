def palindrom(kata): #Palindrom adalah suatu kalimat yang jika dibaca dari belakang itu sama saja, misalkan Radar, Apa, Malam
    if kata.lower() == kata[::-1].lower(): #lower itu kita membuat semua huruf menjadi huruf kecil semua, disini di tes apakah kata yang biasa sama dengan kata yang sudah dibalik
        print("Palindrom") #kata asli sama dengan kata yang sdh di balik
    else:
        print("Bukan Palindrom") #kalau tidak sama itu bukan palindrom

palindrom("12321")

#[::-1] itu adalah sebuah rumus dimana membalik semua huruf, misalnya Mobil jadi liboM
