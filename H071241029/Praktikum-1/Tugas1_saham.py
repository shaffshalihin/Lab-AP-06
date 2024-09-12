# Program Saham
print("# Program Saham #")

saham = float(input("Masukkan Harga Saham Kemarin : "))
saham_hari_ini = 105
rekomendasi = ["Jual", "Tahan", "Beli"]

persentase = (saham_hari_ini - saham)/saham * 100
hasil = rekomendasi[(persentase > -3) + (persentase > 5)]

print(f"Perubahan Persentase Harga Saham = {persentase:.2f}%")
print(f"Rekomendasi Investasi: {hasil}")