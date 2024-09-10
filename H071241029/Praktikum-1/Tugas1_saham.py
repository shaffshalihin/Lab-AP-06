def hitung_persen(harga_kemarin, harga_hari_ini):
    return ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

rekomendasi_investasi = [
    (lambda x: x > 5, "Beli"),
    (lambda x: -3 <= x <= 5, "Tahan"),
    (lambda x: x < -3, "Jual")
]

harga_kemarin = float(input("Masukkan harga saham kemarin: "))

harga_hari_ini = 105.0

persentase_perubahan = hitung_persen(harga_kemarin, harga_hari_ini)

rekomendasi = next(
    rekomendasi for kondisi, rekomendasi in rekomendasi_investasi if kondisi(persentase_perubahan)
)

print(f"Persentase perubahan harga: {persentase_perubahan:.2f}%")
print(f"Rekomendasi investasi: {rekomendasi}")