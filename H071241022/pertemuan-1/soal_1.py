saham_kemarin = int(input("harga saham kemarin: "))

saham_sekarang = int(105)
persentase = ((saham_sekarang - saham_kemarin)/ saham_kemarin )*100

print(f"Perubahan persentase harga saham: {persentase:.2f}%")

beli = persentase > 5 
tahan = 5>=persentase>=-3
jual = persentase<=-3

rekomendasi = "Beli"*beli + "Tahan"*tahan + "Jual"*jual
print(f"Rekomendasi Investasi: {rekomendasi}")
