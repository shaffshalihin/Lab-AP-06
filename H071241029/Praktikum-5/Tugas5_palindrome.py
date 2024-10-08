def palindrome(kalimat):
    kalimat_bersih = kalimat.replace(" ", "").lower()
    
    if kalimat_bersih == kalimat_bersih[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

input_kalimat = input("Masukkan sebuah kalimat: ")

palindrome(input_kalimat)