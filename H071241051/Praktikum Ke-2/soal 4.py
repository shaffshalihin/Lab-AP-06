jumlah_data = int(input('Pemakaian data = '))
rentang_waktu = input('Masukkan rentang waktu pemakaian data (misalnya 10-14) = ')
tipe_pengguna = input('Jenis penggunaan = ')
pukul_awal, pukul_akhir = map(int, rentang_waktu.split('-'))

if jumlah_data < 10:
    Penggunaan_Data = 'ringan'
elif 10 <= jumlah_data <= 50:
    Penggunaan_Data = 'sedang'
else:
    Penggunaan_Data = 'berat'

if  pukul_awal >= 7 and pukul_akhir <= 23:
    waktu = 'peak'
elif pukul_awal >23  and pukul_akhir <7:
    waktu = 'off-peak'

if tipe_pengguna in ['medsos', 'browsing', 'streaming']:
    pengunaan = 'personal'
elif tipe_pengguna in ['conference', 'hosting website', 'cloud services']:
    pengunaan = 'bisnis'
else:
    pengunaan = 'lainnya'

if Penggunaan_Data == 'ringan' and waktu == 'off-peak' and pengunaan == 'personal':
    print('Paket yang sesuai: Paket A')
elif Penggunaan_Data == 'sedang' and waktu == 'peak' and pengunaan == 'personal':
    print('Paket yang sesuai: Paket B')
elif Penggunaan_Data == 'berat' and waktu == 'peak' and (pengunaan == 'personal' or pengunaan == 'bisnis'):
    print('Paket yang sesuai: Paket C')
elif Penggunaan_Data == 'sedang' and waktu == 'off-peak' and pengunaan == 'bisnis':
    print('Paket yang sesuai: Paket D')
else:
    print('Tidak ada paket yang cocok')
