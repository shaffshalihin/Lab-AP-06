import random
angka = random.randint(1, 100)
makscoba = 5
for i in range(makscoba):
    try:
        tebak = int(input("Masukkan tebakan Anda (ketik 0 untuk berhenti): "))
        if tebak == 0:
            print("Anda memilih untuk berhenti")
            break
        if tebak < angka:
            print("Angka terlalu kecil")
        elif tebak > angka:
            print("Angka terlalu besar")
        else:
            print(f"Selamat! Anda menebak angka dengan benar. Angka rahasianya adalah {angka}") 
    except ValueError:
        print("Masukkan Angka di atas 0 di bawah 100")
if i == makscoba-1:
    print(f"Anda kehabisan percobaan. Angka rahasianya adalah {angka}")