# Meminta input jumlah detik dari pengguna
total_detik = int(input("Masukkan jumlah detik: "))

# Menghitung jumlah jam, menit, dan detik
jam = total_detik // 3600
sisa_detik = total_detik % 3600
menit = sisa_detik / 60
detik = sisa_detik % 60

# Menggunakan format untuk menampilkan dengan dua digit
waktu = f"{jam:02}:{menit}:{detik:02}"

# Output hasil
print("Waktu dalam format jam:menit:detik adalah:", waktu)