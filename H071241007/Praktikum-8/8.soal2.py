import re
def IPaddress(ip):
    sifour =r"^(\d{1,3}\.){3}\d{1,2}$"
    sisix = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    if re.match(sifour,ip):
        return "IPv4 Address"
    elif re.match(sisix,ip):
        return "IPv6 Address"
    else:
        return "bukan IP Address"
input_user = input("Masukan IP Address: ")
print(IPaddress(input_user))
