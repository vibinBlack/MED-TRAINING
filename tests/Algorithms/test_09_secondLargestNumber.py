def sortingList(li):
    n=len(li)
    try:
        for i in range(n):
            for j in range(0,n-i-1):
                if li[j] > li[j+1]:
                    temp=li[j]
                    li[j]=li[j+1]
                    li[j+1]=temp
        return li[n-2]
    except Exception as e: 
        return 'Exception occured'

def test_case_01():
    assert sortingList(["z","y","x","t"]) == 'y'

def test_case_02():
    assert sortingList([9,6,5,2,3,5]) == 6

def test_case_03():
    assert sortingList([1,2,'z','l']) == 'Exception occured'

def test_case_04():
    assert sortingList([""]) == ""