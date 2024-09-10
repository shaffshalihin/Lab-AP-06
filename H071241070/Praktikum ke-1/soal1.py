harga_sekarang = 105.0
harga_kemarin = float(input ( "masukkan harga kemarin:"))

persen = ((harga_sekarang - harga_kemarin) / harga_kemarin) * 100
rekomendasi = ((persen > 5)* "beli") + (( -3 <= persen <= 5)* "tahan" ) + (( persen <-3 )* "jual")

print(f"perubahan persentase : {persen :.2f}%")
print(f"rekomendasi investasi : {rekomendasi}")




