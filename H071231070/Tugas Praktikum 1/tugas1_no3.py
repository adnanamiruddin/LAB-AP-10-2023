#Persamaan Kuadrat
a = int(input("Input a = "))
if a == 0:
    exit("a tidak boleh 0")
b = int(input("Input b = "))
c = int(input("Input c = "))

#Rumus
x = b**2
y = 4*a*c
z = 2*a

x1 = (-b + ((x - y)**0.5))/z
x2 = (-b - ((x - y)**0.5))/z

print(f"x1 = {x1:.02f}")
print(f"x2 = {x2:.02f}")
