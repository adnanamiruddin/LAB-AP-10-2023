class Mahasiswa:
    def __init__(self, nama, nim, jurusan, Ipk):   #untuk menginisialisasi objek mahasiswa dengan nilai-nilai atribut yang diberikan saat objek dibuat.
        self.nama = nama  
        self.nim = nim 
        self.jurusan = jurusan
        self.Ipk = Ipk

    def info(self):   # untuk mencetak informasi lengkap tentang seorang mahasiswa, termasuk nama, NIM, jurusan, dan IPK.
        print('Nama     :',self.nama)
        print('nim      :',self.nim)
        print('jurusan  :',self.jurusan)
        print('Ipk      :',self.Ipk)
    
    
    def hitung_predikat(self): #untuk menentukan predikat berdasarkan IPK mahasiswa. Predikat ini mencakup kategori seperti "Cumlaude," "Sangat Memuaskan," "Memuaskan," "Cukup," atau "Kurang," tergantung pada nilai IPK.
        if self.Ipk >= 3.5:
            print("Cumlaude")
        elif self.Ipk >= 3.0:
            print("Sangat Memuaskan")
        elif self.Ipk >= 2.5:
            print("Memuaskan")
        elif self.Ipk >= 2.0:
            print("Cukup")
        else:
            print("Kurang")



mhs1 = Mahasiswa("nay", "H071231017", "Sisfo", 4.0)
mhs2 = Mahasiswa("appil", "H021231021", "Fisika", 3.5)
mhs3 = Mahasiswa("ima", "K011231023", "kesmas", 2.0)
mhs4 = Mahasiswa("adnan", "H071221080", "Sistem Informasi", 4.0)
mhs1.info() 
mhs1.hitung_predikat()  #utk mencetak informasi lengkapttntng mahasiswa
mhs2.info()
mhs2.hitung_predikat()
mhs3.info()
mhs3.hitung_predikat()
mhs4.info()
mhs4.hitung_predikat()





