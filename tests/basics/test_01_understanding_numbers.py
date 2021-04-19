__author__ = 'Hari'

from placeholders import *

# For most of these tests use the interpreter to fill up the blanks.
# type(object) -> returns the object's type.

def test_numbers_types():
    assert __ == type(7).__name__
    assert __ == type(7.5).__name__
    assert __ == type(10L).__name__

def test_numbers_int_arithmetic_operations():
    assert __ == 10 + 20
    assert __ == 10 * 20
    assert __ == 2 ** 5
    assert __ == 10 - 20
    assert __ == 7/3

def test_numbers_string_to_int():
    """hint: execute  print int.__doc__ in python console
       to find out what int(..) does"""
    assert __ == int("FF", 16)
    assert __ == int("77", 8)

def test_numbers_int_to_string():
    assert __ == oct(10)
    assert __ == hex(100)
    assert __ == bin(255)

def test_numbers_long():
    """Long is not the long in c"""
    assert __ == 2 ** 200


three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = __




