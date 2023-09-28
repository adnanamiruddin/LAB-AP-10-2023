n = int(input())
n1 = 0
n2 = 1
if n < 0:
    print ("Angka tidak boleh kecil dari 0")
else :
    for  i in range(n):
        print(n1, end=' ') #penggunaan end di sini bertujuan agar angka yang di hasilakn horizontal atau lurus
        ni = n1 + n2
        n1 = n2
        n2 = ni