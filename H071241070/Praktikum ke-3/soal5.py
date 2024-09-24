populasi_A = int(input("Masukkan populasi awal seragga A :"))
populasi_B = int(input("Masukkan populasi awal seragga B :"))
jumlah_hari = int(input("Masukkan jumlah hari :"))

# Loop untuk setiap hari
for hari in range(1, jumlah_hari + 1):
    print(f"Hari {hari}:")
    if hari % 5 == 0:
        # Predator memakan 10% populasi
        populasi_A *= 0.9
        populasi_B *= 0.9
    elif hari % 2 == 1:
        # Hari ganjil: Pertumbuhan
        populasi_A *= 1.3
        populasi_B *= 1.5
    else:
        # Hari genap: Penurunan
        populasi_A *= 0.8
        populasi_B *= 0.6
    populasi_A_int = int(populasi_A)
    populasi_B_int = int(populasi_B)
    print(f"Serangga A = {populasi_A_int:}, Serangga B = {populasi_B_int:}")