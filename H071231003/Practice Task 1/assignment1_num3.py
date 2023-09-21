a = int(input('Input a= '))
if a==0:
    print('Nilai a tidak bisa diisikan dengan 0')
    exit()
b = int(input('Input b= '))
c = int(input('Input c= '))

x1= (-b + (b**2-4*a*c)**0.5)/2*a
x2= (-b - (b**2-4*a*c)**0.5)/2*a
print(f'x1= ', format(x1, '.2f'))
print(f'x2= ', format(x2, '.2f'))