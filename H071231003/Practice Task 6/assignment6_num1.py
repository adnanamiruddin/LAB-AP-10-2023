dictionary ={
"nama": "", "umur": 0, "alamat": ""
}
tanda = "="*50

print("Selamat datang Untuk memulai, silakan masukkan data Anda.")

dictionary["nama"] = input("Input Nama : ")

while True:
    dictionary["umur"] = int(input("Input Umur : "))
    if dictionary ["umur"] >= 0:
        break
    else:
        print("umur tidak bisa minus,masukan umur yang valid")
 
dictionary["alamat"] = input("Input Alamat : ")

while True:
    print(f"""
{tanda}
Selamat datang {dictionary["nama"]} Silakan pilih Opsi
{tanda}
1. Detail Anda
2. Ubah Nama
3. Ubah Umur
4. Ubah Alamat
5. Keluar
{tanda}""")
    opsi = int(input("Input Opsi : "))
    print (tanda)
    if opsi == 1:
        print(f"""
Data anda adalah
Nama : {dictionary['nama']}
Umur : {dictionary['umur']}
Alamat : {dictionary['alamat']}""")
    elif opsi == 2:
        dictionary["nama"] = input("Silahkan Input Nama Baru : ")
        print("Data Anda Sukses Diperbarui\n")
    elif opsi == 3:
        while True:
            dictionary["umur"] = int(input("Silahkan Input Umur Baru Anda : "))
            if dictionary["umur"] >= 0:
                break
            else:
                print("umur tidak bisa minus")
        print("Data Anda Sukses Diperbarui\n")
    elif opsi == 4:
        dictionary["alamat"] = input("Silahkan Input Alamat Baru Anda : ")
        print("Data Anda Sukses Diperbarui\n")
    elif opsi == 5:
        print(f"Selamat Tinggal {dictionary['nama']}")
        break
    else:
        print('Input tidak valid, masukan inputan yang ada')








    print("Pilih menu:
    * Detail Anda
    * Ubah Nama
    * Jumlah Data pada File
    * Simpan Data pada File
    * Buat Data Baru
    * Keluar
    
    Pilih menu: "