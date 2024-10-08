def cetak_semua_substring(kalimat):
    panjang = len(kalimat)
    
    for panjang_substr in range(1, panjang + 1):
        for i in range(panjang - panjang_substr + 1):
            print(kalimat[i:i + panjang_substr])

input_kalimat = input("Input your string: ").upper()

print("=======================")
cetak_semua_substring(input_kalimat)