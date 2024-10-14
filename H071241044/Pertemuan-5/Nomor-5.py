def caesar_cipher(string, shift):
    result = []
    for char in string:
        if char.isalpha():
            limit	= 'a' if char.islower() else 'A'
            shifted = chr((ord(char) - ord(limit) + shift) % 26 + ord(limit))
            result.append(shifted)
        else:
            result.append(char)
    print(''.join(result))

caesar_cipher(input("Masukkan string: "), int(input("Masukkan jumlah pergeseran: ")))