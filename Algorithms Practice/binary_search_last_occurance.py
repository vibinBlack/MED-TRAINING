
def binary_search(num_list,low,high,num):
    if (len(num_list) == 0):
        return 0 

    while low <= high:
        mid = (low + high)//2

        if num_list[mid] == num:
            if(num_list[mid+1] == num):
                low = mid+1
                
            else:
                return low

        elif num_list[mid] < num:
            low = mid + 1 

        else:
            high = mid - 1 

    return -1 


print("Enter the elements of list with space: ")
num_list = list(map(int, input().split()))


low = 0 
high = len(num_list) -1 

num = int(input("Enter the requried number to get index :"))

result = binary_search(num_list,low,high,num)



if result != -1:
     print("Number is present at index :", result)

else:
    print("Number is not present")





