def mutasi (kata):
    try:
        for i in range (len(kata)):
            kata= kata[-1] +kata[:-1]
            print (kata, end=" | ")
    except:
        print('errorrrrrr')
kata = input('masukan kata: ')
mutasi(kata)