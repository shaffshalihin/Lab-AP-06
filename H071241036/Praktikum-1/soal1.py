hargaKemarin = float(input("Masukkan harga saham kemarin : "))
hargaSekarang = 105.0

perubahanPersen = ((hargaSekarang-hargaKemarin)/hargaKemarin)*100

rekomendasiInvestasi = ["Jual", "Tahan", "Beli"]
rekomendasi = rekomendasiInvestasi [(perubahanPersen >= -3) + (perubahanPersen > 5)]

print(f"Perubahan persentase harga saham : {perubahanPersen:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi}")
print(type(rekomendasi))