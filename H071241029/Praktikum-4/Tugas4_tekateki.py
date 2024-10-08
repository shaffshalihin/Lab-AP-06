def hitung_langkah(n):
    langkah = 0
    
    while n != 1:
        if n % 2 == 0:
            n /= 2    # n = n / 2
        else:
            n = 3 * n + 1
        print(float(n))
        langkah += 1  # langkah = langkah + 1
    return langkah

def main():
    try:
        n = float(input("Masukan angka: "))
        
        if n <= 0:
            print("Input tidak Valid")
        else:
            langkah = hitung_langkah(n)
            print("Jumlah langkah:", langkah)

    except ValueError:
        print("Input tidak Valid")

main()
