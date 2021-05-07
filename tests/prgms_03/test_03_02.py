
def revdigit(n):
    s=0
    while(n>0):
        r=n%10
        s=s*10+r
        n//=10
    return s
a=revdigit(123)
# print(a)


assert 321 == revdigit(123)  

assert 45 == revdigit(54)
