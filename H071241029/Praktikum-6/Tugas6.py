# Data barang di gudang
inventory = {}

# Fungsi menambah barang
def tambah_barang():
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    inventory[nama] = jumlah
    print(f"Barang '{nama}' berhasil ditambahkan.\n")

# Fungsi menghapus barang
def hapus_barang():
    nama = input("Masukkan nama barang yang ingin dihapus: ")
    if nama in inventory:
        del inventory[nama]
        print(f"Barang '{nama}' berhasil dihapus.\n")
    else:
        print(f"Barang '{nama}' tidak ditemukan.\n")

# Fungsi menampilkan daftar barang
def tampilkan_barang():
    if inventory:
        print("Daftar Barang di Gudang:")
        for nama, jumlah in inventory.items():
            print(f"{nama}: {jumlah}")
        print()
    else:
        print("Tidak ada barang di dalam inventory.\n")

# Fungsi mencari barang
def cari_barang():
    nama = input("Masukkan nama barang yang dicari: ")
    if nama in inventory:
        print(f"{nama}: {inventory[nama]}\n")
    else:
        print(f"Barang '{nama}' tidak ditemukan.\n")

# Fungsi mengupdate data barang
def update_barang():
    nama = input("Masukkan nama barang yang ingin diupdate: ")
    if nama in inventory:
        jumlah = int(input(f"Masukkan jumlah baru untuk '{nama}': "))
        inventory[nama] = jumlah
        print(f"Barang '{nama}' berhasil diupdate.\n")
    else:
        print(f"Barang '{nama}' tidak ditemukan.\n")

# Menu interaktif
def menu():
    while True:
        print("Menu:")
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Barang")
        print("4. Cari Barang")
        print("5. Update Barang")
        print("6. Keluar")
        
        pilihan = input("Pilih opsi: ")
        
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            hapus_barang()
        elif pilihan == "3":
            tampilkan_barang()
        elif pilihan == "4":
            cari_barang()
        elif pilihan == "5":
            update_barang()
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

menu()