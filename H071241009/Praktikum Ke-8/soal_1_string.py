import re

pattern = r'^[A-Za-z02468]{40}[13579\s]{5}$'
string = input("Masukkan string: ")
result = re.match(pattern, string)

if result:
    print("True")
else:
    print("False")
    print("String tersebut memiliki panjang tepat 45 karakter.")
    print("40 karakter pertama harus terdiri dari huruf uppercase atau lowercase atau digit bernilai genap.")
    print("5 karakter terakhir terdiri dari digit bernilai ganjil atau whitespace character.")