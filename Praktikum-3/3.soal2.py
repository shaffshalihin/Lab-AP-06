import random

# Komputer memilih angka acak antara 1 hingga 100
angka_rahasia = random.randint(1, 100)
percobaan = 0
maks_percobaan = 5

print("Selamat datang Boskuuu di permainan tebak angka")
print("Kamuu memiliki maksimal 5 kali percobaan untuk menebak angka antara 1 hingga 100.")
print("Ketik '0' kalau mau berhenti.\n")

while percobaan < maks_percobaan:
    # Meminta input tebakan dari pemain
    tebakan = int(input("Masukkan tebakan Anda (0 untuk berhenti): "))
    
    # Jika pemain memasukkan '0', permainan berhenti
    if tebakan == 0:
        print("Permainan dihentikan.")
        break

    percobaan += 1
    
    # Memeriksa apakah tebakan benar atau tidak
    if tebakan == angka_rahasia:
        print("Selamat! Anda menebak angka dengan benar.")
        break
    elif tebakan > angka_rahasia:
        print("Angka terlalu besar.")
    else:
        print("Angka terlalu kecil.")
    
    # Jika percobaan sudah habis dan tebakan masih salah
    if percobaan == maks_percobaan:
        print(f"\nMaaf, Anda telah menggunakan semua percobaan. Angka rahasia adalah {angka_rahasia}.")
