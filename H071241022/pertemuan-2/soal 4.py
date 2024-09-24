#soal 4 prt 2

data = int(input("Masukkan jumlah data yang digunakan (GB): "))
mayoritas = input("Apakah mayoritas penggunaan di luar jawa sibuk (off-peak) atau di jam sibuk (peak)?: ")
pengguna = input("Apakah anda pengguna personal atau bisnis?: ")

if data <= 10 and mayoritas == "off-peak" and pengguna == "personal":
    print("Paket yang sesuai: Paket A")
elif data >= 10 and data <= 50 and mayoritas == "peak" and pengguna == "personal":
    print("Paket yang sesuai: Paket B")
elif data >= 50 and mayoritas == "peak" and pengguna == "personal" or pengguna == "bisnis":
    print("Paket yang sesuai: Paket C")
elif data >= 50 and mayoritas == "off-peak" and pengguna == "bisnis":
    print("Paket yang sesuai: Paket D")
else :
    print("Tidak ada paket yang cocok")