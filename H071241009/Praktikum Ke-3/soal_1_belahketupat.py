baris_belah_ketupat = int(input("Masukkan Jumlah Baris: "))
print()
  
for i in range(baris_belah_ketupat):
    if i % 2 == 1:
        continue
    else:
        print(" " * (baris_belah_ketupat - i) + "* " * (i + 1))

if baris_belah_ketupat % 2 == 1:  
    for i in range(baris_belah_ketupat):
        if i % 2 == 0:
            continue
        else:
            print(" " * (i + 2) + "* " * (baris_belah_ketupat - i - 1))
else:
    for i in range(baris_belah_ketupat):
        if i % 2 == 0:
            continue
        else:
            print(" " * (i + 1) + "* " * (baris_belah_ketupat - i))