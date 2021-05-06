def merge(list,l,r,m):  
    l_list=list[l:m + 1]    # Left sub-list 
    r_list=list[m+1:r+1]    # Right sub-list 
    li=0                    # Left sub-list index
    ri=0                    # Right sub-list index
    si=l                    # Final sorted-list index
    while li<len(l_list) and ri<len(r_list):    # To ensure not to get IndexOutOfBounds exception  
        if l_list[li]<=r_list[ri]:  
            list[si]=l_list[li]  
            li=li+1  
        else:  
            list[si]=r_list[ri]  
            ri=ri+1  
        si=si+1  
    while li<len(l_list):                       # If one array is greater than other then the remaining elements are added 
        list[si]=l_list[li]                     # at the end of the main array
        li=li+1  
        si=si+1    
    while ri<len(r_list):  
        list[si]=r_list[ri]  
        ri=ri+1  
        si=si+1    

def merge_sort(list,l,r):  
    if l>=r:                # Left and Right index
        return    
    m=(l+(r-1))//2          # Middle index
    merge_sort(list,l,m)    # Dividing the given array in to two parts
    merge_sort(list,m+1,r)  
    merge(list,l,r,m)       # Merging smaller arrays
    return list

list= [64, 64, 64, 64, 64, 64, 64]
print(merge_sort(list, 0, len(list) -1))  

def test_second():
    list= [64, 34, 25, 12, 22, 11, 90]
    assert merge_sort(list, 0, len(list) -1)==[11, 12, 22, 25, 34, 64, 90]

def test_empty():
    list= []
    assert merge_sort(list, 0, len(list) -1)==None

def test_same():
    list= [64, 64, 64, 64, 64, 64, 64]
    assert merge_sort(list, 0, len(list) -1)==[64, 64, 64, 64, 64, 64, 64]