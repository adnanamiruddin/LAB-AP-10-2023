gender = int(input("pilih gender anda\n1. pria\n2. wanita\n= "))
tinggi = float(input("masukkan tinggi badan (cm) : "))
berat = float(input("masukkan berat badan (kg) : "))

BMI = berat / ((tinggi / 100)** 2)
BMI_format = f"{BMI:.2f}"

if gender == 1:
    if BMI <18:
        print(f"anda tergolong underweight dengan BMI {BMI_format}")
    elif 18 >= BMI < 23.9:
        print(f"anda tergolong normal dengan BMI {BMI_format}")
    elif 24 >= BMI < 26.9:
        print(f"anda tergolong overweight dengan BMI {BMI_format}")
    elif BMI >=27:
        print(f"anda tergolong obesitas dengan BMI {BMI_format}")

elif gender == 2:
    if BMI <17:
        print(f"anda tergolong underweight dengan BMI {BMI_format}")
    elif 17 >= BMI <23.9:
        print(f"anda tergolong normal dengan BMI {BMI_format}")
    elif 24 >= BMI < 27.9:
        print(f"anda tergolong overweight dengan BMI {BMI_format}")
    elif BMI >= 28:
        print(f"anda tergolong obesitas dengan BMI {BMI_format}")
else:
    print("print tidak valid")