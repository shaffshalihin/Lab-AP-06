usia = int(input("Masukkan Usia : "))
anggota = input("Apakah Anda anggota? (ya/tidak): ")

if usia < 5 :
    harga = 0
elif 5 <= usia <= 12 :
    harga = 50000
elif 13 <= usia <= 59 :
    harga = 100000
else :
    harga = 70000

diskon = harga - (harga * 20/100)

hargaTiket = diskon if anggota == "ya" else harga
print(f"Harga Tiket : Rp {hargaTiket:.0f}")