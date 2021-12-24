def string_multlipilcations_float(str,num):
    num = float(num)
    res = str*num 
    print(res)



def string_multlipilcations_int(str,num):
    res = str*num 
    print(res)



def string_division_int(str,num):
    str_len = len(str)
    if str_len%num != 0:
        print("Invalid Input")
        return 

    size_div = str_len / num 
    k = 0 
    for i in str:
        if k % size_div == 0:
            print ("\n")
        print (i,end="")
        k+=1

    print(" ")



string_str = input("Enter the string: ")
num = int(input("Enter the number : "))

string_multlipilcations_int(string_str,num)
string_division_int(string_str,num)
string_multlipilcations_float(string_str,num)