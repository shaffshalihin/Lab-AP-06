#Program Kelulusan

nilai = int(input("Masukkan Nilai Akhir: "))
kehadiran = int(input("Masukkan Persentase Kehadiran: "))

if 85 <= nilai <= 100:
    print("Lulus dengan Predikat A")
elif 70 <= nilai <= 84:
    print("Lulus dengan Predikat B")
elif 60 <= nilai <= 69:
    print("Lulus dengan Predikat C")
elif nilai < 60:
    tugas_tambahan = int(input("Masukkan Nilai Tugas Tambahan: "))
    if tugas_tambahan > 70 and kehadiran >= 75:
        print("Lulus dengan Predikat C")
else:
    print("Tidak Lulus")


