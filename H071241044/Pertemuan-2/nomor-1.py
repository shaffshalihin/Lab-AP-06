a = float(input("Masukkan panjang sisi pertama (a): "))
b = float(input("Masukkan panjang sisi kedua (b): "))
c = float(input("Masukkan panjang sisi ketiga (c): "))

if a <= 0 or b <= 0 or c <= 0:
    print("Panjang sisi tidak boleh nol atau negatif.")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Sisi-sisi ini tidak dapat membentuk segitiga yang valid.")
else:
    if a == b == c:
        print("Segitiga Sama Sisi: Semua sisi memiliki panjang yang sama.")
    elif a == b or b == c or a == c:
        print("Segitiga Sama Kaki: Dua sisi memiliki panjang yang sama.")
    else:
        print("Segitiga Sembarang: Semua sisi memiliki panjang yang berbeda.")
