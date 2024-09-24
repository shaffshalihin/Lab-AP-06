#prt 3 soal 4

uang_dibayar = int(input("Masukkan uang yang diberikan: "))
total_harga = int(input("Masukkan uang yang diterima: "))

kembalian = uang_dibayar - total_harga

pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

jumlah_lembar = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(pecahan)):
    jumlah_lembar[i] = int(kembalian // pecahan[i])
    kembalian = kembalian % pecahan[i]

for i in range(len(pecahan)):
    if jumlah_lembar[i] > 0:
        print(f"{jumlah_lembar[i]} lembar uang Rp {pecahan[i]}")
