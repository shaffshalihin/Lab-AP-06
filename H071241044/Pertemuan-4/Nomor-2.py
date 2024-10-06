total_jarak = 0
ada_bahaya = False

while True:
	try:
		langkah = int(input("Masukkan langkah (meter) atau 0 untuk selesai: "))
		if langkah == 0:
			break
		elif langkah < 0:
			print("Input tidak valid. Masukkan bilangan bulat positif.")
			continue
		total_jarak += langkah
		if langkah > 20:
			ada_bahaya = True
	except ValueError:
		print("Input tidak valid. Masukkan bilangan bulat.")
		continue
print(f"Total jarak: {total_jarak} meter")
if ada_bahaya:
	print("Ada bahaya: Ya")
	print("Tidak aman untuk menggali harta karun. Coba lagi!")
elif total_jarak == 50:
	print("Ada bahaya: Tidak")
	print("Aman! Kamu tepat menemukan harta karun dan menang!")
else:
	print("Tidak menemukan harta karun. Coba lagi!")