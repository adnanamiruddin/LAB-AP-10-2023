golongan = (input('golongan = '))
daya = int(input('Daya = '))
pemakain = int(input('pemakaian = '))


match golongan :    
    case 'R1':
        if daya == 900:
            print (f'Pemakaian = Jumlah tagihan anda sebesar : Rp,{1352*pemakain:,.1f}'.replace(',','x').replace('.',',').replace('x','.'))
        elif daya == 1300:
            print (f'Pemakaian = Jumlah tagihan anda sebesar : Rp,{1444.70*pemakain:,.1f}'.replace(',','x').replace('.',',').replace('x','.'))
        elif daya == 2200:
            print (f'Pemakaian = Jumlah tagihan anda sebesar : Rp,{1444.70*pemakain:,.1f}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ('data tidak valid')
    case 'R2' :
        if daya >= 3500 and daya <= 5500 :
            print (f'Pemakaian =  Jumlah tagihan anda sebesar : Rp,{1699.53*pemakain:,.1f}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ('data tidak valid')
    case 'R3' :
        if daya >= 6600 :
            print (f'Pemakaian = Jumlah tagihan anda sebesar : Rp,{1699.53*pemakain:,.1f}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ('data tidak valid')
    case 'B2' :
        if daya >=6600 and daya <= 200000 :
            print (f'Pemakaian = Jumlah tagihan anda sebesar : Rp,{1444.70*pemakain:,.1f}'.replace(',','x').replace('.',',').replace('x','.'))
        else : 
            print ('data tidak valid')
    case 'B3' :
        if daya >200000 :
            print (f'Pemakaian= Jumlah tagihan anda sebesar : Rp,{1114.74*pemakain:,.1f}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ('data tidak valid')
    case 'I3' :
        if daya >=200000 :
            print (f'Pemakaian = Jumlah tagihan anda sebesar : Rp,{1314.12*pemakain:,.1f}'.replace(',','x').replace('.',',').replace('x','.'))
        else :
            print ('data tidak valid')
    case 'P1' :
        if daya >=6600 and daya <= 200000 :
            print (f'Pemakaian = Jumlah tagihan anda sebesar : Rp,{1523.28*pemakain:,.1f}'.replace('.','x').replace('.',',').replace('x','.'))
        else :
            print ('data tidak valid')
    case _:
        print("golongan tidak ada dalam data")