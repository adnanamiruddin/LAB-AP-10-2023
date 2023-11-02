import re
string = input("Masukan string: ")
pattern = r"[A-Za-z2468]{40}[13579\s]{5}"

rum = re.match(pattern,string)
if rum and len(string) == 45 :
    print (True)
else :
    print(False)