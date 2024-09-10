#tugas praktikum 1
HargaKemarin = float(input("masukkan harga saham kemarin: "))
HargaSekarang = 105.0

PerubahanPersen = ((HargaSekarang - HargaKemarin) / HargaKemarin)*100

rekomendasi_list = ["Jual", "Tahan", "Beli"]

index = (PerubahanPersen > 5) * 2 + (-3 <= PerubahanPersen <= 5) * 1

print(f"perubahan harga saham: {PerubahanPersen}%")
print(f"rekomendasi {rekomendasi_list[True]}")