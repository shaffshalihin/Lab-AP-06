populasi_awal_A = int(input("Masukkan populasi awal Serangga A: "))
populasi_awal_B = int(input("Masukkan populasi awal Serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

populasi_A = populasi_awal_A 
populasi_B = populasi_awal_B 

for hari in range(1, jumlah_hari + 1):
    if hari % 2 == 1:
      populasi_A = int(populasi_A + (populasi_A * 30/100))
      populasi_B = int(populasi_B + (populasi_B * 50/100))
    else:
      populasi_A = int(populasi_A - (populasi_A * 20/100))
      populasi_B = int(populasi_B - (populasi_B * 40/100))

    if hari % 5 == 0:
      populasi_A = int(populasi_A - (populasi_A * 10/100))
      populasi_B = int(populasi_B - (populasi_B * 10/100))
      print(f"Hari {hari}: Predator memakan 10% populasi.")
    print(f"Hari {hari}: Serangga A = {populasi_A}, Serangga B = {populasi_B}")