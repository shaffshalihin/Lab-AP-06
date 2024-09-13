# Program harga tiket

usia = int(input("Masukkan usia: "))
anggota = input("Apakah Anda anggota (ya/tidak)? ")

# Menentukan harga tiket berdasarkan usia
harga = 0 if usia < 5 else 50000 if 5 <= usia <= 12 else 100000 if 13 <= usia <= 59 else 70000 if usia >= 60 else None

# Menghitung harga setelah diskon jika pengguna adalah anggota
harga = harga * 0.8 if anggota == 'ya' and harga is not None else harga

if harga is not None:
    print(f"Harga tiket yang harus dibayar: Rp{harga:.0f}")
else:
    print("Usia tidak valid.")