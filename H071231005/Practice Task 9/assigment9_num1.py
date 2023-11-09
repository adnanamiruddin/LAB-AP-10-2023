from hero import Warrior,Assassin, Support

warrior = Warrior("Meisya", position=10)
assassin = Assassin("Kiki", position=25)
support = Support("Cece", position=30)

# Before
print("Health (before):", warrior.getHealth())
assassin.attack(warrior)
# After
print("Health (after):", warrior.getHealth())
print("-" * 50)
# Before
print("Warrior (health):", warrior.getHealth())
print("Support (speed):", support.getSpeed())
support.special(warrior)
# After
print("Warrior (health):", warrior.getHealth())
print("Support (speed):", support.getSpeed())
print("-" * 50)

# print (warrior.getPosisi())
# warrior.movement("R")
# print(warrior.getPosisi())
# print (warrior.getPosisi())
# warrior.movement("L")
# print(warrior.getPosisi())