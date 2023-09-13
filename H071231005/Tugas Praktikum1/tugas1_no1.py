#panjang sisi x : 23
#panjang sisi y : 43

print('Menghitung luas permukaan dan keliling segitiga')
x = float (input('Panjang sisi x : '))
y = float (input('Panjang sisi y : '))
#memasukan rumus pytagoras
z = ((x**2+y**2)**0.5)

#masukan rumus luas permukaan dan keliling
luas_permukaan = 0.5*y*x
print (f'luas permukaan : {luas_permukaan:.2f}') 
keliling = x + y + z
print (f'keliling : {keliling:.2f}')
