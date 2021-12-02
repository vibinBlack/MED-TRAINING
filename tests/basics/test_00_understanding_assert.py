"""
basic assert statements in python
"""

__author__ = 'Hari'

# from placeholders import *

NOTES = '''
This lesson introduces the basic assert statement in python. assert is generally used to 'assert' the truth of an
expression. It takes the form assert <expr>, <optional message>. If <expr> evaluates to False an AssertionError is raised with
the <optional message>. If is evaluates to True, nothing happens.

 In the tests below, replace the blanks with values so that the resulting expression is True.
'''


def test_assert_true():
    """ throws assertion error """
    assert True  # This should be True -- replace ___ with True.


def test_assert_true_with_message():
    """ Assert true with message"""
    assert True, "This is the failure message"
    # replace ___ with True to stop seeing the assertion error


def test_assert_equality():
    """Testing assert equality"""
    assert 2 + 5 == 7  # replace __ with the expected value


# Fill in __ in the statements below to make the asserts succeed
def test_make_assert_true_1():
    """ make to assert true by filling the blank"""
    assert 8 > 7, "Fill in a value greater than 7"


# you can use the interpreter to find the value of 2**30
def test_make_assert_true_2():
    """ make to assert true by filling the blank"""
    assert 2 ** 31 > 2 ** 30, "Fill in value greater than 2**30"


def test_make_assert_true_3():
    """ Testing both the strings are true"""
    s_1 = "Hello, World"
    s_2 = "Hello, World"
    assert s_1 == s_2


THREE_THINGS_I_LEARNT = """
- assert keyword, doc strings
- Comparison operations
- Equality operations
"""

TIME_TAKEN_MINUTES = 10
