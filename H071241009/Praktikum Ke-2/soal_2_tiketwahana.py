#Program Tiket Wahana

usia = int(input("Masukkan Usia: "))

if usia < 5:
    harga = 0
elif 5 <= usia <= 12:
    harga = 50000
elif 13 <= usia <= 59:
    harga = 100000
else:
    harga = 70000

keanggotaan = input("Apakah Anda Anggota? (ya/tidak): ")

diskon = harga - (harga * 20/100)

harga_tiket = diskon if keanggotaan == "ya" else harga

print(f'Harga Tiket: Rp{harga_tiket:.0f}')