def difference(l1,l2):# l1=list1 l2=list2
    l=[]              # l=result list
    for i in l1+l2:   # l1+l2=combination of lists
        if i not in l1:
            l.append(i)
        if i not in l2:
            l.append(i)
    return l

l1=[1]
l2=[6]
print(difference(l1,l2))

def test_first():
    l1=[1,2,3,5,4]
    l2=[1,3,5,6]
    assert  difference(l1,l2)==[2,4,6]

def test_equal():
    l1=[1,3,5,6]
    l2=[1,3,5,6]
    assert  difference(l1,l2)==[]

def test_empty():
    l1=[]
    l2=[]
    assert  difference(l1,l2)==[]

def test_single():
    l1=[2]
    l2=[4]
    assert  difference(l1,l2)==[2,4]