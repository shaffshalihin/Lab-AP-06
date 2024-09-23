# Input dari pengguna
karakter				= input("Masukkan karakter yang ingin dicari: ")
kalimat					= input("Masukkan kalimat: ")

# Menggunakan operator `in` untuk memeriksa keberadaan karakter dan memilih pesan
pesan					= ["tidak ditemukan dalam", "merupakan bagian dari"][karakter in kalimat]

# Menampilkan pesan
print(f"'{karakter}' {pesan} '{kalimat}'")