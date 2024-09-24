nilai = int(input("Masukkan nilai akhir: "))
kehadiran = int(input("Masukkan persentase kehadiran: "))
tugas_tambahan = input("Apakah semua tugas tambahan selesai dengan nilai di atas 70? (ya/tidak): ")

if nilai >= 85 and kehadiran >= 75 :
  print("Lulus dengan Predikat A")
elif nilai >= 70 and kehadiran >= 75:
  print("Lulus dengan Predikat B")
elif (nilai >= 60 and kehadiran >= 75) or (nilai < 60 and tugas_tambahan == "ya" and kehadiran >= 75):
  print("Lulus dengan Predikat C")
else:
  print("Tidak Lulus")
