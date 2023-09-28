while True:
    derajat = float(input())
    if 0 <= derajat < 360:
        break
    else:
        print("End of file")

#1 hari = 86400 detik = 360 derajat
#jadi 86400/360 = 240 detik/derajat
detik = int(derajat * 240)

jam = detik // 3600 + 6
if jam >= 24:
    jam = jam % 24
menit = detik % 3600 // 60
detik = detik % 60

if 6 <= jam < 11:
    print("Selamat pagi")
elif 11 <= jam < 15:
    print("Selamat siang")
elif 15 <= jam < 18:
    print("Selamat sore")
else:
    print("Selamat malam")

print(f"{jam:02}:{menit:02}:{detik:02}")