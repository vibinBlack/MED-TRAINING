def binary_search_first(num_list,low,high,num):
    if (len(num_list) == 0):
        return 0

    

    while low <= high:

        mid = (low + high)//2

        if num_list[mid] == num :
        
            if(num_list[mid-1] == num and mid != 0):
                high = mid-1

            if(mid==0 and num_list[mid]==num):
                return mid    
            
            else:   
                return high

        elif num_list[mid] < num:
            low = mid + 1

        else:
            high = mid -1 

    return -1 


print("Enter the elements of list with space: ")
number_list = list(map(int, input().split()))



low_index = 0 
high_index = len(number_list) -1 

number = int(input("Enter the requried number to get index :"))

result = binary_search_first(number_list,low_index,high_index,number)



if result != -1:
     print("Number is present at index :", result)

else:
    print("Number is not present")





