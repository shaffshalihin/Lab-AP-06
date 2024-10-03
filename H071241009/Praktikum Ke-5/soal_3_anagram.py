def hapus(str1, str2):

    freq1 = {}
    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    penghapusan = 0
    for char in freq1:
        if char in str2:
            penghapusan += max(0, freq1[char] - str2.count(char))
        else:
            penghapusan += freq1[char]

    return penghapusan

str1 = input("Masukkan string pertama: ")
str2 = input("Masukkan string kedua: ")
print(f"Jumlah minimum penghapusan untuk membuat anagram: {hapus(str1, str2)}")