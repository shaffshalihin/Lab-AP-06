def caesar_cipher(kata, shift):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  hasil = ""
  for karakter in kata:
    if karakter.lower() in alphabet:
      index = alphabet.find(karakter.lower())
      new_index = (index + shift) % len(alphabet)
      karakter_baru = alphabet[new_index]
      karakter_baru = karakter_baru.upper() if karakter.isupper() else karakter_baru
      hasil += karakter_baru
    else:
      hasil += karakter
  return hasil
if __name__ == "__main__":
  kata = input("Masukkan kata: ")
  shift = int(input("Masukkan jumlah pergeseran: "))
  kata_cipher = caesar_cipher(kata, shift)
  print(f"Text: {kata}")
  print(f"Shift: {shift}")
  print(f"Cipher: {kata_cipher}")
caesar_cipher(kata,shift)
