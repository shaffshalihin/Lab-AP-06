def acronym(kalimat):
    kata = kalimat.upper().split()
    akronim = "".join([i[0] for i in kata])
    return akronim

print(acronym("Negara Kesatuan Republik Indonesia")) 
