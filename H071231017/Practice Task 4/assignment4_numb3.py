def maks(*bil) :   
  max = 0    #digunakan utk melacak nilai maximum.
  for i in bil :
    if i >= max :
      max = i

  print(max)

maks(1,2,4,6,9,3,1,9,10)  #pemanggilan fungsi dgn argumen
