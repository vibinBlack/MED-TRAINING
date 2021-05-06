def checkstrings(bigs,smalls):
    res=[]
    for i in smalls:
    
        if i in bigs:
    
            res.append(True)
    
        else:
    
            res.append(False)
    return res

def test_case1():
    assert checkstrings("this is a big string" , ["this","is","not","a","big","string"]) == [True,True,False,True,True,True]

def test_case2():
    assert checkstrings("",[])==[]

def test_case3():
    assert checkstrings("hereisthecupoftea", ["this","is","coffee"])==[False,True,False]

def test_case4():
    assert checkstrings("here is the coffee",[" "," "," coffee"]) == [True,True,True]

def test_case5():
    assert checkstrings("Testing with special characters(!@#$%^&*())", ["characters","$","^"])==[True,True,True]

def test_case6():
    assert checkstrings("Go", ["G","O","Go"]) == [True,False,True]