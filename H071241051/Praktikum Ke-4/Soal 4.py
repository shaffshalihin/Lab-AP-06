print("selamat datang di kalkulator sederhana")
def kalkulator():
    try:
        angka_pertama = int(input("Angka pertama = "))
    except ValueError :
        print("Input tidak valid, masukan angka")
    try:
        angka_kedua = int(input("Angka kedua = "))
    except ValueError :
        print("Input tidak valid, masukan angka")
    operator = input("Operasi (+, -, x, :) = ")   
    try:
        if operator == "x":
            print(f"hasil dari {angka_pertama} {operator} {angka_kedua} adalah {angka_pertama*angka_kedua}")
        elif operator == ":" :
            print(f"hasil dari {angka_pertama} {operator} {angka_kedua} adalah {angka_pertama/angka_kedua}")
        elif operator == "+" :
            print(f"hasil dari {angka_pertama} {operator} {angka_kedua} adalah {angka_pertama+angka_kedua}")
        elif operator == "-" :
            print(f"hasil dari {angka_pertama} {operator} {angka_kedua} adalah {angka_pertama-angka_kedua}")
    except:
        print("pembagian tak terdefinisi")
kalkulator()