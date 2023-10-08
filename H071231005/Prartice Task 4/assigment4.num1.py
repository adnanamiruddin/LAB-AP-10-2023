def mutasi(kata):
    try:
        for i in range(len(kata)):
            kata = kata[-1] + kata[:-1]
            print (kata, end=' | ')
    except TypeError:
        print ('error')
        
kata = input('Masukan kata : ')
mutasi(kata)