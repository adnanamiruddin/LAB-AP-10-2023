class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk): #atribut nama,nim,jurusan,ipk
        self.nama = nama #atribut harus dpainggil
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def Tampilkan_info(self):
        return (f"Nama : {self.nama}\nNIM : {self.nim}\nJurusan : {self.jurusan}\nIPK : {self.ipk}") #tampilkan data sesuai di objek
    
    def Hitung_Predikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif 3.0 <= self.ipk < 3.5:
            return "Sangat Memuaskan"
        elif 2.5 <= self.ipk < 3.0:
            return "Memuaskan"
        elif 2.0 <= self.ipk < 2.5:
            return "Cukup"
        else:
            return "Kurang"
        
mahasiswa1 = Mahasiswa("Kezia", "H071231070", "Sistem Informasi", 2.3)
mahasiswa2 = Mahasiswa("Dewanti", "H071231020", "Teknik", 4.0)
print(mahasiswa1.Hitung_Predikat())
print(mahasiswa2.Tampilkan_info())