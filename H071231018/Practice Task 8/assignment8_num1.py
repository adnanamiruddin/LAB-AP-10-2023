import re

sentence = input("Masukkan String : ")
pattern = r"[A-Za-z2468]{40}[13579\s]{5}"
status = re.search(pattern, sentence)

if status:
    if len(sentence) <= 45:
        print(True)
    else:
        print(False)
else:
    print(False)