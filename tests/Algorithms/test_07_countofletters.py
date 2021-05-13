def freqofLetters(s):
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq

def test_case_01():
    assert freqofLetters("w3resources") == {'w':1,'3':1,'r':2,'e':2,'s':2,'o':1,'u':1,'c':1}

def test_case_02():
    assert freqofLetters("my name is revanth") == {'m':2,'y':1,' ':3,'n':2 ,'a':2 ,'e':2 , 'i':1,'s':1,'r':1,'v':1,'t':1,'h':1}

def test_case_03():
    assert freqofLetters("") == {}

def test_case_04():
    assert freqofLetters("''")=={"'":2}