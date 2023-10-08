def tangkap (ab,bc,cc):
    a = (ab - cc)**2
    b = (bc - cc)**2
    if a > b :
        return('Cat b')
    elif b > a:
        return ('cat a')
    else:
        return ('mouse c')
try:
    kucingA = int(input(">>Cat A= "))
    KucingB = int(input(">>Cat B= "))
    Tikus = int(input(">>Mouse C= "))
    print(tangkap (kucingA, KucingB, Tikus))
except ValueError:
    print ('inputan hanya berupa angka')