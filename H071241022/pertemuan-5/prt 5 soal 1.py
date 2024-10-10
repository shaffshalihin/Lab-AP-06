def palindrome(s):
    s = s.replace(" ", "").lower() 
    return "Palindrome" if s == s[::-1] else "Not Palindrome"

print(palindrome("Ibu Ratna Antar Ubi"))
