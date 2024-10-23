import os
os.system("CLS")

def cetak_substring():
    kalimat = input("Input your string: ")
    print("=========================")

    # Cetak substring dengan panjang 1 hingga panjang maksimum string
    for panjang in range(1, len(kalimat) + 1):
        for i in range(len(kalimat) - panjang + 1):
            substring = kalimat[i:i + panjang]
            print(substring)
# Cetak semua substring yang mungkin dari string tersebut
cetak_substring()