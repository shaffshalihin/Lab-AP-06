def hitung_langkah(n):
    langkah = 0
    while n != 1:
        if n <= 0:
            return -1 # Input tidak valid
        elif n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        print(n)
        langkah += 1
    return langkah

try:
    n = float(input("Masukkan angka: "))
    jumlah_langkah = hitung_langkah(n)
    if jumlah_langkah == -1:
        print("Input tidak valid (harus bilangan bulat positif)")
    else:
        print("Jumlah langkah:", jumlah_langkah)
except ValueError:
    print("Input tidak valid (harus bilangan bulat)")