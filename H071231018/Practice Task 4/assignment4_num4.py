def catAndMouse(a1,b1,c1):
    a = (a1-c1)**2
    b = (b1-c1)**2
    if a > b :
        return ('cat b')
    elif b > a:
        return ('cat a')
    else :
        return ('Mouse c')
try: 
    a1= int(input("Masukkan jarak catA: "))
    b1= int(input("Masukkan jarak catB: "))
    c1 = int(input('Masukan jarak mouseC:'))
    print(catAndMouse(a1, b1,c1))
except ValueError:
    print ("Inputan hanya angka.")
