def solve(string):
    newString=''
    for i in string:
        #, . : ; ! ?
        if i!='.' and i!=',' and i!=':' and i!=';' and i!='!' and i!='?':
            newString+=i 
    strList = newString.split()
    avg=0.0
    for i in strList:
        avg+=len(i)
    avg=round(avg/len(strList),1)
    return avg


def test_1():
    assert 3.8 == solve('Hi all, my name is Ram .I am originally from Australia.')
def test_2():
    assert 1.0 == solve('a')
def test_3():
    assert 3.5 == solve('hi hello')
def test_4():
    assert 5.0 == solve('Hello World!!')
def test_5():
    assert 2.8 == solve('Hey Hi! How are you?') 