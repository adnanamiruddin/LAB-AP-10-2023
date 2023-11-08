import re

while True:  #dsini buat perulangan untuk inputan n nya, while nya akan  berhenti jika inputan n nya sudah sesuai syarat, yaitu n nya harus besar dari 0, dan n nya harus integer
    try:  #kita buat try except buat ValueError, disini error value itu terjadi kalau kita inputkan bknn sebuah angka didalam n, makanya akan error value karena di n itu, inputannya pertama string, tapi kita ubah ke int jadi kalau bukan bilangan, maka terjadi error
        n = int(input('\nMasukkan jumlah baris: '))  
        if n <= 0:    #memeriksa apkh nilai yg dimasukkan adlah bilangan bulatyg lebih dri nol
            print('\nJumlah baris harus lebih dari nol!')
        else:
            break
    except ValueError: #disini jika terjadi valueerror, maka dia print, trusprogramnya kembali berulang meminta input
        print('\nInputan jumlah baris harus integer!')
ip = [input('\nMasukkan IP Address: ') for _ in range(n)] #disini kita inputkan ip address, tetapi jumlahnya itu sesuai dengan panjang n, misalnya n nya 2, maka inputan disini akan meminta 2 juga,nanti inputannya berubah mebjadi list


for i in ip:
    if re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])$',i):
        print('\nIPv4')
    elif re.match(r'^([0-9a-f]{0,4}:){7}[0-9a-f]{1,4}$', i):
        print('\nIPv6')
    else:
        print('\nBukan IP Address')