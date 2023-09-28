golongan    = input ("Golongan : ")
daya        = int   (input ("Daya : ") )
pemakaian   = int   (input ("Pemakaian : ") )

match golongan:
    case "R1":
        if   daya == 900:
            print (f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {1352*pemakaian:,.2f}") 
        elif daya == 1300:
            print (f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {1444.7*pemakaian:,.2f}")
        elif daya == 2200:
            print (f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {1444.7*pemakaian:,.2f}")
        else:
            print ("data tidak valid")
    case "R2":
        if   3500 <= daya <= 5500:
            print (f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {1699.53*pemakaian:,.2f}")
        else:
            print ("data tidak valid")                        
    case "R3":
        if   daya <= 6600:
            print (f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {1699.53*pemakaian:,.2f}")
        else:
            print ("data tidak valid")
    case "B2":
        if   6600 <= daya <= 200000:
            print (f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {1444.7*pemakaian:,.2f}")
        else:
            print ("data tidak valid")
    case "B3":
        if   daya > 200000:
            print (f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {1114.74*pemakaian:,.2f}")
        else:
            print ("data tidak valid")
    case "I3":
        if   daya >= 200000:
            print (f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {1314.12*pemakaian:,.2f}")
        else:
            print ("data tidak valid")
    case "P1":
        if   6600 <= daya <= 200000:
            print (f"Pemakaian = Jumlah tagihan anda sebesar : Rp. {1523.28*pemakaian:,.2f}")
        else:
            print ("data tidak valid")
