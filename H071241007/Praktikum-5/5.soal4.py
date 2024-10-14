kata = input("Input your kata: ")

for panjang in range(1, len(kata) + 1):
    for i in range(len(kata) - panjang + 1):
        print(kata[i:i + panjang])