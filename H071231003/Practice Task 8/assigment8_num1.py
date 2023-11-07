import re

inputan = input("Masukkan String : ")
pattern = r"[A-Za-z2468]{40}[13579\s]{5}"
status = re.match(pattern, inputan)


if status and len(inputan) == 45:
    print(True)
else:
    print(False) 