tinggi_badan = float (input ("Masukkan tinggi badan (cm): "))
berat_badan  = float (input ("Masukkan berat badan (kg): "))
gender       = input ("jenis kelamin: \n1. Pria \n2. Wanita \n Masukkan pilihan : ")
tinggi_m     = float (tinggi_badan/100)
bmi          = float (f"{berat_badan / (tinggi_m)**2:.2f}")

match gender:
    case "1":
        if bmi < 18 :
            print(f"Anda tergolong Underweight dengan BMI {bmi}")
        elif 18 <= bmi < 23.9:
            print(f"Anda tergolong Normal dengan BMI {bmi}")
        elif 24 <= bmi <26.9 :
            print(f"Anda tergolong Overweight dengan BMI {bmi}")
        else:
            print(f"Anda tergolong Obese dengan BMI {bmi} ")
    case "2":
        if bmi < 17:
            print(f"Anda tergolong Underweight dengan BMI {bmi} ")
        elif 17 <= bmi < 23.9:
            print(f"Anda tergolong Normal dengan BMI {bmi}")
        elif 24 <= bmi < 26.9:
            print(f"Anda tergolong Overweight dengan BMI {bmi}")
        else:
            print(f"Anda tergolong Obese dengan BMI {bmi} ")
