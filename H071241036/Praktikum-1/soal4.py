print("Konversi Suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit")
Celcius = int(input("Masukkan Suhu dalam Celcius : "))

Kelvin = Celcius + 273
Reamur = 4/5 * Celcius
Fahrenheit = (9/5 * Celcius) + 32

print("Hasil konversi dari suhu %d ke Kelvin adalah : %d" % (Celcius, Kelvin))
print("Hasil konversi dari suhu %d ke Reamur adalah : %d" % (Celcius, Reamur))
print("Hasil konversi dari suhu %d ke Fahrenheit adalah : %d" % (Celcius, Fahrenheit))