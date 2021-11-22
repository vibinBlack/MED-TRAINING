'''Understanding control flow statements'''
__author__ = 'Hari'

from placeholders import *

NOTES = '''
python has support for standard control flow statements similar to other languages.
iteration over sequences like list, string etc. is built into the language itself (c# has
similar features) and the loops support an else clause which is not common elsewhere.
'''

def test_if():
    '''Testing if statement'''
    value = 1
    if True:
        value = 2
    assert value == 2

    if not True:
        value = 3
    assert value == 2

def test_if_else():
    '''testing if else'''
    value = 1
    if not True:
        value = 2
    else:
        value = 3
    assert value == 3

def test_if_elif_else():
    '''testing if elif else statment'''
    value_1 = 3
    value_2 = "str"
    if value_1 < 0:
        value_2 = "negative"
    elif value_1 == 0:
        value_2 = "zero"
    else:
        value_2 = "positive"

    assert value_2 == 'positive'

def test_for_loop_range():
    """
    for loops are used to iterate over arbitrary sequences
    """
    nums =[]
    for val in range(1,5):
        nums.append(val)
    assert nums == [1,2,3,4]


def test_for_loop_string():
    '''testing for loop on a string'''
    chars = []
    for val in "engine":
        chars.append(val)
    assert chars == ['e','n','g','i','n','e']

def test_for_loop_list():
    '''testing for loop on a list'''
    result = ""
    for fruit in ["orange", "banana", "apple"]:
        result += fruit
    assert result == "orangebananaapple"

def test_for_loop_list_with_enumerate():
    '''testing loop on list with enumerate'''
    words = ["one", "two", "three"]
    result = []
    for val in enumerate(words):
        result.append(val)

    assert result == [(0,'one'), (1,'two'), (2,'three')]
    mapping = dict(result)
    assert mapping == {0 : 'one', 1:'two', 2:'three' }

def test_for_loop_dict():
    '''testing for loop on dictionary'''
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
    '''testing for loop with break statment'''
    result = []
    for i in range(1,10):
        if i % 5 == 0:
            break
        result.append(i)

    assert result == [1,2,3,4]

def test_for_loop_continue():
    '''testing for loop with continue statment'''
    result = []
    for i in range (1, 10):
        if i % 3 == 0:
            continue
        result.append(i)
    assert result == [1,2,4,5,7,8]

def test_nested_loop_break():
    '''testing break statment in nested loop '''
    result = []
    for val_1 in range(2):
        for val_2 in range(1,5):
            if val_2 % 3 == 0:
                break
            result.append(val_1)

    assert result == [0,0,1,1]

def test_nested_loop_continue():
    '''testing continue statment in nested loop'''
    result = []
    for val_1 in range(2):
        for val_2 in range(1,5):
            if val_2 % 3 == 0:
                continue
            result.append(val_1)

    assert result == [0,0,0,1,1,1]

def test_nested_loop_break_continue():
    '''testing break and continue statment in nested loop'''
    result = []
    for val_1 in range(3):
        for val_2 in range(1,5):
            if val_2%3 == 0:
                continue
            if val_1%2 == 1:
                break
            result.append(val_1)

    assert result == [0,0,0,2,2,2]

# else on loops is not available in other common languages
def test_for_loop_else_plain():
    '''testing for loop with else'''
    result = []
    for val_1 in range(5):
        result.append(val_1)
        print (val_1)
    else:
        result.append(10)

    assert result == [0,1,2,3,4,10]

def test_for_loop_else_break():
    '''testing else in for loop with break statment'''
    result = []
    for val_1 in range(5):
        if val_1 %3 == 0:
            break
        result.append(val_1)
        print( val_1)
    else:
        result.append(10)

    assert result == []

def test_for_loop_else_continue():
    '''testing else in for loop with continue statment'''
    result = []
    for val in range(5):
        if val %3 == 0:
            continue
        result.append(val)
        print (val)
    else:
        result.append(10)

    assert result == [1,2,4,10]

#same as above.
def test_while_loop_else():
    '''testing else in while loop'''
    result = []
    val = 1
    while val in range(5):
        result.append(val)
        val = val+1
        if val%4 == 0:
            break
    else:
        result.append(10)

    assert result == [1,2,3]


THREE_THINGS_I_LEARNT = """
-conditional statements
-loops for, while
-break, continue 
"""

TIME_TAKEN_MINUTES = 30
