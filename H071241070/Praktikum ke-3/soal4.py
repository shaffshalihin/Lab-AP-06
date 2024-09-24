total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan uang yang diberikan: "))

kembalian = uang_diberikan - total_harga
print("Kembalian: Rp", kembalian)
print("Rincian kembalian:")

pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
if uang_diberikan < total_harga :
    print(f"Uang anda kurang {abs(kembalian)}")
else :
    for pecahan_uang in pecahan:
        jumlah_pecahan = kembalian // pecahan_uang
        if jumlah_pecahan > 0:
            print(f"{jumlah_pecahan} lembar Rp {pecahan_uang:,}")
            kembalian %= pecahan_uang
            print(kembalian)