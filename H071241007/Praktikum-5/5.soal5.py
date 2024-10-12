def caesar_cipher(text, shift):
    # Definisikan alfabet huruf kecil
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    result = ''

    for char in text:
        # Jika karakter adalah huruf kecil
        if char in alphabet:
            # Cari posisi huruf di alfabet
            index = alphabet.index(char)
            # Hitung posisi baru setelah pergeseran
            new_index = (index + shift) % 26
            # Tambahkan huruf baru ke hasil
            result += alphabet[new_index]
        else:
            # Karakter non-alfabet tetap sama
            result += char
    
    return result

text = input("Masukkan String: ").lower()
shift = int(input("Masukkan jumlah pergeseran: "))

print("Text    :", text)
print("Shift   :", shift)
print("Cipher  :", caesar_cipher(text, shift))
