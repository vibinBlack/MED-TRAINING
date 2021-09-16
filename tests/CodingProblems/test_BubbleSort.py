def solve(arr):
    # arr = list(map(int,input().split()))
    n=len(arr)
    for i in range(n):
        j=0
        while(j<n-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
            j+=1
    return arr

def test_1():
    assert [2, 6, 11, 19, 27, 31, 45, 121] == solve([19,2,31,45,6,11,121,27])
def test_2():
    assert [2,19] == solve([19,2])
def test_3():
    assert [-1,3,10,22] == solve([10,22,3,-1])
def test_4():
    assert [] == solve([])
