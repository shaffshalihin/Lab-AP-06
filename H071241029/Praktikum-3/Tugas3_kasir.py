total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan uang yang diberikan: "))

kembalian = uang_diberikan - total_harga

if kembalian < 0:
    print("Uang yang diberikan tidak cukup untuk membayar total harga.")
else:
    print(f"Kembalian: {kembalian}")
    
    pecahan_uang = [50000, 20000, 10000, 5000, 2000, 1000]
    print("Rincian kembalian:")
    
    for pecahan in pecahan_uang:
        jumlah_lembaran = kembalian // pecahan
        if jumlah_lembaran > 0:
            print(f"{jumlah_lembaran} lembar Rp {pecahan:,}")
            kembalian %= pecahan