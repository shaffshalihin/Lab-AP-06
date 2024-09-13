# Input jumlah detik dari pengguna
total_detik				= int(input("Masukkan jumlah detik: "))

# Menghitung jumlah jam, menit, dan detik
jam						= total_detik // 3600  # 1 jam = 3600 detik
menit					= (total_detik % 3600) // 60  # Sisa detik setelah diambil jam dibagi 60 untuk menit
detik					= total_detik % 60  # Sisa detik setelah diambil jam dan menit

# Menampilkan hasil
print(f"{jam:02}:{menit:02}:{detik:02}")