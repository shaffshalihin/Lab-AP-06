# soal 2 prt 3

import random

random_number = random.randint (1, 100)
jumlah_tebakan = 0
maksimal = 5

while jumlah_tebakan < maksimal:
    try:
        tebakan = int(input("Masukkan tebakan anda (0 untuk berhenti): "))

        if tebakan == 0:
            print("Permainan selesai")
            break 
        jumlah_tebakan += 1

        if tebakan < random_number:
            print("Angka terlalu kecil")
        elif tebakan > random_number:
            print("Angka terlalu besar")
        else:
            print("Tebakan benar!")
            break
    except ValueError:
        print()

if jumlah_tebakan == maksimal:
    print("Percobaan maksimal telah terpenuhi")
    print(f"Jawaban yang benar yaitu {random_number}")
    
    
