golongan = input("Golongan = ")
daya = int(input("Daya = "))
pemakaian = int(input("Pemakaian = "))

match golongan, daya:
    case "R1", 900:
        tarif = pemakaian * 1352
        print(f"Jumlah tagihan anda sebesar : Rp{tarif:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "R1", 1300:
        tarif = pemakaian * 1444.70
        print(f"Jumlah tagihan anda sebesar : Rp{tarif:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "R1", 2200:
        tarif = pemakaian * 1444.70
        print(f"Jumlah tagihan anda sebesar : Rp{tarif:,.1f}".replace(",","x").replace(".",",").replace("x","."))
    case "R2", daya:
        if daya >= 3500 and daya <= 5500:
            tarif = pemakaian * 1699.53
            print(f"Jumlah tagihan anda sebesar : Rp{tarif:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid!")
    case "R3", daya:
        if daya >= 6600:
            tarif = pemakaian * 1699.53
            print(f"Jumlah tagihan anda sebesar : Rp{tarif:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid!")
    case "B2", daya:
        if daya >= 6600 and daya <= 200000:
            tarif = pemakaian * 1444.70
            print(f"Jumlah tagihan anda sebesar : Rp{tarif:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid!")
    case "B3", daya:
        if daya > 200000:
            tarif = pemakaian * 1114.74
            print(f"Jumlah tagihan anda sebesar : Rp{tarif:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid!")
    case "I3", daya:
        if daya >= 200000:
            tarif = pemakaian * 1314.12
            print(f"Jumlah tagihan anda sebesar : Rp{tarif:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid!")
    case "P1", daya:
        if daya >= 6600 and daya <= 200000:
            tarif = pemakaian * 1523.28
            print(f"Jumlah tagihan anda sebesar : Rp{tarif:,.1f}".replace(",","x").replace(".",",").replace("x","."))
        else:
            print("Data tidak valid!")
    case _:
        print("Data tidak valid!")

