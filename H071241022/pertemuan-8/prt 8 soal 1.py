import re

def ValidasiString(string):
    pattern = r"^(?=.*[a-zA-Z02468])[a-zA-Z0-9\s]{40}[13579\s]{5}$"
    return re.search(pattern, string)

input = input("Masukkan string (45 karakter): ")

if ValidasiString (input):
    print("True")
else:
    print("False")