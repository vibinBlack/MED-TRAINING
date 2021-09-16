def solve(start,end):
    squares=[]
    start+=5
    for i in range(start,end+1):
        squares.append(i*i)
    return squares

def test_1():
    assert [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900] == solve(1,30)

def test_2():
    assert [] == solve(1,5)

def test_3():
    assert [36] == solve(1,6)

def test_4():
    assert [100] == solve(5,10)