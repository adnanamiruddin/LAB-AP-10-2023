def Palindrom(kata: str)->str:   #menerima satu parameter, yaitu string kata dan mengembalikan sebuah string
  reverse = kata[::-1]    #berfungsi membalikkan kata #ikan = naki
  jumlah = 0   #menghitung brp bnyak karakter yg sesuai ketika membandingkan string kata dgn string reverse
  for i in range(len(kata)) : 
    if kata[i] == reverse[i]:
      jumlah += 1      #jika nnti jika kata ke i sama kata yg sudh dibalik itu sma, maka jumlahnya nnti itu ditambah 1.
  if jumlah == len(kata):
    print("palindrom")
  else :
    print("bukan palindrom")

Palindrom("saya")

