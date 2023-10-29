a = input('Masukkan kata: ')
if len(a) <= 3:
    print(a)
elif len(a)%2==0:
    print(a[0] + a[len(a)//2-1] + a[(len(a) // 2)] + a[-1])
else:
    print(a[0] + a[(len(a) // 2)] + a[-1])
