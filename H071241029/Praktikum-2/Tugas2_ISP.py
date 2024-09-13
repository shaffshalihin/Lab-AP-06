# Program paket data

penggunaan_data = int(input("Masukkan jumlah data yang digunakan (GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (Off-Peak) atau di jam sibuk (Peak): ")
jenis_pengguna = input("Apakah anda pengguna Personal atau Bisnis?: ")

if penggunaan_data < 10:
    if waktu_penggunaan == 'Off-Peak' or 'off-peak' and jenis_pengguna == 'Personal' or 'personal':
        paket = "Paket A"
    else:
        paket = "Tidak ada paket yang cocok"
elif 10 <= penggunaan_data <= 50:
    if waktu_penggunaan == 'Peak' or 'peak' and jenis_pengguna == 'Personal' or 'personal':
        paket = "Paket B"
    else:
        paket = "Tidak ada paket yang cocok"
elif penggunaan_data > 50:
    if waktu_penggunaan == 'Peak' or 'peak':
        paket = "Paket C"
    elif waktu_penggunaan == 'Off-Peak' or 'off-peak' and jenis_pengguna == 'Bisnis' or 'bisnis':
        paket = "Paket D"
    else:
        paket = "Tidak ada paket yang cocok"
else:
    paket = "Tidak ada paket yang cocok"

print(f"Paket yang sesuai: {paket}")