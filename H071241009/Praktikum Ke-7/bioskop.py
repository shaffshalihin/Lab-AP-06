import datetime
import os

DATA_TIKET_FILE = "data_tiket.txt"

class Film:
    def __init__(self, judul, genre, durasi):
        self.judul = judul
        self.genre = genre
        self.durasi = durasi

class Tiket:
    def __init__(self, id_tiket, judul_film, waktu_pembelian):
        self.id_tiket = id_tiket
        self.judul_film = judul_film
        self.waktu_pembelian = waktu_pembelian

def generate_id_tiket():
    now = datetime.datetime.now()
    return f"TICK{now.strftime('%d%m%Y%H%M%S')}"

def simpan_tiket_ke_file(tiket):
    folder_tiket = "Tiket"
    if not os.path.exists(folder_tiket):
        os.makedirs(folder_tiket)
    file_path = os.path.join(folder_tiket, "data_tiket.txt")
    with open(file_path, "w+") as file:
        line = f"{tiket.id_tiket},{tiket.judul_film},{tiket.waktu_pembelian}\n"
        file.write(line)
    print(f"Data tiket dengan ID {tiket.id_tiket} berhasil disimpan ke dalam file.")

def tampilkan_daftar_film():
    if not daftar_film:
        print("Tidak ada film yang tersedia.")
        return
    print("Daftar Film:")
    for i, film in enumerate(daftar_film, start=1):
        print(f"{i}. {film.judul} ({film.genre}, {film.durasi} menit)")

def tampilkan_daftar_tiket():
    with open(DATA_TIKET_FILE, "r") as file:
        lines = file.readlines()
        if not lines:
            print("Tidak ada tiket yang terbeli.")
        else:
            for line in lines:
                id_tiket, judul_film, waktu_pembelian = line.strip().split(',')
                print(f"ID Tiket: {id_tiket}, Judul Film: {judul_film}, Waktu Pembelian: {waktu_pembelian}")

def lihat_detail_tiket():
    while True:
        id_tiket = input("Masukkan ID tiket (tekan enter untuk keluar): ")
        if not id_tiket:
            print("Kembali ke menu admin.")
            break
        with open(DATA_TIKET_FILE, "r") as file:
            for line in file:
                data_tiket = line.strip().split(',')
                if data_tiket[0] == id_tiket:
                    print(f"Detail Tiket:")
                    print(f"ID Tiket: {data_tiket[0]}")
                    print(f"Judul Film: {data_tiket[1]}")
                    print(f"Waktu Pembelian: {data_tiket[2]}")
                    return
            print("Tiket tidak ditemukan.")

def hapus_tiket():
    while True:
        id_tiket = input("Masukkan ID tiket yang ingin dihapus (tekan Enter untuk keluar): ")
        if not id_tiket:
            print("Kembali ke menu admin.")
            break 

        with open(DATA_TIKET_FILE, "r") as file:
            lines = file.readlines()

        with open(DATA_TIKET_FILE, "w") as file:
            found = False
            for line in lines:
                data_tiket = line.strip().split(',')
                if data_tiket[0] != id_tiket:
                    file.write(line)
                else:
                    found = True

            if found:
                print("Tiket berhasil dihapus.")
            else:
                print("Tiket tidak ditemukan.")

def menu_daftar_tiket():
    while True:
        print("\nMenu Daftar Tiket")
        print("1. Lihat Daftar Tiket")
        print("2. Lihat Detail Tiket")
        print("3. Hapus Tiket")
        print("4. Kembali")
        pilihan = pilih_opsi(1, 4)

        if pilihan == 1:
            tampilkan_daftar_tiket()
        elif pilihan == 2:
            lihat_detail_tiket()
        elif pilihan == 3:
            hapus_tiket()
        else:
            break

def beli_tiket():
    tampilkan_daftar_film()
    if not daftar_film:
        return

    while True:
        pilihan_film = input("Pilih film yang ingin ditonton (nomor, atau tekan Enter untuk keluar): ")
        if not pilihan_film:
            print("Kembali ke menu pengunjung.")
            break

        try:
            pilihan_film = int(pilihan_film)
            if 1 <= pilihan_film <= len(daftar_film):
                film_terpilih = daftar_film[pilihan_film - 1]
                id_tiket = generate_id_tiket()
                tiket_baru = Tiket(id_tiket, film_terpilih.judul, datetime.datetime.now())
                daftar_tiket.append(tiket_baru)
                simpan_tiket_ke_file(tiket_baru)
                print(f"Tiket berhasil dibeli! ID tiket: {id_tiket}")
                break
            else:
                print("Pilihan film tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Masukkan nomor film yang valid (dalam angka).")

def simpan_film_ke_file(film):
    folder_film = "Film"
    if not os.path.exists(folder_film):
        os.makedirs(folder_film)
    file_path = os.path.join(folder_film, "data_film.txt")
    with open(file_path, "w+") as file:
        line = f"{film.judul},{film.genre},{film.durasi}\n"
        file.write(line)
    print(f"Data film {film.judul} berhasil disimpan.")

def tambah_film():
    while True:
        judul = input("Masukkan judul film (tekan enter untuk keluar): ")
        if not judul:
            print("Kembali ke menu admin.")
            break

        genre = input("Masukkan genre film (tekan enter untuk keluar): ")
        if not genre:
            print("Genre film tidak boleh kosong.")
            continue  

        try:
            durasi = int(input("Masukkan durasi film (menit): "))
        except ValueError:
            print("Durasi film harus berupa angka.")
            continue

        judul = judul.title()
        genre = genre.title()

        if any(film.judul == judul for film in daftar_film):
            print("Film dengan judul yang sama sudah ada.")
            continue

        if judul and genre and durasi:
            film_baru = Film(judul, genre, durasi)
            daftar_film.append(film_baru)
            simpan_film_ke_file(film_baru)
            print("Film berhasil ditambahkan!")
        else:
            print("Data film tidak lengkap. Film tidak ditambahkan.")

        lanjut = input("Apakah Anda ingin menambahkan film lagi? (y/n): ")
        if lanjut.lower() != 'y':
            break

def hapus_film():
    tampilkan_daftar_film()
    if not daftar_film:
        return

    while True:
        hapus_index = input("Masukkan nomor film yang ingin dihapus (tekan Enter untuk kembali): ")
        if not hapus_index:
            print("Kembali ke menu admin.")
            break

        try:
            index = int(hapus_index)
            if 1 <= index <= len(daftar_film):
                del daftar_film[index - 1]
                print("Film berhasil dihapus.")
                break
            else:
                print("Nomor film tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Masukkan nomor film yang valid (dalam angka).")

def tampilkan_menu_utama():
    while True:
        try:
            print("\nSelamat datang di Sistem Informasi Bioskop!")
            print("Sistem Pemesanan Tiket Bioskop")
            print("1. Admin")
            print("2. Pengunjung")
            print("3. Keluar")
            return int(input("Pilih menu: "))
        except ValueError:
            print("Masukkan angka yang valid.")


def pilih_opsi(opsi_min, opsi_max, pesan="Pilih opsi: "):
    while True:
        try:
            pilihan = int(input(pesan))
            if opsi_min <= pilihan <= opsi_max:
                return pilihan
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Masukkan angka yang valid.")

daftar_film = []

daftar_tiket = []

while True:
    pilihan_utama = tampilkan_menu_utama()

    if pilihan_utama == 1:
        while True:
            print("\nMenu Manajemen Film")
            print("1. Tambah Film")
            print("2. Hapus Film")
            print("3. Tampilkan Daftar Film")
            print("4. Daftar Tiket")
            print("5. Kembali")
            pilihan_film = pilih_opsi(1, 5)
            if pilihan_film == 1:
                tambah_film()
            elif pilihan_film == 2:
                hapus_film()
            elif pilihan_film == 3:
                tampilkan_daftar_film()
            elif pilihan_film == 4:
                menu_daftar_tiket()
            else:
                break
    elif pilihan_utama == 2:
        while True:
            print("\nMenu Pembelian Tiket")
            print("1. Tampilkan Daftar Film")
            print("2. Beli Tiket")
            print("3. Kembali")
            pilihan_tiket = pilih_opsi(1, 4)
            if pilihan_tiket == 1:
                tampilkan_daftar_film()
            elif pilihan_tiket == 2:
                beli_tiket()
            else:
                break
    else:
        print("Terima kasih telah berkunjung ke Sistem Informasi Bioskop!")
        break