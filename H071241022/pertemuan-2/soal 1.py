#Tugas pertemuan 2

#NOMOR SATU

pertama = int(input("Masukkan panjang sisi pertama: "))
kedua = int(input("Masukkan panjang sisi kedua: "))
ketiga = int(input("Masukkan panjang sisi ketiga: "))

if pertama == kedua == ketiga:
    print("Segitiga sama sisi")
elif pertama == kedua or kedua == ketiga or pertama == ketiga:
    print("Segitiga sama kaki")
elif pertama != kedua and kedua != ketiga and pertama != ketiga:
    print("Segitiga sembarang")
else :
    print("Tidak dapat membentuk segitiga yang valid")

