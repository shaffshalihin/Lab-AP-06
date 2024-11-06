import os
import datetime

# Fungsi untuk membuat folder jika belum ada
def buat_folder(nama_folder):
    if not os.path.exists(nama_folder):
        os.makedirs(nama_folder)

# Fungsi untuk menambah film
def tambah_film(judul):
    with open("daftar_film.txt", "a") as file:
        file.write(judul + "\n")
    print(f"Film '{judul}' berhasil ditambahkan.")

# Fungsi untuk menampilkan Daftar Tiket
def tampilkan_film():
    try:
        with open("daftar_film.txt", "r") as file:
            films = file.readlines()
        print("Daftar Film:")
        for i, film in enumerate(films, 1):
            print(f"{i}. {film.strip()}")
    except FileNotFoundError:
        print("Belum ada film yang ditambahkan.")

# Fungsi untuk menghapus film
def hapus_film(judul):
    films = []
    with open("daftar_film.txt", "r") as file:
        films = file.readlines()
    for film in films:
        if film.strip() == judul:
            films.remove(film)
            break
    else:
        print(f"Judul film dengan judul '{judul}' tidak ditemukan.")
    
    with open("daftar_film.txt", "w") as file:
        file.writelines(films)
    print(f"Film '{judul}' berhasil dihapus.")
# Fungsi untuk membeli tiket
def beli_tiket(judul_film):
    id_tiket = f"TICK{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
    with open("tiket.txt", "a") as file:
        file.write((f"""
+--------------------------------+
|          TIKET BIOSKOP         |
+--------------------------------+
| ID Tiket : {id_tiket}          |
| Film     : {judul_film}        |
| Tanggal  : {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}|
+-------------------------------+
|  Terima kasih telah membeli   |
|          tiket Anda!          |
+-------------------------------+
"""))
    with open(f"tiket/{id_tiket}.txt", "w") as file:
        file.write((f"""
+--------------------------------+
|          TIKET BIOSKOP         |
+--------------------------------+
| ID Tiket : {id_tiket}          |
| Film     : {judul_film}        |
| Tanggal  : {datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}|
+-------------------------------+
|  Terima kasih telah membeli   |
|          tiket Anda!          |
+-------------------------------+
"""))
    print(f"\nTiket untuk film '{judul_film}' berhasil dibeli. ID Tiket: {id_tiket}")
    return id_tiket
# Fungsi untuk menampilkan tiket
def tampilkan_tiket():
    try:
        tiket_folder = "tiket/"
        tiket_files = os.listdir(tiket_folder)
        print("Daftar Tiket:")
        for file in tiket_files:
            with open(tiket_folder + file, "r") as f:
                tiket = f.read()
                print(tiket)
    except FileNotFoundError:
        print("Belum ada tiket yang dibeli.")
def menu_daftar_tiket():
    while True:
        print("\n=== Daftar Tiket ===")
        print("1. Lihat Daftar Tiket")
        print("2. Lihat Detail Tiket")
        print("3. Hapus Tiket")
        print("4. Kembali")
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == '1':
            try:
                tiket_folder = "tiket/"
                tiket_files = os.listdir(tiket_folder)
                print("Daftar Tiket:")
                for i , file in enumerate(tiket_files, start=1):
                    print(f"{i}.{file.replace(".txt", "")}")
            except FileNotFoundError:
                print("Belum ada tiket yang dibeli.")
        elif pilihan == '2':
            tiket_folder = "tiket/"
            tiket_files = os.listdir(tiket_folder)
            print("\n===Detail Tiket===")
            for i, file in enumerate(tiket_files, start=1):
                print(f"{i}. {file.replace('.txt', '')}")
            print("0. Kembali")
            while True:
                pilihan_tiket = input("\nPilih nomor tiket yang ingin dilihat (atau 0 untuk kembali) : ")
                if pilihan_tiket == '0':
                    print("\nKembali ke Daftar Tiket")
                    break
                else:
                    try:
                        tiket_file = tiket_files[int(pilihan_tiket) - 1]
                        with open(tiket_folder + tiket_file, "r") as f:
                            tiket_detail = f.read()
                            print(f"\nDetail Tiket '{tiket_file.replace('.txt', '')}':")
                            print(tiket_detail)
                            break
                    except (IndexError, ValueError):
                        print("Pilihan tidak valid. Silakan coba lagi.")
        elif pilihan == '3': 
            tiket_folder = "tiket/"
            tiket_files = os.listdir(tiket_folder)
            print("\n===Hapus Tiket===")
            for i, file in enumerate(tiket_files, start=1):
                print(f"{i}. {file.replace('.txt', '')}")
            print("0. Kembali")
            while True:
                pilihan_hapus = input("\nPilih nomor tiket yang ingin dihapus (atau 0 untuk kembali) : ")
                if pilihan_hapus == '0':
                    print("\nKembali ke Daftar Tiket")
                    break
                else:
                    try:
                        tiket_file = tiket_files[int(pilihan_hapus) - 1]
                        os.remove(tiket_folder + tiket_file)
                        print(f"\nTiket '{tiket_file.replace('.txt', '')}' telah dihapus.")
                        
                        break
                    except (IndexError, ValueError):
                        print("Pilihan tidak valid. Silakan coba lagi.")   
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")
# Menu utama
def menu_utama():
    while True:
        print("\n=== Sistem Pemesanan Tiket Bioskop ===")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        pilihan = input("Pilih peran (1-3): ")
        if pilihan == '1':
            menu_admin()
        elif pilihan == '2':
            menu_pembelian_tiket()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan sistem ini.")
            break
        else:
            print("Pilihan tidak valid.")

# Menu manajemen film
def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Daftar Tiket")
        print("4. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            while True:
                print("\n=== Tambah Film ===")
                judul = input("Masukkan judul film yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
                if judul:
                    tambah_film(judul)
                else:
                    print("Kembali ke Menu Admin")
                    break
        elif pilihan == '2':
            while True:
                print(("\n=== Hapus Film ==="))
                print("Daftar Film:")
                with open("daftar_film.txt", "r") as file:
                    films = file.readlines()
                    for i, film in enumerate(films, start=1):
                        print(f"{i}. {film.strip()}")
                print("0. Kembali")
                nomor_film = input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): ")
                if nomor_film == '0':
                    print("\nKembali ke Menu Admin.")
                    break
                else:
                    try:
                        nomor_film = int(nomor_film)
                        if 1 <= nomor_film <= len(films):
                            judul = films[nomor_film - 1].strip()
                            hapus_film(judul)
                        else:
                            print("Nomor film tidak valid.")
                    except ValueError:
                        print("Nomor film harus berupa angka.")
        elif pilihan == '3':
            menu_daftar_tiket()
        elif pilihan == '4':
            print("\nKembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid.")

# Menu pembelian tiket
def menu_pembelian_tiket():
    while True:
        print("\n=== Menu Pengunjung ===")
        print("1. Lihat daftar film")
        print("2. Beli tiket")
        print("3. Kembali ke Menu Utama")
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            tampilkan_film()
        elif pilihan == '2':
            print("\n=== PEMBELIAN TIKET ===")
            print("\nDaftar film:")
            with open("daftar_film.txt", "r") as file:
                films = file.readlines()
            for i, film in enumerate(films, start=1):
                print(f"{i}. {film.strip()}")
            print("0. Kembali")
            while True:
                nomor_film = input("\nPilih nomor film yang ingin ditonton (0 untuk kembali): ")
                if nomor_film == '0':
                    break
                else:
                    try:
                        nomor_film = int(nomor_film)
                        if 1 <= nomor_film <= len(films):
                            judul = films[nomor_film - 1].strip()
                            id_tiket = beli_tiket(judul)
                            print(f"File tiket telah dibuat: tiket/{id_tiket}.txt")
                            break
                        else:
                            print("Nomor film tidak valid.")
                    except ValueError:
                        print("Nomor film harus berupa angka.")
        elif pilihan == '3':
            print("\nKembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid.")

# Memastikan folder dan file yang diperlukan sudah ada
buat_folder("data")
buat_folder("tiket")
if not os.path.exists("daftar_film.txt"):
    open("daftar_film.txt", "w").close()
if not os.path.exists("tiket.txt"):
    open("tiket.txt", "w").close()

# Memulai program
if __name__ == "__main__":
    menu_utama()