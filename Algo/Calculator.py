#Calculator
def addo(n1,n2):
    return n1+n2
def subo(n1,n2):
    return n1-n2
def mulo(n1,n2):
    return n1*n2
def divo(n1,n2):
    return n1/n2

print("Welcome to Calculator")
urcal = 1
while urcal:
    print("Please select the operation to be performed")
    op = int(input("Enter \n 1: Addition \t 2: Subtraction \t 3: Multiplication \t 4: Division \n Your operation : "))
    n1 = int(input("Enter num1 : "))
    n2 = int(input("Enter num2 : "))
    if op == 1:
        print(f"Result of addition is {addo(n1,n2)}")
    elif op == 2:
        print(f"Result of Subtraction is {subo(n1,n2)}")
    elif(op == 3):
        print(f"Result of Multiplication is {mulo(n1,n2)}")
    elif(op==4):
        print(f"Result of Divisin is {divo(n1,n2)}")
    else:
        print("Invalid operation")
    urcal = int(input("Want to perform another operation: \t Yes(1) or No(0) \n Your choice : " ))
