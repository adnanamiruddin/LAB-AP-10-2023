def anagram(kata1, kata2):
    k1= kata1.replace(" ", "").lower()
    k2= kata2.replace(" ", "").lower()
    print(sorted(k1)== sorted(k2))
    print("".join(sorted(k1)), "".join(sorted(k2)))

kata1= input("Masukan kata 1: ")
kata2= input("Masukan kata 2: ")
anagram(kata1, kata2)

