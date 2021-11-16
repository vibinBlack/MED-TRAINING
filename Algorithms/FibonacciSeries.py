def findFibonacci(n, diary={1:1, 2:1}):
    if n in diary:
        return diary[n]

    diary[n] = findFibonacci(n-1, diary) + findFibonacci(n-2, diary)
    return diary[n]

n = int(input("Enter the element to find the fibonacci series: "))
res = findFibonacci(n)
print(res)