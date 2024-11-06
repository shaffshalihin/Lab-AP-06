import re

def validate_string(cek):
    pola = r"^[a-zA-Z02468]{40}[13579\s]{5}$"
    if len(cek) == 45 and re.fullmatch(pola, cek):
        return "True"
    else:
        return "False"

sandi = input("masukkan string: ")
print(validate_string(sandi))
