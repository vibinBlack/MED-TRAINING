def fibonnaci(num):
    number = int(input("Enter the number of elements : "))
    num_lst=[]
    for i in range(number):
        num_int = int(input("Enter the numbers:"))
        num_lst.append(num_int)
    for i in range(num):
        fibo_num = sum(num_lst[-number:])
        num_lst.append(fibo_num)

    result_fibo = num_lst
    return result_fibo



number = int(input("Enter the Number:"))
if (number<0):
    print("Invalid number")
else:
    result = fibonnaci(number) 
    print(result)