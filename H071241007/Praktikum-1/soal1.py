#tugas praktikum 1
HargaKemarin = float(input("masukkan harga saham kemarin: "))
HargaSekarang = 105.0

PerubahanPersen = ((HargaSekarang - HargaKemarin) / HargaKemarin)*100

rekomendasi = {
    PerubahanPersen > 5 : "Beli",
    -3 <= PerubahanPersen <= 5 : "Tahan",
    PerubahanPersen < -3 : "Jual"
}
print(f"perubahan harga saham: {PerubahanPersen}%")
print(f"rekomendasi {rekomendasi[True]}")