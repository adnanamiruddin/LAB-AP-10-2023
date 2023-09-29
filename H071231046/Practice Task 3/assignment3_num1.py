def fibonacci(n):
    a = 0
    b = 1
    if n<0:
        print("Silakan input ulang")
    else:
        for i in range(n):
            print(a, end=" ")
            c = a+b
            a=b
            b=c
            
n = int(input())
hasil = fibonacci(n)
print (f"{hasil}".format(hasil).replace("None",""))
