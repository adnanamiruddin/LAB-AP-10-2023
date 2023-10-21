print("Pilih Gender Anda")
print("1. Pria")
print("2. Wanita")
gender = int(input("="))

tinggi = float(input("Masukkan tinggi badan (cm): ")) / 100
berat = float(input("Masukkan berat badan (kg): "))

bmi = berat / (tinggi * tinggi)


if gender == 1:
    if bmi < 18:
        golongan = "underweight"   
    elif 18 <= bmi < 24:
         golongan =  "normal"   
    elif 24 <= bmi < 27:
        golongan = "Overweight"
    else:
        golongan = "Obese"
    print(f"Anda tergolong {golongan} dengan BMI {bmi:.2f}.")
elif gender == 2:
    if bmi < 17:
         golongan = "underweigt"   
    elif 17 <= bmi < 24:
        golongan = "normal"   
    elif 24 <= bmi < 28:
        golongan = "overweight"
    else:
        golongan = "obese"
    
    print(f"Anda tergolong {golongan} dengan BMI {bmi:.2f}.")
else:
    print("Input tidak valid")