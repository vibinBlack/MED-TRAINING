def find_average_length(s):

    punct='''!@#$%^&*(){}[]:";'<>?,./|\~` '''

    l1=s.split(" ")

    for i in s:

        if i in punct:

            s=s.replace(i,"")
    res=round(len(s)/len(l1),1)
    return res
def test_case1():
    assert find_average_length("Hi all, my name is Ram .Iam originally from Australia.") == 4.2

def test_case2():
    assert find_average_length(" ") == 0

def test_case3():
    assert find_average_length("") == 0

def test_case4():
    assert find_average_length("hereisamathsequation") == 20.0

def test_case5():
    assert find_average_length("@#$%^ z %^&*()") == 0.3