def jumlah_penghapusan_minimum(string1, string2):
    jumlah_hapus = 0
    
    for huruf in "abcdefghijklmnopqrstuvwxyz":
        count1 = string1.count(huruf)
        count2 = string2.count(huruf)
        
        jumlah_hapus += abs(count1 - count2)
    
    return jumlah_hapus

string1 = "abab"
string2 = "aaaa"

print(f"Jumlah minimum penghapusan untuk membuat anagram: {jumlah_penghapusan_minimum(string1, string2)}")

