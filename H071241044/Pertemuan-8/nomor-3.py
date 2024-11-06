import re

def is_valid_username(username):
    pattern = r"^[A-Za-z0-9]{5,20}$"
    return bool(re.match(pattern, username))

def is_valid_email(email):
    pattern = r"^[a-z0-9]+@[a-z]+\.+(com|co\.id|unhas\.ac\.id)$"
    return bool(re.match(pattern, email))

def is_valid_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$"
    return bool(re.match(pattern, password))

username = input("Masukkan username: ")
if not is_valid_username(username):
    print("username Tidak Valid")
    exit()

email = input("Masukkan email: ")
if not is_valid_email(email):
    print("email tidak valid")
    exit()

password = input("Masukkan password: ")
if not is_valid_password(password):
    print("password tidak valid")
    exit()
