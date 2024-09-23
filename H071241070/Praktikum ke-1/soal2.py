karakter = input("masukkan karakter")
kalimat = input("masukkan kalimat")

isi = (f'{karakter} merupakan karakter dalam "{kalimat}".' * (karakter in kalimat) + f'{karakter} tidak ditemukan dalam "{kalimat}".' * (karakter not in kalimat ))
print(isi)