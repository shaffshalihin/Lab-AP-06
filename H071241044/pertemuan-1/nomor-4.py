# Input suhu dalam Celcius dari pengguna
suhu_celcius			= float(input("Masukkan suhu dalam Celcius: "))

# Menghitung konversi ke skala lain
suhu_kelvin				= suhu_celcius + 273.15			# Konversi ke Kelvin
suhu_reamur				= suhu_celcius * 0.8			# Konversi ke Reamur
suhu_fahrenheit			= (suhu_celcius * 1.8) + 32		# Konversi ke Fahrenheit

# Menampilkan hasil konversi
print(f"Suhu dalam Kelvin: {suhu_kelvin:.2f} K")
print(f"Suhu dalam Reamur: {suhu_reamur:.2f} °R")
print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit:.2f} °F")