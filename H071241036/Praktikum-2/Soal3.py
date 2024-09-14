nilai = int(input("Masukkan nilai akhir : "))
kehadiran = int(input("Masukkan persentase kehadiran : "))

if kehadiran < 75 :
    print("Tidak lulus")
elif 85 <= nilai <= 100 :
    print("Lulus dengan Predikat A")
elif 70 <= nilai <= 84 :
    print("Lulus dengan Predikat B")
elif 60 <= nilai <= 69 :
    print("lulus dengan Predikat C")
elif nilai < 60 :
    tugasTambahan = int(input("Nilai tugas tambahan : "))
    if tugasTambahan > 70 and kehadiran >= 75 :
        print("Lulus dengan Predikat C")
else :
    print("Tidak lulus")