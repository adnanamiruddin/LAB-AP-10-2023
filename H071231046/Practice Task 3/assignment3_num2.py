uang_kembalian = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

harga_barang = int(input())
nilai_uang = int(input())

kembalian = nilai_uang - harga_barang

if kembalian < 0:
    print("Uang yang Anda masukkan kurang. Silahkan tambah uang anda")
else:
    for i in uang_kembalian:
        jumlah = kembalian//i
        print(f'{jumlah} uang sejumlah Rp.{i}')
        kembalian -= jumlah * i