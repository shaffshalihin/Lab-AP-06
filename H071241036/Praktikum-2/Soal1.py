a = int(input("Masukkan panjang sisi pertama : "))
b = int(input("Masukkan panjang sisi kedua : "))
c = int(input("Masukkan panjang sisi ketiga : "))

if a + b > c and b + c > a and a + c > b :
    if a == b == c :
        print("Segitiga sama sisi")
    elif a + b or b + c or a + c :
        print("Segitiga sama kaki")
    else :
        print("Segitiga sembarang")
else :
    print("Segitiga tidak valid")
     