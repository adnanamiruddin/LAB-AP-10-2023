from hero import Assassin, Warrior, Support
        
warrior = Warrior("bambang", position=10)
assassin = Assassin("joko", position=25)
support = Support("udin",position=30)
# sebelum
print("health (before)", warrior.getHealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.getHealth())
print("-"*10)

# sebelum
print("Warrior (health)", warrior.getHealth())
print("Support (speed) : ",support.getSpeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.getHealth())
print("Support (speed): ",support.getSpeed())

print("-"*10)
print("Warrior (position)", warrior.getPosition())
warrior.movement("LL")
print("Warrior (position)", warrior.getPosition())