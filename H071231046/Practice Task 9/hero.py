#Class Parent
class Human:
    #Constructor (_init_ function)
    def __init__(self, name, pos_x, speed=5):
        self.name = name
        self.__pos_x = pos_x
        self._speed = speed 

    def get_pos_x(self):
        return self.__pos_x

    def set_pos_x(self, pos_x):
        self.__pos_x = pos_x

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def movement(self, direction):
        if direction == "L":
            self.__pos_x -= self._speed
        elif direction == "R":
            self.__pos_x += self._speed

#Inheritance ke kelas Human
#Class Child
class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x) #Memanggil constructor class parent
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def get_power(self):
        return self._power

    def set_power(self, power):
        self._power = power

    def get_health(self):
        return self._health

    def set_health(self, health):
        self._health = health

    def get_armor(self):
        return self._armor

    def set_armor(self, armor):
        self._armor = armor

    def attack(self, target):
        if hasattr(target, '_health'):
            # has attribute 
            #Fungsi hasattr mengembalikan True jika objek memiliki atribut yang ditentukan, dan False jika tidak.
            target.set_health(target.get_health() - self._power)

#Inheritance ke kelas Hero
class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._armor = 45
        self._power = 32
        if hasattr(target, '_health'):
            target.set_health(target.get_health() - self._power)

#Inheritance ke kelas Hero
class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self.speed = 4

    def special(self, target):
        self._speed = 7
        self._power = 42
        if hasattr(target, '_health'):
            target.set_health(target.get_health() - self._power)

#Inheritance ke kelas Hero
class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self, target):
        self._speed = 6
        if hasattr(target, '_health'):
            target.set_health(target.get_health() + 150)