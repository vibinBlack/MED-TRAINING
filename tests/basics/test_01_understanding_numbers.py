__author__ = 'Hari'

from placeholders import *

# For most of these tests use the interpreter to fill up the blanks.
# type(object) -> returns the object's type.

def test_numbers_types():
    assert 'int' == type(7).__name__
    assert 'float' == type(7.5).__name__
    #assert __ == type(10L).__name__     Python 3 treats all integers as long integer, So L has been removed.
    #                                    And it is limited only by available memory.

def test_numbers_int_arithmetic_operations():
    assert 30 == 10 + 20
    assert 200 == 10 * 20
    assert 32 == 2 ** 5
    assert -10 == 10 - 20
    assert 2.3333333333333335 == 7/3

def test_numbers_string_to_int():
    """hint: execute  print int.__doc__ in python console
       to find out what int(..) does"""
    assert 255 == int("FF", 16)
    assert 63 == int("77", 8)

def test_numbers_int_to_string():
    assert '0o12' == oct(10)
    assert '0x64' == hex(100)
    assert '0b11111111' == bin(255)

def test_numbers_long():
    """Long is not the long in c"""
    assert 1606938044258990275541962092341162602522202993782792835301376 == 2 ** 200

"""
three_things_i_learnt = 
-In Python 3 Int and Long are merged together as int
- (/) -gives float value (//) -gives int value
-oct,hel,bin functions can be used to get octal,hexadecimal and binary values of decimal respectively
time_taken_minutes = 10"""




