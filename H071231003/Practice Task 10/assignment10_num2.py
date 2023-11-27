from abc import ABC, abstractmethod

class Mobil(ABC): #abstrak base class
    def __init__(self, merk):
        self._merk = merk

    @abstractmethod
    def info(self):
        pass

class Sedan(Mobil):
    def __init__(self, merk, tipe, warna):
        super().__init__(merk)
        self._tipe = tipe
        self._warna = warna

    def info(self):
        print("Mobil Sedan:", self._merk)
        print("Tipe:", self._tipe)
        print("Warna:", self._warna)

class SUV(Mobil):
    def __init__(self, merk, tipe, warna):
        super().__init__(merk)
        self._tipe = tipe
        self._warna = warna

    def info(self):
        print("Mobil SUV:", self._merk)
        print("Tipe:", self._tipe)
        print("Warna:", self._warna)

while True:
    print("="*50)
    inputan = print("Masukkan pilihan Anda: \n1. Sedan \n2. SUV \n3. Keluar")
    pilihan = input("Silahkan Pilih Opsi Anda: ")
    if pilihan == "1":
        merk = input("Masukkan merk mobil sedan: ")
        tipe = input("Masukkan tipe mobil sedan: ")
        warna = input("Masukkan warna mobil sedan: ")
        print("="*50)
        sedan_saya = Sedan(merk, tipe, warna)
        sedan_saya.info()
    elif pilihan == "2":
        merk = input("Masukkan merk mobil SUV: ")
        tipe = input("Masukkan tipe mobil SUV: ")
        warna = input("Masukkan warna mobil SUV: ")
        print("="*50)
        suv_teman = SUV(merk, tipe, warna)
        suv_teman.info()
    elif pilihan == "3":
        print("="*50)
        print("see you, this is last TP bang")
        print("="*50)
        break
    else:
        print("pilihannya cuman 1,2, atau 3 bang")

#sedan= toyota, vios, kuning
#suv= toyota, rush, hitam