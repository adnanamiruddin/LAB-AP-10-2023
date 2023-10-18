def string (kata):
    if len(kata) >=3:
        kata2 = kata[0] + kata[len(kata)//2] + kata[-1]
        print (kata2)
    else :
        print ("masukan minimal 3 kata")

masukan = (input("Masukan kata: "))
string(masukan)