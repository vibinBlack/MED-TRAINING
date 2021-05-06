def non_repeating(s):
    d={}
    for i in s:
        if i in d.keys():   # If the given character is found in dictionary(d) increment the value of character 
            d[i]=d[i]+1
        else:
            d[i]=1          # Otherwise assign 1 to the character
    index=0
    for i in s:
        if d[i]==1:         # Check for the first "1" in values of dictionary and break out of loop
            return index
        index+=1
    return -1               # For no unique case

s="crucru"
print(non_repeating(s))

def test_third():
    s="crunchy"
    assert non_repeating(s)==1

def test_allUnique():
    s="crunhy"
    assert non_repeating(s)==0

def test_allRepeate():
    s="crucru"
    assert non_repeating(s)==-1