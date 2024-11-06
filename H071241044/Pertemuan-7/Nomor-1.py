import time

def generate_ticket_id():
	return f"TICK{time.strftime('%d%m%Y%H%M%S')}"

def tambah_film(nama_film):
	try:
		with open("film.txt", "a") as file:
			file.write(f"{nama_film}\n")
		print(f"Film '{nama_film}' berhasil ditambahkan ke 'film.txt'.")
	except Exception as e:
		print(f"Terjadi kesalahan saat menambah film: {e}")

def hapus_film():
	if tampilkan_film() == False:
		return print('Tidak ada data untuk dihapus!')
	try:
		nama_film = input("Masukkan nama film: ")
		with open("film.txt", "r") as file:
			films = file.readlines()
		with open("film.txt", "w") as file:
			film_dihapus = False
			for film in films:
				if film.strip("\n") != nama_film:
					file.write(film)
				else:
					film_dihapus = True
		if film_dihapus:
			print(f"Film '{nama_film}' berhasil dihapus dari 'film.txt'.")
		else:
			print(f"Film '{nama_film}' tidak ditemukan.")
	except FileNotFoundError:
		print("File 'film.txt' tidak ditemukan.")
	except Exception as e:
		print(f"Terjadi kesalahan saat menghapus film: {e}")

def tampilkan_film():
	try:
		with open("film.txt", "r") as file:
			films = file.readlines()
		if not films:
			print("Menu ini belum bisa diakses sebab daftar film kosong.")
			return False
		else:
			print("Film yang tersedia:")
			for i, film in enumerate(films, 1):
				print(f"{i}. {film.strip()}")
	except FileNotFoundError:
		print("File 'film.txt' tidak ditemukan.")
	except Exception as e:
		print(f"Terjadi kesalahan saat menampilkan daftar film: {e}")

def beli_tiket():
	daftar_film = tampilkan_film()
	if daftar_film:
		print("Daftar film kosong. Tidak ada tiket yang dapat dibeli.")
		return
	try:
		nama_film = input("Masukkan judul film yang ingin dibeli: ")
		ticket_id = generate_ticket_id()
		simpan_tiket(ticket_id, nama_film)
		print(f"Tiket berhasil dibeli. Detail: ID: {ticket_id}, Film: {nama_film}")
	except Exception as e:
		print(f"Terjadi kesalahan saat membeli tiket: {e}")

def simpan_tiket(ticket_id, nama_film):
	try:
		with open("tiket.txt", "a") as file:
			file.write(f"Ticket ID: {ticket_id}, Film: {nama_film}\n")
		print(f"Informasi tiket berhasil disimpan ke 'tiket.txt'.")
	except Exception as e:
		print(f"Terjadi kesalahan saat menyimpan tiket: {e}")

def tampilkan_tiket():
	try:
		with open("tiket.txt", "r") as file:
			data = file.readlines()
		if not data:
			print("Menu ini belum bisa diakses sebab tidak ada tiket yang dibeli.\n", '='*50)
			return False
		else:
			print("Daftar tiket yang telah dibeli:")
			for i, line in enumerate(data, 1):
				print(f"{i}. {line.strip()}")
	except FileNotFoundError:
		print("File 'tiket.txt' tidak ditemukan.")
	except Exception as e:
		print(f"Terjadi kesalahan saat menampilkan tiket: {e}")

def tampilkan_detail_tiket():
	tampilkan_tiket()
	ticket_id = input("Masukkan ID tiket yang ingin ditampilkan: ")
	try:
		with open("tiket.txt", "r") as file:
			data = file.readlines()
		for line in data:
			if ticket_id in line:
				film_name = line.split(", ")[1].split(": ")[1].strip()
				print(f"\nDetail tiket:\n\t- {line.split(',')[0].split(': ')[0]}\t\t: {line.split(',')[0].split(': ')[1]}\n\t- {line.split(', ')[1].split(': ')[0]}\t\t\t: {line.split(', ')[1].split(': ')[1]}", end='')
				break
		else:
			print(f"Tiket dengan ID '{ticket_id}' tidak ditemukan.")
			return
		with open("film.txt", "r") as film_file:
			available_films = {line.strip() for line in film_file}
		print(f"\t- Ketersediaan film\t: Tersedia") if film_name in available_films else print(f"\t- Ketersediaan film\t: Tidak tersedia")
	except FileNotFoundError:
		print("File 'tiket.txt' tidak ditemukan.")
	except Exception as e:
		print(f"Terjadi kesalahan saat menampilkan detail tiket: {e}")

def hapus_tiket():
	daftar_tiket = tampilkan_tiket()
	if daftar_tiket:
		print("Tidak ada tiket yang tersedia untuk dihapus.")
		return
	try:
		ticket_id = input("Masukkan ID tiket yang ingin dihapus: ")
		with open("tiket.txt", "r") as file:
			tiket_list = file.readlines()
		tiket_dihapus = False
		with open("tiket.txt", "w") as file:
			for ticket in tiket_list:
				if ticket_id not in ticket:
					file.write(ticket)
				else:
					tiket_dihapus = True
		if tiket_dihapus:
			print(f"Tiket dengan ID '{ticket_id}' berhasil dihapus.")
		else:
			print(f"Tiket dengan ID '{ticket_id}' tidak ditemukan.")
	except FileNotFoundError:
		print("File 'tiket.txt' tidak ditemukan.")
	except Exception as e:
		print(f"Terjadi kesalahan saat menghapus tiket: {e}")

def menu_admin():
	while True:
		print("\n", " Menu Admin ".center(60, '=').upper())
		print("1. Tambah Film")
		print("2. Hapus Film")
		print("3. Tampilkan Daftar Film")
		print("4. Tampilkan Semua Tiket")
		print("5. Tampilkan Detail Tiket")
		print("6. Hapus Tiket")
		print("7. Logout")
		pilihan = input("Pilih opsi: ")
		if pilihan == "1":
			nama_film = input("Masukkan nama film: ")
			tambah_film(nama_film)
		elif pilihan == "2":
			hapus_film()
		elif pilihan == "3":
			tampilkan_film()
		elif pilihan == "4":
			tampilkan_tiket()
		elif pilihan == "5":
			tampilkan_detail_tiket()
		elif pilihan == "6":
			hapus_tiket()
		elif pilihan == "7":
			print("Logout...")
			break
		else:
			print('Imputan tidak valid!')

def menu_pengunjung():
	while True:
		print("\n", " Menu Pengunjung ".center(60, '=').upper())
		print("1. Tampilkan Daftar Film")
		print("2. Beli Tiket")
		print("3. Logout")
		pilihan = input("Pilih opsi: ")
		if pilihan == "1":
			tampilkan_film()
		elif pilihan == "2":
			beli_tiket()
		elif pilihan == "3":
			print("Logout...")
			break
		else:
			print('Imputan tidak valid!')

def menu_utama():
	while True:
		print("\n", " Selamat datang di Sistem Informasi Bioskop ".center(60, '=').upper())
		print("1. Admin")
		print("2. Pengunjung")
		print("3. Keluar")
		peran = input("Pilih peran Anda: ")
		if peran == "1":
			menu_admin()
		elif peran == "2":
			menu_pengunjung()
		elif peran == "3":
			print("Keluar dari sistem.")
			break
		else:
			print('Imputan tidak valid!')

if __name__ == "__main__":
	menu_utama()
