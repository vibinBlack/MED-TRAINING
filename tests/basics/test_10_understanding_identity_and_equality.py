'''
Identity equality for lists, strings, numbers and none values
'''
__author__ = 'Hari'

# from placeholders import *

NOTES = '''
 Identity and equality are 2 concepts which most beginners are confused about.
 The 'is' operator is used to test identity and == is used to test equality.

 Two objects are identical if they are the same object
 Two objects can be equal even if they are not the same object, if they are of the same type and the type defines some
 equality semantics. E.g. all string objects with content "abc" are equal irrespective of where the objects are in memory,
 two lists can be equal if all elements in them are equal in same order etc.
'''

def test_identity_equality_lists():
    ''' testing identity equality for lists'''
    var_a = []
    var_b = []
    assert (var_a is var_b) is False
    assert (var_a == var_b) is True

    var_a.append("one")
    assert (var_a is var_b) is False
    assert (var_a == var_b) is False

    var_c = []
    var_d = var_c
    assert (var_c is var_d) is True
    assert (var_c == var_d) is True

    var_c.append("one")
    assert (var_c is var_d) is True
    assert (var_c == var_d) is True

def test_identity_equality_string():
    ''' testing identity equality for strings'''
    var_a = var_b = "hello"

    assert (var_a is var_b) is True
    assert (var_a == var_b) is True

    var_c = "hello"
    var_d = "".join(["hel", "lo"])
    assert (var_c is var_d) is False
    assert (var_c == var_d) is True

def test_identity_equality_numbers():
    ''' testing identity equality for numbers'''
    var_a = var_b = 10000
    assert (var_a is var_b) is True
    assert (var_a == var_b) is True

    var_c = 10000
    var_d = int("10000")
    assert (var_c is var_d) is False
    assert (var_c == var_d) is True

def test_identity_equality_small_numbers():
    """
    why do small numbers behave differently? google and find out!
    """
    var_a = var_b = 10
    assert (var_a is var_b) is True
    assert (var_a == var_b) is True

    var_c = 10
    var_d = int("10")
    assert (var_c is var_d) is True
    assert (var_c == var_d) is True

def test_identity_equality_none():
    ''' testing identity equality for None values'''
    var_a = var_b = None
    assert (var_a is var_b) is True
    assert (var_a == var_b) is True

    var_a = None
    var_b = None
    assert (var_a is var_b) is True
    assert (var_a == var_b) is True


NOTES_ON_NONE = '''
None is a builtin constant as you can see above. This allows you to write more
readable code like if x is None: instead of if x == None:
'''

THREE_THINGS_I_LEARNT = """
- Identity equlity for lists
- Identity equlity for strings
- Identity equlity for numbers
"""

TIME_TAKEN_MINUTES = 20
