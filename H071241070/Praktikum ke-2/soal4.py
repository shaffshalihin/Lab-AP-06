penggunaan_data = float(input("Masukkan penggunaan data dalam GB: "))
waktu_penggunaan = input("Masukkan waktu penggunaan (peak/Off-Peak): ")
jenis_pengguna = input("Masukkan jenis pengguna (Personal/Bisnis): ")

if penggunaan_data < 10:
  penggunaan = "Ringan"
elif penggunaan_data <= 50 and penggunaan_data >= 10:
  penggunaan = "Sedang"
else:
  penggunaan = "Berat"

if waktu_penggunaan == "Off-Peak":
  waktu = "Luar Jam Sibuk"
else:
  waktu = "Jam Sibuk"

if penggunaan == "Ringan" and waktu == "Luar Jam Sibuk" and jenis_pengguna == "personal":
  print("Rekomendasi: Paket A")
elif penggunaan == "Sedang" and waktu == "Jam Sibuk" and jenis_pengguna == "personal":
  print("Rekomendasi: Paket B")
elif penggunaan == "Berat" and (jenis_pengguna == "Personal" or jenis_pengguna == "Bisnis") and waktu == "Jam Sibuk":
  print("Rekomendasi: Paket C")
elif penggunaan == "Berat" and waktu == "Luar Jam Sibuk" and jenis_pengguna == "Bisnis":
  print("Rekomendasi: Paket D")
else:
  print("Tidak ada paket yang cocok")