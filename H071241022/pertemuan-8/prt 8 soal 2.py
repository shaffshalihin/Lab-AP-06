import re
def checkIP(address):
    pattern4 = r"^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
    pattern6 = r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$"
    
    if re.match(pattern4, address):
        return "IPv4"
    elif re.match(pattern6, address):
        return "IPv6"
    return "Bukan IP Address"

input_user = int(input("Masukkan jumlah input: "))

for i in range(input_user):
    address = input("Masukkan IP address: ")
    result = checkIP(address)
    print(result)