def checkString(count,k):
    for i in count:
        if i>0 and i<k:
            return False
    return True

# string,k = input().split()
# k = int(k)

def solve(string,k):
    ans=0

    for i in range(len(string)):
        j=i
        count =[0]*26
        while(j<len(string)):
            count[ord(string[j])-ord('a')]+=1
            if(checkString(count,k)):
                ans=max(ans,j-i+1)
            j+=1
    return ans
# print(solve('abcdefaa',2))
def test_1():
    assert 5 == solve('ababbc',2)
def test_2():
    assert 6 == solve('ababbc',1)
def test_3():
    assert 0 == solve('ababbc',3)
def test_4():
    assert 2 == solve('abcdefaa',2)
def test_5():
    assert 3 == solve('bbbabc',3)
def test_6():
    assert 3 == solve('abcccba',3)