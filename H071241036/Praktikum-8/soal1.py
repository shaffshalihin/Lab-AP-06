import re

def validasi_syarat(s):
    if len(s) != 45:
        return False

    first_40 = s[:40]
    if not re.match(r'^[A-Za-z0-9]{40}$', first_40):
        return False
    
    if not all(char.isdigit() and int(char) % 2 == 0 for char in first_40 if char.isdigit()):
        return False

    last_5 = s[40:]
    if not re.match(r'^[13579\s]{5}$', last_5):
        return False

    return True

input_string = input("Masukkan string: ")
print("True" if validasi_syarat(input_string) else "False")
