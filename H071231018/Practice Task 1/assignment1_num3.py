# a =float(input("a= "))
# if a==0:
#     print("a tidak boleh sama dengan nol")
#     exit()
# b =float(input("b= "))
# c =float(input("c= "))


# x1 = (-b+(b**2-4*a*c)**(0.5))/2*a
# print (f"x1 = {x1:.2f}")
# x2 = (-b-(b**2-4*a*c)**(0.5))/2*a
# print (f"x2 = {x2:.2f}")


a = int(input("Input a = "))
if a==0:
    print("a tidak sama dengan nol")
    exit()
b = int(input("Input b = "))
c = int(input("Input c = "))

p = b ** 2
q = 4 * a * c
r = 2 * a

x1 = (-b + ((p - q)**0.5))/r
x2 = (-b - ((p - q)**0.5))/r

print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")
