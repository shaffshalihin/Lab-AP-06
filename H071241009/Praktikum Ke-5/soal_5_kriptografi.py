def kriptografi(text, shift):

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  result = ""
  for char in text:
    if char.lower() in alphabet:
      index = alphabet.find(char.lower())
      new_index = (index + shift) % len(alphabet)
      new_char = alphabet[new_index]
      new_char = new_char.upper() if char.isupper() else new_char
      result += new_char
    else:
      result += char
  return result

text = input("Masukkan String: ")
shift = int(input("Masukkan jumlah pergeseran: "))

cipher_text = kriptografi(text, shift)
print(f"Text: {text}")
print(f"Shift: {shift}")
print(f"Cipher: {cipher_text}")