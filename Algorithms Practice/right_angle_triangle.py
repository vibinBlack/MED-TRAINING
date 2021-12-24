def right_angle_pythagerous(num1,num2,num3):
    if(num1**2 + num2**2 == num3**2) or(num1**2 + num3**2 == num2**2) or (num2**2 + num3**2 == num1**2) :
        print("Triangle is Right Angle Triangle")


num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int(input("Enter the third number :"))

right_angle_pythagerous(num1,num2,num3)