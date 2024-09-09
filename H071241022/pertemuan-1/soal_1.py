harga_hari_ini = 105.0
harga_kemarin = float(input("Masukkan harga kemarin: "))

perubahan_persentase = ((harga_hari_ini - harga_kemarin) / harga_kemarin) * 100

while(perubahan_persentase > 5.0):
    rekomendasi = "beli"
    break;

while(perubahan_persentase <= 5.0 and perubahan_persentase >= -3.0):
    rekomendasi = "tahan"
    break;

while(perubahan_persentase < -3.0):
    rekomendasi = "jual"
    break;

print("Perubahan persentase harga saham:", perubahan_persentase, "%")
print("rekomendasi investasi:", rekomendasi)