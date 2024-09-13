#Program Segitiga

sisi1 = int(input("Masukkan panjang sisi pertama: "))
sisi2 = int(input("Masukkan panjang sisi kedua: "))
sisi3 = int(input("Masukkan panjang sisi ketiga: "))

if sisi1 + sisi2 <= sisi3 or sisi1 + sisi3 <= sisi2 or sisi2 + sisi3 <= sisi1 or sisi1 == sisi2 == sisi3 == 0:
    print("Tidak dapat membentuk segitiga yang valid")
elif sisi1 == sisi2 == sisi3:
    print("Segitiga Sama Sisi")
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print("Segitiga Sama Kaki")
else:
    print("Segitiga Sembarang")

