
def index(a,t):
    start=0
    end=len(a)-1
    while start<=end:            # binary search => here , 'a' must be sorted
        mid=(start+end)//2       # floor division
        if a[mid] == t:
            return mid
        elif a[mid] < t:
            start = mid+1
        else:
            end = mid-1
    return end + 1

a = [3,4,6,8,9,12]
t=7

b=index(a,t)
assert 3 == b

def test_01():
    assert 0 == index(a,2)

def test_02():
    assert 0 == index(a,1)

def test_03():
    assert 5 == index(a,10)

