def triangle_pattern(num):
    for i in range(1,num+1):
        star = "* "*i
        left_spaces = " "*(num-i) 
        pattern = left_spaces + star 

        print(pattern) 

number = int(input("Enter the Number:"))
triangle_pattern()