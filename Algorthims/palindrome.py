def palindrome(string):
    for i in range(len(string)//2):
        if string[i] != string[-(i+1)]:
            return 1
    else:
        return -1

string = input("Enter the input string:")
result=palindrome(string)
if result == -1:
    print("string is pallindrome")
else:
    print("string is not a pallindrome")