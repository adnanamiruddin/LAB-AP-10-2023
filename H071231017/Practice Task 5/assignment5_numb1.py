s1 = input('s1: ')
s2 = input('s2: ')[::-1]
hasil = ''              # untuk tampung nilai hasil

lenMax = max(len(s1),len(s2))    #cari nilai maxnya antara panjang s1 dan s2 yg mna panjang maka itu nnti msuk ke lenmax

for i in range(lenMax):     
    if i < len(s1):
        hasil += s1[i]   
    if i < len(s2):
        hasil += s2[i]
print(hasil)