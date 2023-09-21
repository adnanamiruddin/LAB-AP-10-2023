# diketahui sebuah segitiga yang mempunyai sisi x, y, dan z. buatlah program yang menghitung luas dan keliling segitiga xyz

import math
x = int(input("masukkan nilai x(tinggi): "))
y = int(input("masukkan nilai y(luas)"))
z = math.sqrt(x**2 + y**2)

luas = x*y/2
keliling = x+y+z
print(f"luas permukaan {luas:.2f}")
print(f"keliling {keliling:.2f}")


