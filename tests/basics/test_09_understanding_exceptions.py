'''Understanding exceptions'''
__author__ = 'Hari'

from placeholders import *

NOTES = """
Exceptions are the default runtime error reporting mechanism in python.

Most modern languages like c#, java have a similar exception model, so your
understanding will carry forward if you end up learning those languages.
"""

def test_exception_flow_1():
    '''Testing basic exceptional flow'''
    fruit = "orange"
    result = []
    try:
        fruit = fruit.upper()
        result.append("one")
        fruit.missingmethod() # what happens to the control flow here?
        result.append("two")
    except AttributeError:
        result.append("three")

    assert result == ["one", "three"]

def test_exception_flow_2():
    '''Testing basic exceptional flow'''
    fruit = "orange"
    result = []
    try:
        result.append("one")
        value = 1/0 #division by zero.
        result.append("two")
        fruit.missingmethod() #missing attribute
        result.append("three")
    except AttributeError:
        result.append("four")
    except ZeroDivisionError:
        result.append("five")

    assert result == ["one", "five"]

def test_raise_error():
    '''Testing exception raise statment'''
    result = []
    try:
        result.append("one")
        raise AttributeError("some error here")
    except AttributeError:
        result.append("three")

    assert result == ["one", "three"]

def test_missing_except():
    '''testing any attribute missing exception'''
    result = []
    fruit = "orange"
    try:
        result.append("one")
        #what happens now? fix it with an appropriate try except
        fruit.missingmethod()
        result.append("two")
    except AttributeError:
        result.append("two")

    assert result == ["one", "two"]

def function_with_except(result):
    '''function wit exception handling'''
    fruit = "orange"
    result.append("f:enter")
    try:
        fruit.missingmethod()
    except AttributeError:
        result.append("f:except")

    result.append("f:return")

def function_without_except(result):
    '''function without exception handling'''
    fruit = "orange"
    result.append("f:enter")
    fruit.missingmethod()
    result.append("f:return")

def test_function_call_with_except():
    '''testing calling a function that has exception handling'''
    result = []
    try:
        result.append("m:beforecall")
        function_with_except(result)
        result.append("m:aftercall")
    except AttributeError:
        result.append("m:except")
    assert result == ["m:beforecall", "f:enter", "f:except", "f:return", "m:aftercall"]

def test_function_call_without_except():
    '''testing calling a function without having exception handling'''
    result = []
    try:
        result.append("m:beforecall")
        function_without_except(result)
        result.append("m:aftercall")
    except AttributeError:
        result.append("m:except")
    assert result == ["m:beforecall", "f:enter", "m:except"]

def test_else_on_exception():
    '''testing try else block on exception'''
    result = []
    try:
        result.append("m:beforecall")
        function_with_except(result)
        result.append("m:aftercall")
    except AttributeError:
        result.append("m:except")
    else:
        result.append("m:else")

    assert result == ["m:beforecall", "f:enter", "f:except", "f:return", "m:aftercall", "m:else"]


def test_else_on_no_exception():
    '''testing else on no exception'''
    result = []
    try:
        result.append("m:beforecall")
        function_without_except(result)
        result.append("m:aftercall")
    except AttributeError:
        result.append("m:except")
    else:
        result.append("m:else")

    assert result == ["m:beforecall", "f:enter", "m:except"]

def test_finally_on_exception():
    '''testing finally code block with exception'''
    result = []
    try:
        result.append("m:beforecall")
        function_with_except(result)
        result.append("m:aftercall")
    except AttributeError:
        result.append("m:except")
    else:
        result.append("m:else")
    finally:
        result.append("m:finally")

    assert result == \
        ["m:beforecall", "f:enter", "f:except", "f:return", "m:aftercall", "m:else", "m:finally"]


def test_finally_on_no_exception():
    '''testing finally block without any exception'''
    result = []
    try:
        result.append("m:beforecall")
        function_without_except(result)
        result.append("m:aftercall")
    except AttributeError:
        result.append("m:except")
    else:
        result.append("m:else")
    finally:
        result.append("m:finally")

    assert result == ["m:beforecall", "f:enter", "m:except", "m:finally"]

NOTSE_2 = '''
To understand why exceptions are a good thing for writing applications,
read up the link below after finishing this module.
http://blogs.msdn.com/b/brada/archive/2003/09/30/50403.aspx
'''


THREE_THINGS_I_LEARNT = """
-exceptions, its flow
-else keyword in try block
-
"""

TIME_TAKEN_MINUTES = 30
