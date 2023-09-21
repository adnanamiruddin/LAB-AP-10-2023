golongan = input("Golongan = ")
daya = float(input("Daya = "))
pemakaian = float(input("Pemakaian = "))

tagihan = 0

match golongan, daya:
    case "R1", 900:
        tagihan = pemakaian * 1352
    case "R1", 1300:
        tagihan = pemakaian * 1444.70
    case "R1", 2200:
        tagihan =pemakaian * 1444.70
    case "R2", daya: 
        if daya>=3500 and daya<= 5500:
            tagihan = pemakaian * 1699.53
    case "R3", daya:
        if daya>=6600: 
            tagihan = pemakaian * 1699.53
    case "B2", daya:
        if daya>=6600 and daya<=200000:
            tagihan = pemakaian * 1444.7
    case "B3", daya:
        if daya>200000:
            tagihan = pemakaian * 114.74
    case "I3", daya:
        if daya>=200000:
            tagihan = pemakaian * 1314.12
    case "P1", daya: 
        if daya>=6600 and daya<=200000:
            tagihan = pemakaian * 1523.28
    case _:
        print("Input tidak valid")
        exit()
        

print(f"Pemakaian = Jumlah tagihan anda sebesar : Rp, {tagihan:,.1f}".format(tagihan).replace(",","x").replace(".",",").replace("x","."))
