# pengujian jenis karakter
print ('pengujian jenis karakter')
print ('-------------------------')

karakter = (input('karakter = '))
kapital = karakter.isupper ()
print ('Huruf kapital? ',kapital)

huruf_kecil = karakter.islower ()
print ('Huruf kecil? ',huruf_kecil)

angka = karakter.isdigit ()
print ('Angka? ',angka)

