def acronym(kalimat):
    kata_kata = kalimat.split()
    
    acronym = ''.join([kata[0].upper() for kata in kata_kata])

    return acronym

input_kalimat = input("Masukkan sebuah kalimat: ")

print(acronym(input_kalimat))