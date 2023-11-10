import os
import datetime
import random

def awal_trx_history(): #trx_history beda dengan id_transaksi, trx history itu diluar folder
    '''MEMBUAT JUDUL ATAU KEPALA DARI HISTORI TRANSAKSI''' 
    with open(trx_history, mode="a") as history: #membuka file trx_history dengan mode a, disini bisa menggunakan mode w karena cuma bagian judulnya yang ditulis
        history.write(f"{'='*70}\n|{'RIWAYAT TRANSAKSI'.center(68)}|\n{'='*70}\n") #Center 68 dikarenakan huruf | dihitung sebagai 1 otomatis dikurangi menjadi 70-2 (2 kali | muncul)
        history.write(f"|{'Waktu'.center(16)}|{'ID Transaksi'.center(25)}|{'Nominal Transaksi'.center(25)}|\n{'='*70}\n")  # 25+25+16 ditambah dengan | berjumlah 4 otomatis = 66 + 4 = 70
def isi_trx_history(): #isis trx_history otomatis dipanggil berkali-kali setiap kita membuat transaksi baru
    '''MEMBUAT ISI ATAU BAGIAN DARI HISTORI TRANSAKSI'''
    global total_keseluruhan #Global : Berguna untuk dapat mengambil variabel yang dari luar, dan dipanggil kedalam tanpa menjadikannya parameter
    waktu_struk = datetime.datetime.now() #Mengambil waktu yang saat ini
    total_keseluruhan = "Rp" + str(total_keseluruhan) # membuat total keseluruhan yang awalnya integer jadi string lalu ditambah didepannya Rp agar jadi seperti misalnya "Rp12000"
    with open(trx_history, mode="a") as isi: #disini wajib menggunakan mode a atau append karena ingin menambah history atau riwayat transaksinya
        isi.write(f"|{waktu_struk.strftime('%y/%m/%d %H:%M').center(16)}|{id_transaksi.ljust(25)}|{str(total_keseluruhan).rjust(25)}|\n{'='*70}\n")
        #Penggunaan ljust : left just (hanya kiri) berarti dia rapat ke kiri
        #Penggunaan rjust : right just (hanya kanan) berarti dia rapat ke kanan
        #Penggunaan center :  tengah berarti dia di rapatkan ke tengah
        #penggunaan ljust ataupun sejenisnya harus menggunakan parameter () yang isinya adalah jumlah spasi, misal diantara 70 karakter saya mau "a" berada ditengah-tengahnya, otomatis "a".center(70)
def opsi(): #Hanya print opsi saja
    '''OPSI'''
    print(f"{'='*70}\nPilih opsi:\n1. Transaksi baru\n2. Cari transaksi\n3. Keluar\n{'='*70}")
    
def awal_struk(FileStruk, NamaKasir, tampung): #Disini namanya awal_struk tetapi isinya sudah keseluruhan struk dari awal sampai akhir
    global total_keseluruhan, kasir #fungsi global adalah mengambil atau memanggil variabel diluar fungsi def ke dalam tanpa dimasukkan ke parameter
    kasir = kasir.upper() #Membuat nama kasir jadi huruf besar semua, tidak memengaruhi nama kasir yang ada diluar fungsi, hanya memengaruhi didalam, 
                        #misal nama kasir diluar variabel "Kezia" terus disini diubah jadi "KEZIA" tapi perubahan ini tidak dibawa keluar fungsi def
    waktu_kasir = datetime.datetime.now() #buat waktu kasir
    with open(FileStruk, mode="a") as struk: #menulis isi struk atau menulis isi dari txt
        struk.write(f"\n{f'TOKO {kasir}'.center(70)}\n\n")
        struk.write(f'{"="*70}\n')
        struk.write(f"Nama kasir      : {NamaKasir}\n")
        struk.write(f"Waktu transaksi : {waktu_kasir.strftime('%y/%m/%d %H:%M')}\n") #penggunaan / dan : disini untuk mempercantik saja, contohnya 23/12/09 17:45
        struk.write(f'{"="*70}\n')
        struk.write(f"\n{'Daftar Produk'.center(70)}\n\n")
        struk.write(f"{('='*60).center(70)}\n") #disini "=" dikali 60 dan di center 70 otomatis formatnya sama dengannya ditengah tengah
        struk.write(f"|{'Nama'.center(14)}|{'Harga'.center(14)}|{'Jumlah'.center(13)}|{'Total'.center(14)}|".center(70)) #dihitung 14+14+13+14 ditambah lagi dengan "|" berjumlah 5 otomatis 55+5 = 60, lalu dicenter 70
        struk.write(f"\n{('='*60).center(70)}\n")
        for barang in tampung: #ini mengapa ada perulangan dikarenakan, misal kita beli barang lebih dari 1, otomatis barang yang ada lebih dari satu juga
            total_perbarang = barang['Harga'] * barang['Jumlah'] #total per satu nama barang, harganya dikali jumlah barang yang kita ambil
            total_keseluruhan += total_perbarang #total keseluruhannya yang awalnya 0 jadi ditambah dengan total barang yang kita belanja, dia berulang sampai habis barang yang kita beli jadi otomatis ada dua variabel, ada total satu merk barang, dan total semua belanjaan kita
            if len(barang['Produk']) > 14: #maksudnya disini jika nama barang kita terlalu panjang jadinya disingkat agar lebih bagus saja diliat dan tidak membuat tabel yang kita buat jadi hancur
                barang['Produk'] = barang['Produk'][:11] + "..." #11 huruf dari nama barang ditambah dengan 3 titik
            struk.write(f"|{str(barang['Produk']).ljust(14)}|{('Rp' +str(barang['Harga'])).rjust(14)}|{str(barang['Jumlah']).center(13)}|{('Rp' + str(total_perbarang)).rjust(14)}|".center(70) + "\n")  #ditulis barang belanjaan kita setiap barang
            # struk.write("\n")
        struk.write(f"{('='*60).center(70)}\n")
        struk.write(f"|{'TOTAL'.center(43)}|{('Rp' + str(total_keseluruhan)).rjust(14)}|".center(70)) #disini total keseluruhan baru terpakai 
        struk.write(f"\n{('='*60).center(70)}\n\n")
        struk.write(f'{"="*70}\n')
        struk.write(f"{'TERIMA KASIH TELAH BERBELANJA'.center(70)}")
        struk.write(f'\n{"="*70}\n')
    return total_keseluruhan #Mengapa total_keseluruhan di return? karena nantinya total keseluruhan akan dipanggil di luar fungsi def, (total seluruh ini dipakai di trx_history juga)
waktu            = datetime.datetime.now()
trx_history      = "trx_history.txt" #nama file trx history yang diluar folder invoice
folder_invoice   = "Invoice" #nama folder yang isinya akan ada id_transaksi.txt
print(f'{"="*70}\n{"SELAMAT DATANG".center(70)}\n{"="*70}') #Program jika di run yang muncul di terminal adalah ini
kasir       = input("Masukkan nama kasir : ").title() #pakai title() agar huruf judul, misal nama yang kita input "kezia dewanti" akan otomatis jadi "Kezia Dewanti"
inisial = "" #inisial digunakan saat men-regenerate id_transaksi #tempat ditaruh sebuah huruf inisial nantinya
x       = kasir.split() # Variabel x hanya sebagai sementara saja jadi di split jika inputan kita "Kezia dewanti" jadi otomatis ["Kezia", "Dewanti"] mengapa "d"nya jadi huruf besar dikarenakan title() tadi hihi
for i in x: #i berulang sebanyak x, otomatis jika kita ambil sampel "Kezia dewanti" tadi otomatis berulang 2x sebagai "Kezia" dan "Dewanti"
    inisial += i[0] #disini inisial yaitu string kosong ditambahkan dengan i[0] jadi otomatis "Kezia" index-0 nya "K" begitu juga "Dewanti" index-0nya "D"
tampung_barang = [] #Disini tampung barang itu list dan akan diiisi dengan dictionary dan dipanggil saat pembuatan struk
while True:
    opsi()
    pilihan = int(input("Masukkan opsi pilihan  : ")) #pilihan 1, 2 dan 3
    match pilihan:
        case 1: #Case 1 itu adalah membuat struk (belanja barang)
            total_keseluruhan = 0   
            while True: #Berulang dikarenakan jika kita ingin beli lebih dari 1 barang
                print("="*70)
                one_item = {
                    'Produk' : input("Masukkan nama produk   : "),
                    'Harga' : int(input("Masukkan harga produk  : ")),
                    'Jumlah' : int(input("Masukkan jumlah produk : "))
                }
                tampung_barang.append(one_item) #menambahkan dictionary ini ke dalam list kosong tampung barang tadi
                print("="*70)
                lanjut = input("Tambah produk? (y/t)   : ")
                if lanjut == "y": 
                    continue #inputan kita y akan dia skip dan keawal lagi tepatnya ke line 70 lagi
                else: #inputan selain y bisa t atau x atau yang lain
                    id_transaksi    = f"{inisial}{waktu.strftime('%y%m%d%H%M')}{random.randint(100, 999)}" #Pembuatan ID Transaksi misal "KD2310281720999"
                    # "KD2310281720999"
                    # KD adalah Inisial, 23 adalah tahun, 10 adalah bulan, 28 adalah tanggal, 17 adalah jam(format 24-jam), 20 adalah menit, dan juga 999 adalah angka random dari range 100-999 diambil dari random.randint(100,999)
                    
                    print(f"{'='*70}\n{'TRANSAKSI BERHASIL'.center(70)}")
                    if not os.path.exists(folder_invoice): #jika folder_invoice "Invoice" belum ada
                        os.mkdir(folder_invoice) #Maka dia akan buat terlebih dahulu foldernya, kalau sudah ada yasudah saja dia skip
                    if not os.path.exists(trx_history): #jika file txt dari trx_history.txt belum ada maka dibuat dlu
                        awal_trx_history() #panggil fungsi dikarenakan didalam fungsi dia langsung buat file dan juga tulis kepala atau awlan dari trx_historynya
                    file_struk = os.path.join(folder_invoice, f"{id_transaksi}.txt") #disini mengakses file didalam folder, misal Invoice>1231231.txt dia akan akses txtnya, namun jika belum ada akan dibuat
                    total_keseluruhan += awal_struk(file_struk, kasir, tampung_barang) #total keseluruhan yang awalnya 0 tadi ditambah dengan fungsi def awal struk dikarenakan fungsi def awal struk me-return/menghasilkan total_keseluruhan
                    tampung_barang.clear() #disini menggunakan clear agar setiap kita selesai berbelanja barang yang sudah dibelanja atau diinput tadi dihapus, agar tidak ganda, 
                                           #Logikanya seperti sedang antri di minimarket, agar barang yang kita belanja beda lagi dengan barang yang dibelanja oleh orang didepan kita, sehingga apa yang dia belanja tidak masuk ditagihan kita, sehingga dihapus
                    isi_trx_history() #menulis isi trx_history
                    break #keluar dari perulangan opsi 1 (input barang) tapi tidak keluar di perulangan milih opsi
        case 2: #Mencari sebuah struk kita, dari ID transaksi
            print(f"{'='*70}")
            cari = input("Masukkan ID transaksi  : ")
            pathfolder = folder_invoice + "/" + cari + ".txt" #mengakses sebuah file txt di dalam folder "Invoice"
            with open(pathfolder, mode="r") as cari: #dia buka sebagai mode "r" saja karena kita tidak ingin mengubah/menulis hanya ingin dibaca saja
                print(cari.read()) #menggunakan print agar muncul di terminal
                #kalau kita cari ID transaksi yang tidak ada otomatis akan error, (Tidak saya buatkan kondisi jika file txtnya tidak ada)
        case 3: #keluar
            print(f"{'='*70}\n{'SAMPAI JUMPA'.center(70)}\n{'='*70}")
            break


#Kode di atas adalah program Python yang menciptakan sebuah kasir sederhana untuk mencatat transaksi produk dan mencetak struk. Berikut adalah algoritma utama dari kode tersebut:

#1. Program dimulai dengan mengimpor beberapa modul Python, seperti os, datetime, dan random.

#2. Fungsi awal_trx_history() dan isi_trx_history() digunakan untuk membuat dan mengisi riwayat transaksi ke dalam file trx_history.txt. Ini mencakup penulisan informasi transaksi seperti waktu, ID transaksi, dan nominal transaksi.

#3. Fungsi opsi() digunakan untuk menampilkan menu opsi kepada pengguna, di mana mereka dapat memilih untuk membuat transaksi baru, mencari transaksi berdasarkan ID, atau keluar dari program.

#4. Fungsi awal_struk() digunakan untuk membuat struk transaksi. Ini mencakup informasi tentang toko, nama kasir, waktu transaksi, daftar produk, dan total keseluruhan. Struk ini dicetak dalam file dengan nama yang sesuai dengan ID transaksi.

#5. Program meminta nama kasir, mengambil inisial dari nama tersebut, dan memulai daftar barang yang akan dibeli.

#6. Program memasuki loop utama yang memungkinkan pengguna untuk menambahkan produk ke dalam daftar belanja. Setiap produk termasuk nama, harga, dan jumlah. Jumlah total transaksi dihitung selama proses ini.

#7. Setelah selesai memasukkan produk, ID transaksi dibuat dengan menggunakan inisial kasir, waktu, dan angka acak. Struk transaksi dibuat dan dicetak ke dalam file di folder "Invoice", dan riwayat transaksi juga diperbarui.

#8. Pengguna dapat memilih untuk mencari transaksi berdasarkan ID transaksi, yang akan mencetak struk dari file sesuai dengan ID yang dimasukkan.

#9. Pengguna dapat memilih untuk keluar dari program, yang akan mengakhiri loop utama dan menampilkan pesan selamat tinggal.

#Demikianlah algoritma utama dari kode tersebut. Program ini digunakan untuk mengelola transaksi kasir dan mencetak struk sebagai bukti pembayaran.