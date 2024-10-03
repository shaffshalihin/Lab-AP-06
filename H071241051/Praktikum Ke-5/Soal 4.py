kata = input("Input your string: ")
def substring(kata):
    for i in range(1, len(kata)):
        for j in range(len(kata) - i + 1):
            print(kata[j:j+i])
substring(kata)
