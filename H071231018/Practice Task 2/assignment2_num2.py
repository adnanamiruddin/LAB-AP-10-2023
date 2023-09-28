a = input ("Masukkan Input Pertama : ")
b = input ("Masukkan Input Kedua : ")
c = input ("Masukkan Input Ketiga : ")

if a== "vertebrado":
    if b== "ave":
        if c== "carnivoro":
            print ("agula")
        elif c== "onivoro":
            print ("pomba")
        else:
            print("invalid data")
    else:
        print("invalid data")
    if b== "mamifero":
        if c== "onivoro":
            print ("homem")
        elif c== "herbivoro":
            print ("vaca")
        else:
            print("invalid data")
    else:
        print("invalid data")
if a== "invertebrado":
    if b== "inseto":
        if c== "hematofago":
            print ("pulga")
        elif c== "herbivoro":
            print ("lagarta")
        else:
            print("invalid data")
    else:
        print("invalid data")
    if b== "anelideo":
        if c== "hematofago":
            print ("sanguessuga")
        elif c== "onivoro":
            print ("minhoca")
        else:
            print("invalid data")
    else:
        print("invalid data")
