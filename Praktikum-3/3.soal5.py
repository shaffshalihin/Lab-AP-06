populasi_A = int(input("Masukkan populasi awal Serangga A: "))
populasi_B = int(input("Masukkan populasi awal Serangga B: "))
N = int(input("Masukkan jumlah hari: "))

for hari in range(1, N + 1):
    if hari % 2 == 1:
        populasi_A += int(populasi_A * 0.3) 
        populasi_B += int(populasi_B * 0.5)
    else:
        populasi_A -= int(populasi_A * 0.2)
        populasi_B -= int(populasi_B * 0.4)

    if hari % 5 == 0:
        populasi_A -= int(populasi_A * 0.1)
        populasi_B -= int(populasi_B * 0.1)

    print(f"Hari {hari}: Populasi A = {populasi_A}, Populasi B = {populasi_B}")

print(f"Setelah {N} hari:")
print(f"Populasi Serangga A: {populasi_A}")
print(f"Populasi Serangga B: {populasi_B}")