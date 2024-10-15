def tambah_barang(inventory):
    kode_barang = input("Masukkan kode barang: ")
    nama_barang = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah: "))
    harga = int(input("Masukkan harga: "))
    inventory[kode_barang] = {"kode": kode_barang, "nama": nama_barang, "jumlah": jumlah, "harga": harga}
    print("Barang berhasil ditambahkan!")
    
def hapus_barang(inventory):
    while True:
        hapus = input("Cari menggunakan kode barang (1) atau menggunakan nama barang (2): ")
        if hapus == "1":
            hapus_kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
            if hapus_kode_barang in inventory:
                del inventory[hapus_kode_barang]
                print("Barang berhasil dihapus!")
            else:
                print("Barang tidak ditemukan!")
            break
        elif hapus == "2":
            hapus_nama_barang = input("Masukkan nama barang yang ingin dihapus: ").lower()
            barang_dihapus = []
            for barang, data in inventory.items():
                if data['nama'].lower() == hapus_nama_barang:
                    barang_dihapus.append(barang)
            for barang in barang_dihapus:
                del inventory[barang]
            if barang_dihapus:
                print("Barang berhasil dihapus!")
            else:
                print("Barang tidak ditemukan!")
            break
        else:
            print("Pilihan tidak valid! Ketikkan angka 1 untuk menghapus barang menggunakan kode barang atau angka 2 untuk mencari barang menggunakan nama barang")

def tampilkan_barang(inventory):
    print("Daftar Barang:")
    for barang in inventory.values():
        print(f"Kode: {barang['kode']}, Nama Barang: {barang['nama']}, Jumlah: {barang['jumlah']} buah, Harga: Rp{barang['harga']}")

def cari_barang(inventory):
    while True:
        cari = input("Cari menggunakan kode barang (1) atau menggunakan nama barang (2): ")
        if cari == "1":
            cari_kode_barang = input("Masukkan kode barang yang ingin dicari: ")
            if cari_kode_barang in inventory:
                barang = inventory[cari_kode_barang]
                print(f"Barang ditemukan: {barang['kode']}, {barang['nama']}, {barang['jumlah']} buah, Rp{barang['harga']}")
            else:
                print("Barang tidak ditemukan!")
            break
        elif cari == "2":
            cari_nama_barang = input("Masukkan nama barang yang ingin dicari: ").lower()
            hasil_pencarian = []
            for barang in inventory.values():
                if barang['nama'].lower() == cari_nama_barang:
                    hasil_pencarian.append(barang)
                if hasil_pencarian:
                    print("Hasil pencarian:")
                    for barang in hasil_pencarian:
                        print(f"Kode: {barang['kode']}, Nama Barang: {barang['nama']}, Jumlah: {barang['jumlah']} buah, Harga: Rp{barang['harga']}")
                else:
                    print("Barang tidak ditemukan!")
            break
        else:
            print("Pilihan tidak valid! Ketikkan angka 1 untuk mencari barang menggunakan kode barang atau angka 2 untuk mencari barang menggunakan nama barang")

def update_barang(inventory):
    while True:
        cari = input("Cari menggunakan kode barang (1) atau menggunakan nama barang (2): ")
        if cari == "1":
            kode_barang = input("Masukkan kode barang yang ingin diupdate: ")
            if kode_barang in inventory:
                jumlah_baru = int(input("Masukkan jumlah baru: "))
                harga_baru = int(input("Masukkan harga baru: "))
                inventory[kode_barang]['jumlah'] = jumlah_baru
                inventory[kode_barang]['harga'] = harga_baru
                print("Data barang berhasil diupdate!")
                return
            else:
                print("Kode barang tidak ditemukan!")
        elif cari == "2":
            nama_barang = input("Masukkan nama barang yang ingin diupdate: ").strip().lower()
            for barang, data in inventory.items():
                if data['nama'].lower() == nama_barang:
                    jumlah_baru = int(input("Masukkan jumlah baru: "))
                    harga_baru = int(input("Masukkan harga baru: "))
                    data['jumlah'] = jumlah_baru
                    data['harga'] = harga_baru
                    print("Data barang berhasil diupdate!")
                    return
            print(f"Barang dengan nama '{nama_barang}' tidak ditemukan.")
        else:
            print("Pilihan tidak valid! Ketikkan angka 1 untuk mencari barang menggunakan kode barang atau angka 2 untuk mencari barang menggunakan nama barang.")

inventory = {}

while True:
    print("\nMenu:")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Tampilkan Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

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
        print("Terima kasih telah menggunakan program inventory!")
        break
    else:
        print("Pilihan tidak valid!")