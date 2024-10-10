#prt 4 soal 4

def main():
    print("Selamat datang di kalkulator sederhana!")

    try:
        angka_pertama = int(input("Angka pertama: "))
    except ValueError:
        print("Input tidak valid.")
        return

    try:
        angka_kedua = int(input("Angka kedua: "))
    except ValueError:
        print("Input tidak valid.")
        return

    operasi = input("Operasi (+, -, *, /): ")

    if operasi not in ['+', '-', '*', '/']:
        print("Operasi tidak valid. Gunakan +, -, * atau /")
        return

    if operasi == '/' and angka_kedua == 0:
        print("Pembagian dengan nol tidak diperbolehkan.")
        return

    if operasi == '+':
        hasil = angka_pertama + angka_kedua
    elif operasi == '-':
        hasil = angka_pertama - angka_kedua
    elif operasi == '*':
        hasil = angka_pertama * angka_kedua
    elif operasi == '/':
        hasil = angka_pertama / angka_kedua

    print(f"Hasil: {hasil}")

main()
