'''
Testing controlflow statement.
'''
__author__ = 'Hari'

# from placeholders import *

NOTES = '''
python has support for standard control flow statements similar to other languages.
iteration over sequences like list, string etc. is built into the language itself (c# has
similar features) and the loops support an else clause which is not common elsewhere.
'''

def test_if():
    ''' testing conditional statement if'''
    value = 1
    if True:
        value = 2
    assert value == 2

    if not True:
        value = 3
    assert value == 2

def test_if_else():
    ''' testing conditional statements if, else'''
    value = 1
    if not True:
        value = 2
    else:
        value = 3
    assert value == 3

def test_if_elif_else():
    ''' testing conditional statements if, elif, else'''
    value = 3
    str1 = "str"
    if value < 0:
        str1 = "negative"
    elif value == 0:
        str1 = "zero"
    else:
        str1 = "positive"

    assert str1 == 'positive'

def test_for_loop_range():
    """
    for loops are used to iterate over arbitrary sequences
    """
    nums =[]
    for i in range(1,5):
        nums.append(i)
    assert nums == [1,2,3,4]


def test_for_loop_string():
    ''' testing for loop for a string'''
    chars = []
    for i in "engine":
        chars.append(i)
    assert chars == ['e','n','g','i','n','e']

def test_for_loop_list():
    ''' testing for loop for a list'''
    result = ""
    for fruit in ["orange", "banana", "apple"]:
        result += fruit
    assert result == "orangebananaapple"

def test_for_loop_list_with_enumerate():
    ''' testing for loop list using enumerate'''
    words = ["one", "two", "three"]
    result = []
    for i in enumerate(words):
        result.append(i)

    assert result == [(0,'one'), (1,'two'), (2,'three')]
    mapping = dict(result)
    assert mapping == {0 : 'one', 1:'two', 2:'three' }

def test_for_loop_dict():
    ''' testing for loop for a dictionary'''
    num_to_word = {1 : "one", 2 : "two", 3 : "three"}
    result = []
    for item in num_to_word:
        result.append(item)
    assert result == [1,2,3]

def test_while_loop():
    '''testing while loop'''
    result = []
    while len(result) < 3:
        result.append(10)
    assert result == [10,10,10]

def test_for_loop_break():
    ''' testing for loop with break statement'''
    result = []
    for i in range(1,10):
        if i % 5 == 0:
            break
        result.append(i)

    assert result == [1,2,3,4]

def test_for_loop_continue():
    '''testing for loop with continue statement'''
    result = []
    for i in range (1, 10):
        if i % 3 == 0:
            continue
        result.append(i)
    assert result == [1,2,4,5,7,8]

def test_nested_loop_break():
    ''' testing nested loop with break statement'''
    result = []
    for i in range(2):
        for j in range(1,5):
            if j%3 == 0:
                break
            result.append(i)

    assert result == [0,0,1,1]

def test_nested_loop_continue():
    '''testing nested loop with continue statement'''
    result = []
    for i in range(2):
        for j in range(1,5):
            if j%3 == 0:
                continue
            result.append(i)

    assert result == [0,0,0,1,1,1]

def test_nested_loop_break_continue():
    ''' testing nested loops with break and continue statement '''
    result = []
    for i in range(3):
        for j in range(1,5):
            if j%3 == 0:
                continue
            if i%2 == 1:
                break
            result.append(i)

    assert result == [0,0,0,2,2,2]

# else on loops is not available in other common languages
def test_for_loop_else_plain():
    '''testing else condition for for loop'''
    result = []
    for i in range(5):
        result.append(i)
        print (i)
    else:
        result.append(10)

    assert result == [0,1,2,3,4,10]

def test_for_loop_else_break():
    ''' testing the else condition for
    for loop with break statement'''
    result = []
    for i in range(5):
        if i %3 == 0:
            break
        result.append(i)
        print(i)
    else:
        result.append(10)

    assert result == []

def test_for_loop_else_continue():
    ''' testing the else condition for
    for loop with continue statement'''
    result = []
    for i in range(5):
        if i %3 == 0:
            continue
        result.append(i)
        print (i)
    else:
        result.append(10)

    assert result == [1,2,4,10]

#same as above.
def test_while_loop_else():
    ''' testing the else condition for while loop '''
    result = []
    i = 1
    while i in range(5):
        result.append(i)
        i = i+1
        if i%4 == 0:
            break
    else:
        result.append(10)

    assert result == [1,2,3]


THREE_THINGS_I_LEARNT = """
- Conditional Statements 
- Loops 
- break and continue keywords
"""

TIME_TAKEN_MINUTES = 30
