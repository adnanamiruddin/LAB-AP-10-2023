print('konversi detik ke jam')

detik1 = int(input('masukan jumlah detik: '))

jam    = int(detik1 // 3600)
menit  = int((detik1-(jam*3600))//60)
detik  = int(detik1-(jam*3600)-(menit*60))

print (f'{jam:02d}:{menit:02d}:{detik:02d}')
