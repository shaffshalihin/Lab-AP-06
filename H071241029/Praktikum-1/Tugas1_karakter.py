# program karakter dalam kalimat
print("# Program Karakter dalam Kalimat #")

karakter = input("Masukkan Karakter : ")
kalimat = input("Masukkan Kalimat : ")

cek_karakter = (karakter in kalimat) and f"{karakter} ditemukan dalam \"{kalimat}\"" or f"{karakter} tidak ditemukan dalam \"{kalimat}\""

print(cek_karakter)