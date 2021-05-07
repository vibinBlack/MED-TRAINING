
a = [3,4,6,8,9,12]
t=7

def index(a,t):
    f=0
    for i in range(len(a)):
        if (a[i]==t):
            return i
        elif(a[i]!=t and a[i]>t):
            return i
    
b=index(a,t)
assert 3 == b

assert 0 == index(a,2)
