harga_barang= int(input("Masukan harga barang: ")) #total belanjaan anda
uang= int(input("Masukan jumlah uang anda: "))#jumlah uang anda
kembalian= uang - harga_barang  

if kembalian < 0: #logikannya tidak ada kembalian yang mines
    print("Maaf uang anda kurang")
else:  
    pecahan= [100000, 50000, 20000, 10000, 5000,2000,1000] #tuple untuk menyimpan data
    for i in pecahan: 
        lembaran= kembalian // i #floor division supaya hasil pembagiannya menghasilkan bilangan bulat, menghasilkan brp lembar nilai mta uang 100k dll 
        print(f"{lembaran} Jumlah uang bernilai Rp {i}") 
        kembalian -= lembaran * i
        