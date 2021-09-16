def solve(string):
    dictionary={}
    for i in string:
        dictionary[i] = dictionary.get(i,0)+1
    return dictionary


def test_1():
    assert {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1} == solve('w3resource')

def test_2():
    assert {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1} == solve('helloworld')

def test_3():
    assert {'a':3,'b':2,'c':3,'d':1,'e':1,'f':4} == solve('abcdeffffaabcc')

def test_4():
    assert {'P':1,'y':1,'t':1,'h':1,'o':1,'n':1,'!':3} == solve('Python!!!')