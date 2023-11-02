data_pengguna = {}    #menyimpan data pengguna 

if not data_pengguna:       #memeriksa apakah data pengguna msih kosong
    print("Selamat datang untuk memulai silahkan input data anda")
    nama = input("Input Nama : ")
    while True:
        umur = int(input("Input Umur : "))
        if umur > 0:
            break
        else:
            print("Inputan harus positif")
    alamat = input("Input Alamat : ")

    data_pengguna["nama"] = nama
    data_pengguna["umur"] = umur
    data_pengguna["alamat"] = alamat

def detail():     #utk mencetak data pengguna
    print("Data anda adalah")
    print("Nama: ",data_pengguna["nama"])
    print("Umur: ",data_pengguna["umur"])
    print("Alamat: ",data_pengguna["alamat"])
    
while True:   # menampilkan menu opsi kpd pengguna
    print("\n")
    print("="*50)
    print("Selamat datang", data_pengguna["nama"],"silahkan pilih opsi")
    print("="*50)
    print("1. Detail anda ")
    print("2. Ubah Nama")
    print("3. Ubah Umur")
    print("4. Ubah Alamat")
    print("5. Keluar")    #keluar dari program
    print("="*50)
    print("\n")
    input_opsi = int(input("Input Opsi: "))
    print("\n")
    match input_opsi :  #utk mengevaluasi pilihan user dan melakukan tindakan sesuai dgn opsi yg dipilih
        case 1:
            detail()    # utk menapilkan detail data user
        case 2:
            nama1 = input("Silahkan input nama baru: ")
            data_pengguna["nama"] = nama1
            print("Data anda sukses diperbarui")
        case 3:
            while True:
                umur1 = input("Silahkan input umur baru: ")
                data_pengguna["umur"] = int(umur1)                
                if data_pengguna["umur"] > 0:
                    break
                else:
                    print("Inputan harus positif")    
            print("Data anda sukses diperbarui")
                   
        case 4:
            alamat1 = input("Silahkan input alamat baru: ")
            data_pengguna["alamat"] = alamat1
            print("Data anda sukses diperbarui")
        case 5:
            print("="*50)
            print("Selamat Tinggal ", data_pengguna["nama"])
            break
        case _:
            print("Input yang anda masukkan salah")