data = int(input("Masukkan data yang digunakan (GB) : "))
waktuPenggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ")
pengguna = input("Apakah Anda pengguna Personal atau Bisnis? ")

if data < 10 and waktuPenggunaan == "off-peak" and pengguna == "Personal" :
    print("Paket yang sesuai : Paket A")
elif 10 <= data <= 50 and waktuPenggunaan == "peak" and pengguna == "Personal" :
    print("Paket yang sesuai : Paket B")
elif data > 50 and pengguna == "Personal" or "Bisnis" and waktuPenggunaan == "peak":
    print("Paket yang sesuai : Paket C")
elif data > 50 and waktuPenggunaan == "off-peak" and pengguna == "Bisnis" :
    print("Paket yang sesuai : Paket D")
else :
    print("Tidak ada paket yang cocok")