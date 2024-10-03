def palindrome(string):

    string == string.lower().replace(" ","")
    return string == string[::-1]

frasa = input("palindrome: ")
string = frasa.lower()
if palindrome(string):
     print("Palindrome")
else:
    print("Not Palindrome")