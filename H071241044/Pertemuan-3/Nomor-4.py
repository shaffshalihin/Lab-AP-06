barang		= int(input('Masukkan Harga Barang: '))
pecahans	= [100000, 50000, 20000, 10000, 5000, 2000, 1000]
def hitungLembar(kembalian, lembaran):
	hit	= kembalian // lembaran
	print(f"{hit} lembar uang Rp.{lembaran}") if hit != 0 else ''
	return hit
while True:
	bayar = int(input('Masukkan Pembayaran: '))
	if bayar < barang:
		print(f"Tabe kurang Rp.{abs(bayar-barang)} uang ta!\n\n")
	elif bayar == barang:
		print("Uang pas dih, makasih sudah berbelanja")
		break
	else:
		kembalian = bayar - barang
		for pecahan in pecahans:
			kembalian = kembalian - pecahan * hitungLembar(kembalian, pecahan)
		break