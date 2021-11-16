def checkPalindrome(s):
    if len(s) == 0 or s == None:
        return "Please enter the string"
    if len(s) == 1:
        return "Palindrome"
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return "Not palindrome"

    return "Palindrome"

s = input("Enter the string: ")
res = checkPalindrome(s)
print(res)