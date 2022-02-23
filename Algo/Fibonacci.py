#Fibonacci Series
def fibon(n1,n2):
    return n1 + n2
    

fibo = int(input("Enter the size of Fibonacci series:"))
if fibo == 0:
    print("Invalid entry")
elif fibo == 1:
    print('0')
else:
    n1 = 0
    n2 = 1
    li = list()
    li.append(n1)
    li.append(n2)
    count  = 2 
    while count < fibo:
        su = fibon(n1,n2)
        li.append(su)
        n1 = n2
        n2 = su 
        count += 1 
    for i in li:
        print(i , end=' ')
