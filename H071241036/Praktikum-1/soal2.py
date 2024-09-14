karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan Kalimat : ")

output = karakter in kalimat

pesan = ["tidak ditemukan dalam", "merupakan bagian dari"][output]

hasil = f"{karakter} {pesan} '{kalimat}'"
print(hasil)