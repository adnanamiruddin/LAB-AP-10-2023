import os
from datetime import datetime
import random

def template():
    os.chdir("invoices")
    invoice_name = format_invoices + ".txt"
    os.path.join("invoices", invoice_name)
    with open(str(invoice_name), 'w') as file:
        file.write("\n" + "_" * 60 + "\n" + "\n")
        file.write("TOKO SisFo".center(60) + "\n")

        file.write("\n" + "=" * 60 + "\n")
        file.write("Nama Kasir".ljust(25) + ": " + cashier + "\n")
        file.write("Waktu Transaksi".ljust(25) + ": " + str(sekarang.strftime('%d/%m/%y')) + str(sekarang.strftime('  %H:%M\n')))
        file.write("=" * 60 + "\n")

        file.write("\n" + "Daftar Produk".center(60) + "\n")

        file.write("\n" + ("=" * 52).center(60))
        file.write("\n" + "|".rjust(5) + "{:^15}|{:^13}|{:^8}|{:^11}|".format("Nama", "Harga", "Jumlah", "Total"))
        file.write("\n" + ("=" * 52).center(60))
            
        for i in range(len(data["Nama"])):
            data["Nama"][i] = (data["Nama"][i][:12] + '...') if len(data["Nama"][i]) > 12 else data["Nama"][i]
            data["Harga"][i] = ("Rp" + str(data["Harga"][i])[:7] + '...') if len(str(data["Harga"][i])) > 7 else "Rp" + str(data["Harga"][i])
            data["Total"][i] = ("Rp" + str(data["Total"][i])[:8] + '...') if len(str(data["Total"][i])) > 8 else "Rp" + str(data["Total"][i])
            file.write("\n" + "|".rjust(5) + "{:<15}|{:>13}|{:^8}|{:>11}|".format(data["Nama"][i], data["Harga"][i], str(data["Jumlah"][i]), data["Total"][i]))

        file.write("\n" + ("=" * 52).center(60))
        file.write("\n" + "|".rjust(5) + "{:^15}|{:^23}{:>11}|".format("TOTAL", " ", "Rp" + str(total_price)))
        file.write("\n" + ("=" * 52).center(60) + "\n")

        file.write("\n" + ("=" * 60))
        file.write("\n" + "TERIMA KASIH, SELAMAT DATANG KEMBALI".center(60))
        file.write("\n" + ("=" * 60))
        file.write("\n" + "\n" + "_" * 60 + "\n" + "\n")

# Mendapatkan waktu saat ini
sekarang = datetime.now()

print("=" * 60, "\n" + "SELAMAT DATANG".center(60), "\n" + "=" * 60)
while True:
    cashier = input("Masukkan nama kasir".ljust(25) + ": ")
    if not (cashier.isalpha() or " " in cashier):
        print("Input tidak valid!!!")
        print("=" * 60)
        continue
    else:
        break
data = {'Nama': [],
        'Harga': [],
        'Jumlah': [],
        'Total': []}

real_directory = os.getcwd()
while True:
    print("=" * 60)
    print("Pilih opsi: ", "\n1. Transaksi Baru", "\n2. Cari Transaksi", "\n3. Keluar", "\n" + "=" * 60)
    try:
        option = int(input("Masukkan opsi pilihan".ljust(25) + ": "))
        if option not in range(1,4):
            print("Opsi tidak valid!!!")
            continue
        else:
            if option == 1:
                for key in data:
                    data[key] = []
                while True:
                    print("=" * 60)
                    try:
                        product_name = input("Masukkan nama produk".ljust(25) + ": ")
                        if not (product_name.isalpha() or " " in product_name):
                            raise ValueError
                        price = int(input("Masukkan harga produk".ljust(25) + ": "))
                        amount = int(input("Masukkan jumlah produk".ljust(25) + ": "))

                        total = price * amount
                        data["Nama"].append(product_name)
                        data["Harga"].append(price)
                        data["Jumlah"].append(str(amount))
                        data["Total"].append(total)
                        total_price = sum(data["Total"])

                        trx_history = {"waktu" : [],
                                    "id" : [],
                                    "nominal" : []}
                        
                        print("=" * 60)
                        add = input("Tambah produk? (y/t)".ljust(25) + ": ")
                        if not (add == "y" or add == "t"):
                            raise ValueError
                    except ValueError:
                        print("Input tidak valid!!!")
                        continue
                    if add == "y":
                        continue
                    else:
                        angka_acak = random.randint(100, 999)
                        print("=" * 60, "\n" + "TRANSAKSI BERHASIL".center(60))
                        os.chdir(real_directory)
                        format_invoices = cashier[0].upper() + cashier[len(cashier)//2].upper() + cashier[-1].upper() + str(sekarang.strftime("%y")) + str(sekarang.strftime("%m")) + str(sekarang.strftime("%d")) + str(sekarang.strftime('%H%M')) + str(angka_acak)
                        if not os.path.exists("invoices"):
                            invoices = os.path.join(os.getcwd(), "invoices")
                            os.mkdir(invoices)
                            template()
                        else:
                            template()
                            
                        os.chdir(real_directory)    
                        os.path.join(real_directory, "trx_history.txt")
                        trx_history["waktu"].append(str(sekarang.strftime('%d/%m/%y')) + str(sekarang.strftime('  %H:%M\n')))
                        trx_history["id"].append(format_invoices)
                        trx_history["nominal"].append(total_price)

                        for i in range(len(trx_history["waktu"])):
                            waktu = trx_history["waktu"][i]
                            id_transaksi = trx_history["id"][i]
                            nominal_transaksi = str(trx_history["nominal"][i])
                            data_row = "\n|{:^20}|{:^28}|{:^28}|".format(waktu.rstrip("\n"), id_transaksi, "Rp" + nominal_transaksi)
                            
                        if not os.path.exists("trx_history.txt"):
                            with open("trx_history.txt", "w") as file:
                                file.write("=" * 80)
                                file.write("\n" + "|{:^78}|".format("RIWAYAT TRANSAKSI"))
                                file.write("\n" + "=" * 80)
                                file.write("\n" + "|{:^20}|{:^28}|{:^28}|".format("Waktu", "ID Transaksi", "Nominal Transaksi") +"\n" + ("=" * 80))
                                file.write(data_row)
                                file.write("\n" + "=" * 80)
                        else:
                            with open("trx_history.txt", "a") as file:
                                file.write(data_row)
                                file.write("\n" + "=" * 80)
                            break
                    break                    
                continue
            elif option == 2:
                os.chdir(real_directory)
                os.chdir("invoices")
                print("=" * 60)
                transaction_id = input("Masukkan id transaksi".ljust(25) + ": ")
                if os.path.exists(transaction_id + ".txt"):
                    with open(transaction_id + ".txt", "r") as file:
                        file = file.read()
                        print(file)
                else:
                    print("File not found")
                continue
            elif option == 3:
                print("=" * 60, "\n" + "SAMPAI JUMPA".center(60), "\n" + "=" * 60)
                break
    except ValueError:
        print("Opsi tidak valid!!!")  
        continue      
    break