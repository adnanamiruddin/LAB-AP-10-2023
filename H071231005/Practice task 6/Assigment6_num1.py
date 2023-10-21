dictionary = {"nama": "", "umur": "", "alamat": ""}

print("Selamat datang! Untuk memulai, silakan masukkan data Anda.")
dictionary["nama"] = input("Input Nama : ")
dictionary["umur"] = int(input("Input Umur : "))
if dictionary["umur"] < 0:
    print("Input umur tidak boleh negatif")
    exit()
dictionary["alamat"] = input("Input Alamat : ")
Panjang= len(f'Selamat datang {dictionary["nama"]} Silakan pilih Opsi')
Panjang_Tanda = Panjang*"="
#Panjang_tanda = "="*55

while True:
    print(f"""
{Panjang_Tanda}
Selamat datang {dictionary["nama"]} Silakan pilih Opsi
{Panjang_Tanda}
1. Detail Anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar
{Panjang_Tanda}""")
    opsi = int(input("Input Opsi : "))
    print (Panjang_Tanda)
    if opsi == 1:
        print(f"""
Data anda adalah
Nama : {dictionary['nama']}
Umur : {dictionary['umur']}
Alamat : {dictionary['alamat']}""")
    elif opsi == 2:
        dictionary["nama"] = input("Silahkan Input Nama Baru : ")
        print("Data Anda Sukses Diperbarui!\n")
    elif opsi == 3:
        while True:
            dictionary["umur"] = int(input("Silahkan Input Umur Baru Anda : "))
            if dictionary["umur"] >= 0:
                break
            else:
                print("Input Umur Tidak Boleh Negatif")
        print("Data Anda Sukses Diperbarui\n")
    elif opsi == 4:
        dictionary["alamat"] = input("Silahkan Input Alamat Baru Anda : ")
        print("Data Anda Sukses Diperbarui\n")
    elif opsi == 5:
        print(f"Selamat Tinggal {dictionary['nama']}")
        break
    else:
        print('Input tidak valid')