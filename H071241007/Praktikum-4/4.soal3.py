def rumus(n):
    langkah = 0
    while n > 1:
        print(n)  # Menampilkan nilai n pada setiap langkah
        if n % 2 == 0:
            n //= 2  # Jika n genap, bagi 2 (menggunakan pembagian bulat)
        else:
            n = n * 3 + 1  # Jika n ganjil, kalikan 3 lalu tambah 1
        langkah += 1
    # print(n)
    return langkah

def main():
    try:
        n = float(input("Masukkan bilangan bulat positif: "))
        if n <= 0:
            print("Input tidak Valid")
        else:
            langkah = rumus(n)
            print(f"Jumlah langkah: {langkah}")
    except ValueError:
        print("Input tidak Valid")

# Jalankan program
main()
