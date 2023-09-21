gender = int(input('Pilih gender Anda: \n1.Pria\n2.Wanita\n= ')) 

tinggi=float(input('Masukan tinggi badan (cm): '))/ 100
berat= float(input('Masukan berat badan (kg): '))

BMI= berat/(tinggi**2)
format_BMI= f'{BMI:.2f}'

if gender == 1:
    if BMI <18:
     print(f'Anda tergolong Underweight dengan BMI {format_BMI}')
    elif 18 <= BMI <= 23.9:
     print(f'Anda tergolong Normal dengan BMI {format_BMI}')
    elif 24 <= BMI <= 26.9:
     print(f'Anda tergolong Overweight dengan BMI {format_BMI}')
    else:
     print(f'Anda tergolong Obesitas dengan BMI {format_BMI}')
elif gender == 2:
    if BMI <17:
     print(f'Anda tergolong Underweight dengan BMI {format_BMI}')
    elif 17 <= BMI <= 23.9:
     print(f'Anda tergolong Normal dengan BMI {format_BMI}')
    elif 24 <= BMI <= 27.9:
     print(f'Anda tergolong Overweight dengan BMI {format_BMI}')
    else:
     print(f'Anda tergolong Obesitas dengan BMI {format_BMI}')
else:
    print('jenis kelamin tidak ditemukan')