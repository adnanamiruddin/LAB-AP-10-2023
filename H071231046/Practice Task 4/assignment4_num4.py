def catAndMouse(catA, catB, mouseC):
    # Menghitung jarak kucing A dengan tikus C
    if mouseC > catA:
        distance_catA = mouseC - catA
    else:
        distance_catA = catA - mouseC
    # Menentukan jarak kucing B dengan tikus C
    if mouseC > catB:
        distance_catB = mouseC - catB
    else:
        distance_catB = catB - mouseC


    if distance_catA < distance_catB:
        return "Cat A"
    elif distance_catB < distance_catA:
        return "Cat B"
    else:
        return "Mouse C"

inputcatA = int(input("catA = "))
inputcatB = int(input("catB = "))
inputmouseC = int(input("mosC = "))

output = catAndMouse(inputcatA, inputcatB, inputmouseC)
print(output)
