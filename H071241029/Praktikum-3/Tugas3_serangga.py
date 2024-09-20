populasi_awal_A = int(input("Masukkan populasi awal Serangga A: "))
populasi_awal_B = int(input("Masukkan populasi awal Serangga B: "))
jumlah_hari = int(input("Masukkan jumlah hari: "))

populasiA = populasi_awal_A 
populasiB = populasi_awal_B 

for hari in range(1, jumlah_hari + 1):
    if hari % 2 == 1:
      populasiA = int(populasiA + (populasiA * 30/100))
      populasiB = int(populasiB + (populasiB * 50/100))
    else:
      populasiA = int(populasiA - (populasiA * 20/100))
      populasiB = int(populasiB - (populasiB * 40/100))

    if hari % 5 == 0:
      populasiA = int(populasiA - (populasiA * 10/100))
      populasiB = int(populasiB - (populasiB * 10/100))
      print(f"Hari {hari}: Predator memakan 10% populasi.")
    print(f"Hari {hari}: Serangga A = {populasiA:.0f}, Serangga B = {populasiB:.0f}")