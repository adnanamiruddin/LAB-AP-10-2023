#panjang sisi XYZ
print('Menghitung luas permukaan dan keliling segitiga')
X = int(input ('Panjang sisi X = '))
Y = int(input ('Panjang sisi Y = '))

#menhitung panjang sisi miring  
Z = (X**2 + Y**2)**0.5


keliling = X + Y + Z
luas =  (0.5*X*Y)

print('Luas Permukaan: ',format(luas, '.2f'))
print('Keliling: ',format (keliling, '.2f'))