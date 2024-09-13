penggunaan_data		= float(input("Masukkan penggunaan data bulanan (dalam GB): "))
waktu_penggunaan	= input("Apakah mayoritas penggunaan di luar jam sibuk (11 malam - 7 pagi)? (ya/tidak): ").strip().lower()
jenis_pengguna		= input("Masukkan jenis pengguna (personal/bisnis): ").strip().lower()

if penggunaan_data < 10:
    kategori_penggunaan = "ringan"
elif 10 <= penggunaan_data <= 50:
    kategori_penggunaan = "sedang"
else:
    kategori_penggunaan = "berat"

if kategori_penggunaan == "ringan" and waktu_penggunaan == "ya" and jenis_pengguna == "personal":
    paket = "Paket A, Penggunaan Ringan dengan mayoritas penggunaan di Luar Jam Sibuk oleh Pengguna Personal."
elif kategori_penggunaan == "sedang" and waktu_penggunaan == "tidak" and jenis_pengguna == "personal":
    paket = "Paket B, Penggunaan Sedang dengan mayoritas penggunaan di Jam Sibuk oleh Pengguna Personal."
elif kategori_penggunaan == "berat":
    if waktu_penggunaan == "tidak":
        paket = "Paket C, Penggunaan Berat oleh Pengguna Personal atau Bisnis yang mayoritas penggunaannya di Jam Sibuk."
    elif waktu_penggunaan == "ya" and jenis_pengguna == "bisnis":
        paket = "Paket D, Penggunaan Berat dengan mayoritas penggunaan di Luar Jam Sibuk oleh Pengguna Bisnis."
    else:
        paket = "Tidak ada paket yang cocok."

print(f"Paket yang sesuai: {paket}")
