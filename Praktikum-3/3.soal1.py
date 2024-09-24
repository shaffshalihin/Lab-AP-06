import os
os.system('cls')

tinggi = int(input("Masukkan Jumlah Baris: "))

panjang = 1

while True:
    print(("*"*panjang).center(tinggi))
    panjang += 2
    if panjang > tinggi:
        break



while True:
    print(("*"*panjang).center(tinggi))
    panjang -= 2
    if panjang <= 0:
        break