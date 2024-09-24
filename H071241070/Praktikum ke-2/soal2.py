usia = int(input("Masukkan usia Anda: "))
anggota = input("Apakah Anda anggota (ya/tidak): ")

if usia < 5:
    harga_dasar = 0
elif usia <= 12:
    harga_dasar = 50_000
elif usia <= 59:
    harga_dasar = 100_000
else:
    harga_dasar = 70_000

harga_dasar = harga_dasar * 0.8 if anggota == "ya" else harga_dasar
    
print("Harga tiket: Rp.", harga_dasar)
