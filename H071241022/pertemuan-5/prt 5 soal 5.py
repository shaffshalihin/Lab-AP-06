def enkripsi(sentence, shift):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for char in sentence:
        if char in upper_case:
            x = upper_case.find(char)
            if x != -1:
                new_index = (x + shift) % 26
                result += upper_case[new_index]
        elif char in lower_case: 
          x = lower_case.find(char)
          if x != -1:
                new_index = (x + shift) % 26
                result += lower_case[new_index]
        else:
            result += char
    return result

input_sentence = input("Masukkan string: ")
input_shift = int(input("Masukkan jumlah pergeseran: "))

print(f"Text: {input_sentence}")
print(f"Shift: {input_shift}")
print(f"Cipher: {enkripsi(input_sentence, input_shift)}")
