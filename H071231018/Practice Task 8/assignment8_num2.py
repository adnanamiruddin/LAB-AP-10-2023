import re

IPv4 = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(\d|\d{2}|1\d{2}|2[1-4]\d|25[1-5])$"
IPv6 = r"^(([A-z0-9]?[A-z0-9]?[A-z0-9]?[A-z0-9]?)\:){7}([A-z0-9]?[A-z0-9]?[A-z0-9]?[A-z0-9]?)$"
jumlahInput = int(input("Berapa kali input? "))
list = [] 
for i in range(jumlahInput):
    j = input("Masukkan IP : ") 
    list.append(j)
for cek in list:
    if re.search(IPv4, cek):
        print("IPv4")
    elif re.search(IPv6, cek):
        print("IPv6")
    elif len(cek) >= 500:
        print("lebih dari 500 karakter")
    else:
        print("Bukan IP Address")

        
# def IPv4(check):
#     pattern = r"^((\d|\d{2}|1\d{2}|2[1-4]\d|25[1-5])\.){3}(\d|\d{2}|1\d{2}|2[1-4]\d|25[1-5])$"
#     return re.search(pattern, check)

# def IPv6(check):
#     pattern = r"^([\da-f]{1,4}:){7}[\da-f]{1,4}[\da-f]{1,4}$"
#     return re.search(pattern, check)

# perulangan = int(input("Berapa kali Anda ingin menginput? : "))

# var = []
# for i in range(perulangan):
#     var.append(input(f"Masukkan input ke {i + 1} : "))

# for STRING in var:
#     if IPv4(STRING):
#         print("IPv4")
#     elif IPv6(STRING):
#         print("IPv6")
#     else:
#         print("Bukan IP Adress")