class Human: #ini adalah kelas kakek dari bapaknya yaitu hero, dan cucunya yaitu warrior, support, assasin
    def __init__(self, name, position, speed=1): #Constructor, langsung dijalankan tanpa di panggil seperti method
        self.name = name #ini adalah atribut
        self.__position = position #ini adalah atribut
        self._speed = speed #ini adalah atribut protected
        
    def Movement(self, arah): #ini adalah method untuk ukur pergerakan hero nanti
        if arah == "R":
            self.__position += self._speed
        elif arah == "L":
            self.__position -= self._speed
        else:
            pass #klo ada huruf selain R dan L nanti na pass itu huruf alias diabaikan dan langsung lanjut kehuruf R atau L slnjtnya

    def getPosition(self): #ini juga method untuk mengakses nilai position yang privat
        return self.__position
    def setPosition(self, position):
        self.__position = position
        
    def getSpeed(self): #untuk akses nilai speed 
        return self._speed
    def setSpeed(self, speed): 
        self._speed = speed
        
class Hero(Human):  #class Anak(Parent)
    def __init__(self, name, position):
        super().__init__(name, position) #super() ini berfungsi mengambil atribut dari class parentnya
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
    def Attack(self, target): #ketika target di attact atau diserang, method ini berfungsi untuk mengetahui health nya target
        target._health -= self._power
        print(f"{self.name} Sedang Menyerang, Health {target.name} berkurang sebanyak {self._power}, dan tersisa {target._health}")
    
    def getPower(self): #buat method biar bisa tinggal di panggil di bawah
        return self._power
    def getHealth(self):
        return self._health
    def getArmor(self):
        return self._armor
    def setPower(self, power):
        self._power = power
    def setHealth(self, health):
        self._health = health
    def setArmor(self, armor):
        self._armor = armor
    
class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 26
        self._armor = 30
        
    def special(self, target): 
        self._armor = 45
        self._power = 32
        target._health -= self._power
        print(f"{self.name} Sedang menggunakan special skill!")

class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 35 
        self._speed = 4
        
    def special(self, target):
        self._speed = 7
        self._power = 42
        target._health -= self._power
        print(f"{self.name} Sedang menggunakan special skill!")
        
class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        target._health += 150
        print(f"{self.name} Sedang menggunakan special skill!")