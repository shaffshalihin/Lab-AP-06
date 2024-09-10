print("Konversi suhu dari Celsius ke Kelvin, Reamur dan Fahrenheit")
celcius = int(input("Masukkan suhu dalam Celcius: "))

kelvin = celcius + 273.15
reamur = celcius * 4/5
fahrenheit = (celcius * 4/5)

print(f"Suhu dalam kelvin: {kelvin:.2f} K")
print(f"suhu dalam reamur: {reamur:.2f} R")
print(f"suhu dalam fahrenheit: {fahrenheit:.2f} F")