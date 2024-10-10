# prt 4 soal 3

def main():
    # Meminta input dari pengguna
    try:
        n = int(input("Masukkan angka: "))
        if n <= 0:
            raise ValueError("Input tidak valid.")
    except ValueError:
        print("Input tidak Valid")
        return

    langkah = 0  # Menghitung jumlah langkah

    while n != 1:
        if n % 2 == 0:  # Bilangan genap
            n //= 2
        else:  # Bilangan ganjil
            n = n * 3 + 1
        
        langkah += 1  # Menambah langkah setiap iterasi
        print(f"{n:.1f}")

    print(f"Jumlah langkah: {langkah}")

main()
