harga_total=int(input("Masukan harga total : "))
bayar=int(input("Masukan uang yang diberikan : "))
kembalian=bayar-harga_total
uang=[100000,50000,20000,10000,5000,2000,1000]
if kembalian==0:
    print("tidak ada kembalian")
for pecahan in uang:
    if kembalian>=pecahan:
        jumlah_lembar=kembalian//pecahan
        kembalian%=pecahan
        print(f"{jumlah_lembar} Lembar Rp{pecahan}")

            