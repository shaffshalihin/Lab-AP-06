print("Konversi detik ke jam")
hitung_detik = int(input("Masukkan jumlah detik: "))
hours = hitung_detik // 3600
minutes = (hitung_detik % 3600) // 60
seconds = hitung_detik % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")