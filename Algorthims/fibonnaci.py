def fibonnaci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b 

    return a
    

number = int(input("Enter the Number:"))
if (number<0):
    print("Invalid number")
else:
    result = fibonnaci(number) 
    print(result)