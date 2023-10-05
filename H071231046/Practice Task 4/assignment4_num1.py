def stringPermutation(kata):
    try:
        for i in range(len(kata)):
            kata = kata[-1] + kata[:-1]
            print( kata, end="|" )
    except IndexError:
        print("Tidak ada input yang diberikan")

kata = input("stringPermutation: ")
stringPermutation(kata)
