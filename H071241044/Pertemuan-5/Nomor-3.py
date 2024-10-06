def min_hapus_anagram(s1, s2):
    count1 = {i: s1.count(i) for i in s1}
    count2 = {i: s2.count(i) for i in s2}
    deletions = 0
    for char in count1:
        deletions += abs(count1[char] - count2[char]) if char in count2 else count1[char]
    for char in count2:
        deletions += count2[char] if char not in count1 else 0
    print(deletions)
min_hapus_anagram(input("Masukkan string pertama: "), input("Masukkan string kedua: "))