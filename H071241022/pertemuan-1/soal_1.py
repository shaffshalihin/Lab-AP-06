saham = int(input("Masukkan harga saham kemarin: "))
harga_hari_ini = 105
persentase = (harga_hari_ini - saham)/saham * 100

rekomendasi = {
    persentase > 5: "Beli",
    -3 <= persentase < 5: "Tahan",
    persentase <= -3: "Jual"
}

print(f"Persentase = {persentase:.2f}%")
print(rekomendasi[True])