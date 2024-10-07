penggunaan_data = float(input("Masukkan penggunaan data per bulan (dalam GB): "))
waktu_penggunaan = input("Apakah mayoritas penggunaan terjadi di jam sibuk (on-peak) atau luar jam sibuk (off-peak)? (on/off)): ")
jenis_pengguna = input("Apakah Anda pengguna Personal atau Bisnis? (personal/bisnis): ")

if penggunaan_data < 10:
    if waktu_penggunaan == 'off' and jenis_pengguna == 'personal':
        paket = "Paket A"
    else:
        paket = "Tidak ada paket yang cocok"
elif 10 <= penggunaan_data <= 50:
    if waktu_penggunaan == 'on' and jenis_pengguna == 'personal':
        paket = "Paket B"
    else:
        paket = "Tidak ada paket yang cocok"
elif penggunaan_data > 50:
    if waktu_penggunaan == 'on':
        if jenis_pengguna == 'personal' or jenis_pengguna == 'bisnis':
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
    elif waktu_penggunaan == 'off' and jenis_pengguna == 'bisnis':
        paket = "Paket D"
    else:
        paket = "Tidak ada paket yang cocok"
else:
    paket = "Tidak ada paket yang cocok"

print(f"Paket yang cocok untuk Anda: {paket}")