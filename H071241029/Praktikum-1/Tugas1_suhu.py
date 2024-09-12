# program konversi suhu
print("# Program Konversi Suhu #")

celcius = float(input("Masukkan Suhu dalam Celcius : "))

kelvin = float(celcius + 273.15)
reamur = int(celcius * (4/5))
fahrenheit = int((9/5 * celcius) + 32)

print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Kelvin adalah : {kelvin:.02f}K")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Reamur adalah : {reamur}R")
print(f"Hasil konversi dari suhu {celcius} derajat Celcius ke Fahrenheit adalah : {fahrenheit}F")