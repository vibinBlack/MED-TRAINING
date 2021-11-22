'''Understanding classes'''
__author__ = 'Hari'

from placeholders import *

NOTES = '''
Python allows users to add user defined types via classes. This allows you to augment
builtin types like dict, list, tuple with your own types with their own specific behavior.

Like most common languages like java and c#, python supports objected oriented features
like class definitions, inheritance and polymorphism.

However, unlike java and c#, python does not insist that you have to forcibly model your
problem domain as classes if it does not make sense. You could use any mix of modules,
functions and classes to model your application. For e.g. if you goal is to code up the
fibonacci function or write a routine that sorts a sequence then defining a class
does not make sense.

This assignment only deals with the syntax of classes and its features. You must
look up references to actually learn object oriented programming.

http://c2.com/cgi/wiki?AlanKaysDefinitionOfObjectOriented
'''


NOTES_1 = '''
 We are defining the classes in the function scope so that we can redefine them for every test.
 Generally you would define them at the module scope.
'''


#classes are objects too, they have a type, have attributes, can be passed
# to functions, held in data structures etc.
def test_classes_are_objects():
    '''Testing classes are objects'''
    class Queue:
        """Queue with push and pop functions."""

    def get_attr_count(obj):
        '''returns the count of attributes in the given object'''
        return len(dir(obj))

    assert type(Queue).__name__ == 'type'  #note this.
    assert Queue.__doc__ == "Queue with push and pop functions."
    assert get_attr_count(Queue) == 26

def test_classes_are_callable_objects():
    '''testing classes are callable objects'''
    class Queue:
        '''class Queue'''

    #classes are callable objects just like function objects
    assert callable(Queue) is True


def test_classes_are_object_factories():
    '''testing classes are object factories'''
    class Queue:
        '''Class queue'''

    queue_1 = Queue()  # you can 'call' a class to create an instance
    queue_2 = Queue()

    assert type(queue_1).__class__ == type
    assert type(queue_2).__class__ == type

    assert (queue_1 is Queue) is False
    assert (queue_2 is Queue) is False
    assert (queue_2 is queue_1) is False

    assert isinstance(queue_1, Queue) is True
    assert isinstance(queue_2, Queue) is True

    assert len(dir(Queue)) == 26
    assert len(dir(queue_1)) == 26
    assert len(dir(queue_2)) == 26


#if an __init__ method exists it is called with the object that is
#being created, so you can initialize it.
def test_classes_init_constructor():
    '''test init constructor'''
    test_list = []

    class Queue:
        '''class queue'''
        def __init__(self):
            assert True, "Entered here !"
            test_list.append(self)

    queue_1 = Queue() # fix the assert to pass this.
    self_argument = test_list[0]
    assert (self_argument is queue_1) is True

def test_classes_init_with_args():
    '''testing __init__ with args'''
    class Queue:
        '''class queue'''
        def __init__(self, name):
            self.name = name

    queue_1 = Queue("q1")
    queue_2 = Queue("q2")

    assert queue_1.name == "q1"
    assert queue_2.name == "q2"

    try:
        queue_3 = Queue()
    except TypeError: #what error do you get?
        pass


#just like def, class is also a runtime statement which bounds a class name with the class body code
def test_class_is_an_executable_statement():
    '''testing class is an executable statment'''
    def create_class(value):
        '''creates a new class'''
        if value > 10:
            class Queue:
                '''Queue class'''
                def __init__(self):
                    self.name = ">10queue"
        else:
            class Queue:
                '''Queue class'''
                def __init__(self):
                    self.name = "<=10queue"

        return Queue

    Q_class = create_class(20)
    queue_1 = Q_class()
    assert queue_1.name == ">10queue"

    Q_class = create_class(5)
    queue_1 = Q_class()
    assert queue_1.name == "<=10queue"


# the self argument name is just a convention but it is
# followed widely, so don't change the name of the first argument
# this is in contrast to other languages where the instance is implicit via
# the 'this' keyword.
def test_classes_methods():
    '''test class methods'''
    class Queue:
        '''class Queue'''
        def __init__(self, name):
            self.name = name
            self._queue = []

        def push(self, obj):
            '''adds a given object to the queue'''
            self._queue.append(obj)

        def pop(self):
            '''removes the first object in the queue'''
            return self._queue.pop(0)

    queue_1 = Queue("q1")
    queue_1.push(10) #note that we pass only one argument
    assert queue_1.pop() == 10

    #above is a equivalent to
    Queue.push(queue_1, 10)
    assert Queue.pop(queue_1) == 10


def test_classes_bound_and_unbound_methods():
    '''test bound and unbound methods'''
    class Queue:
        '''class Queue'''
        def __init__(self, name):
            self.name = name
            self._queue = []

        def push(self, obj):
            '''add given object to the queue'''
            self._queue.append(obj)

        def pop(self):
            '''remove the first element in the queue'''
            return self._queue.pop(0)

    queue_1 = Queue("q1")
    q1_push = queue_1.push

    assert (queue_1.push is Queue.push) is False

    #assert None == Queue.push.__self__   #unbound method
    #assert None == q1_push.__self__      #bound method

    # now understand the output of these 2 statements.
    print (queue_1.push)
    print (Queue.push)

def test_classes_can_have_state():
    '''testing class have states'''
    class Queue:
        '''class Queue'''
        count = 0
        def __init__(self, name):
            self.name = name
            self._queue = []
            Queue.count += 1

        def push(self, obj):
            '''add a new object to the queue'''
            self._queue.append(obj)

        def pop(self):
            '''remove the first object from the queue'''
            return self._queue.pop(0)

    assert Queue.count == 0
    queue_1 = Queue("q1")
    assert Queue.count == 1
    queue_2 = Queue("q2")
    assert Queue.count == 2

    try:
        value = queue_1.count
    except NameError:
        pass


THREE_THINGS_I_LEARNT = """
-classes and their instances
-
-
"""

TIME_TAKEN_MINUTES = 60
