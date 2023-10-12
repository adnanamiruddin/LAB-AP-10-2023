def CatAndMouse(CatA, CatB, MouseC): #Misalnya kejar kejaran kucing tikus, jika jarak kucing a nya lebih besar dibanding kucing b, maka kucing b menang
    A = ((CatA - MouseC)**2)**0.5  #Ini rumus mencari jarak kucing a ke tikus c
    B = ((CatB - MouseC)**2)**0.5   #Ini rumus mencari jaraka kucing b ke tikus c

    if A < B: #Jika jarak kucing a lebih sedikit dibanding B maka otomatis Kucing A yang menang
        print("Cat A")
    elif A > B:
        print("Cat B")
    else:
        print("Mouse C") #jika kucing a dan kucing B jaraknya sama otomatis berdua berkelahi dan tikus c nya lari, dan tikus c nya menang

CatAndMouse(CatA=16, CatB=24, MouseC=15)