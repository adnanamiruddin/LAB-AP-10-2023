def palindrom(kata):
    kata = kata.lower()
    if kata == kata[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"

kata = input("Palindrom : ")
print(palindrom(kata))