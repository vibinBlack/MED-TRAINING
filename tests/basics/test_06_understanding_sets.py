'''Understanding sets'''
__author__ = 'Hari'

from placeholders import  *

NOTES = '''
sets are  unordered collection of elements without duplicates. Conceptually they are similar to dicts except that
the keys are not associated with any values.
'''


def test_set_type():
    '''Testing set type'''
    test_set = {"one", "two", "three"}   # note the new syntax
    assert type(test_set).__name__ == 'set'

def test_set_empty():
    '''testing empty set'''
    empty_set_wrong = {}
    #curly braces are used for both sets and dicts, so how do you disambiguate?
    assert isinstance(empty_set_wrong, set) is False

    empty_set = set()
    assert isinstance(empty_set, set) is True
    assert len(empty_set) == 0

def test_set_length():
    '''testing set length'''
    fruits = {"apple", "apple", "apple"}
    assert len(fruits) == 1  #are duplicates removed?

    veggies = {"beetroot", "potato", "spinach"}
    assert len(veggies) == 3

def test_set_creation():
    """
    sets can be created from any sequence like list or a tuple.
    """
    test_list = [1, 2, 1, 3]
    set1 = set(test_list)
    assert set1 == {1,2,3}

    test_string = "apple"
    set2 = set(test_string)
    assert set2 == {'a','p','p','l','e'}

    test_dict = { 1: "one", 2 : "two"}
    set3 = set(test_dict)
    assert set3 == {1,2}

    set4 = set(test_dict.values())
    assert set4 == {'one','two'}

    set5 = set(test_dict.items())
    assert set5 == {(1,'one'),(2,'two')}

def test_set_membership():
    '''testing set membership'''
    fruits = {"apple", "mango", "kiwi"}
    assert ("apple" in fruits) is True
    assert ("dog" in fruits) is False

def test_set_operations():
    '''testing set operations'''
    set1 = {"one", "two", "three"}
    set2  =  {"three", "four"}

    union_set = set1 | set2 # union
    assert union_set == {'one','two','three','four'}

    common = set1 & set2
    assert common == {'three'}

    diff1 = set1 - set2
    assert diff1 == {'one','two'}

    diff2 = set2 - set1
    assert diff2 == {'four'}

    diff3 = set1 - set1
    assert diff3 == set()

    diff4 = set1.symmetric_difference(set2)
    assert diff4 == {'one','two','four'}

    #read up help on other method using the help method in the python console.

def test_set_valid_members():
    '''testing set only contains immutables'''
    test_set = set()
    test_set.add("hello")
    test_set.add(1)
    test_set.add((1,2))

    try:
        test_set.add([])
    except TypeError as exp:
        print (exp)
        assert True

    try:
        test_set.add((1,[]))   #  TypeError: unhashable type: 'list'
    except TypeError as exp:
        print (exp)
        assert True

    assert test_set == {1,'hello',(1,2)}

THREE_THINGS_I_LEARNT = """
-sets, unordered and doesn't allow duplicates
-sets methods
-
"""

TIME_TAKEN_MINUTES = 20
