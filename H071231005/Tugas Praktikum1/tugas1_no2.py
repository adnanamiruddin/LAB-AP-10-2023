#konversi suhu dari celcius ke kelvin, reamur dan fahrenheit
#masukan suhu dalam celcius : 50

print('Konversi suhu dari celcius ke Kelvin, Reamur, dan fahrenheit')
celcius = float(input('masukan suhu dalam celcius : '))
kelvin = int(celcius + 273)
print (f'hasil konversi dari suhu {celcius} derajat celcius ke kelvin adalah : {kelvin}K')
reamur = int(4/5*celcius)
print (f'hasil konversi dari suhu {celcius} derajat celcius ke reamur adalah : {reamur}R')
fahrenheit = int(9/5*celcius + 32)
print (f'hasil konversi dari suhu {celcius} derajat celcius ke fahrenheit adalah : {fahrenheit}F')

