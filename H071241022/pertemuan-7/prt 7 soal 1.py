import datetime
import os
print("--- Sistem Persamaan Tiket Bioskop---")

def pilih_peran():
    while True:
        try:
            user_input = int(input(" 1. Admin\n 2. Pengunjung\n 3. Keluar\n Pilih peran (1/2/3): "))
            if user_input in (1, 2, 3):
                return user_input
        except ValueError:
            print("Input tidak valid. Masukkan angka yang sesuai")    

def admin_menu():
    while True:
        print("---Menu Admin\n 1. Tambah Film\n 2. Hapus Film\n 3. Daftar Tiket\n 4. Kembali")
        input_admin = int(input("Pilih opsi (1/2/3/4): "))

        if input_admin == 1:
            while True:
                input_tambahFilm = input("Masukkan nama film yang ingin ditambahkan (atau tekan 0 untuk kembali): ")

                if input_tambahFilm == "0":
                    break

                with open('films.txt', 'a') as file:
                    file.write(input_tambahFilm + "\n")

                print(f"Film '{input_tambahFilm}' berhasil ditambahkan")

        elif input_admin == 2:
            while True:
                print("---Hapus film---\n Daftar film:")
                with open("films.txt", "r") as file:
                    films = file.readlines()

                for idx, film in enumerate(films, start=1):
                    print(f"{idx}. {film.strip()}")

                try:
                    input_hapusFilm = input("Masukkan nomor film yang ingin dihapus (atau 0 untuk kembali): ")
                    input_hapusFilm = int(input_hapusFilm)

                    if input_hapusFilm == 0:
                        break
                    elif 1 <= input_hapusFilm <= len(films):
                        film_to_remove = films.pop(input_hapusFilm - 1).strip()

                        with open("films.txt", "w") as file:
                            file.writelines(film for film in films) #ini kayaknya loopnya

                            print (f"Film '{film_to_remove}' berhasil dihapus")
                except ValueError:
                    print("Input tidak valid. Masukkan nomor yang sesuai")

        elif input_admin == 3:
            daftar_ticket_menu()
        
        else:
            return

def pengunjung_menu():
    while True:
        print("---Menu Pengunjung---\n 1. Lihat daftar film\n 2. Beli tiket\n 3. Kembali")
        input_pengunjung = int(input("Pilih opsi (1/2/3): "))

        if input_pengunjung == 1:
            with open("films.txt", "r") as file:
                films = file.readlines()

            if not films:
                print("Tidak ada film yang tersedia")
            else:
                print("---Daftar Film---")
                for idx, film in enumerate(films, start=1):
                    print(f"{idx}. {film.strip()}")
        
        elif input_pengunjung == 2:
            while True:
                with open("films.txt", "r") as file:
                    films = file.readlines()
                
                for idx, film in enumerate(films, start=1):
                        print(f"{idx}. {film.strip()}")
                
                try:
                    input_beliTiket = input("Masukkan nomor film yang ingin ditonton (atau 0 untuk kembali): ")
                    input_beliTiket = int(input_beliTiket)

                    if input_beliTiket == 0:
                        break
                    elif 1 <= input_beliTiket <= len(films):
                        selected_film = films[input_beliTiket].strip()

                        current_time = datetime.datetime.now()
                        formatted_time = current_time.strftime("%d%m%Y%H%M%S")
                        ticket_code = f"TICK{formatted_time}"
                        formatted_ticket = (f"""
+-------------------------------------------------------+
|                        |                              |
+------------------------+                              |  
| ID Tiket : {ticket_code}                              | 
| Film     : {selected_film}                            |  
| Tanggal  : {current_time.strftime('%d-%m-%Y %H:%M')}  |
+-------------------------------------------------------+
|      Terimakasih telah membeli tiket Anda!            |
+-------------------------------------------------------+ 
""")
                        
                        ticket_filename = f"{ticket_code}.txt"
                        with open(ticket_filename, "w") as file:
                            file.write(formatted_ticket)

                        print(f"Tiket berhasil dibeli. ID tiket anda: TICK{ticket_code}")

                except ValueError:
                    print("Masukkan nomor film yang valid") 

        elif input_pengunjung == 3:
            return

def daftar_ticket_menu():
                while True:
                    print("--- Daftar Tiket---\n 1. Lihat daftar tiket\n 2. Lihat detail tiket\n 3. Hapus Tiket\n 4. Kembali")
                    input_adminDaftar = int(input("Pilih opsi (1/2/3/4): "))

                    if input_adminDaftar == 1:
                        ticket_files = [f for f in os.listdir() if f.startswith("TICK") and f.endswith(".txt")]
                        if not ticket_files:
                            print("Tidak ada tiket yang tersedia.")
                        else:
                            print("---Daftar Tiket---")
                            for idx, ticket_file in enumerate(ticket_files, start=1):
                                print(f"{idx}. {ticket_file.replace(".txt", "")}")

                    elif input_adminDaftar == 2:
                        ticket_files = [f for f in os.listdir() if f.startswith("TICK") and f.endswith(".txt")]
                        if not ticket_files:
                            print("Tidak ada tiket yang tersedia")
                            continue

                        print("---Daftar Tiket---")
                        for idx, ticket_file in enumerate(ticket_files, start=1):
                            print(f"{idx}. {ticket_file.replace('.txt', '')}")

                        try:
                            ticket_choice = int(input("Pilih nomor tiket yang ingin dilihat (atau 0 untuk kembali): "))

                            if ticket_choice == 0:
                                break

                            elif 1 <= ticket_choice <= len(ticket_files):
                                selected_ticket = ticket_files[ticket_choice - 1]
                                ticket_filename = selected_ticket

                                with open(ticket_filename, "r") as file:
                                    print("--- Detail Tiket ---")
                                    print(file.read())
                            else:
                                print("Pilihan tidak valid. Harap pilih nomor tiket yang sesuai")
                        except ValueError:
                            print("Input tidak valid")

                    elif input_adminDaftar == 3:
                        ticket_files = [f for f in os.listdir() if f.startswith("TICK") and f.endswith(".txt")]
                        if not ticket_files:
                            print("Tidak ada tiket yang tersedia")
                            continue

                        print("---Daftar Tiket---")
                        for idx, ticket_file in enumerate(ticket_files, start=1):
                            print(f"{idx}. {ticket_file.replace('.txt', '')}")

                        try:
                            ticket_choice = int(input("Pilih nomor tiket yang ingin dihapus (atau 0 untuk kembali): "))
                            if 1 <= ticket_choice <= len(ticket_files):
                                selected_ticket = ticket_files[ticket_choice - 1]
                                ticket_filename = selected_ticket

                                os.remove(ticket_filename)
                                print(f"Tiket '{ticket_filename.replace('.txt', '')}' berhasil dihapus")
                            else:
                                print("Pilihan tidak valid")

                        except ValueError:
                            print("Input tidak valid")
                        
                        print("--- Daftar Tiket---")
                        ticket_files =[f for f in os.listdir() if f.startswith("TICK") and f.endswith(".txt")]
                        if not ticket_files:
                            print("Tidak ada tiket yang tersedia")
                        else:
                            for idx, ticket_file in enumerate(ticket_files, start=1):
                                print(f"{idx}. {ticket_file.replace('.txt', '')}")

                    elif input_adminDaftar == 4:
                        return

                    else:
                        print("Pilihan tidak valid. Silahkan pilih lagi")

def main_menu():
    while True:
        user_input = pilih_peran()

        if user_input == 1:
            admin_menu()
        elif user_input == 2:
            pengunjung_menu()
        elif user_input == 3:
            print("Terima kasih, program selesai")
            break



main_menu()
            




   


        




                    


