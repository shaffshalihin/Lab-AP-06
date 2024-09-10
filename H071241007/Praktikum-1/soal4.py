celcius = float(input("Masukkan suhu dalam Celcius: "))

# Mengonversi ke Kelvin, Reamur, dan Fahrenheit
kelvin = celcius + 273.15
reamur = celcius * 4 / 5
fahrenheit = celcius * 9 / 5 + 32

# Menampilkan hasil konversi
print(f"Suhu dalam Kelvin: {kelvin:.2f} K")
print(f"Suhu dalam Reamur: {reamur} °R")
print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f} °F")