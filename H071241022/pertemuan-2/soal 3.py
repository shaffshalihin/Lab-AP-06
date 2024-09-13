#soal 3 prt 2

nilai = int(input("Masukkan nilai akhir: "))
kehadiran = int(input("Masukkan persentase kehadiran: "))

if nilai <= 60 and kehadiran >= 75: #tidak works 
    print("Lulus dengan predikat C")

elif kehadiran >= 75:
    if nilai >= 85 and nilai <= 100:
        print("Lulus dengan predikat A")
    elif nilai >= 70 and nilai <= 84:
        print("Lulus dengan predikat B")
    elif nilai >= 60 and nilai <= 69:
        print("Lulus dengan predikat C")
    else :
        print("Tidak lulus")

else :
    print("Tidak lulus")

