def kalkulator():
    print("Selamat datang di Kalkulator Sederhana!")
    
    try:
        angka_pertama = float(input("Angka pertama: "))
        angka_kedua = float(input("Angka kedua: "))
        operasi = input("Operasi (+, -, *, /): ")
        
        if operasi == '+':
            hasil = angka_pertama + angka_kedua
            print("Hasil:", int(hasil))
        elif operasi == '-':
            hasil = angka_pertama - angka_kedua
            print("Hasil:", int(hasil))
        elif operasi == '*':
            hasil = angka_pertama * angka_kedua
            print("Hasil:", int(hasil))
        elif operasi == '/':
            if angka_kedua == 0:
                print("Pembagian dengan nol tidak diperbolehkan.")
            else:
                hasil = angka_pertama / angka_kedua
                print("Hasil:", int(hasil))
        else:
            print('Operasi tidak valid. Gunakan +, -, *, atau /.')
    except ValueError as e:
        print(f"Input tidak valid: {e}")

kalkulator()