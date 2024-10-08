def hitung_frekuensi(kalimat):
    frekuensi = {}
    for char in kalimat:
        if char in frekuensi:
            frekuensi[char] += 1
        else:
            frekuensi[char] = 1
    return frekuensi

def minimum_hapus_untuk_anagram(str1, str2):
    frekuensi_str1 = hitung_frekuensi(str1)
    frekuensi_str2 = hitung_frekuensi(str2)
    total_hapus = 0

    for char in frekuensi_str1:
        if char in frekuensi_str2:
            total_hapus += abs(frekuensi_str1[char] - frekuensi_str2[char])
        else:
            total_hapus += frekuensi_str1[char]
    
    for char in frekuensi_str2:
        if char not in frekuensi_str1:
            total_hapus += frekuensi_str2[char]

    return total_hapus

str1 = input("Masukkan string pertama: ").lower()
str2 = input("Masukkan string kedua: ").lower()
str1 = ''.join(filter(str.isalpha, str1))
str2 = ''.join(filter(str.isalpha, str2))

print("Jumlah minimum penghapusan untuk membuat anagram:", minimum_hapus_untuk_anagram(str1, str2))