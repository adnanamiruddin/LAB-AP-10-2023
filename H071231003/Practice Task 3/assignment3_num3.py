while True:
    try:
        M = float(input("Masukan derajat: ")) 

        total_detik = int((M / 360) * 24 * 3600) #menghitung berapa bagian derajat M dari 360 #utk mengetahui jumlah total detik

        jam = (total_detik // 3600 + 6) % 24 #menghitung brp jam lengkap dari total detik, +6 krn pada soal diminta agar 0 derajat == jam 6 pagi, % 24 agar memastikan jamnya sesuai dgn format 24 jam
        menit = (total_detik % 3600) // 60 #Menghitung sisa dtk setelah membagi dgn jumlah dtk dalam 1 jam, utk mendapatkan jumlah menit
        detik = total_detik % 60 #Menghitung dtk dgn mengambil sisa dtk setelah membagi dengan 60 

        if 6 <= jam < 12:
         waktu = "Selamat Pagi"
        elif 12 <= jam < 18:
         waktu = "Selamat Siang"
        elif 18 <= jam < 24:
         waktu = "Selamat Sore"
        else:
         waktu = "Selamat Malam"
        print(waktu)
        print(f"{jam:02d}:{menit:02d}:{detik:02d}")
    except:
        print ("end of file") 
        break


   