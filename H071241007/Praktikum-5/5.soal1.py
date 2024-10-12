a = input("masukkan kata: ").lower()

def palindrom(a):
    b = a [::-1]
    if a == b:
        return print("ini adalah palindrom")
    else:
        return print("ini bukan palindrom")
    

palindrom(a)