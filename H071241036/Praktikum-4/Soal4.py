print("selamat datang di kalkulator sederhana!")

def kalkulator():
    a = float(input("angka pertama: "))
    b = float(input("angka kedua: "))
    operasi = input("operasi (+, -, *, /): ")
    
    if operasi == '+':
        return a + b
    elif operasi == '-':
        return a - b
    elif operasi == '*':
        return a * b
    elif operasi == '/':
        if b != 0:
            return a / b
        else:
            print("Error: Pembagian dengan nol")
            return None
    else:
        print("Operasi tidak valid")
        return None

hasil = kalkulator()

print(f"hasil: {hasil:.0f}")