try:
    def kalkulator(a, b, operator):
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b
        else:
            return print("tidak ada operator yang cocok, masukkan operator yang valid")


    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    operator = input("masukkan operator (+, -, *, /): ")

    print(f"hasilnya adalah: {kalkulator(a, b, operator)}")

except ZeroDivisionError:
    print("pembagian dengan nol tidak bisa dilakukan")
except ValueError:
    print("Masukkan angka bukan string")