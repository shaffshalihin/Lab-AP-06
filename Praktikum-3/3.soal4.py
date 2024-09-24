# Pecahan uang yang tersedia
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

# Input dari pengguna
total_harga = int(input("Masukkan total harga: "))
uang_diberikan = int(input("Masukkan jumlah uang yang diberikan: "))

# Menghitung kembalian
kembalian = uang_diberikan - total_harga

if kembalian < 0:
    print("uang tidak cukup")
else:
    print(f"Kembalian: {kembalian}")

    
if kembalian > 0:
    print("Rincian pecahan uang kembalian:")
    for pecahan in pecahan_uang:
        jumlah_lembar = kembalian // pecahan
        if jumlah_lembar > 0:
            print(f"Pecahan {pecahan}: {jumlah_lembar} lembar")
        kembalian = kembalian % pecahan
else:
    print("Tidak ada kembalian.")