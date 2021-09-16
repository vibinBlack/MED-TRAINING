import sys

def solve(arr):
    firstMax = arr[0]
    secondMax = -sys.maxsize-1

    for i in arr:
        firstMax=max(firstMax,i)
    
    for i in arr:
        if i>secondMax and i<firstMax:
            secondMax=i

    return secondMax

print(solve([10,9]))

def test_1():
    assert 9 == solve([10,9,2,3,1])
def test_2():
    assert -1 == solve([-9,-1,0,-6])
def test_3():
    assert 2 == solve([3,2])
def test_4():
    assert 1 == solve([-10,-1,1,10])