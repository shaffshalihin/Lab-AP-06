import datetime
import os

# Fungsi untuk menghasilkan ID tiket unik
def generate_ticket_id():
    return "TICK" + datetime.datetime.now().strftime("%d%m%Y%H%M%S")

# Fungsi untuk memuat data film dari file
def load_films():
    films = []
    if os.path.exists("films.txt"):
        with open("films.txt", "r") as file:
            films = [line.strip() for line in file.readlines()]
    return films

# Fungsi untuk menyimpan data film ke file
def save_films(films):
    with open("films.txt", "w") as file:
        for film in films:
            file.write(film + "\n")

# Fungsi untuk memuat data tiket dari file
def load_tickets():
    tickets = []
    if os.path.exists("tickets.txt"):
        with open("tickets.txt", "r") as file:
            tickets = [line.strip().split(";") for line in file.readlines()]
    return tickets

# Fungsi untuk menyimpan data tiket ke file
def save_ticket(ticket_info):
    with open("tickets.txt", "a") as file:
        file.write(";".join(ticket_info) + "\n")

# Fitur Admin: Tambah Film
def add_film():
    film_name = input("Masukkan nama film: ")
    films = load_films()
    films.append(film_name)
    save_films(films)
    print(f"Film '{film_name}' berhasil ditambahkan!")

# Fitur Admin: Hapus Film
def delete_film():
    films = load_films()
    print("\nDaftar Film:")
    for i, film in enumerate(films):
        print(f"{i + 1}. {film}")
    choice = int(input("\nPilih film yang akan dihapus (nomor): ")) - 1
    if 0 <= choice < len(films):
        deleted_film = films.pop(choice)
        save_films(films)
        print(f"Film '{deleted_film}' berhasil dihapus!")
    else:
        print("Pilihan tidak valid.")

# Fitur Admin: Tampilkan Daftar Film
def display_films():
    films = load_films()
    if not films:
        print("Tidak ada film yang tersedia.")
    else:
        print("\nDaftar Film:")
        for film in films:
            print(f"- {film}")

# Fitur Pengunjung: Beli Tiket
def buy_ticket():
    films = load_films()
    if not films:
        print("Tidak ada film yang tersedia.")
        return

    print("\nDaftar Film:")
    for i, film in enumerate(films):
        print(f"{i + 1}. {film}")
    choice = int(input("\nPilih film yang ingin dibeli (nomor): ")) - 1
    if 0 <= choice < len(films):
        name = input("Masukkan nama Anda: ")
        ticket_id = generate_ticket_id()
        selected_film = films[choice]
        save_ticket([ticket_id, name, selected_film])
        print(f"Tiket berhasil dibeli! ID Tiket: {ticket_id}")
    else:
        print("Pilihan tidak valid.")

# Fitur Admin: Tampilkan Daftar Tiket
def display_tickets():
    tickets = load_tickets()
    if not tickets:
        print("Tidak ada tiket yang telah dibeli.")
    else:
        print("\nDaftar Tiket:")
        for ticket in tickets:
            print(f"ID: {ticket[0]}, Nama: {ticket[1]}, Film: {ticket[2]}")

# Fitur Admin: Tampilkan Detail Tiket
def view_ticket_detail():
    tickets = load_tickets()
    ticket_id = input("Masukkan ID tiket: ")
    for ticket in tickets:
        if ticket[0] == ticket_id:
            print(f"Detail Tiket - ID: {ticket[0]}, Nama: {ticket[1]}, Film: {ticket[2]}")
            return
    print("Tiket tidak ditemukan.")

# Fitur Admin: Hapus Tiket
def delete_ticket():
    tickets = load_tickets()
    ticket_id = input("Masukkan ID tiket yang akan dihapus: ")
    updated_tickets = [ticket for ticket in tickets if ticket[0] != ticket_id]
    if len(updated_tickets) < len(tickets):
        with open("tickets.txt", "w") as file:
            for ticket in updated_tickets:
                file.write(";".join(ticket) + "\n")
        print(f"Tiket dengan ID '{ticket_id}' berhasil dihapus!")
    else:
        print("Tiket tidak ditemukan.")

# Menu utama
def main_menu():
    while True:
        print("Selamat datang di Aplikasi SIB! \nMenu Utama")
        print("1. Tambah Film (Admin)")
        print("2. Hapus Film (Admin)")
        print("3. Tampilkan Daftar Film (Admin & Pengunjung)")
        print("4. Beli Tiket (Pengunjung)")
        print("5. Tampilkan Daftar Tiket (Admin)")
        print("6. Tampilkan Detail Tiket (Admin)")
        print("7. Hapus Tiket (Admin)")
        print("0. Keluar")

        choice = input("Pilih menu: ")
        if choice == '1':
            add_film()
        elif choice == '2':
            delete_film()
        elif choice == '3':
            display_films()
        elif choice == '4':
            buy_ticket()
        elif choice == '5':
            display_tickets()
        elif choice == '6':
            view_ticket_detail()
        elif choice == '7':
            delete_ticket()
        elif choice == '0':
            print("Terima kasih telah menggunakan Aplikasi SIB ini!")
            break
        else:
            print("Mohon maaf, pilihan tidak valid!")

if __name__ == "__main__":
    main_menu()