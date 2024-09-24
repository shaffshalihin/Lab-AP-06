nilai_akhir		= float(input("Masukkan nilai akhir mahasiswa (0-100): "))
kehadiran		= float(input("Masukkan persentase kehadiran mahasiswa (0-100): "))
tugas_tambahan	= float(input("Masukkan nilai rata-rata tugas tambahan (0-100): "))

if kehadiran < 75:
    status = "Tidak Lulus: Kehadiran kurang dari 75%."
elif nilai_akhir >= 85:
    status = "Lulus dengan Predikat A."
elif nilai_akhir >= 70:
    status = "Lulus dengan Predikat B."
elif nilai_akhir >= 60:
    status = "Lulus dengan Predikat C."
else:
    status = "Lulus dengan Predikat C." if tugas_tambahan >= 70 else "Tidak Lulus."

print(f"Status Kelulusan: {status}")