def is_anagram(s1, s2):
    freq_s1 = [0] * 26
    freq_s2 = [0] * 26

    for char in s1:
        freq_s1[ord(char) - ord('a')] += 1

    for char in s2:
        freq_s2[ord(char) - ord('a')] += 1
    
    total_deletions = 0
    for i in range(26):
        total_deletions += abs(freq_s1[i] - freq_s2[i])

    return total_deletions

s1 = input("Masukkan string pertama: ")
s2 = input("Masukkan string kedua: ")

print("Jumlah minimum pengahpusan untuk membuat anagram:", is_anagram(s1, s2))

