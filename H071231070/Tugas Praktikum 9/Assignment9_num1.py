from hero import Warrior, Assassin, Support
    
warrior = Warrior("bambang", 10)
assassin = Assassin("joko", 25)
support = Support("udin", 30)

#Sebelum
print("health (before)", warrior.getHealth())
assassin.Attack(warrior) # warrior nya jadi target
#Sesudah
print("health (after)", warrior.getHealth())
print("-"*10)
#Sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed)", support.getSpeed())

support.special(warrior)
#Sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed)", support.getSpeed())


print("-"*10)
print(warrior.getPosition())
warrior.Movement("R")
print(warrior.getPosition())
warrior.Movement("L")
print(warrior.getPosition())