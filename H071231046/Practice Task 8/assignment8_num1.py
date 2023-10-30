import re

text = input('Masukkan Kalimat : ')
# text = '2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57' #True
# text = 'x4202v2A22A8a6aaaaaa2G2222m222qwertyYuIo1395779' #False
# text = 'aaasdfgesdfghasdsawfdsefdsfdsawfkjnwjybh79333' #True
pattern = '[A-Za-z02468]{40}[13579\s]{5}'
result = re.fullmatch(pattern, text) #Mencocokkan pola dengan seluruh string

if result:
    print(True)
else:
    print(False)