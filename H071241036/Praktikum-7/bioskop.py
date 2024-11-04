import os
from datetime import datetime

nama_folder = 'film'
daftar_film = os.path.join(nama_folder, 'daftar_film.txt')
nama_folder2 = 'tiket'

def folder_tiket():
    os.makedirs(nama_folder2, exist_ok=True)

def folder_film():
    os.makedirs(nama_folder, exist_ok=True)

def load_film():
    if not os.path.exists(daftar_film):
        return []
    with open(daftar_film, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_film(film):
    with open(daftar_film, 'a') as file:
        file.write(film + '\n')

def hapus_film(film_index):
    film = load_film()
    if 1 <= film_index <= len(film):
        del film[film_index - 1]
        with open(daftar_film, 'w') as file:
            for f in film:
                file.write(f + '\n')
        print("Film berhasil dihapus.")
    else:
        print("Film yang dipilih tidak valid.")

def tampilkan_daftar_film():
    film = load_film()
    print("Daftar Film:")
    for i, f in enumerate(film):
        print(f"{i + 1}. {f}")

def tambah_film():
    print("\n--- Tambah Film ---")
    nama_film = input("Masukkan nama film  yang ingin ditambahkan (atau tekan Enter untuk kembali): ")
    film_info = f"{nama_film}"
    save_film(film_info)
    print(f"\nFilm '{nama_film}' berhasil ditambahkan.")

def buat_id_tiket():
    return f"TICK{datetime.now().strftime('TICK%d%m%Y%H%M%S')}"

def format_info_tiket(id_tiket, film):
    print (f"Detail Tiket {'id_tiket'}:")
    return (f"+---------------------------------+\n"
            f"|           TIKET BIOSKOP         |\n"
            f"+---------------------------------+\n"
            f"| ID Tiket : {id_tiket}           |\n"
            f"| Film     : {film}               |\n"
            f"| Tanggal  : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')} |\n"
            f"+---------------------------------+\n"
            f"|    Terima kasih telah membeli   |\n"
            f"|            tiket Anda!          |\n"
            f"+---------------------------------+")

def beli_tiket(film_pilihan):
    film = load_film()
    if 1 <= film_pilihan <= len(film):
        film_terpilih = film[film_pilihan - 1]
        id_tiket = buat_id_tiket()
        tiket_info = format_info_tiket(id_tiket, film_terpilih)

        folder_tiket()
        with open(os.path.join(nama_folder2, f"{id_tiket}.txt"), 'w') as file:
            file.write(tiket_info)
        print(f"\nTiket berhasil dibeli. ID tiket Anda: {id_tiket}")
        print(f"File tiket telah dibuat: tickets/{id_tiket}.txt")
    else:
        print("Film yang dipilih tidak tersedia.")

def load_tiket():
    if not os.path.exists(nama_folder2):
        print("Folder tiket tidak ditemukan.")
        return []
    
    return [(file, open(os.path.join(nama_folder2, file)).read().strip()) for file in os.listdir(nama_folder2) if file.endswith('.txt')]

def tampilkan_daftar_tiket():
    tiket_list = load_tiket()
    if not tiket_list:
        print("Tidak ada tiket yang tersedia.")
        return
    
    print("Daftar Tiket:")
    for i, (file, _) in enumerate(tiket_list):
        print(f"{i + 1}. {file}")


def tampilkan_detail_tiket(tiket_index):
    tiket_list = load_tiket()
    if 1 <= tiket_index <= len(tiket_list):
        print("Detail Tiket:")
        print(tiket_list[tiket_index - 1][1])
    else:
        print("Tiket yang dipilih tidak valid.")

def hapus_tiket(tiket_index):
    tiket_list = load_tiket()
    if 1 <= tiket_index <= len(tiket_list):
        os.remove(os.path.join(nama_folder2, tiket_list[tiket_index - 1][0]))
        print("Tiket berhasil dihapus.")
    else:
        print("Tiket yang dipilih tidak valid.")

def menu_daftar_tiket():
    while True:
        print("\n--- Daftar Tiket ---")
        print("1. Tampilkan Daftar Tiket")
        print("2. Lihat Detail Tiket")
        print("3. Hapus Tiket")
        print("0. Kembali ke Menu Admin")

        pilihan = input("Pilih opsi: ")
        if pilihan == '0':
            break
        elif pilihan == '1':
            tampilkan_daftar_tiket()
        elif pilihan == '2':
            tampilkan_daftar_tiket()
            try:
                tiket_index = int(input("Pilih tiket untuk melihat detail (nomor): "))
                tampilkan_detail_tiket(tiket_index)
            except ValueError:
                print("Input tidak valid.")
        elif pilihan == '3':
            tampilkan_daftar_tiket()
            try:
                tiket_index = int(input("Pilih tiket untuk dihapus (nomor): "))
                hapus_tiket(tiket_index)
            except ValueError:
                print("Input tidak valid.")
        else:
            print("Opsi tidak valid.")

def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Film")
        print("2. Hapus Film")
        print("3. Daftar Tiket")
        print("4. Kembali")

        pilihan = input("Pilih opsi (1/2/3/4): ")
        if pilihan == '0':
            break
        elif pilihan == '1':
            tambah_film()
        elif pilihan == '2':
            tampilkan_daftar_film()
            try:
                film_index = int(input("\nMasukkan nomor film yang ingin dihaput (atau Enter untuk kembali): "))
                hapus_film(film_index)
            except ValueError:
                print("Input tidak valid.")
        elif pilihan == '3':
            menu_daftar_tiket()
        elif pilihan == '4':
            print("\nKembali ke Menu Utama.")
            main()
        else:
            print("Opsi tidak valid.")

def menu_pengunjung():
    while True:
        print("\n--- Menu Pengunjung ---")
        print("1. Tampilkan Daftar Film")
        print("2. Beli Tiket")
        print("3. Kembali")
        
        pilihan = input("Pilih opsi (1/2/3): ")
        if pilihan == '0':
            break
        elif pilihan == '1':
            tampilkan_daftar_film()
        elif pilihan == '2':
            tampilkan_daftar_film()
            try:
                film_pilihan = int(input("\nPilih nomor file yang ingin dinonton: "))
                beli_tiket(film_pilihan)
            except ValueError:
                print("Input tidak valid.")
        elif pilihan == '3':
            print("Kembali ke Menu Utama.")
            main()
        else:
            print("Opsi tidak valid.")

def main():
    folder_film()  
    while True:
        print("\n--- Sistem Pemesanan Tiket Bioskop ---")
        print("1. Admin")
        print("2. Pengunjung")
        print("3. Keluar")

        pilihan = input("Pilih peran (1/2/3): ")
        if pilihan == '3':
            print("\nTerima kasih telah menggunakan sistem ini!")
            return
        elif pilihan == '1':
            menu_admin()
        elif pilihan == '2':
            menu_pengunjung()
        else:
            print("Opsi tidak valid.")

main()