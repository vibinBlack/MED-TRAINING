""" NESTED FUNCTIONS """
__author__ = 'Hari'

NOTES = '''
nested functions underlie many advanced features of python. So a basic understanding of this
feature is essential to mastering python.

nested functions are defined in the scope of a function, behave exactly the same except
that they have a read only access to variables in the outer function.
'''


# from placeholders import *

def outer_func(outer_var):
    """ testing outer function returns inner function """

    def inner_func(inner_var):
        return outer_var + inner_var

    return inner_func


def test_inner_func_scope():
    """ inner_func not accessible by default """
    try:
        inner_func()
    except NameError:
        # print(type(e))  # fill up the exception
        pass

    # this syntax does not work either, it is not just static scoping.
    try:
        outer_func.inner_func()
    except AttributeError:
        # print(type(e)) # fill up the exception
        pass


def test_inner_func_can_be_returned():
    """ testing inner function can be returned """
    fun_1 = outer_func(10)
    assert type(fun_1).__name__ == 'function'
    assert fun_1(20) == 30


def test_each_invocation_returns_a_new_func():
    """ testing each invocation returns a new function """
    fun_1 = outer_func(10)
    fun_2 = outer_func(10)

    assert (fun_1 is fun_2) is False
    assert (fun_1 == fun_2) is False

    fun_3 = fun_2
    assert (fun_3 is fun_2) is True
    assert (fun_3 == fun_2) is True


def test_inner_func_has_access_to_outer_variables_after_return():
    """ testing inner function has access to outer variables after return """
    fun_1 = outer_func(20)
    fun_2 = outer_func(50)

    assert fun_1(30) == 50
    assert fun_1(40) == 60

    assert fun_2(30) == 80
    assert fun_2(40) == 90


def print_attributes(obj):
    """ function for printing attributes """
    for i in dir(obj):
        print("attribute: " + i)
        print(getattr(obj, i))


def test_inner_func_attributes():
    """ testing inner function attributes """
    fun_1 = outer_func(10)
    assert len(dir(fun_1)) == 35  # how many attributes does f1 have
    print(dir(fun_1))
    # use the print_attributes function to explore the properties
    # fill up the attribute name that you think holds a reference to the
    # function scope variables
    # ref_to_outer_scope = __


# if you understand this, you have understood nested funcs :)
def test_inner_func_scoping():
    """ testing scope for inner function """

    def outer():
        funcs = []
        for i in range(10):
            def inner():
                return i

            funcs.append(inner)
        result = []
        for func in funcs:
            result.append(func())
        return result

    assert outer() == [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]


# generally you should not write code like this :), this is only to learn
def test_outer_scope_is_read_only():
    """ testing outer scope is read only """
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

    assert outer(20) == [30, 50, 30, 20, 30]


# def is an executable statement. the function name is nothing more than a name
# binding to a code object! So same scope rules as variables apply to function names.
# read up more at http://effbot.org/zone/default-values.htm
def test_def_is_a_statement():
    """ testing def is a statement """

    def outer(var_x):
        if var_x > 10:
            def fun_0():
                return var_x * 2
        else:
            def fun_0():
                return var_x * 3
        return fun_0

    assert outer(20)() == 40
    assert outer(5)() == 15


THREE_THINGS_I_LEARNT = """
- Nested functions
- Scope for inner functions
- Scope for outer functions
"""

TIME_TAKEN_MINUTES = 60
