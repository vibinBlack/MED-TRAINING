def squareofNumbers(start,end):
    res=[]
    try:
        for i in range(start,end+1):
            temp=i**2
            res.append(temp)
        return res[5::]
    except Exception as E:
        return "Exception occured"

def test_case_01():
    assert squareofNumbers(1, 30) == [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]

def test_case_02():
    assert squareofNumbers("start","end") == "Exception occured"

def test_case_03():
    assert squareofNumbers(5, 5) == []

def test_case_04():
    assert squareofNumbers(1, 5) == []