#soal 1 prt 3

jumlah_baris = int(input("Masukkan jumlah baris: "))

for i in range(0, jumlah_baris):
    for j in range(0, jumlah_baris - i - 1):
        print(" ", end="")
    for j in range(0, i + 1):
        print("* ", end="")
    print()

for i in range(0, jumlah_baris-1):
    for j in range(0,i +1):
        print(" ", end="")
    for j in range(0, jumlah_baris - i -1):
        print("* ", end="")
    print()