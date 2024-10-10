def acronym(s):
    words = s.split()
    acronym = "".join(word[0].upper() for word in words)
    return acronym

print(acronym("Negara Kesatuan Republik Indonesia"))