def decimal_to_binary(decimal_number):
    decimal_list=[]

    while (decimal_number > 0):
        rem = decimal_number % 2
        decimal_list.append(rem) 
        decimal_number = decimal_number // 2 
    decimal_list.reverse() 

    for i in decimal_list:
        print(i,end="")
    print()


decimal_number = int(input("Enter the Decimal Number:"))

if (decimal_number<0):
    print("Invalid Input")
elif (decimal_number == 0):
    print(decimal_number)

else:
    decimal_to_binary(decimal_number)
