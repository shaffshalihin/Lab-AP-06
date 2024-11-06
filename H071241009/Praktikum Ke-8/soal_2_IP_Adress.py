import re

ipv4_pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
ipv6_pattern = r"^[0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){7}$"

N = int(input())
addresses = []
for _ in range(N):
    address = input().strip() 
    addresses.append(address)

results = []
for address in addresses:
    if re.match(ipv4_pattern, address):
        octets = address.split('.')
        if all(0 <= int(octet) <= 255 for octet in octets):
            results.append("IPv4")
        else:
            results.append("Bukan IP Address")
    elif re.match(ipv6_pattern, address):
        results.append("IPv6")
    else:
        results.append("Bukan IP Address")

print(*results, sep='\n')