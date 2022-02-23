given = input()
given = list(given)
n = len(given)
if given == given[n::-1]:
    print("It is palindrome")
else:
    print("Not palindrome")
