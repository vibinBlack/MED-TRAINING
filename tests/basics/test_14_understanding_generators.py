'''Understanding generators'''
__author__ = 'Hari'

from placeholders import *

NOTES = '''
Generators are a easy way to create your own custom iterators. They look like
functions but do a lot of heavy lifting under the covers.

There are also useful when you want to 'generate' data on demand rather than
create all data at one shot - typically in memory constrained scenarios.

You can also think of generators as resumable functions. The caller needs to keep
calling next() to keep moving the function forward and at every stop point where you
have a yield or return the function can return something new.
'''

# The state of the function is saved between yields and re-invoked on call to next.
def demo_generator():
    '''generator demo'''
    yield "how"
    yield "are"
    yield "you?"

def test_generator_type():
    '''testing generator type'''
    assert type(demo_generator).__name__ == 'function'  #definition is a function
    assert type(demo_generator()).__name__ == 'generator' #once you invoke it, you get a generator

def test_generator_is_an_iterator1():
    '''testing generator is an iterator'''
    assert hasattr(demo_generator, "next") is False
    assert hasattr(demo_generator(), "next") is False

def test_generator_is_an_iterator2():
    '''testing generator is an iterator'''
    result = demo_generator()
    try:
        assert next(result) == "how"  # builtin which calls the iterator.next()
        assert next(result) == "are"
        assert next(result) == "you?"
        assert next(result) is None
    except Exception:
        assert True

    assert ".".join(demo_generator()) == "how.are.you?" #join takes a iterable

# Note that this function takes any sequence, and returns a reversed form
# element by element, so at no point is a new reversed sequence object
# created though to the consumer it appears like a sequence.
def demo_reverse(sequence):
    '''reverses a given sequence'''
    for index in range(len(sequence)-1, -1, -1):
        yield sequence[index]


def test_generator_reverse():
    '''testing generator reverse'''
    result = []
    for item in demo_reverse("Hello World"):
        result.append(item)
    assert result == ["d", "l","r","o","W"," ","o","l","l","e","H"]

def test_range_allocates_memory():
    '''test range() will allocate memory'''
    try:
        for item in range(1000 * (10**6)):
            if item%5 == 1:
                break
    except MemoryError:  # what error do you get when you allocate 1 billion ints?
        assert True

# range using a generator (xrange does something similar)
def demo_range(limit):
    '''range using a genrator'''
    value = 0
    while value < limit:
        yield value
        value = value + 1

def test_generator_range_does_not_allocate_memory():
    '''testing generator range does not allocate memory'''
    for item in demo_range(1000 * (10**6)):
        if item%5 ==1:
            break
    assert True # did you reach here without any memory exception?


#write a statement that can collect all results from the generator into a list
def demo_generator_to_list(generator):
    '''convert a generator sequence to list'''
    # fill code here.
    result = []
    for item in generator:
        result.append(item)
    return result


def test_collapse_generator():
    '''test collapse generator'''
    assert [0,1,2,3] == demo_generator_to_list(demo_range(4))
    assert ["how", "are", "you?"] == demo_generator_to_list(demo_generator())

def test_generator_return():
    '''test generator return'''
    def func():
        yield 1
        yield 2
        return
        yield 3
    assert [1,2] == demo_generator_to_list(func())

def test_generator_control_flow():
    '''testing generator control flow'''
    def func():
        for val in range(5):
            yield val
        yield 10
    assert demo_generator_to_list(func()) == [0,1,2,3,4,10]

def test_generator_exception():
    '''testing generator exception'''
    def func():
        try:
            yield 10
            raise Exception("some message")
        except Exception:
            yield 20
        else:
            yield 40
        finally:
            yield 50
        yield 30

    assert demo_generator_to_list(func()) == [10,20,50,30]


THREE_THINGS_I_LEARNT = """
-yeild keyword
-generators
-memory error
"""

TIME_TAKEN_MINUTES = 40
