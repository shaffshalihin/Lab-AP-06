Detik = int(input("Masukkan jumlah detik: "))
jam = Detik // 3600
menit = (Detik % 3600) // 60
detik = Detik % 60
print(f'{jam:02}:{menit:02}:{detik:02}')
