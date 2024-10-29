import time
list_film = []

def tambah_film_admin():
    tambahfilm = input("Masukkan film yang ingin ditambahkan: ").lower()
    for barang in list_film:
        if barang["film"] == tambahfilm:
            print(f"film {tambahfilm} sudah ada silahkan tambahkan film lain\n")
            return      
    list_film.append({"film": tambahfilm})
    print("Film berhasil ditambahkan!\n")
 

def hapus_film_admin():
    hapus = input("Masukkan nama film yang ingin dihapus: ").lower()
    for barang in list_film:
        if barang["film"] == hapus:
            list_film.remove(barang)
            print("film berhasil dihapus!\n")
            return
    print("film tidak ditemukan!\n")

def tampilkan_film():
    if not list_film:
        print("ups, maaf admin tercinta belum menambahkan film\n")
    else:
        print("Film yang tersedia :")
        for i, barang in enumerate(list_film, start=1):
            print(f"{i}. {barang['film']}")
        print("\n")


def cetak_tiket(film, kode):
    with open("tiket.txt", "a") as file:
        file.write(f"Tiket Film: {film}\n")
        file.write(f"Kode Tiket: {kode}\n")
        file.write("-" * 20 + "\n")
    print(f"Tiket berhasil dicetak untuk film {film} dengan kode {kode}\n")

def beli_tiket_pengunjung():
    if not list_film:
        print("ups, tidak ada film yang tersedia saat ini.\n")
        return
    
    print("Tiket film apa yang mau dibeli?")
    tampilkan_film()
    pilihan = input("Jadi mau nonton yang mana nih?(ketik nama filmnya yah): ").lower()
    
    for barang in list_film:
        if barang["film"] == pilihan:
            kode = time.time()
            cetak_tiket(pilihan, kode)
            return
    
    print(f"Film {pilihan} tidak ditemukan dalam daftar!\n")


def menu():
    while True:
        print("siapakah kamu?")
        print("1. Admin")
        print("2. Pengunjung")
        print("0. Keluar")
        lojin = input("Pilih Mode: ")
        print("\n")

        if lojin == "1":
            print("selamat datang admin:")
            print("1. Tambah Film")
            print("2. Hapus Film")
            print("3. Tampilkan Daftar Film")
            print("0. Keluar")
            pilihan = input("Pilih menu: ")
            print("\n")
            if pilihan == "1":
                tambah_film_admin()
            elif pilihan == "2":
                hapus_film_admin()
            elif pilihan == "3":
                tampilkan_film()
            elif pilihan == "0":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid!\n")

        elif lojin == "2":
            print("selamat datang wahai Pengunjung terhormat :)")
            print("1. lihat list Film yang tersedia")
            print("2. beli tiket")
            print("0. Keluar")
            pilihan = input("Pilih Menu: ")
            print("\n")
            if pilihan == "1":
                tampilkan_film()
            elif pilihan == "2":
                beli_tiket_pengunjung()
            elif pilihan == "0":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid!\n")
        
        elif lojin == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!\n")
menu()