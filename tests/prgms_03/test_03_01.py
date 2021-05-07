
def rev_digit(m):
    n=abs(m)
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n//=10
    if m>0:
        return s
    else:
        return -s
        
a=rev_digit(123)
# print(a)

def test_01():
    assert -321 == rev_digit(-123)  

def test_02():
    assert 45 == rev_digit(54)
