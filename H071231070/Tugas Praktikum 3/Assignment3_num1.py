n = int(input("n = ")) 
if n < 0:
    print("Bukan Fibonacci") 
u1 = 0 
u2 = 1 
for i in range(n): 
    print(u1, end=" ")  
    u3 = u1 + u2        
    u1 = u2             
    u2 = u3             
