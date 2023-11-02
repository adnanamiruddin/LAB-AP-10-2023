s1 = input('\nMasukkan kata pertama: ').replace(' ','').lower()
s2 = input('Masukkan kata kedua: ').replace(' ','').lower()

x, y = 0, -1       #untuk menampung nilai nantinya
if(len(s1)==len(s2)):
    y += 1
    for i in s1:         #dmn i itu adalah char char yg ada di dalamnya s1
        x += s1.count(i)    #x ditambahkan dgn jumlah i dalam string s1
        y += s2.count(i)
print(x == y)