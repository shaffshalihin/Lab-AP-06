populasi_awal_a = int(input("Masukkan populasi awal Serangga A: "))
populasi_awal_b = int(input("Masukkan populasi awal Serangga B: "))
hari = int(input("Masukkan jumlah hari: "))

for hari in range(1, hari + 1):
    if hari % 2 == 1:
        populasi_awal_a = int(populasi_awal_a * 1.3)
        populasi_awal_b = int(populasi_awal_b * 1.5)
    else:
        populasi_awal_a = int(populasi_awal_a * 0.8)
        populasi_awal_b = int(populasi_awal_b * 0.6)
    if hari % 5 == 0:
        populasi_awal_a = int(populasi_awal_a * 0.9)
        populasi_awal_b = int(populasi_awal_b * 0.9)
        print(f"Hari {hari}: Predator memakan 10% populasi.")
    
    print(f"Hari {hari}: Serangga A = {populasi_awal_a:.0f}, Serangga B = {populasi_awal_b:.0f}")