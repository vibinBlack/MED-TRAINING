""" Understanding Modules """
import sys

import placeholders
# from placeholders import *

__author__ = 'Hari'

NOTES = '''
modules are a abstraction feature which greatly aids in building large applications.

modules are defined in .py file (socket.py, random.py, csv.py ...) and usually contain
a set of function, data and class definitions which provide a specific functionality. This
 allows for easy reuse and discovery of functionality. e.g. you can be pretty sure that
 socket module exposes functionality related to communication using sockets.
'''

NOTES_1 = '''
All these tests uses module1.py to module4.py. Take a look at them before starting the tests.
'''
#this is a global import, generally you use only these. rarely will you use function level imports,
#but we are doing that here for the sake of testing.

def test_module_without_import():
    ''' testing module without import '''
    try:
        module1.greet("jack")
    except NameError:
        # print(type(e))
        assert True

def test_module_usage_needs_import():
    ''' testing usage of module needs import '''
    import module1
    assert module1.greet("jack") == 'module1 says hi to jack'

def test_module_usage_multiple():
    ''' testing usage of multiple modules '''
    import module1
    import module2

    assert module1.greet("jack") == 'module1 says hi to jack'
    assert module2.greet("jack") == 'module2 says hi to jack'

def test_module_import_affects_current_namespace():
    ''' testing module import affects current namespace '''
    import module1

    def inner_func():
        import module2
        assert ('module2' in locals()) is True
        return module2.greet("jack")

    assert module1.greet("jack") == 'module1 says hi to jack'
    assert inner_func() == 'module2 says hi to jack'

    assert ('placeholders' in locals()) is False
    assert ('placeholders' in globals()) is True

    assert ('module1' in locals()) is True
    assert ('module1' in globals()) is False

    assert ('module2' in locals()) is False
    assert ('module2' in globals()) is False

def test_module_type():
    ''' testing module type '''
    assert type(placeholders).__name__ == 'module'

def test_module_is_an_object():
    ''' testing module is an object '''
    assert len(dir(placeholders)) == 12
    assert placeholders.__name__ == 'placeholders'
    assert placeholders.__doc__ == 'Placeholders'

def test_module_from_import():
    ''' testing module from import'''
    from module1 import greet

    assert ('module1' in locals()) is False
    assert ('greet' in locals()) is True

    try:
        module1.greet()
    except NameError:
        # print(type(e))
        pass

    assert greet("jack") == 'module1 says hi to jack'

def test_module_why_from_import_is_a_bad_idea():
    '''  testing module why from import is a bad idea '''
    from module1 import greet
    from module2 import greet

    assert greet("jack") == 'module2 says hi to jack'

def test_modules_are_cached():
    ''' Testing the modules are cached '''
    import module1
    import module1 as new_name
    def inner():
        import module1
        return module1.some_attr

    try:
        inner()
    except AttributeError:
        # print(type(e)) # what exception do you get here?
        pass

    module1.some_attr = 10
    assert inner() == 10

    def inner2():
        import module1
        return module1.some_attr

    assert inner2() == 10

    assert type(sys.modules).__name__ == 'dict'
    assert (module1 is sys.modules['module1']) is True
    assert ('new_name' in sys.modules) is False
    assert (new_name is module1) is True
    assert (new_name is sys.modules['module1']) is True

s1 = set()
s2 = set()
s3 = set()

s1 = set(dir())
from module3 import *
s2 = set(dir())
from module4 import *
s3 = set(dir())

def test_module_star_import():
    ''' testing module star import '''
    # * imports are not allowed within functions, so we had to do it at global scope
    assert (s2 - s1) == {'m3_func1', 'm3_func2'}  # what did module3 import bring in.
    assert (s3 - s2) == {'m4_func1', '_m4_func3'}  # what did module4 import bring in.

NOTES_2 = '''
http://effbot.org/zone/import-confusion.html
'''

THREE_THINGS_I_LEARNT = """
- modules
- importing modules
- module attributes
"""

TIME_TAKEN_MINUTES = 60
