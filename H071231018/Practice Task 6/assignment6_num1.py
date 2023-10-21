print("Selamat datang untuk memulai silahkan input data anda")
nama = input ("Input nama: ").title()
while True:
    umur = int (input("Input umur: "))
    if umur > 0:
        break
    else:
        print("Umur tidak negatif")
alamat = input("Input alamat: ").title()
banyakTanda = len(f"Selamat datang {nama} silahkan pilih opsi")

while True:
    data = {
        "Nama": f"{nama}",
        "Umur": f"{umur}",
        "Alamat": f"{alamat}"
    }

    print("="*banyakTanda) 
    print(f"Selamat datang {nama} silahkan pilih opsi")
    print("="*banyakTanda)
    print("1. Detail anda")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")
    print("="*banyakTanda)

    opsi = int (input("Input opsi: "))

    match opsi:
        case 1 :
            print("\nData anda adalah")
            for k,v in data.items():
                    print(f"{k}: {v}")
        case 2 :
            nama_baru = input("\nSilakan input nama baru: ")
            nama = nama_baru
            print("\nData anda sukses diperbarui")
        case 3:
            while True:
                umur_baru = input("\nSilakan input umur baru: ")
                umur = int(umur_baru)
                if umur > 0:
                    print("\nData anda sukses diperbarui")
                    break
                else:
                    print("Umur tidak negatif")    
        case 4:
            alamat_baru = input("\nSilakan input alamat baru: ")
            alamat = alamat_baru
            print("\nData anda sukses diperbarui")
        case 5:
            print("="*banyakTanda)
            print(f"Selamat Tinggal {nama}")
            break