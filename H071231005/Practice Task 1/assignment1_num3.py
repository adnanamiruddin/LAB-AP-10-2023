
#menggunakan float (float adalah milai desimal yaitu angka di belakang koma)
a = float (input('input a = '))
if a == 0:
    print('a todak boleh sama dengan nol')
    exit()
b = float (input('input b = '))
c = float (input('input c = '))

#memasukan rumus
x1 =(-b+(b**2-4*a*c)**(0.5))/(2*a)
print (f'x1 = {x1:.2f}')
x2 =(-b-(b**2-4*a*c)**(0.5))/(2*a)
print (f'x2 = {x2:.2f}')
