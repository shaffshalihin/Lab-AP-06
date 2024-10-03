kata = input("kata = ")
def kata_palindrom(kata):
    format = kata.lower() 
    if format == format[::-1]: 
        print(f"{kata} adalah Palindrom")
    else:
        print(f"{kata} bukan Palindrom")
kata_palindrom(kata)
