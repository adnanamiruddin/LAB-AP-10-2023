n = int (input())
if n < 0 :
    print ("bukan fibonacci")
elif n == 0 :
    print (0)
a = 0
b = 1
for i in range (n) :
    print (a, end = " ")
    c = a + b
    a = b 
    b = c