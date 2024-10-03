def akronim(string):
  
  teks = string.split()
  akronim = ""
  for kata in teks:
    akronim += kata[0].upper()
  return akronim

string = input("Masukkan string: ")   
print(akronim(string))