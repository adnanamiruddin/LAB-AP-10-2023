def cek_palindrom(kata: str) -> str:
    kata = kata.lower()
    if kata == kata[::-1]:
        return "Palindrom"
    else:
        return "Bukan Palindrom"
    
print(cek_palindrom(input()))