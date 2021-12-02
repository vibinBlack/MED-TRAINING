""" Understanding Classes """
__author__ = 'Hari'

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

# from placeholders import *

NOTES_1 = '''
 We are defining the classes in the function scope so that we can redefine them for every test.
 Generally you would define them at the module scope.
'''


# classes are objects too, they have a type, have attributes, can be passed
# to function, held in data structures etc.
def test_classes_are_objects():
    """ testing classes are objecsts """

    class Queue:
        """Queue with push and pop functions."""
        pass

    def get_attr_count(obj):
        return len(dir(obj))

    assert type(Queue).__name__ == 'type'  # note this.
    assert Queue.__doc__ == "Queue with push and pop functions."
    assert get_attr_count(Queue) == 26


def test_classes_are_callable_objects():
    """ testing classes are callable objects """

    class Queue:
        """ testing classes are callable objects """
        pass

    # classes are callable objects just like function objects
    assert callable(Queue) is True


def test_classes_are_object_factories():
    """ testing classes are objects factories """

    class Queue:
        """ testing classes are objects factories """
        pass

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


# if an __init__ method exists it is called with the object that is
# being created, so you can initialize it.
def test_classes_init_constructor():
    """ testing class __init__ constructor """
    test_list = []

    class Queue:
        """ testing class __init__ constructor """

        def __init__(self):
            assert self, "Entered here !"
            test_list.append(self)

    queue_1 = Queue()  # fix to assert to pass this.
    self_argument = test_list[0]
    assert (self_argument is queue_1) is True


def test_classes_init_with_args():
    """ testing class __init__ with arguments """

    class Queue:
        """ testing class __init__ with arguments """

        def __init__(self, name):
            self.name = name

    queue_1 = Queue("q1")
    queue_2 = Queue("q2")

    assert queue_1.name == "q1"
    assert queue_2.name == "q2"

    try:
        queue_3 = Queue()
    except TypeError:
        # print(type(e)) #what error do you get?
        pass


# just like def, class is also a runtime statement which bounds a class name with the class body code
def test_class_is_an_executable_statement():
    """ testing class is an executable statement """

    def create_class(value):
        """ testing class is an executable statement """
        if value > 10:
            class Queue:
                """ testing class is an executable statement """

                def __init__(self):
                    self.name = ">10queue"
        else:
            class Queue:
                """ testing class is an executable statement """

                def __init__(self):
                    self.name = "<=10queue"

        return Queue

    Q_class = create_class(20)
    queue_1 = Q_class()
    assert queue_1.name == '>10queue'

    Q_class = create_class(5)
    queue_1 = Q_class()
    assert queue_1.name == '<=10queue'


# the self argument name is just a convention, but it is
# followed widely, so don't change the name of the first argument
# this is in contrast to other languages where the instance is implicit via
# the 'this' keyword.
def test_classes_methods():
    """ testing class methods """

    class Queue:
        """ testing class methods """

        def __init__(self, name):
            self.name = name
            self._queue = []

        def push(self, obj):
            """ function to append """
            self._queue.append(obj)

        def pop(self):
            """ function to remove """
            return self._queue.pop(0)

    queue_1 = Queue("q1")
    queue_1.push(10)  # note that we pass only one argument
    assert queue_1.pop() == 10

    # above is a equivalent to
    Queue.push(queue_1, 10)
    assert Queue.pop(queue_1) == 10


def test_classes_bound_and_unbound_methods():
    """ testing bound and unbound methods in classes """

    class Queue:
        """ testing bound and unbound methods in classes """

        def __init__(self, name):
            self.name = name
            self._queue = []

        def push(self, obj):
            """ function to append """
            self._queue.append(obj)

        def pop(self):
            """ function to remove """
            return self._queue.pop(0)

    queue_1 = Queue("q1")
    q1_push = queue_1.push

    assert (queue_1.push is Queue.push) is False

    assert Queue.push.__class__.__name__ == 'function'  # unbound method
    assert q1_push.__class__.__name__ == 'method'  # bound method

    # now understand the output of these 2 statements.
    print(q1_push)
    print(Queue.push)


def test_classes_can_have_state():
    """ testing classes can have state """

    class Queue:
        """ testing classes can have state """
        count = 0

        def __init__(self, name):
            self.name = name
            self._queue = []
            Queue.count += 1

        def push(self, obj):
            """ function to append """
            self._queue.append(obj)

        def pop(self):
            """ function to remove """
            return self._queue.pop(0)

    assert Queue.count == 0
    queue_1 = Queue("q1")
    assert Queue.count == 1
    queue_2 = Queue("q2")
    assert Queue.count == 2

    try:
        value = queue_1.count
    except Exception:
        # print(type(e))
        pass


THREE_THINGS_I_LEARNT = """
- classes and objects
- init constructors, methods
- bounded and unbounded methods
"""

TIME_TAKEN_MINUTES = 60
