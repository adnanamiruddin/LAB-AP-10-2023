def stringPermutation(kata) :
  try:
    for i in range(len(kata)):     #merupakan perulangan dmn len...., 
      kata = kata[-1] + kata[:-1]  #kata [-1] artinya karakter terakhir, kata[:-1] artinya semua yg diambil kecuali karakter terakhir.
      print(kata, end= " | ") #berfungsi utk memisahkan karakter

  except TypeError:          #jika yg dimasukkan itu tidak valid
    print("Invalid Input")

stringPermutation("Ayam")