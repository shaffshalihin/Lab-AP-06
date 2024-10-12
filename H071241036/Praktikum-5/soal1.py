def palindrome(string):
    string = string.lower()
    reserved_string = string[::-1]
    if string == reserved_string:
       print("Palindrome")
    else:
        print("Not Palindrome") 

palindrome("Ibu Ratna Antar Ubi")