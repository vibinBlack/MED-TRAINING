__author__ = 'Hari'

from basics import placeholders

notes = '''
This lesson introduces the basic assert statement in python. assert is generally used to 'assert' the truth of an
expression. It takes the form assert <expr>, <optional message>. If <expr> evaluates to False an AssertionError is raised with
the <optional message>. If is evaluates to True, nothing happens.

 In the tests below, replace the blanks with values so that the resulting expression is True.
'''


def test_assert_true():
    #throws assertion error
    assert True #This should be True -- replace ___ with True.

def test_assert_true_with_message():
    assert True  # replace ___ with True to stop seeing the assertion error

def test_assert_equality():
    assert 7 == 2 + 5   #replace __ with the expected value

#Fill in __ in the statements below to make the asserts succeed
def test_make_assert_true_1():
    assert 77 > 7, "Fill in a value greater than 7"
#you can use the interpreter to find the value of 2**30
def test_make_assert_true_2():
    assert (2**30 + 1) > 2**30, "Fill in value greater than 2**30"

def test_make_assert_true_3():
    s1 = "Hello, World"
    s2 = "Hello, World"
    assert s1 == s2

''' three_things_i_learnt = """
I've learnt what assert statement is, I understood how it is used in programs
"""

time_taken_minutes = 1-2 minutes
'''

