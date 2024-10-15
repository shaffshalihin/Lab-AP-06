inventory = []

def tambah_barang():
    kode = input("Masukkan kode barang: ").lower()
    for barang in inventory:
        if barang["kode"] == kode:
            print(f"kode {kode} sudah ada silahkan gunakan kode lain\n")
            return      
    nama = input("Masukkan nama barang: ").lower()
    jumlah = int(input("Masukkan jumlah barang: "))
    harga = float(input("Masukkan harga barang: "))
    inventory.append({"kode": kode, "nama": nama, "jumlah": jumlah, "harga": harga})
    print("Barang berhasil ditambahkan!\n")


def hapus_barang():
    kode = input("Masukkan kode barang yang ingin dihapus: ").lower()
    for barang in inventory:
        if barang['kode'] == kode:
            inventory.remove(barang)
            print("Barang berhasil dihapus!\n")
            return
    print("Barang tidak ditemukan!\n")

def tampilkan_barang():
    if not inventory:
        print("Inventory kosong!\n")
    else:
        for barang in inventory:
            print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}")
        print()

def cari_barang_nama():
    nama = input("Masukkan nama barang yang dicari: ").lower()
    for barang in inventory:
        if barang['nama'] == nama:
            print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}\n")
            return
    print("Barang tidak ditemukan!\n")

def cari_barang_kode():
    kode = input("Masukkan kode barang yang dicari: ").lower()
    for barang in inventory:
        if barang['kode'] == kode:
            print(f"Kode: {barang['kode']}, Nama: {barang['nama']}, Jumlah: {barang['jumlah']}, Harga: {barang['harga']}\n")
            return
    print("Barang tidak ditemukan!\n")

def update_barang():
    kode = input("Masukkan kode barang yang ingin diupdate: ").lower()
    for barang in inventory:
        if barang['kode'] == kode:
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            harga_baru = float(input("Masukkan harga baru: "))
            barang['jumlah'] = jumlah_baru
            barang['harga'] = harga_baru
            print("Data barang berhasil diperbarui!\n")
            return
    print("Barang tidak ditemukan!\n")

def menu():
    while True:
        print("1. Tambah Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Daftar Barang")
        print("4. Cari Barang (Nama)")
        print("5. Cari Barang (Kode)")
        print("6. Update Barang")
        print("7. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            tampilkan_barang()
        elif pilihan == '4':
            cari_barang_nama()
        elif pilihan == '5':
            cari_barang_kode()
        elif pilihan == '6':
            update_barang()
        elif pilihan == '7':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!\n")

menu()