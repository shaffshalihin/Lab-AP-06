#Program Paket Internet

jumlah_data = int(input("Masukkan jumlah data yang Anda gunakan: "))
penggunaan = input("Apakah mayoritas penggunaan di luar jam sibuk (off-peak) atau di jam sibuk (peak)? ")
personal_bisnis = input("Apakah Anda pengguna Personal atau Bisnis? ")

if jumlah_data < 10 and penggunaan == "off-peak" and personal_bisnis == "personal":
    print("Paket yang Sesuai: Paket A")
elif 10 <= jumlah_data <= 50 and penggunaan == "peak" and personal_bisnis == "personal":
    print("Paket yang Sesuai: Paket B")
elif jumlah_data > 50 and penggunaan == "peak" and personal_bisnis == "personal" == "bisnis":
    print("Paket yang Sesuai: Paket C")
elif jumlah_data > 50 and penggunaan == "off-peak" and personal_bisnis == "bisnis":
    print("Paket yang Sesuai: Paket D")
else:
    print("Tidak Ada Paket yang Cocok")