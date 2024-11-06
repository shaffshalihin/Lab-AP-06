# import os
# os.system("CLS")

def penghapusan_minimum():
    # Buat dictionary untuk menyimpan frekuensi huruf dalam setiap string
   
    frekuensi_s1 = {}
    frekuensi_s2 = {}

    s1 = input("Masukkan string pertama: ").lower()
    s2 = input("Masukkan string kedua: ").lower()

    # Hitung frekuensi huruf dalam setiap string
    for karakter in s1:
        if karakter.isalpha():  # abaikan simbol
            if karakter in frekuensi_s1:
                frekuensi_s1[karakter] += 1
            else:
                frekuensi_s1[karakter] = 1

    for karakter in s2:
        if karakter.isalpha():  # abaikan simbol
            if karakter in frekuensi_s2:
                frekuensi_s2[karakter] += 1
            else:
                frekuensi_s2[karakter] = 1

    # Hitung jumlah minimum penghapusan karakter yang diperlukan
    penghapusan = 0
    for karakter in frekuensi_s1:
        if karakter in frekuensi_s2:
            penghapusan += abs(frekuensi_s1[karakter] - frekuensi_s2[karakter])
        else:
            penghapusan += frekuensi_s1[karakter]

    for karakter in frekuensi_s2:
        if karakter not in frekuensi_s1:
            penghapusan += frekuensi_s2[karakter]

    print("Jumlah minimum penghapusan untuk membuat anagram:", penghapusan)      


penghapusan_minimum()

