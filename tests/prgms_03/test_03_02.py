
def index(a,t):
    f=0
    for i in range(len(a)):
        if (a[i]==t):
            return i
        elif(a[i]!=t and a[i]>t):
            return i


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