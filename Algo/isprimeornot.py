n = int(input())
flag = 1
for i in range(2,int(n**(1/2))):
    if n%i == 0:
        flag = 0
if flag:
    print("It is a prime number")
else:
    print("Not prime")
