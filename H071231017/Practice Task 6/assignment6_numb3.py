try:
    x = [int(i) for i in input('\nMasukkan beberapa angka (pisahkan dengan spasi): ').split(' ')]
    angkanol, angkaGanjil, angkaGenap, kelipatanLima = set(), set(), set(), set()
    for i in x:     #loop for untuk mengiterasi melalui setiap angka dalam list x
        if i == 0:
            angkanol.add(i)
        if i % 2 == 0 and i !=0:
            angkaGenap.add(i)
        if i % 2 != 0 and i !=0:
            angkaGanjil.add(i)
        if i % 5 == 0 and i !=0:
            kelipatanLima.add(i)
    print(f"\nAngka nol: {list(angkanol)}\nAngka genap: {list(angkaGenap)}\nAngka ganjil: {list(angkaGanjil)}\nAngka yang habis dibagi lima: {list(kelipatanLima)}\n")
except ValueError:
    print('\nInputan invalid.')