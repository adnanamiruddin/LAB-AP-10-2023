print("="*50)
print("Selamat datang untuk memulai silahkan input data anda")
print("="*50)

inputnama = input("Input nama: ")
inputumur = int(input("Input umur: "))
if inputumur < 0:
    print("Input umur tidak boleh negatif!")
    exit()
inputalamat = input("Input alamat: ")
    
data = {
    "nama" : inputnama,
    "umur" : inputumur,
    "alamat" : inputalamat,
}

while True:
    print("="*50)
    print(f"Selamat datang {data['nama']} silahkan pilih opsi")
    print("="*50)
    print("1. Detail anda\n2. Ubah Nama\n3. Ubah Umur\n4. Ubah Alamat\n5. Keluar")
    print("="*50)
    inputan = int(input("Input opsi : "))
    print("="*50)  
    match inputan:
        case 1:
            print(f"Data anda adalah\nNama : {data['nama']}\nUmur : {data['umur']}\nAlamat : {data['alamat']}")
        case 2:
            data["nama"] = input("Silakan Input nama baru : ")
            print("Data anda sukses di diperbarui")
        case 3:
            data["umur"] = int(input("Silahkan input umur baru : "))
            if data["umur"] < 0:
                    print("Input umur tidak boleh negatif!")
                    exit()
            else:
                print("Data anda sukses di diperbarui")    
        case 4:
            data["alamat"] = input("Silahkan input alamat baru : ")
            print("Data anda sukses di diperbarui")
        case 5:
            print(f"Selamat Tinggal {data['nama']}")
            break
        case _:
            print("Inputan diluar opsi")
            