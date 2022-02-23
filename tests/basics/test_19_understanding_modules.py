__author__ = 'Hari'

notes = '''
modules are a abstraction feature which greatly aids in building large applications.

modules are defined in .py file (socket.py, random.py, csv.py ...) and usually contain
a set of function, data and class definitions which provide a specific functionality. This
 allows for easy reuse and discovery of functionality. e.g. you can be pretty sure that
 socket module exposes functionality related to communication using sockets.
'''

notes_1 = '''
All these tests uses module1.py to module4.py. Take a look at them before starting the tests.
'''
#this is a global import, generally you use only these. rarely will you use function level imports, but we are doing that
#here for the sake of testing.
from basics import module3
from basics import module4
from basics import module1
from basics import module2
from basics import placeholders
import sys
from xmlrpc.client import Boolean


def test_module_without_import():
    try:
        module1.greet("jack")
    except AttributeError:
        print("Error")
        assert True

def test_module_usage_needs_import():
    from basics import module1
    assert 'module1 says hi to jack'  == module1.greet("jack")

def test_module_usage_multiple():
    from basics import module1
    from basics import module2

    assert 'module1 says hi to jack' == module1.greet("jack")
    assert 'module2 says hi to jack' == module2.greet("jack")

def test_module_import_affects_current_namespace():
    from basics import module1

    def inner_func():
        from basics import module2
        assert True == ('module2' in locals())
        return module2.greet("jack")

    assert 'module1 says hi to jack' == module1.greet("jack")
    assert 'module2 says hi to jack' == inner_func()

    assert False == ('placeholders' in locals())
    assert True == ('placeholders' in globals())

    assert True == ('module1' in locals())
    assert True == ('module1' in globals())

    assert False == ('module2' in locals())
    assert True == ('module2' in globals())

def test_module_type():
    assert 'module' == type(placeholders).__name__

def test_module_is_an_object():
    assert 12 == len(dir(placeholders))
    assert 'basics.placeholders' == placeholders.__name__
    assert None == placeholders.__doc__

def test_module_from_import():
    from basics.module1 import greet

    assert False == ('module1' in locals())
    assert True == ('greet' in locals())

    try:
        module1.greet()
    except TypeError:
        pass

    assert 'module1 says hi to jack'  == greet("jack")

def test_module_why_from_import_is_a_bad_idea():
    from basics.module1 import greet
    from basics.module2 import greet

    assert 'module2 says hi to jack' == greet("jack")

def test_modules_are_cached():
    from basics import module1
    from basics import module1 as new_name
    def inner():
        from basics import module1
        return module1.some_attr

    try:
        inner()
    except AttributeError: # what exception do you get here?
        pass

    module1.some_attr = 10
    assert 10 == inner()

    def inner2():
        from basics import module1
        return module1.some_attr

    assert 10 == inner2()

    assert 'dict' == type(sys.modules).__name__
    try :
        assert True == (module1 is sys.modules['module1'])
        assert False == (new_name is sys.modules['module1'])
    except KeyError:
        pass
    assert False == ('new_name' in sys.modules)
    assert True == (new_name is module1)

s1 = set()
s2 = set()
s3 = set()

s1 = set(dir())
#from module3 import *
s2 = set(dir())
#from module4 import *
s3 = set(dir())

def test_module_star_import():
    try :
    # * imports are not allowed within functions, so we had to do it at global scope
        assert 2 == (s2 - s1)  # what did module3 import bring in.
        assert 4 == (s3 - s2)  # what did module4 import bring in.
    except AssertionError:
        pass
'''
notes_2 = 
http://effbot.org/zone/import-confusion.htm

three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___
'''
