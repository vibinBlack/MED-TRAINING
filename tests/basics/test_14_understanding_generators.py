''' Generator '''
__author__ = 'Hari'

NOTES = '''
Generators are a easy way to create your own custom iterators. They look like
functions but do a lot of heavy lifting under the covers.

There are also useful when you want to 'generate' data on demand rather than
create all data at one shot - typically in memory constrained scenarios.

You can also think of generators as resumable functions. The caller needs to keep
calling next() to keep moving the function forward and at every stop point where you
have a yield or return the function can return something new.
'''

# from placeholders import *

# The state of the function is saved between yields and re-invoked on call to next.
def demo_generator():
    ''' function for demo generator '''
    yield "how"
    yield "are"
    yield "you?"

def test_generator_type():
    ''' testing the generator types'''
    assert type(demo_generator).__name__ =='function' #definition is a function
    assert type(demo_generator()).__name__ == 'generator' #once you invoke it, you get a generator

def test_generator_is_an_iterator1():
    ''' testing generator is on iterator '''
    assert hasattr(demo_generator, "next") is False
    assert hasattr(demo_generator(), "next") is False

def test_generator_is_an_iterator2():
    ''' testing generator is on iterator '''
    result = demo_generator()
    try:
        assert next(result) == 'how'  # builtin which calls the iterator.next()
        assert next(result) == 'are'
        assert next(result) == 'you?'
        assert next(result) == StopIteration
    except StopIteration:
        assert True

    assert ".".join(demo_generator()) == 'how.are.you?' #join takes a iterable

# Note that this function takes any sequence, and returns a reversed form
# element by element, so at no point is a new reversed sequence object
# created though to the consumer it appears like a sequence.
def demo_reverse(sequence):
    ''' demo function for reverse '''
    for index in range(len(sequence)-1, -1, -1):
        yield sequence[index]


def test_generator_reverse():
    ''' converting generator to reverse '''
    result = []
    for item in demo_reverse("Hello World"):
        result.append(item)
    assert result == ['d', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H']

def test_range_allocates_memory():
    ''' testing the range allocates memory '''
    try:
        for item in range(1000 * (10**6)):
            if item%5 == 1:
                break
    except MemoryError:  # what error do you get when you allocate 1 billion ints?
        assert True

# range using a generator (xrange does something similar)
def demo_range(limit):
    ''' testing the range using generator '''
    value = 0
    while value < limit:
        yield value
        value = value + 1

def test_generator_range_does_not_allocate_memory():
    ''' testing generator range does not allocate memory '''
    for item in demo_range(1000 * (10**6)):
        if item%5 ==1:
            break
    assert True # did you reach here without any memory exception?


#write a statement that can collect all results from the generator into a list
def demo_generator_to_list(generator):
    ''' converting generator to list '''
    result = []
    for i in generator:
        result.append(i)
    return result

def test_collapse_generator():
    ''' testing to collapse generator '''
    assert demo_generator_to_list(demo_range(4)) == [0, 1, 2, 3]
    assert demo_generator_to_list(demo_generator()) == ['how', 'are', 'you?']

def test_generator_return():
    ''' return generator '''
    def func():
        yield 1
        yield 2
        return
        yield 3
    assert demo_generator_to_list(func()) == [1, 2]

def test_generator_control_flow():
    ''' testing control flow for generator '''
    def func():
        for i in range(5):
            yield i
        yield 10
    assert demo_generator_to_list(func()) == [0, 1, 2, 3, 4, 10]

def test_generator_exception():
    ''' testing the generator exceptions '''
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

    assert demo_generator_to_list(func()) == [10, 20, 50, 30]


THREE_THINGS_I_LEARNT = """
- generators
- yield keyword
- memory allocations
"""

TIME_TAKEN_MINUTES = 40
