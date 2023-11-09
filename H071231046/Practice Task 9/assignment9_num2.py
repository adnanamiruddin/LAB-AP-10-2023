class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        return (f"Nama: {self.nama}\nNIM: {self.nim}\nJurusan: {self.jurusan}\nIPK: {self.ipk}")

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Cukup"
        else:
            return "Kurang"

mahasiswa1 = Mahasiswa("Chelsea", "H071231046", "Sistem Informasi", 4)
# #Jika ingin memasukkan inputan
# a = input('Masukkan nama mahasiswa = ')
# b = input('Masukkan NIM = ')
# c = input('Masukkan Jurusan = ')
# d = float(input('Masukkan IPK = '))
# mahasiswa1 = Mahasiswa(a, b, c, d)

print(mahasiswa1.tampilkan_info())
print(mahasiswa1.hitung_predikat())
