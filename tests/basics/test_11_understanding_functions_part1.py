'''
Funtions Part1
'''
__author__ = 'Hari'

# from placeholders import *

NOTES = '''
Functions are the basic unit of modularization in python. You use functions to group
together a meaningful action and use it when you need it.

The feature set of functions in python is richer than every major programming
language and makes it easy to expose elegant and usable apis.

This is a big topic, we will revisit this topic again.
'''


def my_print(var_x):
    '''print the object'''
    print (var_x)


def my_increment(var_x):
    ''' incrementing the object by 1'''
    return var_x + 1


def my_min_max(numbers):
    ''' return minimum and maximum of the object'''
    return min(numbers), max(numbers)

# functions are kinds of objects, they have a type too!
def test_function_type():
    ''' testing funtion types'''
    assert type(my_print).__name__ == 'function'
    assert type(my_increment).__name__ == 'function'
    assert type(test_function_type).__name__ == 'function'

# functions are objects which can be 'called'
def test_function_callable_type():
    ''' testing callable type functions'''
    assert callable(1) is False
    assert callable(my_increment) is True
    assert callable(my_increment(10)) is False

# functions can be held by references just like any other object
def test_function_assignment():
    ''' testing function assignment'''
    demo = my_increment
    result = demo(20)
    assert result == 21

# every function returns an object, even when it does not!
def test_every_function_returns_something():
    ''' testing every function return something'''
    result = my_print(10)
    assert result is None

    result = my_increment(10)
    assert result == 11

    result = my_min_max([20, 30, 5])
    assert result == (5, 30)

def demo1():
    """returns 10"""
    return 10


def demo2():
    '''returns 20'''
    return 20

#The documentation of every function, if the author wrote it, is available at runtime.
#This makes it easy to access help from console or build specialized help commands like help.
def test_function_documentation():
    ''' testing function documentation'''
    assert demo1.__doc__ == 'returns 10'
    assert demo2.__doc__ == 'returns 20'

def my_callfunc(func):
    ''' calling the function in return'''
    return func()

# functions can be passed around.
def test_functions_can_be_passed_as_objects():
    ''' testing the functions by passing as objects'''
    assert my_callfunc(demo1) == 10
    assert my_callfunc(demo2) == 20


def my_greet(greeting, name="world"):
    ''' return the string format'''
    return "{0} {1}".format(greeting, name)


def test_default_arguments():
    ''' testing ddefault arguements '''
    assert my_greet("Hello") == 'Hello world'
    assert my_greet("Hello", "john") == 'Hello john'

def my_add_to_list1(sequence, target=[]):
    """
    Uses a mutable default, usually leads to unexpected behavior
    """
    target.extend(sequence)
    return target


def my_add_to_list2(sequence, target=None):
    """
    Uses None as default and creates a target list on demand.
    """
    if target is None:
        target = []
    target.extend(sequence)


def test_function_defaults_are_evaluated_at_definition_time():
    ''' testing function defaults at definition time'''
    assert my_add_to_list1("hi") == ['h', 'i']
    assert my_add_to_list1("bye") == ['h', 'i', 'b', 'y', 'e']

    assert my_add_to_list2("hi") is None
    assert my_add_to_list2("bye") is None


def demo_parameter_passing1(obj_x):
    '''passing demo parameter'''
    obj_x = obj_x + 1


def demo_parameter_passing2(names):
    '''passing demo parameter'''
    names = []


def demo_parameter_passing3(names):
    '''passing demo parameter'''
    names.append("something")

# read up after you finish this to make sure you get this
# right: http://effbot.org/zone/call-by-object.html
def test_function_params_passed_by_object_reference():
    ''' testing function parameters which are passed by object reference'''
    var_x = 10
    demo_parameter_passing1(var_x)
    assert var_x == 10

    names = ["one", "two"]
    demo_parameter_passing2(names)
    assert names == ['one', 'two']

    demo_parameter_passing3(names)
    assert names == ['one', 'two', 'something']


THREE_THINGS_I_LEARNT = """
- Fucntion types
- checking callable or not
- return in functions
- function assignment
- passing functions as an objects
"""

TIME_TAKEN_MINUTES = 60
