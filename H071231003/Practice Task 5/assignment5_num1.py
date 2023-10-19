def mixed (s1, s2):
    s3= "" 
    minimal= min(len(s1),len(s2))
    for i in range (minimal):
    #balik= "".join(reversed(s2)) #membalikkan
        s3 += s1[i] + s2[-(i+1)]
    print(s3)

s1= input("Masukan kata 1: ")
s2= input("Masukan kata 2: ")
mixed(s1, s2)

  