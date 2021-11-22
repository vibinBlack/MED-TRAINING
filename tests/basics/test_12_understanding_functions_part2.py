'''Understanding functions part 2'''
__author__ = 'Hari'

from placeholders import *

def demo(first, second=2, third=3):
    '''convert keyword arguments to a list'''
    return [first, second, third]

# keyword arguments allows you to write one api without having a large number
# of overloads for various scenarios.
# add extra arguments where necessary.

def test_function_call_with_keyword_arguments():
    '''testing function call with keyword arguments'''
    assert demo(10) == [10, 2, 3]
    assert demo(10, 20) == [10, 20, 3]
    assert demo(10, 20, 30) == [10, 20, 30]
    assert demo(10, second=20) == [10, 20, 3]
    assert demo(10, second=20, third=30) == [10, 20, 30]
    assert demo(first=10, third=30) == [10, 2, 30]
    assert demo(10, third=30) == [10, 2, 30]


def demo_variable_args(first, *args):
    '''demo for variable arguments'''
    return args


def my_merge(separator, *args):
    '''combines the given args'''
    return separator.join(args)


def test_function_with_variable_args():
    '''test function with variable arguments'''
    result = demo_variable_args("hello", "world")
    assert type(result).__name__ == 'tuple'  #this is the type of args
    assert result == ("world",)              #this is the value of args

    assert demo_variable_args("hello", 1, 2, 3) == (1, 2, 3)

    assert my_merge(".", "one", "two", "three") == "one.two.three"
    assert my_merge(",", "one", "two", "three") == "one,two,three"


def demo_with_keyword_args(name, *args, **kwargs):
    '''demo for keyword args'''
    return kwargs


def test_function_with_keyword_args():
    '''test function with keyword args'''
    result = demo_with_keyword_args("jack", age=10, height=100)
    assert type(result).__name__ == 'dict'
    assert result == {"age": 10, "height": 100}
    assert demo_with_keyword_args("jack", "address", age=10, height=100) == \
        {"age": 10, "height": 100}
    assert demo_with_keyword_args("jack", address="address", age=10, height=100) == \
        {"address":"address", "age":10, "height": 100}


def demo_sub(*args, **kwargs):
    '''demo sub'''
    return args, kwargs


def demo_unpacking(name, *args, **kwargs):
    '''demo for unpacking of arguments'''
    return demo_sub(*args, **kwargs)


def demo_no_unpacking(name, *args, **kwargs):
    '''Demo for no unpacking'''
    return demo_sub(args, kwargs)


def test_function_unpacking():
    '''test function unpackign'''
    result = demo_unpacking("jack", 1, 2, k1="v1", k2="v2")
    assert result == ((1,2),{"k1": "v1", "k2": "v2"})

    result = demo_no_unpacking("jack", 1, 2, k1="v1", k2="v2")
    assert result == (((1,2),{"k1": "v1", "k2": "v2"}),{})

    result = demo_sub(1,2, k1="v1")
    assert result == ((1,2),{"k1":"v1"})

    result = demo_sub((1,2), {"k1" :"v1"})
    assert result == (((1,2), {"k1":"v1"}), {})

    result = demo_sub(*(1,2), **{"k1": "v1"})
    assert result == ((1,2), {"k1":"v1"})

    #you can unpack lists as well
    result = demo_sub(*[1,2], **{"k1":"v1"})
    assert result == ((1,2), {"k1":"v1"})



THREE_THINGS_I_LEARNT = """
- About *args
- About **kwargs
- Unpacking
"""

TIME_TAKEN_MINUTES = 40
