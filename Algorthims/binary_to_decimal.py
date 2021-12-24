def binary_to_decimal(binary_number):
    len_binary_number = len(str(binary_number))
    power = 0 
    decimal_number = 0 
    for i in range(len_binary_number-1,-1,-1):
        binary_str_number = str(binary_number)
        decimal_number += int(binary_str_number[i])*2**(power) 
        power +=1 

    print(decimal_number) 


binary_number = int(input("Enter the Binary Number:"))
if(binary_number<0):
    print("Invalid Input")

else:
    binary_str_number = str(binary_number)
    for i in binary_str_number:
        if (i != "0" and i != '1'):
             print("Invalid Input")  
             break
    
    else:
        binary_to_decimal(binary_number)
    
    