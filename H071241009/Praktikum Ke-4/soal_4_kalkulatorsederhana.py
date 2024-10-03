def kalkulator_sederhana():
    """Fungsi untuk melakukan perhitungan sederhana."""

    while True:
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            operator = input("Masukkan operasi (+, -, *, /): ")

            if operator == "+":
                hasil = angka1 + angka2
            elif operator == "-":
                hasil = angka1 - angka2
            elif operator == "*":
                hasil = angka1 * angka2
            elif operator == "/":
                while angka2 == 0:
                    print("Pembagian dengan nol tidak diperbolehkan. Masukkan angka kedua yang berbeda:")
                    angka2 = float(input("Masukkan angka kedua: "))
                hasil = angka1 / angka2
            else:
                print("Operasi tidak valid. Gunakan +, -, *, atau /.")
                continue

            print("Hasil:", hasil)
            break

        except ValueError as e:
            print(f"Input tidak valid: {e}")

kalkulator_sederhana()