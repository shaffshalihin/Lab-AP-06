nilai_akhir = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))
tugas_tambahan = input("Apakah tugas tambahan selesai dengan baik? (ya/tidak): ")

if kehadiran < 75:
    hasil = "Tidak Lulus (Kehadiran kurang dari 75%)"
elif nilai_akhir >= 85:
    hasil = "Lulus dengan Predikat A"
elif 70 <= nilai_akhir < 85:
    hasil = "Lulus dengan Predikat B"
elif 60 <= nilai_akhir < 70:
    hasil = "Lulus dengan Predikat C"
else:
    if tugas_tambahan == 'ya' and kehadiran >= 75:
        hasil = "Lulus dengan Predikat C (karena tugas tambahan diselesaikan dengan baik)"
    else:
        hasil = "Tidak Lulus"

print(f"Status kelulusan: {hasil}")