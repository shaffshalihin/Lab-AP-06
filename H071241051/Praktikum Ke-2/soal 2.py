usia = int(input('Masukan Usia = '))
anggota = input('Apakah anda anggota (ya/tidak) = ')
harga_tiket = (
    'Gratis' if usia < 5 else 
    50000 * 0.8 if 5 <= usia <= 12 and anggota == 'ya' else 50000 if 5 <= usia <= 12 else
    100000 * 0.8 if 13 <= usia <= 59 and anggota == 'ya' else 100000 if 13 <= usia <= 59 else
    600000 * 0.8 if usia >= 60 and anggota == 'ya' else 600000
)
print('Harga tiket:', harga_tiket)
