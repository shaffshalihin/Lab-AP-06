import re 
 
def validasi_user(username): 
    pattern = r"^[A-Za-z0-9]{5,20}$" 
    return re.search(pattern, username) 
 
def validasi_email(email): 
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|co\.id)$" 
    return re.search(pattern, email) 
 
def validasi_pass(password): 
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]${8, }" 
    return re.search(pattern, password) 
 
username = input("Masukkan username: ") 
 
if validasi_user(username): 
    email = input("Masukkan email: ") 
 
    if validasi_email(email): 
        password = input("Masukkan password: ") 
 
        if validasi_pass(password): 
            print(f"\nRegistrasi berhasil! Halo {username}") 
        else: 
            print("\nPassword yang kamu input beresiko dihack. Registrasi gagal")
 
    else: 
        print("\nEmail yang kamu input tidak valdi. Registrasi gagal!") 
 
else: 
    print("\nInputan username tidak valid dalam sistem. Registrasi gagal!") 