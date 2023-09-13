#Tugas 3 Persamaan kuadrat

a = float(input("Input a = "))
if a == 0:
    print("Input a tidak boleh 0!")
    exit()
b = float(input("Input b = "))
c = float(input("Input c = "))

a1 = 2 * a
b1 = b ** 2
c1 = 4 * a * c

#Rumus Persamaan Kuadrat
x1 = (-b + ((b1 - c1)**0.5))/a1
x2 = (-b - ((b1 - c1)**0.5))/a1

print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")

