def linear_search(num_list,num):
    if(len(num_list) == 0):
        return 0

    for i in range(len(num_list)):
        if num_list[i] == num:
            return i        
    else :
        return -1



number = int(input("Enter the length of list:"))
num_list = []
for i in range(number):
    num_int = int(input())
    num_list.append(num_int) 

num = int(input("Enter the requried number to find index :"))

result = linear_search(num_list,num) 

if result ==0 :
    print("Enter valid Number of Inputs in list")

elif (result != -1):
    print("Number is present at index", result)



else:
    print("number is not present")