#number of prime numbers in given range
def isPrime(n):
    if n == 1: 
        return 0
    elif n == 2 or n == 3:
        return 1 
    else:
        for i in range(2,int(n**(1/2)+1)):
            if n%i == 0:
                return 0
    return 1 

r1 = int(input())
r2 = int(input())
li = list()
count = 0
for i in range(r1,r2):
    res = isPrime(i)
    if res:
        count += 1 
        li.append(i)
print("The no. prime numbers between the given numbers is :",count)
print("The prime numbers are:")
for i in li:
    print( i,end=' ')
