import re

def is_ipv4(address):
    # Regular Expression untuk memvalidasi IPv4
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, address)
    # Mengecek format cocok dan setiap segmen bernilai antara 0-255
    if match:
        return all(0 <= int(part) <= 255 for part in match.groups())
    return False

def is_ipv6(address):
    # Regular Expression untuk memvalidasi IPv6
    pattern = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    return bool(re.match(pattern, address))

def main():
    # Input jumlah baris
    N = int(input("Masukkan jumlah baris: "))
    # Loop untuk membaca setiap baris dan validasi
    for _ in range(N):
        line = input().strip()
        if is_ipv4(line):
            print("IPv4")
        elif is_ipv6(line):
            print("IPv6")
        else:
            print("Bukan IP Address")

main()