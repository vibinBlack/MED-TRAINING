'''UNDERSTANDING STRINGS'''
__author__ = 'Hari'

from placeholders import *

NOTES = """string is one of the most commonly used data types, it has different
behavior than a char* in C."""

def test_string_type():
    '''Testing string type'''
    assert type("Hello World").__name__ == 'str'
    assert True is isinstance("Hello World", str)

def test_single_quoted_strings_are_strings():
    '''Testing single quoted string type'''
    assert True is isinstance('Hello World', str)

def test_double_quoted_strings_are_strings():
    '''Testing double quoted string type'''
    assert True is isinstance("Hello World", str)

def test_triple_quoted_strings_are_strings():
    '''Testing triple quoted string type'''
    assert True is isinstance("""Hello World""", str)

def test_triple_single_quoted_strings_are_strings():
    '''Testing triple single quoted string type'''
    assert True is isinstance('''Hello World''', str)

def test_raw_strings_are_strings():
    '''Testing raw string type'''
    assert True is isinstance(r"Hello World", str)

def test_single_quoted_strings_can_have_double_quotes():
    '''testing single quoted strings can have double quotes'''
    first = 'The pilot said "Jump"'
    second = "The pilot said \"Jump\""  #note back slash escaping of "
    are_equal = (first == second)
    assert are_equal is True

def test_double_quoted_strings_can_have_single_quotes():
    '''testing double quoted strings can have single quotes'''
    first = "The pilot said 'Jump'"
    second = 'The pilot said \'Jump\''  #note back slash escaping of '
    are_equal = (first == second)
    assert are_equal is True

def test_triple_quoted_strings_can_have_both_single_and_double_quotes():
    '''testing triple quoted strings can have both single and double quotes'''
    # Edit tq_str to make are_equal True
    tq_str = """ Isn't the "Hobbit" great? """
    dq_str = "Isn't the \"Hobbit\" great?"
    are_equal = (tq_str == dq_str)
    assert are_equal is False

def test_triple_quoted_strings_can_span_lines():
    '''testing tripe quoted strings can span lines'''
    tq_str = """Hello
World"""
    dq_str = "Hello\nWorld"   # what is the double quoted form of tq_str
    assert tq_str == dq_str

def test_string_len():
    '''testing string length'''
    assert len("Hello 'world'") == 13
    assert len('Hello \'world\'') == 13

def test_triple_quoted_strings_span_lines_len_and_type():
    '''testing triple quoted strings length and type with lines'''
    string = """Hello
    World"""
    assert isinstance(string, str) is True
    assert len(string) == 15

def test_strings_can_be_indexed():
    '''testing strings can be indexed'''
    string = "Hello"
    assert string[0] == 'H'
    assert string[1] == 'e'
    assert string[2] == 'l'
    assert string[3] == 'l'
    assert string[4] == 'o'
    assert string[-1] == 'o'   # solves the common use case to iterate from end
    assert string[-2] == 'l'
    assert string[-3] == 'l'
    assert string[-4] == 'e'
    assert string[-5] == 'H'
    assert string[-0] == 'H'   # hint -0 is 0
    assert len(string) == 5
    try:
        out_of_bounds = string[5] #raises an error, we will revisit exceptions later
    except IndexError as exp:
        print(exp)   #string index out of range
        assert True  #make this True to proceed.

def test_chars_are_strings_too():
    '''testing char type'''
    string = "Hello"
    first_char = string[0]
    assert type(first_char).__name__ == 'str'
    assert type('a').__name__ == 'str'
    assert type("a").__name__ == 'str'

def test_strings_are_immutable():
    """ strings in python cannot be modified unlike in C """
    string = "Hello"
    try:
        string[0] = "M"
    except TypeError as exp:
        print(exp)
        assert True

def test_string_concat():
    '''testing string concatenation'''
    assert "Hello " + " world" == "Hello  world"
    assert """Hello """ + 'world' == "Hello world"
    assert 'Hello ' + "world" == "Hello world"


def test_string_slicing():
    """ Slicing creates new strings """
    string = "Hello world"
    #with begin : end
    assert string[0:0] == ''

    assert string[0:2] == 'He'
    assert string[1:5] == 'ello'
    assert string[1:-1] == 'ello worl'
    assert string[2:-2] == 'llo wor'

    #with :end
    assert string[:0] == ''
    assert string[:4] == 'Hell'
    assert string[:-1] == 'Hello worl'

    #with begin:
    assert string[0:] == 'Hello world'
    assert string[4:] == 'o world'
    assert string[-1:] == 'd'

    #observe the invariant
    assert string[:0] + string[0:] == 'Hello world'
    assert string[:1] + string[1:] == 'Hello world'
    assert string[:2] + string[2:] == 'Hello world'
    assert string[:3] + string[3:] == 'Hello world'


def test_string_repeat():
    '''testing string repeatation'''
    assert "Hello" * 3 == "HelloHelloHello"
    assert len("Hello " * 2) == 12

def test_string_combine():
    """
    Use slicing to pass the assert.
    """
    hello = "Hello World"
    bye = "Goodbye moon"
    assert  bye[0:8] + hello[6:]  == "Goodbye World"

def test_string_formatting():
    '''testing string formatting'''
    greeting = "Hello '{0}'".format("learner")
    assert greeting == "Hello 'learner'"

    truth = "{1} plus {1} makes {0}".format("two","one")
    assert truth == "one plus one makes two"

    stmt = "{name} is {age} years old".format(name="Ravi", age=25)
    assert stmt == "Ravi is 25 years old"

def test_string_membership():
    '''Testing string memebership'''
    assert ('c' in 'apple') is False  #is there a precedence issue here?
    assert ('a' in 'apple') is True
    assert ('app' in 'apple') is True
    # '==' and 'in' operators have same precedence
    # And are interpreted from left to right in the expression


THREE_THINGS_I_LEARNT = """
-strings, string slicing and formatting
-
-
"""

TIME_TAKEN_MINUTES = 30
