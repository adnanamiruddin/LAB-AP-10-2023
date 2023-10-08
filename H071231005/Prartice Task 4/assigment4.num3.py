def maximum(*n):
    max = n[0]
    for i in n:
       if  i > max :
           max = i
    print (max)
    
maximum( 10, 28,27,28,45,23)