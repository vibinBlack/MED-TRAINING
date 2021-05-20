def sublist(l,s):       # l=list s=sublist
    for i in s:         # Checking if all elements of sublist present in main list
        if i not in l:  # If not present then it is not sublist
            return False
    return True

l=[1,2,3,4]
s=[1,2]
print(sublist(l,s))

def test_first():
    l=[1,2,3,4]
    s=[1,2]
    assert sublist(l,s)==True
    
def test_second():
    l=[]
    s=[1,2]
    assert sublist(l,s)==False
    
def test_third():
    l=[1,2]
    s=[1,2,3,4]
    assert sublist(l,s)==False
    
def test_fourth():
    l=[1,2]
    s=[1,2]
    assert sublist(l,s)==True
    
def test_fifth():
    l=[]
    s=[]
    assert sublist(l,s)==True