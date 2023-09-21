input1 = input("Masukkan Input Pertama: ")
input2 = input("Masukkan Input Kedua: ")
input3 = input("Masukkan Input Ketiga: ")

if input1 == "vertebrado":
    if input2 == "ave":
        if input3 == "carnivoro":
            print("aguia")
        elif input3 == "onivoro":
            print("pomba")
        else:
            print("invalid input")
    elif input2 == "mamifero":
        if input3 == "onivoro":
            print("homem")
        elif input3 == "herbivoro":
            print("vaca")
        else:
            print("invalid input")
    else:
        print("invalid input")
elif input1 == "invertebrado":
    if input2 == "inseto":
        if input3 == "hematofago":
            print("pulga")
        elif input3 == "herbivoro":
            print("lagarta")
        else:
            print("invalid input")
    elif input2 == "anelideo":
        if input3 == "hematofago":
            print("sanguessuga")
        elif input3 == "onivoro":
            print("minhoca")
        else:
            print("invalid input")
    else:
        print("invalid input")
else:
    print("Invalid input")