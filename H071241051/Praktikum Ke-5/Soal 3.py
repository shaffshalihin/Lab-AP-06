str1 = input("Masukan String Pertama = ")
str2 = input("Masukan String Kedua = ")
def anagram(str1, str2):
    frekuensi = {}
    for karakter in str1:
        if karakter in frekuensi:
            frekuensi[karakter] += 1
        else:
            frekuensi[karakter] = 1 
    penghapusan = 0
    for karakter in frekuensi:
        if karakter in str2:
            penghapusan += max(0, frekuensi[karakter] - str2.count(karakter))
        else:
            penghapusan += frekuensi[karakter] 
    return penghapusan
print(f"Jumlah karakter yang perlu dihapus: {anagram(str1, str2)}")
