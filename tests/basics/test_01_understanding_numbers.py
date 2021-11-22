'''
Understanding the Numbers
'''
__author__ = 'Hari'

# from placeholders import *

# For most of these tests use the interpreter to fill up the blanks.
# type(object) -> returns the object's type.

def test_numbers_types():
    ''' testing the type of the numbers'''
    assert type(7).__name__ == 'int'
    assert type(7.5).__name__ == 'float'
   # assert 'int' == type(10L).__name__
   # In Python 3 the long datatype has been removed and all integer \
   # values are handled by the Int class. The default size of Int will \
   # depend on your CPU architecture.
   # 32 bit systems the default datatype for integers will be 'Int32'->[-2147483648,2147483647]
   # 64 bit systems the default datatype for integers will be \
   # 'Int64'->[-9223372036854775808,9223372036854775807]

def test_numbers_int_arithmetic_operations():
    ''' testing the numbers with arithematic operations'''
    assert 10 + 20 == 30
    assert 10 * 20 == 200
    assert 2 ** 5 == 32
    assert 10 - 20 == -10
    assert 7/3 == 2.3333333333333335

def test_numbers_string_to_int():
    """hint: execute  print int.__doc__ in python console
       to find out what int(..) does"""
    assert int("FF", 16) == 255
    assert int("77", 8) == 63

def test_numbers_int_to_string():
    ''' testing the octal, binary hexa numbers into the strings'''
    assert oct(10) == '0o12'
    assert hex(100) == '0x64'
    assert bin(255) == '0b11111111'

def test_numbers_long():
    """Long is not the long in c"""
    assert 2 ** 200 == 1606938044258990275541962092341162602522202993782792835301376


THREE_THINGS_I_LEARNT = """
- arithematic operations
- string to integer
- integer to string
- long numbers
"""

TIME_TAKEN_MINUTES = 10
