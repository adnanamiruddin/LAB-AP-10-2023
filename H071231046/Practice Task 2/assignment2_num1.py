gender = input("Pilih Gender Anda\n1. Pria\n2. Wanita\n= ")
tinggi = float(input("Masukkan tinggi badan (cm) = "))
berat = float(input("Masukkan berat badan (kg) = "))

#Rumus cm k m
tinggi2 = tinggi/100
#Rumus calculator BMI
BMI = tinggi2/((berat)**2)
BMI_format = f"{BMI:.2f}"
#kondisi
if gender == "1" :
    if BMI<18:
        print(f"Anda tergolong Normal dengan BMI {BMI_format}")
    elif BMI>= 18 and BMI<=23.9:
        print(f"Anda tergolong Normal dengan BMI {BMI_format}")
    elif BMI>=24 and BMI<=26.9:
        print(f"Anda tergolong Overweight dengan BMI {BMI_format}")
    elif BMI>=27:
        print(f"Anda tergolong Obese dengan BMI {BMI_format}");
elif gender == "2" :
    if BMI<17:
        print("Anda tergolong Underweight dengan BMI {BMI_format}")
    elif BMI>=17 and BMI<=23.9:
        print(f"Anda tergolong Normal dengan BMI {BMI_format}")
    elif BMI>=24 and BMI<=27.9:
        print(f"Anda tergolong Overweight dengan BMI {BMI_format}")
    elif BMI>=28:
        print(f"Anda tergolong Obese dengan BMI {BMI_format}")
else:
    print("Input tidak valid")
    exit()



