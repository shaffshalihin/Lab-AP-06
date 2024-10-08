def caesar_cipher_enkripsi(kalimat, shift):
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hasil = ""

    for char in kalimat:
        if char in huruf_besar:
            pos = huruf_besar.find(char)
            if pos != -1:
                new_index = (pos + shift) % 26
                hasil += huruf_besar[new_index]
        elif char in huruf_kecil:
            pos = huruf_kecil.find(char)
            if pos != -1:
                new_index = (pos + shift) % 26
                hasil += huruf_kecil[new_index]
        else:
            hasil += char
    return hasil

input_kalimat = input("Masukkan String: ")
input_shift = int(input("Masukkan jumlah pergeseran: "))

print(f"Text : {input_kalimat}")
print(f"Shift: {input_shift}")
print(f"Cipher: {caesar_cipher_enkripsi(input_kalimat, input_shift)}")