one = input("Masukkan Input Pertama : ").lower()
two = input("Masukkan Input Kedua : ").lower()
three = input("Masukkan Input Ketiga : ").lower()

match one, two, three :
    case "vertebrado", "ave", "carnivoro":
        print("aguia")
    case "vertebrado", "ave", "onivoro":
        print("pomba")
    case "vertebrado", "mamifero", "onivoro":
        print("homem")
    case "vertebrado", "mamifero", "herbivoro":
        print("vaca")
    case "invertebrado", "inseto", "hematofago":
        print("pulga")
    case "invertebrado", "inseto", "herbivoro":
        print("lagarta")
    case "invertebrado","anelideo", "hematofago":
        print("sanguessuga")
    case "invertebrado", "anelideo", "onivoro":
        print("minhoca")
    case _:
        print("Input tidak valid")