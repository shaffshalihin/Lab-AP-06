#pertemuan 2 soal 2

usia = int(input("Masukkan usia: "))
anggota = input("Apakah anda anggota(ya/tidak): ")

if usia < 5 :
    print("Gratis")
elif usia >= 5 and usia <= 12:
    print("harga tiket: Rp 40.000") if anggota == "ya" else print("harga tiket: Rp. 50.000")    
elif usia >= 13 and usia <= 59:
    print("harga tiket: Rp. 80.000") if anggota == "ya" else print("harga tiket: Rp. 100.000")
else :
    print("harga tiket: Rp 56.000") if anggota == "ya" else print("harga tiket: Rp. 70.000")