def string (kata):
    if len(kata)>=3:
        kata2= kata[0] + kata[len(kata)//2] + kata[-1]
        print(kata2)
    else:
        print("Masukan minimal 3 huruf")

kata= input("Masukan kata: ")
string (kata)