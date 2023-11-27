from hero import Warrior, Assassin, Support

warrior = Warrior("Bambang", pos_x=10)
assassin = Assassin("Joko", pos_x=25)
support = Support("Udin", pos_x=30)

# #Jika ingin mememasukkan inputan
# a = int(input('Posisi x untuk Warrior = '))
# b = int(input('Posisi x untuk Assassin = '))
# c = int(input('Posisi x untuk Support = '))
# warrior = Warrior("Bambang", pos_x=a)
# assassin = Assassin("Joko", pos_x=b)
# support = Support("Udin", pos_x=c)

#sebelum
print("\nhealth (before)", warrior.get_health())
assassin.attack(warrior)
#sesudah
print("health (after)", warrior.get_health())

print("-"*10)

#sebelum
print("Warrior (health)", warrior.get_health())
print("Support (speed) : ", support.get_speed())

support.special(warrior)

#sesudah
print("Warrior (health)", warrior.get_health())
print("Support (speed): ", support.get_speed())
print("-"*10)

print(warrior.get_pos_x())
warrior.movement("")
print(warrior.get_pos_x())