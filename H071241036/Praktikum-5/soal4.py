def semua_substring(teks):
    panjang = len(teks)
    
    for panjang_substring in range(1, panjang + 1):
        for i in range(panjang - panjang_substring + 1):
            substring = teks[i:i + panjang_substring]
            print(substring) 

input_teks = input("Input your string: ")
semua_substring(input_teks)
