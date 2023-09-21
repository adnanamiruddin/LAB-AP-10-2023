x = int(input('masukkan nilai x: '))
y = int(input('masukkan nilai y: '))
z = (x**2+y**2)**0.5


luas = x*y/2
keliling = x + y + z

print(f'luas segitiga adalah {luas:.2f}')
print(f'keliling segitiga adalah {keliling:.2f}')