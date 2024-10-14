def anagram(string1, string2):
    penghapusan = 0

    for karakter in set(string1 + string2):  
        penghapusan += abs(string1.count(karakter) - string2.count(karakter))

    return penghapusan

str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")

hasil = anagram(str1, str2)

print(f"Jumlah minimum penghapusan untuk membuat anagram: {hasil}")