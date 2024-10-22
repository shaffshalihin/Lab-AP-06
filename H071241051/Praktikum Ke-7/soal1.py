import os
import datetime

def menu_utama():
    os.makedirs("film", exist_ok=True)
    os.makedirs("tickets", exist_ok=True)
    while True:
        print("============selamat datang============")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")
        pilihan = input("Pilih opsi (1-3) = ")
        try:
            if pilihan == "1":
                menu_admin()
            elif pilihan == "2":
                menu_pengunjung()
            elif pilihan == "3":
                print("Terimakasih sampai jumpa lagi!")
                break
            else:
                print("Input tidak valid")
        except ValueError:
            print("Terjadi kesalahan")

def menu_admin():
    while True:
        print("\n=============menu admin============")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Daftar Tiket")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1-4) = ")
        try:
            if pilihan == "1":
                tambah_film()
            elif pilihan == "2":
                hapus_film()
            elif pilihan == "3":
                daftar_tiket()
            elif pilihan == "4":
                break
            else:
                print("Input tidak valid")
        except ValueError:
            print("Terjadi kesalahan")

films=[]
def tambah_film():
    judul = input("Masukan judul film = ")
    genre = input("Masukan genre film = ")
    durasi = input("Masukan durasi film (dalam menit) = ")
    while not durasi.isdigit():
        print("Input tidak valid, masukan angka")
        durasi = input("Masukan durasi film (dalam menit) = ")
    film = {"judul": judul, "genre": genre, "durasi": durasi}
    films.append(film)
    simpan_film()
    print(f"Film '{judul}' berhasil ditambahkan")

def simpan_film():
     with open("film/film.txt", "w") as f:
        for film in films:
            f.write(f"{film['judul']},{film['genre']},{film['durasi']}\n")

def muat_film():
    global films
    films = []
    try:
        with open("film/film.txt", "r") as f:
            for line in f:
                judul, genre, durasi = line.strip().split(",")
                films.append({"judul": judul, "genre": genre, "durasi": durasi})
    except FileNotFoundError:
        pass

def tampilkan_daftar_film():
    muat_film()
    if films:
        print("\nDaftar Film:")
        for i, film in enumerate(films):
            print(f"{i+1}. {film['judul']} - Genre: {film['genre']}, Durasi: {film['durasi']} menit")
    else:
        print("Tidak ada film yang tersedia saat ini.")

def hapus_film():
    muat_film()  
    tampilkan_daftar_film()
    judul = input("Masukkan judul film yang ingin dihapus: ")
    for film in films:
        if film['judul'].lower() == judul.lower():
            films.remove(film)  
            simpan_film() 
            print(f"Film '{judul}' berhasil dihapus dari daftar.")
            return
    print(f"Film '{judul}' tidak ditemukan.")

def daftar_tiket():
    while True:
        print("\nPilih tindakan:")
        print("1. Lihat Daftar Tiket")
        print("2. Lihat Detail Tiket")
        print("3. Hapus Tiket")
        print("4. Kembali")
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            tampilkan_daftar_tiket()
        elif pilihan == "2":
            tampilkan_detail_tiket()
        elif pilihan == "3":
            hapus_tiket()
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")

def tampilkan_daftar_tiket():
    tiket_file = "tickets/tickets.txt"
    try:
        if os.path.exists(tiket_file) and os.path.getsize(tiket_file) > 0:
            print("\nDaftar Tiket:")
            with open(tiket_file, "r") as f:
                tickets = f.readlines()
                for i in range(0, len(tickets), 4):
                    id_tiket = tickets[i].strip()
                    print(f"{(i // 4) + 1}. {id_tiket}")
        else:
            print("Belum ada tiket yang terjual.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan daftar tiket: {e}")

def tampilkan_detail_tiket():
    file_tiket = "tickets/tickets.txt"
    id_tiket = input("Masukkan ID tiket = ").strip()  
    try:
        with open(file_tiket, "r") as file:
            data = file.readlines()

        for i in range(0, len(data), 4):  
            if id_tiket == data[i].strip():
                id = data[i].strip()  
                judul_film = data[i+1].strip()  
                durasi = data[i+2].strip() 

                print(f"\nDetail Tiket:\n\t- ID Tiket\t\t: {id}")
                print(f"\t- Judul Film\t\t: {judul_film}")
                print(f"\t- Durasi Film\t\t: {durasi}")
                return

        print(f"Tiket dengan ID '{id_tiket}' tidak ditemukan.")
    except FileNotFoundError:
        print("Tiket tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menampilkan detail tiket: {e}")

def hapus_tiket():
    file_tiket = "tickets/tickets.txt"
    if os.path.exists(file_tiket):
        id_tiket = input("Masukkan ID tiket = ")
        with open(file_tiket, "r") as f:
            lines = f.readlines()

        with open(file_tiket, "w") as f:
            found = False
            for i in range(0, len(lines), 4):
                if id_tiket not in lines[i]:
                    f.writelines(lines[i:i+4])
                else:
                    found = True
            if found:
                print(f"Tiket dengan ID '{id_tiket}' berhasil dihapus.")
            else:
                print(f"Tiket dengan ID '{id_tiket}' tidak ditemukan.")
    else:
        print("Tidak ada tiket untuk dihapus.")

def menu_pengunjung():
    while True:
        print("\nMenu Pengunjung:")
        print("1. Lihat Daftar Film")
        print("2. Beli Tiket")
        print("3. Kembali")
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            tampilkan_daftar_film()
        elif pilihan == "2":
            beli_tiket()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid.")

def beli_tiket():
    tampilkan_daftar_film()
    if not films:
        print("Tidak ada film yang tersedia.")
        return

    try:
        pilihan = int(input("Pilih nomor film yang ingin ditonton: ")) - 1
        if 0 <= pilihan < len(films):
            film = films[pilihan]
            id_tiket = hasilkan_id_tiket()
            tiket = {"id": id_tiket, "film": film['judul'], "durasi": film['durasi']}

            simpan_informasi_tiket(tiket)
            print(f"Tiket berhasil dibeli! ID Tiket: {id_tiket}")
        else:
            print("Pilihan tidak valid.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan nomor film yang benar.")

def hasilkan_id_tiket():
    waktu_sekarang = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    return f"TICK{waktu_sekarang}"

def simpan_informasi_tiket(tiket):
    tiket_file = "tickets/tickets.txt"
    with open(tiket_file, "a") as f:
        f.write(f"{tiket['id']}\n")
        f.write(f"{tiket['film']}\n")
        f.write(f"{tiket['durasi']} menit\n\n")

menu_utama()