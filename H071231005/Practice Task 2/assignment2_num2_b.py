pertama = input('masukan inputan pertama : ')
kedua = input('masukan inputan kedua : ')
ketiga = input('masuakan inputan ketiga : ')

match pertama,kedua,ketiga:
    case 'vertebrado','ave','carnivoro':
        print ('aguia')
    case 'vertebrado','ave','onivoro':
        print ('pomba')
    case 'vertebrado','mamifero','onivoro':
        print ('homen')
    case 'vertebrado','mamifero','herbivoro':
        print ('vaca')
    case 'intervertebrado','inseto','hematofago':
        print ('pulga')
    case 'intervertebrado','inseto','herbivoro':
        print ('lagarta')
    case 'intervertebrado','anelideo','hematofago':
        print ('sanguessuga')
    case 'intervertebrado','anelideo','onivoro':
        print ('minhoca')
    case _ :
        print ('invalid input')