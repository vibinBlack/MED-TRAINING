def dictionary2(d):         # For dict containing two values
    l=list(d.values())      # Values of dictionary as list l
    r=[]                    # result list
    for i in l[0]:
        for j in l[1]:
            a=i+j
            r.append(a)
    return r

def dictionary(d):          # For dict containing more than two values
    l=list(d.values())      # Values of dictionary as list l
    m=len(l)                # length of list l
    r=[]                    # result list
    for i in range(m):      # To select any two lists from the given total list of keys
        for j in range(i,m):
            for a in l[i]:  # To combine elements of each list with elements of another list
                for b in l[j]:
                    if i!=j:
                        s=a+b
                        r.append(s)
    return r

data={'1':['a','b'], '2':'c'}
print(dictionary(data))
print(dictionary2(data))

def test_first():   # Two elements in dict
    data={'1':['a','b'], '2':['c','d']}
    assert dictionary(data)==['ac', 'ad', 'bc', 'bd']

def test_second():  # Three elements in dict
    data={'1':['a','b'], '2':['c','d'], '3':['e','f']}
    assert dictionary(data)==['ac', 'ad', 'bc', 'bd', 'ae', 'af', 'be', 'bf', 'ce', 'cf', 'de', 'df']
    
def test_third():   # Single element in list
    data={'1':['a','b'], '2':['c']}
    assert dictionary(data)==['ac', 'bc']
      
def test_fourth():  # Without List
    data={'1':['a','b'], '2':'c'}
    assert dictionary(data)==['ac', 'bc']