kemarin = float(input("Masukkan harga saham kemarin: "))
hari_ini = 105.0
perubahan_persen = ((hari_ini - kemarin) / kemarin) * 100
pesan = [
    "Jual",      
    "Tahan",     
    "Beli" ]
indeks = max(0, min(2, int((perubahan_persen > 5) + (perubahan_persen > -3))))
print(f"Perubahan persentase harga saham : {perubahan_persen:.2f}%")
print(f"Rekomendasi investasi: {pesan[indeks]}")



