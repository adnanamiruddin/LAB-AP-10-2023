#nomor 2
def palindrom (x):
    rumus= x.lower()
    kata= x[:: -1] #dibalik
    if rumus == kata:
        print ("Palindrom")
    else:
        print ("Bukan Palindrom")
masukan = input('masukan kata: ')
palindrom(masukan)