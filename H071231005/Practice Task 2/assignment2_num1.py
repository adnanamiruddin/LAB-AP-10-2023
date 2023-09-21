print ('pilih gender anda\n1.pria\n2.wanita')
gender = int (input ('= '))
Tinggi_badan = float (input('masukan tinggi badan anda (cm) : '))
berat = float (input('masukan berat badan (kg) : '))

tinggi = Tinggi_badan/100
bmi = (berat/(tinggi**2))
bmi_format = f'{bmi:.2f}'

if gender == 1 :
    if bmi <18:
        print (f'Anda tergolong Underweight dengan BMI {bmi_format}')
    elif bmi >= 18 and bmi <= 23.9:
        print (f'Anda tergolong Normal dengan BMI {bmi_format}')
    elif bmi >=24 and bmi <=26.9:
        print (f'Anda tergolong Overweight dengan BMI {bmi_format}')
    else :
        print (f'Anda tergolong Obeses dengan BNI {bmi_format}')
elif gender == 2 :
    if bmi <17:
        print (f'Anda tergolong Underweight dengan BMI {bmi_format}')
    elif bmi >=17 and bmi <=23.9:
        print (f'Anda tergolong Normal dengan BMI {bmi_format}')
    elif bmi >=24 and bmi <=27.9: 
        print (f'Anda tergolong Overweight dengan BMI {bmi_format}')
    else :
        print (f'Anda tergolong Obeses dengan BMI {bmi_format}')