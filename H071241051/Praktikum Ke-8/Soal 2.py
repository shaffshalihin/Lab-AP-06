import re
def IPaddress(IP):
    ipv4 =r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
           r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
           r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\." \
           r"(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$"
    ipv6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    if re.match(ipv4,IP):
        print("IPv4 Address")
        return "IPv4 Address"
    
    elif re.match(ipv6,IP):
        print("IPv6 Address")
        return "IPv6 Address"
    else:
        print("bukan IP Address") 
while True:
    input_user = input("Masukan IP Address: ")
    hasil = IPaddress(input_user)
    if hasil in ["IPv4 Address","IPv6 Address"]:
        break