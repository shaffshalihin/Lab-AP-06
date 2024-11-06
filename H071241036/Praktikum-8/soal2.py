import re

def validate_ip(ip):
    ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    if re.match(ipv4_pattern, ip):
        return "IPv4"
    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    else:
        return "Bukan IP Address"

while True:
    try:
        n = int(input("Masukkan jumlah baris: "))
        break
    except ValueError:
        print("Inputmu tidak valid kocak. Masukkan angka untuk jumlah baris.") 
for _ in range(n):
    ip = input("Masukkan alamat IP: ")
    result = validate_ip(ip)
    print(result)