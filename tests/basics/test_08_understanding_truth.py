'''Understanding truth'''
__author__ = 'Hari'

from placeholders import *

NOTES = '''
Just like C, python has notions on what values are considered true
and what values are considered false.

Assigning truth equivalence to non-bool types leads to much more
elegant way of writing code instead of having explicit comparisons
with base values of the data types like 0, '', [] etc.
'''

#None is a first class object in python
def test_none_type():
    '''Testing none type'''
    assert type(None).__name__ == 'NoneType'

#In control flow, builtin objects like string, list, tuple have truth
#and false values

def test_truth_none():
    '''testing truth none'''
    value = None
    result = "not-set"
    #is None treated as true or false? =>flase(else loop)
    if value:
        result = "true"
    else:
        result = "false"

    assert result == 'false'

# a helper function used to test the truth value of an object.
def truth_test(obj, description):
    '''testing truth value of an object'''
    if obj:
        return description + " is treated as true"

    return description + " is treated as false"

def test_truth_values():
    '''testing truth values of different object types'''
    assert truth_test("", "empty string") == 'empty string is treated as false'
    assert truth_test((), "empty tuple") == 'empty tuple is treated as false'
    assert truth_test([], "empty list") == 'empty list is treated as false'
    assert truth_test({}, "empty dict") == 'empty dict is treated as false'
    assert truth_test(set(), "empty set") == 'empty set is treated as false'
    assert truth_test(" ", "white space") == 'white space is treated as true'
    assert truth_test(0, "0") == '0 is treated as false'
    assert truth_test(1, "1") == '1 is treated as true'
    assert truth_test("a", "non-empty-string") == 'non-empty-string is treated as true'
    assert truth_test((1,2), "non-empty-tuple") == 'non-empty-tuple is treated as true'
    assert truth_test([1], "non-empty-list") == 'non-empty-list is treated as true'
    assert truth_test({1:2}, "non-empty-dict") == 'non-empty-dict is treated as true'
    assert truth_test({1}, "non-empty-set") == 'non-empty-set is treated as true'

# The fact that certain things are treated as True or False by
# control flow statements does not mean that they are equal to True or False.
def test_equality():
    '''testing equality'''
    assert ("" is True) is False
    assert (() is True) is False
    assert ([] is True) is False
    assert (set() is True) is False
    assert (0 is True) is False
    assert ("" is False) is False
    assert (() is False) is False
    assert ([] is False) is False
    assert (set() is False) is False
    assert (0 == False) is True
    assert (1 == True) is True
    assert ("a" is True) is False
    assert ((1,2) is True) is False
    assert ([1] is True) is False
    assert ({1} is True) is False


THREE_THINGS_I_LEARNT = """
-truth and false values
-any object having a value treated as true
-empty values, empty string, 0 will be treated as false
"""

TIME_TAKEN_MINUTES = 30
