total_harga = int(input("Masukkan total harga: "))
uang_pelanggan = int(input("Masukkan uang yang diberikan: "))
nominal_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]
kembalian = (uang_pelanggan - total_harga)

for nominal in nominal_uang :
    if kembalian >= nominal:
        nominal_uang = kembalian // nominal
        kembalian -= nominal_uang * nominal
        print(f"{nominal_uang} lembar Rp.{nominal}")