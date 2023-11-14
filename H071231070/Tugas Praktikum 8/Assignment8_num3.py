import re
username    = input("Masukkan Username : ")
pattern_usn = r"^[a-zA-Z0-9]{5,20}"
if re.fullmatch(pattern_usn, username):
    email       = input("Masukkan Email    : ")
    pattern_email = r"^[a-z]+([0-9]{2,})?@([a-z]+)(\.com|\.co\.id)"
    if re.fullmatch(pattern_email, email):
        password    = input("Masukkan Password : ")
        pattern_pw  = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
        if re.fullmatch(pattern_pw, password): 
            print(f"Registrasi Berhasil!, Selamat datang, {username}!")
        else:
            print("Password anda tidak valid")
    else:
        print("Email yang dimasukkan tidak valid!")
else:
    print("Username yang dimasukkan tidak valid!")