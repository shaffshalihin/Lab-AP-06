inventory = []

def tampilkan_barang(inventory):
    if not inventory:
        print("Inventory kosong.")
    else:
        print("Daftar Barang:")
        for item in inventory:
            kode, nama, jumlah, harga = item
            print(f"Kode: {kode}, Nama: {nama}, Jumlah: {jumlah}, Harga: {harga}")

def tambah_barang(inventory):
    kode = input("Masukkan kode barang: ")
    for item in inventory:
        if item[0] == kode:
            print("Barang dengan kode ini sudah ada.")
            return

    nama = input("Masukkan nama barang: ")
    while True:
        try:
            jumlah = int(input("Masukkan jumlah barang: "))
            harga = float(input("Masukkan harga barang: "))
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")
    
    inventory.append([kode, nama, jumlah, harga])
    print("Barang berhasil ditambahkan.")

def hapus_barang(inventory):
    kode = input("Masukkan kode barang yang ingin dihapus: ")
    for item in inventory:
        if item[0] == kode:
            inventory.remove(item)
            print("Barang berhasil dihapus.")
            return
    print("Barang tidak ditemukan.")

def cari_barang(inventory):
    kode = input("Masukkan kode barang yang dicari: ")
    for item in inventory:
        if item[0] == kode:
            nama, jumlah, harga = item[1], item[2], item[3]
            print(f"Barang ditemukan - Kode: {kode}, Nama: {nama}, Jumlah: {jumlah}, Harga: {harga}")
            return
    print("Barang tidak ditemukan.")

def update_barang(inventory):
    kode = input("Masukkan kode barang yang ingin diupdate: ")
    for item in inventory:
        if item[0] == kode:
            nama = input("Masukkan nama baru barang: ")
            while True:
                try:
                    jumlah = int(input("Masukkan jumlah baru barang: "))
                    harga = float(input("Masukkan harga baru barang: "))
                    break
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka yang benar.")
            
            item[1] = nama
            item[2] = jumlah
            item[3] = harga
            print("Barang berhasil diupdate.")
            return
    print("Barang tidak ditemukan.")

def menu():
    global inventory
    while True:
        print("\n============ MENU INVENTORY ============\n"
              "1. Tambah Barang\n"
              "2. Hapus Barang\n"
              "3. Tampilkan Daftar Barang\n"
              "4. Cari Barang\n"
              "5. Update Barang\n"
              "6. Keluar")
        
        pilihan = input("Pilih opsi (1-6): ")
        
        if pilihan == '1':
            tambah_barang(inventory)
        elif pilihan == '2':
            hapus_barang(inventory)
        elif pilihan == '3':
            tampilkan_barang(inventory)
        elif pilihan == '4':
            cari_barang(inventory)
        elif pilihan == '5':
            update_barang(inventory)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()
