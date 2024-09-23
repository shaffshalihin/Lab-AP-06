# Menerima input dari pengguna
a = int(input("Masukkan panjang sisi pertama: "))
b = int(input("Masukkan panjang sisi kedua: "))
c = int(input("Masukkan panjang sisi ketiga: "))

# Memeriksa validitas sisi segitiga
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Sisi-sisi tersebut tidak membentuk segitiga yang valid.")
else:
    # Menentukan jenis segitiga
    if a == b == c:
        print("Segitiga Sama Sisi")
    elif a == b or b == c or a == c:
        print("Segitiga Sama Kaki")
    else:
        print("Segitiga Sembarang")