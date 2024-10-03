def substring(string):

    substrings = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substrings.append(string[i:j])
    return substrings

string = input("Masukkan string: ")
all_substrings = substring(string)

for length in range(1, len(string) + 1):
    for i in range(len(string) - length + 1):
        print(string[i:i+length])