import re

s = []
N = int(input())
for i in range(N):
    i = input() 
    s.append(i)

# IPv4 pattern
patternipv4 = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$' 
    
# IPv6 pattern
patternipv6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'


for x in s:
    if re.search(patternipv4, x):
        print("IPv4")
    elif re.search(patternipv6, x):
        print("IPv6")
    else:
        print("Bukan IP Address")
    