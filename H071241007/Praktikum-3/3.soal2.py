import random

angka_rahasia = random.randint(1, 100)
percobaan = 0

print("Selamat datang Boskuuu di permainan tebak angka")
print("Kamuu memiliki maksimal 5 kali percobaan untuk menebak angka antara 1 hingga 100.")
print("Ketik '0' kalau mau berhenti.\n")

while percobaan < 5:
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    
    if tebakan == 0:
        print("Permainan dihentikan.")
        break

    percobaan += 1
    
    if tebakan == angka_rahasia:
        print("Selamat! Anda menebak angka dengan benar.")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")
    
print(f"\nMaaf, Anda telah menggunakan semua percobaan. Angka rahasia adalah {angka_rahasia}.")
