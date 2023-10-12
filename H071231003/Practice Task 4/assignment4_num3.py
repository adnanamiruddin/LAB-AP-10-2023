def terbesar (*args):
    b = args[0]
    for i in args:
        if i > b:
            b=i
    print(b)
terbesar(1,2,4,6,9,3,1,9,10)