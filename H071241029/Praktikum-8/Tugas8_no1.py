import re

def validate_string(s):
    # Memastikan panjang string 45 karakter
    if len(s) != 45:
        return False
    # Regular Expression untuk memvalidasi string sesuai syarat
    pattern = r"^[a-zA-Z02468]{40}[13579\s]{5}$"
    # Mengecek string sesuai dengan pola
    return bool(re.match(pattern, s))

# Input dari pengguna
input_string = input("Masukkan string: ")

if validate_string(input_string):
    print("True")
else:
    print("False")