kuota = input(input("Masukkan jumlah data yang digunakan (GB): "))
jam_sibuk = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ")
jenis_pengguna = input("Apakah Anda pengguna Personal atau Bisnis? ").lower()

if jenis_pengguna == "bisnis":
  if kuota > 50 and jam_sibuk == "peak":
    print("Paket yang sesuai: Paket C")
  elif kuota > 50:
    print("Paket yang sesuai: Paket D")
  else:
    print("Tidak ada paket cocok")
else:
  if kuota > 30 and jam_sibuk == "peak":
    print("Paket yang sesuai: Paket B")
  elif kuota <= 30:
    print("Paket yang sesuai: Paket A")
  else:
    print("Tidak ada paket cocok")