harga_barang = int(input("Masukkan harga_barang Barang : "))
uang = int(input("Masukkan Uang Anda : "))

kembalian = uang - harga_barang
if kembalian < 0 :
    print ('Uang anda Kurang')
else :
    pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]
    for pecahan in pecahan_uang:
        jumlah_uang = kembalian // pecahan
        print(f"{jumlah_uang} uang sejumlah Rp.{pecahan}")
        kembalian %= pecahan
