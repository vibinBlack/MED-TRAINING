def solve(bigString,smallString):

    boolArr = [False]*len(smallString)
    if bigString == smallString[0]:
        boolArr[0]=True

    bigString = bigString.split()

    if len(bigString)==len(smallString):
        for i in range(len(smallString)):
            if(smallString[i] == bigString[i]):
                boolArr[i]=True
    
    return boolArr


def test_1():
    assert [True, False, True, False, True] == solve("this is a big string",["this", "not", "a", "small", "string"])
def test_2():
    assert [True] == solve("",[""])
def test_3():
    assert [True] == solve("HelloWorld",["HelloWorld"])
def test_4():
    assert [True, False, True, True, False] == solve("He!!o World!@. Thi$ is Amazing",["He!!o","World","Thi$","is","$uper"])