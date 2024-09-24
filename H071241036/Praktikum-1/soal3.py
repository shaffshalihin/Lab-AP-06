print("Konversi detik ke jam")
Detik = int(input("Masukkan jumlah detik : "))

Jam = (Detik // 3600)
Menit = (Detik - (Jam * 3600))//60
Detik = (Detik - (Jam * 3600) - (Menit * 60))

print("%02d : %02d : %02d" % (Jam, Menit, Detik))
print(type(Jam))