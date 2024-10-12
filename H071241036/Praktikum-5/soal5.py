def caesar_cipher(teks, shift):
    hasil = ""

    for char in teks:
        if char.isalpha():  
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            hasil += new_char
        else:
            hasil += char

    return hasil

input_teks = input("Masukkan string: ")
shift = int(input("Masukkan jumlah pergeseran: "))

encrypted_text = caesar_cipher(input_teks, shift)

print("Text      :", input_teks)
print("Shift     :", shift)
print("Chiper    :", encrypted_text)
