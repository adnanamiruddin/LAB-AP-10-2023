import os
import random
from datetime import datetime 

print("="*50)
print("SELAMAT DATANG".center(50))
print("="*50)
while True:
    name = input("Masukkan nama kasir \t = ")
    if not name.strip(): #Saat pengguna menginput hanya spasi
        print("="*50)
        print("Input tidak boleh hanya spasi!")
        print("="*50)
        continue
    else:
        break

while True:
    print("="*50)
    print("Pilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar ")
    print("="*50)
    inputan = input("Masukkan opsi pilihan \t = ")
    print("="*50)
    match inputan:
        case '1':
            nama_produk = []
            harga_produk = []
            jumlah_produk = []
            while True:
                try:
                    input_nama_produk = input("Masukkan nama produk \t = ")
                    if not input_nama_produk.strip():
                        print("Input tidak boleh hanya spasi!")
                        continue
                    nama_produk.append(input_nama_produk)
                    while True:
                        try:
                            input_harga_produk = int(input("Masukkan harga produk \t = "))
                            if input_harga_produk < 0 :
                                print("Input harga tidak boleh negatif!")
                            else:
                                break
                        except ValueError: #Jika pengguna memasukkan huruf bukan angka
                            print("Input harus angka!")
                    harga_produk.append(input_harga_produk)
                    while True:
                        try:
                            input_jumlah_produk = int(input("Masukkan jumlah produk \t = "))
                            if input_jumlah_produk < 0 :
                                print("Input jumlah produk tidak boleh negatif!")
                            else:
                                break
                        except ValueError:
                            print("Jumlah produk harus berupa angka!")
                    jumlah_produk.append(input_jumlah_produk)
                except KeyboardInterrupt: #Mengatasi jika pengguna ingin skip ke literasi berikutnya
                    print("Tolong diisi!")
                    continue
                
            
                print("="*50)
                while True:
                    choose = input("Tambah produk? (y/t) \t  = ")
                    if choose == 'y' or choose == 't':
                        break
                    else:
                        print("Diluar opsi! Masukkan (y/t)")
                        continue
                if choose == 'y':
                    print ("="*50)
                    continue
                else:
                    break
            print("="*50)

            Total = []
            for i in range(len(harga_produk)):
                Total.append(harga_produk[i]*jumlah_produk[i]) 

            All = sum(Total)

            data = {
                'NAMA' : nama_produk,
                'HARGA' : harga_produk,
                'JUMLAH' : jumlah_produk,
                'TOTAL' : Total
            }

            widths = {
                'NAMA' : 20,
                'HARGA' : 12,
                'JUMLAH' : 8,
                'TOTAL' : 14
            }

            inisial_nama = (name[0] + name[len(name)//2] + name[-1]).upper() #Fungsinya dimasukkan ke dalam ID
            angka_acak = str(random.randint(100,999)).zfill(3)
            ID = inisial_nama + datetime.now().strftime('%y%m%d%H%M') + angka_acak #datetime.now untuk mengambil waktu sekarang sesuai waktu di komputer

            folder = "Invoices"
            if not os.path.exists(folder): #kalau foldernya tidak ada maka akan membuat folder baru
                os.mkdir(folder) #perandaian ini tidak dieksekusi kalau foldernya telah ada

            path = folder + "/" + ID + ".txt"

            with open(path, 'w') as file:
                file.write(f"\n {' '*25} TOKO CHELSEA\n")
                file.write("\n")    
                file.write(f"="*70)
                file.write(f"\nNama Kasir {' '*10}: {name}")
                file.write(f"\nWaktu Transaksi {' '*4} : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                file.write(f"="*70)
                file.write("\n")
                file.write(f"\n {' '*25} Daftar Produk\n")
                file.write(f"\n \t===============================================================\n")
                file.write('\t| ' + ' |'.join([f"{key.center(widths[key])}" for key in data.keys()]) + '|\n')
                file.write("\t===============================================================\n")
                
                for nama, harga, jumlah, total in zip(data['NAMA'], data['HARGA'], data['JUMLAH'], data['TOTAL']):
                    if len(nama) > 18:
                        nama = nama[:15]+'...'
                    file.write(f"\t| {nama.ljust(20)} |")
                    file.write(f" {('Rp.'+str(harga)).rjust(11)} |") #Diberikan string agar dapat menyambung dengan Rp.
                    file.write(f" {str(jumlah).center(7)} |") #agar dapat diatur posisinya
                    file.write(f" {('Rp.'+str(total)).rjust(12)} |\n")
                file.write("\t===============================================================\n")
                file.write(f"\t| {('Total'.ljust(44))} | {('Rp.'+str(All)).rjust(12)} |\n")
                file.write("\t===============================================================\n")
                file.write(F"\n{'='*70}\n{'TERIMA KASIH TELAH BERBELANJA'.center(70)}\n{'='*70}\n")
            print("TRANSAKSI BERHASIL".center(50))

            History = "trx_history.txt"

            if not os.path.exists(History) :
                with open(History,"w") as file2:
                    file2.write(f"{'='*70}\n| {'DAFTAR TRANSAKSI'.center(66)} |\n{'='*70} \n")
                    file2.write(f"| {'Waktu'.center(19)} | {'ID Transaksi'.center(20)} | {'Nominal Transaksi'.center(21)} |\n{'='*70}\n")

            with open(History,"a") as file2 :
                file2.write(f"| {datetime.now().strftime('%d/%m/%Y %H:%M:%S').center(19)} | {ID.ljust(20)} | {('Rp.'+str(All)).rjust(21)} |\n{'='*70}\n")

        case '2':
            id_transaksi = input("Masukkan ID Transaksi : ")
            print("="*50)

            folder = "Invoices"
            file_read = folder + "/" + id_transaksi + ".txt"

            if not os.path.exists(file_read) :
                print(f"File ID {ID} tidak ada")
                print("="*75)
            else :
                read = open(file_read,"r")
                print(read.read())
            y = input("Tekan Apapun untuk Kembali : ")
        
        case '3':
            print(f"Selamat Tinggal {name}".center(50))
            print("="*50)
            break

        case _ :
            print("Inputan diluar opsi!")
            x = input("Tekan Enter untuk melanjutkan : ")
            continue
