'''Understanding nested functions'''
__author__ = 'Hari'

from placeholders import *

NOTES = '''
nested functions underlie many advanced features of python. So a basic understanding of this
feature is essential to mastering python.

nested functions are defined in the scope of a function, behave exactly the same except
that they have a read only access to variables in the outer function.
'''

def outer_func(outer_var):
    '''outer function'''
    def inner_func(inner_var):
        '''inner function'''
        return outer_var + inner_var
    return inner_func

def test_inner_func_scope():
    '''test inner function scope'''
    # inner_func not accessible by default
    try:
        inner_func()
    except NameError:  # fill up the exception
        pass

    # this syntax does not work either, it is not just static scoping.
    try:
        outer_func.inner_func()
    except AttributeError: # fillup the exception
        pass

def test_inner_func_can_be_returned():
    '''testing inner function can be returned'''
    func_1 = outer_func(10)
    assert type(func_1).__name__ == 'function'
    assert func_1(20) == 30

def test_each_invocation_returns_a_new_func():
    '''testing each calling of a function returns a new function'''
    func_1 = outer_func(10)
    func_2 = outer_func(10)

    assert (func_1 is func_2) is False
    assert (func_1 == func_2) is False

    func_3 = func_2
    assert (func_3 is func_2) is True
    assert (func_3 == func_2) is True

def test_inner_func_has_access_to_outer_variables_after_return():
    '''testing inner function has access to variable of outer fucntion after return'''
    func_1 = outer_func(20)
    func_2 = outer_func(50)

    assert func_1(30) == 50
    assert func_1(40) == 60

    assert func_2(30) == 80
    assert func_2(40) == 90

def print_attributes(obj):
    '''print attributs of given object'''
    for attr in dir(obj):
        print("attribute: " + attr)
        print(getattr(obj, attr))

def test_inner_func_attributes():
    '''test inner function attributes'''
    func_1 = outer_func(10)
    assert len(dir(func_1)) == 35 #how many attributes does f1 have

    # use the print_attributes function to explore the properties
    # fill up the attribute name that you think holds a reference to the
    # function scope variables
    ref_to_outer_scope = outer_func


# if you understand this, you have understood nested funcs :)
def test_inner_func_scoping():
    '''test inner function scoping'''
    def outer():
        funcs = []
        for value in range(10):
            def inner():
                return value
            funcs.append(inner)
        result = []
        for func in funcs:
            result.append(func())
        return result

    assert outer() == [9,9,9,9,9,9,9,9,9,9]

# generally you should not write code like this :), this is only to learn
def test_outer_scope_is_read_only():
    '''testing outer function variable is read only'''
    var_y = 30
    def outer(var_x):
        def inner1():
            var_x = 30
            return var_x
        def inner2():
            return var_x + var_y
        def inner3():
            var_y = 10
            return var_x + var_y
        return [inner1(), inner2(), inner3(), var_x, var_y]

    assert outer(20) == [30,50,30, 20, 30]

# def is an executable statement. the function name is nothing more than a name
# binding to a code object! So same scope rules as variables apply to function names.
# read up more at http://effbot.org/zone/default-values.htm
def test_def_is_a_statement():
    '''testing def is a statment'''
    def outer(var_x):
        if var_x > 10:
            def inner():
                return var_x * 2
        else:
            def inner():
                return var_x * 3
        return inner

    assert outer(20)() == 40
    assert outer(5)() == 15


THREE_THINGS_I_LEARNT = """
-nested functions
-
-
"""

TIME_TAKEN_MINUTES = 45
