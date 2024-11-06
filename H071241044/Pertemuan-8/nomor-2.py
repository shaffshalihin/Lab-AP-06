import re

def check_ip(ip):

    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6_pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    if re.match(ipv4_pattern, ip):
        return "IPv4"
    elif re.match(ipv6_pattern, ip):
        return "IPv6"
    else:
        return "Bukan IP Address"


n = int(input("Masukkan jumlah IP Address: "))
for _ in range(n):
    ip = input("Masukkan IP Address: ")
    print(check_ip(ip))

