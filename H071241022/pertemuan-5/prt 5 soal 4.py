def generate_substrings(s):
    length = len(s)

    for substring_length in range(1, length + 1):
        for i in range(length - substring_length + 1):
            print(s[i:i + substring_length])

user_input = input("Input your string: ")

generate_substrings(user_input)
