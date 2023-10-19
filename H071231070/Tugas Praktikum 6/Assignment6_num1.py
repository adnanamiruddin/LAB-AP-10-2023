def InputAwal():
    print("Selamat Datang untuk memulai silahkan input data anda") 
    dict["nama"] = (input("Input nama : ")).title()

    while True:
          dict["umur"] = int(input("Input umur : "))
          if dict["umur"] >=0:
              break
          else:
              print("umur tidak ada yang negatif,masukkan umur yang valid")
              
    dict["alamat"] = input("Input alamat : ")

def opsi():
    while True: #memakai while karena perulangan
        print(f"{'=' * 51}\nSelamat datang {dict['nama']}! Silahkan Pilih Opsi\n{'=' * 51}")
        print(f"1. Detail Anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar\n{'=' * 51}")
        pilihan = int(input("Input Opsi : "))
        match pilihan:
            case 1:
                print(f"{'=' * 51}\nData anda adalah\nNama: {dict['nama']}\nUmur: {dict['umur']}\nAlamat: {dict['alamat']}")
            case 2:
                dict["nama"] = (input("Silahkan Input Nama Baru: ")).title()
                print("Data anda sukses diperbarui!")
            case 3:
                while True:
                    dict["umur"] = int(input("Silahkan Input Umur Baru: "))
                    if dict["umur"] >=0:
                        break
                    else:
                        print("umur tidak ada yang negatif,masukkan umur yang valid")
                print("Data anda sukses diperbarui!")
            case 4:
                dict["alamat"] = input("Silahkan Input alamat Baru: ")
                print("Data anda sukses diperbarui!")
            case 5:
                print(f"{'=' * 51}\nSelamat Tinggal {dict['nama']}")
                break
            case _:
                break

dict = {"nama":"", "umur":"", "alamat":""} #di soal disuruh membuat dictionary kosong
InputAwal() #mengakses fungsi input awal
opsi() #mengakses fungsi opsi