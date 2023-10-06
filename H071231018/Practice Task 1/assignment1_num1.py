# z=int(input ())
# x=23
# y=43
# luas=1/2 * x * y
# keliling=x + y + z
# print (f'luas ={luas}')
# print (f'keliling ={keliling}')

x = int(input("Panjang Sisi X : "))
y = int(input("Panjang Sisi Y : "))
z = (x**2+y**2)**0.5

luas=1/2 * x * y
keliling=x + y + z

print (f'luas permukaan :{luas:.2f}')
print (f'keliling :{keliling:.2f}')
#rumus z=(x**2+y**2)**0.5