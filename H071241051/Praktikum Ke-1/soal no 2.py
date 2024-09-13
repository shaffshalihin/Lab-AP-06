kalimat = input("Masukkan kalimat: ")
karakter = input("Masukkan karakter yang ingin dicari: ")
hasil = (karakter in kalimat)
pesan = (
    "Karakter merupakan bagian dari Kalimat" * hasil + 
    "Karakter tidak ditemukan dalam Kalimat" * (not hasil))
print(pesan)
