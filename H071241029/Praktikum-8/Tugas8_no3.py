import re

# Fungsi untuk validasi username
def validasi_username(username):
    pattern = r'^[A-Za-z0-9]{5,20}$'
    return re.match(pattern, username) is not None

# Fungsi untuk validasi email
def validasi_email(email):
    pattern = r'^[a-z0-9]+[0-9]*@[a-z]+\.(com|co\.id)$'
    return re.match(pattern, email) is not None

# Fungsi untuk validasi password
def validasi_password(password):
    panjang_cukup = len(password) >= 8
    huruf_kecil = re.search(r'[a-z]', password)
    huruf_besar = re.search(r'[A-Z]', password)
    angka = re.search(r'\d', password)
    simbol_anekaragam = re.search(r'[^A-Za-z0-9]', password)
    return panjang_cukup and huruf_kecil and huruf_besar and angka and not simbol_anekaragam

# Fungsi utama untuk registrasi
def registrasi():
    username = input("Masukkan username: ")
    if not validasi_username(username):
        print("Username tidak valid! Registrasi gagal!")
        return
    
    email = input("Masukkan email: ")
    if not validasi_email(email):
        print("Email yang kamu input tidak valid, Registrasi gagal!")
        return

    password = input("Masukkan password: ")
    if not validasi_password(password):
        print("Password yang kamu input tidak mencapai 8 inputan, Registrasi gagal!")
        return

    print(f"Registrasi berhasil! Selamat datang, {username}")

registrasi()