detik = int(input('masukkan jumlah detik:'))

jam = detik//3600
menit = (detik%3600)//60
sisa_detik = detik%60

print(f'{jam:02d}:{menit:02d}:{sisa_detik:02d}')