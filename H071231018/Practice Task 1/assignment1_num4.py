# n=input("karakter= ")
# n=bool(n)

# print(f"{n}")
# print(f"huruf kapital= {n}")
# print(f"angka= {n}")

# char=input("karakter= ")

# if char is upper:
#     print(f'{char}true ')
# elif char is digit:
#     print(f'{char}true ')
# else:
#     print(f'{char} false')

# char=bool(input("Masukkan huruf= "))

# if char is upper:
#     print(char)
# elif char is lower:
#     print(char)
# else:
#     print(char)

char=input("karakter = ")

kapital=char.isupper()
print(f"Huruf Kapital? {kapital}")
huruf_kecil=char.islower()
print(f"Huruf Kecil? {huruf_kecil}")
angka=char.isdigit()
print(f"Angka? {angka}")
