def palindrome(kata):
    kata = kata.replace(" ","").lower()
    if kata == kata[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome("Ibu Ratna Antar Ubi")