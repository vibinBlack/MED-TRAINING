'''Understanding inheritance'''
__author__ = 'Hari'

from placeholders import *

NOTES = '''
 Inheritance is another standard feature of object oriented programming.
 This exercise illustrates the syntax and language features for using inheritance in Python.
'''

def test_inheritance_basic():
    '''Inheritance basic'''
    class ParentA: # ParentA inherits from object.
        '''Parent class'''
        def fun_f(self):
            '''Parent A Function f'''

    class ChildB(ParentA):      #ChildB inherits from ParentA or ChildB derives ParentA
        '''Child class'''
        def fun_g(self):
            '''Child B Function g'''

    assert issubclass(ParentA, object) is True
    assert issubclass(ParentA, ParentA) is True
    assert issubclass(ParentA, ChildB) is False

    assert issubclass(ChildB, ParentA) is True
    assert issubclass(ChildB, ChildB) is True
    assert issubclass(ChildB, object) is True

# base class methods are available for derived class objects
def test_inheritance_methods():
    '''Testing inheritance methods'''
    class ParentA: # ParentA inherits from object.
        '''Parent class'''
        def fun_f(self):
            '''Parent A Function f'''
            return "A:f()"

    class ChildB(ParentA):      #ChildB inherits ParentA's behavior (attributes)
        '''child class'''
        def fun_g(self):
            '''Child B Function g'''
            return "B:g()"

    obj_b = ChildB()
    assert obj_b.fun_f() == "A:f()"
    assert obj_b.fun_g() == "B:g()"

    obj_a = ParentA()
    assert obj_a.fun_f() == "A:f()"
    try:
        assert obj_a.fun_g() is None
    except AttributeError as exp:
        print(exp)  #uncomment this line after filling up

def test_inheritance_overrides():
    '''Testing inheritance overiding methods'''
    class ParentA: # ParentA inherits from object.
        '''Parent class'''
        def fun_f(self):
            '''Parent A Function f'''
            return "A:f()"

        def fun_g(self):
            '''Parent A Function g'''
            return "A:g()"

    class ChildB(ParentA):      #ChildB can override ParentA's methods
        '''child class'''
        def fun_g(self):
            '''Child B Function g'''
            return "B:g()"

    obj_a = ParentA()
    assert obj_a.fun_f() == "A:f()"
    assert obj_a.fun_g() == "A:g()"

    obj_b = ChildB()
    assert obj_b.fun_f() == "A:f()"
    assert obj_b.fun_g() == "B:g()"

def test_inheritance_init():
    '''Checking __init__ cases using inheritance'''
    class ParentA:
        '''Parent class'''
        def __init__(self):
            self.a_1 = []

        def append(self, obj):
            '''Appends a new object'''
            self.a_1.append(obj)

    class ChildB(ParentA):
        '''child class'''
        def __init__(self):
            self.b_1 = []

    obj_a = ParentA()
    assert getattr(obj_a, "a_1", None) == []
    assert getattr(obj_a, "b_1", None) is None

    obj_b = ChildB()
    assert getattr(obj_b, "a_1", None) is None
    assert getattr(obj_b, "b_1", None) == []

    try:
        obj_b.append("orange")
    except AttributeError:  #what happened here?
        pass

    # Since methods of A depend on init being called, we must always
    # chain __init__ to the base class if the derived class overrides it.

    #lets redefine ChildB now, to chain the inits to the base class.
    class ChildB(ParentA):
        '''child class'''
        def __init__(self):
            ParentA.__init__(self)
            self.b_1 = "b1"

    obj_b = ChildB()
    assert getattr(obj_b, "a_1", None) == []
    assert getattr(obj_b, "b_1", None) == "b1"
    obj_b.append("orange")
    assert obj_b.a_1 == ["orange"]

def test_inheritance_invoking_using_super():
    '''Testing inheritance using'''
    #super can be used instead of explicitly invoking base.
    class ParentA: # ParentA inherits from object.
        '''Parent class'''
        def fun_f(self):
            '''Parent A Function f'''
            return "A:f()"

        def fun_g(self):
            '''Parent A Function g'''
            return "A:g()"

    class ChildB(ParentA):      #ChildB can override ParentA's methods
        '''child class'''
        def fun_g(self):
            '''Child B Function g'''
            return super().fun_g() + ":"+ "B:g()"

    obj_b = ChildB()
    assert obj_b.fun_g() == "A:g():B:g()"


NOTES_1 = '''
 Inheritance if one of the most abused features of object oriented programming especially by novices.
 Think carefully before using it :). We will cover usage in assignments.
'''

THREE_THINGS_I_LEARNT = """
-inheritance of classes
-overriding
-super keyword
"""

TIME_TAKEN_MINUTES = 30
