total_harga = int(input("Masukkan total harga: "))
uang_tunai = int(input("Masukkan jumlah yang diberikan: "))

kembalian = uang_tunai - total_harga

if kembalian < 0:
    print("Uang yang diberikan kurang Rp", total_harga - uang_tunai )
elif kembalian == 0:
    print("Uang yang diberikan pas. Tidak ada kembalian.")

pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
for nilai in pecahan:
    jumlah_pecahan = kembalian//nilai
    if jumlah_pecahan > 0:
        print(jumlah_pecahan, "lembar Rp", nilai)
        kembalian %= nilai