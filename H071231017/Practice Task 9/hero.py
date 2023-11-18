class Human:  #kls ini mewakili entitas manusia dlm game
    def __init__(self, name, position) :
        self.name = name
        self.__position = position
        self._speed = 1
        
    def movement(self, direction):  #utk menggerakkan manusia berdasarkan arah yg diberikan
        for i in direction:
            match i:
                case 'R':
                    self.__position += self._speed  #Jika karakter adalah 'R', maka posisi akan ditambah dengan kecepatan.
                case 'L':
                    self.__position -= self._speed
                case _:
                    pass
    
    def setPosition (self, position):   # utk mendapatkan dan mengatur nilai posisi dan kecepatn
        self.__position = position
    
    def setSpeed (self, speed):
        self._speed = speed
        
    def getPosition (self):
        return self.__position
    
    def getSpeed (self):
        return self._speed
    
    
class Hero(Human): #mewarisi dri human
    def __init__(self, name, position):
        super().__init__(name, position)  # klo mauki ambil datanya itu, pake ki super init, jdi dia ambilki datanya dri class human#agar semua dri human bisa diwariskan
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
    def attack(self, target):  #digunakan utk menyerang target dgn mengurangi health target
        target.setHealth((target.getHealth() - self._power)) # krna dalam sistem game itu, helath itu ky darah dan power itu kekuatan yg dikeluarkan . jdi klau kekuatan, sesuai dgn power yg dikeluarkan
        
    def setPower (self, power):
        self._power = power
        
    def setHealth (self, health):
        self._health = health
        
    def setArmor (self, armor):
        self._armor = armor
    
    def getPower (self):
        return self._power

    def getHealth (self):
        return self._health
    
    def getArmor (self):
        return self._armor
    
class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._power = 26
        self._armor = 30
        
    def special(self, target):
        self._armor = 45
        self._power = 32
        self.attack(target)  #mngatur kekuatan dn pelindungnya sblm menyerang trget
        
class Assassin(Hero):
    def __init__(self, name, position):  #menginisialisasi obejk asasin
        super().__init__(name, position)
        self._power = 35
        self._speed = 4
        
    def special(self, target):
        self._speed = 7
        self._power = 42
        self.attack(target)
        
class Support(Hero):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500
        self._armor = 8
        self._speed = 4
        
    def special(self, target):
        self._speed = 6
        target.setHealth((target.getHealth() + 150)) #utk support yg mengatur kecepatan dan memberikan tambahan kesehatan pada targwt