def calculator (first_number,second_number,operator):
    if operator == '+':
        return first_number + second_number 
    elif operator == '-':
        return first_number - second_number 
    elif operator == '*':
        return first_number * second_number 
    elif operator == '/':
        return first_number / second_number 

    else:
        return "Invalid input"


first_number = int(input("Enter the first number:"))
second_number = int(input("Enter the Second number:"))
operator = input("Enter the operator:")

result = calculator(first_number,second_number,operator)
print(result)