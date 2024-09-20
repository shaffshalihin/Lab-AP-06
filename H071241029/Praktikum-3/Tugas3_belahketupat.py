belah_ketupat = int(input('Masukkan Jumlah Baris: '))
print()
  
for i in range(belah_ketupat):
  if i%2 == 1:
    continue
  else:
    print(' ' * (belah_ketupat - i) + '* ' * (i + 1))

if belah_ketupat%2 == 1:  
    for i in range(belah_ketupat):
        if i%2 == 0:
            continue
        else:
            print(' ' * (i + 2) + '* ' * (belah_ketupat - i - 1))
            
else:
    for i in range(belah_ketupat):
        if i%2 == 0:
            continue
        else:
            print(' ' * (i + 1) + '* ' * (belah_ketupat - i))