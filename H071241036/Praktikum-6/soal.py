inventaris = {}

def tampilkan_menu():
    print("\nMenu Inventaris")
    print("1. Tambah Barang")
    print("2. Hapus Barang")
    print("3. Lihat Daftar Barang")
    print("4. Cari Barang")
    print("5. Update Data Barang")
    print("6. Keluar")

def tambah_barang():
    try:
        kode = input("Masukkan kode barang: ")
        if kode in inventaris:
            raise ValueError ("Kode telah digunakan, silahkan masukkan kode lain!")
        
        nama = input("Masukkan nama barang: ")
        for item in inventaris.values():
            if item ['nama'].lower() == nama.lower():
                print("Barang dengan nama ini sudah ada.")
        while True:
            jumlah = int(input("Masukkan jumlah barang: "))
            if jumlah <= 0:
                print("Jumlah harus lebih dari 0!")
                continue
            break
        while True:
            harga = float(input("Masukkan harga barang: "))
            if harga <= 0:
                print("Masukkan harga yang masuk akal!")
                continue
            break
        inventaris[kode] = {'nama': nama, 'jumlah': jumlah, 'harga': harga}
        print(f"Barang '{nama}' dengan kode '{kode}' berhasil ditambahkan.")
    except :
        print("Masukkan angka!")

def hapus_barang():
    kode = input("Masukkan kode barang yang ingin dihapus: ")
    if kode in inventaris:
        del inventaris[kode]
        print(f"Barang dengan kode '{kode}' berhasil dihapus.")
    else:
        print(f"Barang dengan kode '{kode}' tidak ditemukan.")

def lihat_barang():
    if inventaris:
        print("\nDaftar Barang:")
        for kode, i in inventaris.items():
            print(f"Kode: {kode}, Nama: {i['nama']}, Jumlah: {i['jumlah']}, Harga: {i['harga']}")
    else:
        print("Inventaris kosong.")

def cari_barang():
    kata_kunci = input("Masukkan kode atau nama barang yang ingin dicari: ")
    ditemukan = False
    for kode, detil in inventaris.items():
        if kata_kunci == kode or kata_kunci.lower() == detil['nama'].lower():
            print(f"Barang ditemukan: Kode = {kode}, Nama = {detil['nama']}, Jumlah = {detil['jumlah']}, Harga = {detil['harga']}")
            ditemukan = True
            break
    if not ditemukan:
        print(f"Barang dengan kode atau nama '{kata_kunci}' tidak ditemukan.")

def update_barang():
    try:
        kode = input("Masukkan kode barang yang ingin diubah: ")
        if kode in inventaris:
            nama_baru = input("Masukkan nama baru : ")
            jumlah_baru = input("Masukkan jumlah baru: ")
            harga_baru = input("Masukkan harga baru: ")

            if nama_baru != "":
                inventaris[kode]['nama'] = nama_baru
            if jumlah_baru != "":    
                inventaris[kode]['jumlah'] = jumlah_baru
            if harga_baru != "":
                inventaris[kode]['harga'] = harga_baru
            print(f"Barang dengan kode '{kode}' berhasil diubah.")
        else:
            print(f"Barang dengan kode '{kode}' tidak ditemukan.")
    except ValueError:
        print("Harap diinput dengan benar")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih opsi (1-6): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            lihat_barang()
        elif pilihan == '4':
            cari_barang()
        elif pilihan == '5':
            update_barang()
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()