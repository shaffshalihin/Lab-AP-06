import random

angka_rahasia = random.randint(1, 100)
percobaan = 5
while percobaan > 0:
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    if tebakan == angka_rahasia :
        print("Selamat! Anda menebak angka dengan benar.")
        break
    elif tebakan == 0 :
        print()
        break
    elif tebakan > angka_rahasia :
        percobaan -= 1
        print("Angka terlalu besar.")
        print(f'Tersisa {percobaan} kesempatan lagi')
    elif tebakan < angka_rahasia :
        percobaan -= 1
        print("Angka terlalu kecil.")
        print(f'Tersisa {percobaan} kesempatan lagi')

#sisa cara untuk membatasi sampe 5 kali percobaan