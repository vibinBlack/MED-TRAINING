def dictionary(d):
    c=0                 # variable for counting items in a dictionary value that is a list.
    l=list(d.values())  # Values of dictionary as list l
    for i in l:
        if type(i) is list:
            c+=len(i)
    return c

dict =  {'Alex': [1], 'David': [1,3]}
print(dictionary(dict))

def test_first():
    dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
    assert dictionary(dict)==5

def test_second():
    dict =  {'Alex': [], 'David': ['subj1', 'subj2']}
    assert dictionary(dict)==2

def test_empty():
    dict =  {'Alex': [], 'David': []}
    assert dictionary(dict)==0

def test_no_list():
    dict =  {'Alex': 12, 'David': 'subj2'}
    assert dictionary(dict)==0