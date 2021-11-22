'''
Scope for Local variables and Global variables
'''
import inspect
import symtable

__author__ = 'Hari'

NOTES = '''
 Scopes and namespaces govern the accessibility rules and lifetime of python variables.

 Namespaces is a mapping of names to objects. Each python block creates a new namespace. The 3 python blocks are
 modules (files), functions and classes.

 An object can have many names in the same namespace
 An object can have names in different namespaces.

 Scope is a textual area in which a variable can be directly accessible by its name.

 Variable which are bound (created) in a block are called local variables in that block
 Variables which are scoped to the the whole file (module) are called global
 Variables which are scoped to outer functions (in case of nested functions) are called non-local or free.
'''

# from placeholders import *

count = 10

#used to by pass any local shadow variables.
def get_global_count():
    ''' function to return global variable '''
    return count

def test_scope_basic():
    ''' testing the scope '''
    local_names = get_locals(test_scope_basic)

    value = count

    assert ('value' in local_names) is True
    assert ('value' in global_names) is False

    assert ('count' in local_names) is False
    assert ('count' in global_names) is True

    assert count == value

    try:
        my_name = name #name variable is not in local or  global scope
    except NameError : # fill up the exception
        pass

    assert ('my_name' in local_names) is True
    assert ('name' in local_names) is False
    assert ('name' in global_names) is False

def test_variable_shadow():
    ''' testing variable shadow '''
    local_names = get_locals(test_variable_shadow)
    count = 20

    assert ('count' in local_names) is True
    assert ('count' in global_names) is True

    assert count == 20
    assert get_global_count() == 10

def test_global_write():
    ''' testing the global write '''
    local_names = get_locals(test_global_write)

    global count # declare that we want to use the read/write to global count
    count = 30

    try:
        assert ('count' in local_names) is False
        assert ('count' in global_names) is True

        assert count == 30
        assert get_global_count() == 30
    finally:
        count = 10 #reset to original value

def test_scope_is_bound_at_definition_time():
    ''' testing the scope is bound at definition time '''
    local_names = get_locals(test_scope_is_bound_at_definition_time)

    assert ('count' in local_names) is True
    assert ('count' in global_names) is True

    try:
        value = count
        count = 30
    except UnboundLocalError: # what happens when you read a variable before initializing it?
        # print(ex) #uncomment after you fill up above
        assert True
    finally:
        count = 20

    assert count == 20
    assert get_global_count() == 10


def test_scope_writing_globals():
    ''' testing the scope for writing globals '''
    local_names = get_locals(test_scope_writing_globals)

    assert ('count' in local_names) is False
    assert ('count' in global_names) is True

    global count

    try:
        count = 40
        assert count == 40
        assert get_global_count() == 40
    finally:
        count = 10

    assert get_global_count() == 10



THREE_THINGS_I_LEARNT = """
- local variables
- global variables
- scope for both
"""

TIME_TAKEN_MINUTES = 60


#helper functions which get the variables in locals and globals using the compiler's symbol tables.
def get_locals(func):
    ''' function to get locals '''
    source = inspect.getsource(func)
    top = symtable.symtable(source, "<string>", "exec")
    func = top.get_children()[0]  #since we are passing only the func code.
    return func.get_locals()

def get_globals():
    ''' function to get globals '''
    module = inspect.getmodule(get_globals)
    source = inspect.getsource(module)
    top = symtable.symtable(source, "<string>", "exec")
    return top.get_identifiers()

global_names = get_globals()
