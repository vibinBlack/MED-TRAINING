def prime(num):
    if num<2:
        return 0
    
    for i in range(2,num):
        if (num % i) == 0:
            return 1 

    return -1 

number = int(input("Enter the number:"))
result = prime(number) 

if result == -1:
    print("Number is prime") 
elif result == 0 :
    print("Invalid Input")
else:
    print("Number is not a prime")