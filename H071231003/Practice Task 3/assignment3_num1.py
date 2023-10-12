n= int(input("berapa banyak suku yang ingin dijumlahkan: "))

n1= 0 #suku fibonacci itu dimulai dari 0
n2= 1

if n <=0:
    print("jumlah suku harus lebih dari 0")
else:
    for i in range(n): #range itu jangkauan data
        print(n1, end= " ") #end berfungsi agar outputnya terus kekanan
        n3= n1 + n2 #suku ketiga diperoleh dari penjumlahan suku pertama dan kedua
        n1= n2 #otomatis membuat suku pertama dan kedua selalu berubah
        n2= n3 #suku fibonacci itu deretan angkanya diperoleh dari hasil menjumlahkan dua suku sebelumnya
        #supaya angknya tidak monoton/begitu-begitu saja

