def solve(inputData):
    res=set()
    for Dictionary in inputData:
        for value in Dictionary.values():
            res.add(value)
    return res

# print(solve( [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))

def test_1():
    assert {'S005', 'S009', 'S001', 'S002', 'S007'} ==  solve([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])
def test_2():
    assert {11,23,2} == solve([{'a':11},{'b':23},{'c':11},{'a':2}])
def test_3():
    assert {7} == solve([{'a':7},{'b':7},{'c':7}])
def test_4():
    assert {1,2,3} == solve([{'a':3},{'b':1},{'c':2}])