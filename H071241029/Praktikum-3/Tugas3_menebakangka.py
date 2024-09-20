import random
angka_rahasia = random.randint(1, 100)
max_percobaan = 5

print("Anda memiliki maksimal 5 kali percobaan untuk menebak angka tersebut.")

for percobaan in range(1, max_percobaan + 1):
    try:
        tebakan = int(input(f"Percobaan {percobaan}: Masukkan angka tebakan Anda (0 untuk berhenti): "))

        if tebakan == 0:
            print("Permainan dihentikan oleh pemain.")
            break
        if tebakan == angka_rahasia:
            print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dengan benar.")
            break
        elif tebakan > angka_rahasia:
            print("Angka terlalu besar.")
        else:
            print("Angka terlalu kecil.")
    except ValueError:
        print("Masukkan angka yang valid.")
else:
    print(f"Maaf, Anda telah mencapai jumlah percobaan maksimal. Angka yang benar adalah {angka_rahasia}.")
