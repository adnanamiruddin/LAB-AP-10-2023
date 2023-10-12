#nomor 4
def CatAndMouse (CatA, CatB, MouseC):
    a= (CatA - MouseC)**2
    b=  (CatB - MouseC)**2
    if a>b:
        print ("Cat B")
    elif a<b:
        print ("Cat A")
    else:
        print ("Mouse C")

CatA = int (input("Masukan Jarak Cat A: "))
CatB = int (input("Masukan Jarak Cat B: "))
MouseC= int (input("Masukan Jarak Mouse C: "))

CatAndMouse (CatA, CatB, MouseC)