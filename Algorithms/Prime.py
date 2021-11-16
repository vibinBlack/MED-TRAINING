def checkPrime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return "Not Prime"

    return "Prime"


n = int(input("Enter the number: "))
res = checkPrime(n)
print(res)