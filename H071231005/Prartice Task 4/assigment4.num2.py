def palindrom (kata: str)-> str:
    try:
        kata = kata.lower()
        rumus = kata[::-1]
        if kata == rumus:
            print ('palindrom')
        else :
            print ('Bukan palindrom')
    except :
        print ('Iinput Berupa huruf')

masukan = input('Masukan Kata: ')
palindrom(masukan)