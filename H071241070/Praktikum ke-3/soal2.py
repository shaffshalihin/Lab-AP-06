import random

angka_min = 1
angka_maks = 100
scrt_num = random.randint(angka_min,angka_maks)

percobaan = 0
while percobaan <5 :
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    if tebakan == 0 :
        print("Terima kasih sudah bermain!")
        break
    percobaan +=1
    if tebakan < scrt_num :
        print("Angka terlalu kecil.")
    elif tebakan > scrt_num :
        print("Angka terlalu besar.")
    else:
        print("Selamat! Anda menebak angka dengan benar.")
        break
if percobaan == 5 and tebakan != scrt_num :
    print(f"Anda kehabisan percobaan. Angka rahasianya adalah{scrt_num}.")


