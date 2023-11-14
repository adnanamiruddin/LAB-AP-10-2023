from hero import Warrior, Assassin, Support

warrior = Warrior("thamuz", 10)
assassin = Assassin("aamon", 25)
support = Support("estes", 30)

#Sebelum
print("health (before)", warrior.getHealth())
assassin.Attack(warrior)
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
warrior.Movement("L")
print(warrior.getPosition())

