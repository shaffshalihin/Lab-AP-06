#prt 3 soal 5

populasi_a = int(input("Masukkan populasi awal serangga A: "))
populasi_b = int(input("Masukkan populasi awal serangga B: "))
hari = int(input("Masukkan jumlah hari: "))

for hari_ke in range(1, hari + 1):
    #hari ganjil
    if hari_ke % 2 != 0:
        populasi_a *= 1.30
        populasi_b *= 1.50
    else: #hari genap
        populasi_a *= 0.80
        populasi_b *= 0.60

    if hari_ke % 5 == 0:
        total_populasi = populasi_a + populasi_b
        populasi_a -= total_populasi * 0.10
        print(f"Hari {hari_ke}: Predator memakan 10% populasi")

    print(f"Hari {hari_ke}: Serangga A = {round(populasi_a)}, Serangga B = {round(populasi_b)}")

    