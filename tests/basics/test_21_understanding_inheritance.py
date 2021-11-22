"""" Understanding Inheritance """
__author__ = 'Hari'

NOTES = '''
 Inheritance is another standard feature of object oriented programming.
 This exercise illustrates the syntax and language features for using inheritance in Python.
'''

# from placeholders import *

def test_inheritance_basic():
    ''' testing inheritance '''
    class Aclass:
        ''' A inherits from object. '''
        def func_f(self):
            ''' pass '''
            # pass

    class Bclass(Aclass):
        ''' B inherits from A or B derives A '''
        def func_g(self):
            ''' pass '''
            # pass

    assert issubclass(Aclass, object) is True
    assert issubclass(Aclass, Aclass) is True
    assert issubclass(Aclass, Bclass) is False

    assert issubclass(Bclass, Aclass) is True
    assert issubclass(Bclass, Bclass) is True
    assert issubclass(Bclass, object) is True

# base class methods are available for derived class objects
def test_inheritance_methods():
    ''' testing inheritance methods '''
    class Aclass:
        ''' A inherits from object. '''
        def func_f(self):
            ''' return string '''
            return "A:f()"

    class Bclass(Aclass):
        ''' B inherits A's behavior (attributes) '''
        def func_g(self):
            ''' return string'''
            return "B:g()"

    var_b = Bclass()
    assert var_b.func_f() == 'A:f()'
    assert var_b.func_g() == 'B:g()'

    var_a = Aclass()
    assert var_a.func_f() == 'A:f()'
    try:
        assert var_a.func_g() is None
    except AttributeError:
        # print(type(e))  #uncomment this line after filling up
        pass

def test_inheritance_overrides():
    ''' testing inheritance overrides '''
    class Aclass:
        ''' A inherits from object '''
        def func_f(self):
            ''' return string '''
            return "A:f()"

        def func_g(self):
            ''' return string '''
            return "A:g()"

    class Bclass(Aclass):
        ''' B can override A's methods '''
        def func_g(self):
            ''' return string '''
            return "B:g()"

    var_a = Aclass()
    assert var_a.func_f() == 'A:f()'
    assert var_a.func_g() == 'A:g()'

    var_b = Bclass()
    assert var_b.func_f() == 'A:f()'
    assert var_b.func_g() == 'B:g()'

def test_inheritance_init():
    ''' testing inheritance init '''
    class Aclass:
        ''' A inherits from object '''
        def __init__(self):
            ''' init function '''
            self.var_a1 = []

        def append(self, obj):
            ''' funtion for append '''
            self.var_a1.append(obj)

    class Bclass(Aclass):
        ''' B inherits from class A '''
        def __init__(self):
            ''' init function '''
            self.var_b1 = []

    var_a = Aclass()
    assert getattr(var_a, "var_a1", None) == []
    assert getattr(var_a, "var_b1", None) is None

    var_b = Bclass()
    assert getattr(var_b, "var_a1", None) is None
    assert getattr(var_b, "var_b1", None) == []

    try:
        var_b.append("orange")
    except AttributeError:
        # print(type(e))  #what happened here?
        pass

    # Since methods of A depend on init being called, we must always
    # chain __init__ to the base class if the derived class overrides it.

    #lets redefine B now, to chain the inits to the base class.
    class Bclass(Aclass):
        ''' lets redefine B now, to chain the init to the base class '''
        def __init__(self):
            ''' init function for class B '''
            Aclass.__init__(self)
            self.var_b1 = "var_b1"

    var_b = Bclass()
    assert getattr(var_b, "var_a1", None) == []
    assert getattr(var_b, "var_b1", None) == 'var_b1'
    var_b.append("orange")
    assert var_b.var_a1 == ['orange']

def test_inheritance_invoking_using_super():
    ''' testing inheritance invoking using super ,
        super can be used instead of explicitly invoking base '''
    class Aclass:
        ''' A inherits from object '''
        def func_f(self):
            ''' self funtion for g'''
            return "A:f()"

        def func_g(self):
            ''' self funtion for g'''
            return "A:g()"

    class Bclass(Aclass):
        ''' B can override A's methods '''
        def func_g(self):
            ''' function g using super '''
            return super().func_g() + ":"+ "B:g()"

    var_b = Bclass()
    assert var_b.func_g() == 'A:g():B:g()'


NOTES_1 = '''
 Inheritance if one of the most abused features of object oriented programming especially by novices.
 Think carefully before using it :). We will cover usage in assignments.
'''

THREE_THINGS_I_LEARNT = """
- Inheritance
- Inheritance methods and overrides
- super keyword
"""

TIME_TAKEN_MINUTES = 60
