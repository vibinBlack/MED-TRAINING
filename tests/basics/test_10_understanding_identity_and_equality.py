'''Understanding identity and equality'''
__author__ = 'Hari'

from placeholders import *

NOTES = '''
 Identity and equality are 2 concepts which most beginners are confused about.
 The 'is' operator is used to test identity and == is used to test equality.

 Two objects are identical if they are the same object
 Two objects can be equal even if they are not the same object, if they are of the same type and the type defines some
 equality semantics. E.g. all string objects with content "abc" are equal irrespective of where the objects are in memory,
 two lists can be equal if all elements in them are equal in same order etc.
'''

def test_identity_equality_lists():
    '''testing identity and equality of lists'''
    list_1 = []
    list_2 = []
    assert (list_1 is list_2) is False
    assert (list_1 == list_2) is True

    list_1.append("one")
    assert (list_1 is list_2) is False
    assert (list_1 == list_2) is False

    list_3 = []
    list_4 = list_3
    assert (list_3 is list_4) is True
    assert (list_3 == list_4) is True

    list_3.append("one")
    assert (list_3 is list_4) is True
    assert (list_3 == list_4) is True

def test_identity_equality_string():
    '''testing identity and equaltiy of strings'''
    str_1 = str_2 = "hello"

    assert (str_1 is str_2) is True
    assert (str_1 == str_2) is True

    str_3 = "hello"
    str_4 = "".join(["hel", "lo"])
    assert (str_3 is str_4) is False
    assert (str_3 == str_4) is True

def test_identity_equality_numbers():
    '''testing equality of numbers'''
    num_1 = num_2 = 10000
    assert (num_1 is num_2) is True
    assert (num_1 == num_2) is True

    num_3 = 10000
    num_4 = int("10000")
    assert (num_3 is num_4) is False
    assert (num_3 == num_4) is True

def test_identity_equality_small_numbers():
    """
    why do small numbers behave differently? google and find out!
    """
    num_1 = num_2 = 10
    assert (num_1 is num_2) is True
    assert (num_1 == num_2) is True

    num_3 = 10
    num_4 = int("10")
    assert (num_3 is num_4) is True
    assert (num_3 == num_4) is True

def test_identity_equality_None():
    '''testing identitiy and equality of None type'''
    val_1 = val_2 = None
    assert (val_1 is val_2) is True
    assert (val_1 == val_2) is True

    val_1 = None
    val_2 = None
    assert (val_1 is val_2) is True
    assert (val_1 == val_2) is True


NOTES_ON_NONE = '''
None is a builtin constant as you can see above. This allows you to write more
readable code like if x is None: instead of if x == None:
'''

THREE_THINGS_I_LEARNT = """
-equal to operator is used for checking values of both the operands
-"is" is used for checking whether both the operands refer to the same object or not
-
"""

TIME_TAKEN_MINUTES = 30
