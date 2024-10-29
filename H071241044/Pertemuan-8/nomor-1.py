import re

def validate_string(s):
    pattern = r'^[a-zA-Z02468]{0,40}[13579\s]{5}$'
    return bool(re.match(pattern, s))

s = input("Masukkan string: ")
print("True" if validate_string(s) else "False")
