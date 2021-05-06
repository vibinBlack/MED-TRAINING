def greatestSum(A):
    if len(A)==0:
        return 0
    sum = [0] * len(A)
    ind=[0]*len(A)
    inde=[]
    sum[0]=A[0]
    for i in range(1, len(A)):
        ind[i]=i
        for j in range(i):            
            if A[i] > A[j]:             # If current number is greater than previous number 
                if sum[j]+A[i]>sum[i]:  # Check if sum at current index(i) less than sum at index j + value at index i
                    sum[i]=sum[j]+A[i]  # Sum is changed
                    ind[i]=j            # Index j from where we are getting sum[j] in array ind for getting the values of
                                        # subsequence later
    m=max(sum)                          # Max sum is found
    i=sum.index(m)                      # Max sum index is found
    inde.append(A[i])                   # Last element used to get the sum is added to list
    while sum.index(m)!=ind[i]:
        m=sum[ind[i]]                   
        i=sum.index(m)                  # All the elements used to get the sum are backtracked and
        inde.insert(0,A[i])             # Insrted at the start of result list to get strictly increasing subsequence
    result=[]
    result.append(max(sum))
    result.append(inde)
    return result

A = [10]
n=greatestSum(A)
print("The maximum sum of the increasing subsequence is", n)

def test_four():
    A = [10,70,20,30,50,11,30]
    assert greatestSum(A)==[110, [10, 20, 30, 50]]

def test_same():
    A = [10,10,10,10,10,10,10]
    assert greatestSum(A)==[10, [10]]

def test_single():
    A = [10]
    assert greatestSum(A)==[10, [10]]

def test_empty():
    A = []
    assert greatestSum(A)==0