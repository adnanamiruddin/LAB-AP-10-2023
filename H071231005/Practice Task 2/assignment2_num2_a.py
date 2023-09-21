a = (input('masukan inputan pertama : '))
b = (input('masukan inputan kedua : '))
c = (input('masuakan inputan ketiga : '))

if a == 'vertebrado':
    if b == 'ave' :
        if c == 'carnivoro':
             print('aguia')
        elif c == 'onivoro':
             print('pomba')
        else :
             print('Invalid input')          
    elif b == 'mamifero':
        if c == 'onivoro':
              print ('homem')
        elif c == 'herbivoro':
             print ('vaca')
        else :
             print ('invalid input')
    else :
         print ('Invalid input')
elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
             print('pulga')
        elif c == 'herbivoro':
             print('lagarta')
        else :
              print ('Invalid input')    
    elif b == 'andelideo':
        if c == 'hematofago':
             print ('sanguessuga')
        elif c == 'onivoro':
             print ('minhoca')
        else :
              print ('Invalid input')
    else :
         print ('Invalid input')
else :
     print ('Invalid input')