''' ITERATORS '''
__author__ = 'Hari'

# from placeholders import *

NOTES = '''
Iterators are objects that represent a stream of data. next() method on an iterator returns
the next available element. StopIteration is raised when elements are finished.

Python builtins like sequences (strings, lists, tuples), sets and dicts are iterable (ie) you can call iter(obj) on them
and get an iterator object on their data.

Iterators allows us to write functions and implement language features which can
work with any iterable instead of having specialized implementation for each of
list, tuple, string etc.
'''

def test_iterator_type():
    ''' testing iterator type'''
    list_iter = iter(["one", "two", "three"])
    assert type(list_iter).__name__ == 'list_iterator'
    assert hasattr(list_iter, "next") is False

    string_iter = iter("hello")
    assert type(string_iter).__name__ == 'str_iterator'
    assert hasattr(string_iter, "next") is False

    tuple_iter = iter((1,2,3))
    assert type(tuple_iter).__name__ == 'tuple_iterator'
    assert hasattr(tuple_iter, "next") is False

def test_int_iterable():
    ''' testing the integer iterables'''
    try:
        iter(10)
    except TypeError:  # replace by appropriate except so this test passes
        pass

def test_enumerate_iter():
    ''' testing the enumerate iter'''
    list_iter = iter(["one", "two", "three"])
    try:
        assert list_iter.__next__() == 'one'
        assert list_iter.__next__() == 'two'
        assert list_iter.__next__() == 'three'
        assert list_iter.__next__() == StopIteration #note what happens when items are finished.
    except StopIteration:
        pass

#note this function which can convert any iterable into a list.
def convert_to_list(iterable):
    ''' convert the iterables to list '''
    seq_iterator = iter(iterable)
    result = []
    try:
        while True:
            item = seq_iterator.__next__()
            result.append(item)
    except StopIteration:
        return result

def test_convert():
    ''' testing the the function conversions '''
    assert convert_to_list("hello") == ['h', 'e', 'l', 'l', 'o']
    assert convert_to_list((1,2,3,4)) == [1, 2, 3, 4]
    assert convert_to_list(range(5)) == [0, 1, 2, 3, 4]
    #string.join also works using the iteration protocol!
    #accepts any iterable
    assert ".".join("hello") == 'h.e.l.l.o'
    assert ".".join(["hello", "world"]) == 'hello.world'
    assert ".".join(("hello", "there")) == 'hello.there'

    try:
        ".".join([1,2,4]) #does not accept all element types though!
    except TypeError:
        assert True

# list creation also uses the iterator protocol!
# note via help(list). we have already used this, you know how it works now!
def test_list_creation():
    ''' testing list creation'''
    assert list("hello") == ['h', 'e', 'l', 'l', 'o']
    assert list((1,2,3,4)) == [1, 2, 3, 4]
    assert list(range(5)) == [0, 1, 2, 3, 4]

# tuple constructor function works the same way!
def test_tuple_creation():
    ''' testing tuple creation'''
    assert tuple("hello") == ('h', 'e', 'l', 'l', 'o')
    assert tuple([1,2,3,5]) == (1, 2, 3, 5)
# Note that none of these functions below know which exact type they are working
# with, as long as their parameters support the iterator protocol they will work.
# Consider the immense productivity gain you have with this approach.
def test_functions_that_work_on_iterables():
    ''' testing the functions that word on iterables'''
    test_dict = {"one": 1, "two":2}
    assert sorted(test_dict) == ["one", "two"]
    assert list(test_dict) == ["one", "two"]

# Go through the functions at http://docs.python.org/2/library/functions.html
# and enter all the functions that operate on iterables into the funcs list.
def test_find_builtins_that_work_on_iterables():
    ''' finding the builints that work on iterables'''
    funcs = [iter, tuple, list, set, dict, any]
    assert len(funcs) == 6


THREE_THINGS_I_LEARNT = """
- Iterators
- types of iterators
- conversion of iterators
"""

TIME_TAKEN_MINUTES = 30
