harga_barang = int (input())
uang = int (input())
kembalian = uang - harga_barang
if kembalian < 0 :
    print("Uangnya kurang")
else:
    pecahan = (100000, 50000, 20000, 10000, 5000, 2000, 1000)
    for i in pecahan : 
        banyak_lembar = kembalian // i
        kembalian -= banyak_lembar * i
        print (f"{banyak_lembar} Jumlah uang bernilai Rp. {i}")