import random as rn
angka_rahasia=rn.randint(1,100)
maksimal=5
for percobaan in range(maksimal):
    n=int(input(f"Masukan Tebakan anda (0 untuk berhenti) percobaan {percobaan+1}: "))  
    if n==0:
        print("Permainan dihentikan.")
        break
    if n==angka_rahasia:
        print(f"Selamat! Anda berhasil menebak angka yang benar. Angkanya adalah {angka_rahasia}")
        break
    elif n<angka_rahasia:
        print("Angka terlalu kecil.")
    elif n>angka_rahasia:
        print("Angka terlalu besar.")
    if percobaan==maksimal-1:
        print(f"Permainan berakhir. Angka yang benar adalah {angka_rahasia}")