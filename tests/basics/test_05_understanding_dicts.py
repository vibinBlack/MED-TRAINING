'''
Dictionary and Its Methods
'''
__author__ = 'Hari'

# from placeholders import *

NOTES = '''
dicts are unordered sets of key value pairs which facilitate
fast lookups by key.
'''

def test_dictionary_type():
    '''dictionary type'''
    test_dict = {1 : "one"}   # note the new syntax
    assert type(test_dict).__name__ == 'dict'

def test_dictionary_empty():
    ''' empty dictionary'''
    empty_dict_1 = {}
    assert isinstance(empty_dict_1, dict) is True

    empty_dict_2 = dict() # another way of creating empty dict
    assert len(empty_dict_2) == 0

    assert empty_dict_1 == empty_dict_2

def test_dictionary_create():
    ''' creating a dictionary'''
    dict_1 = { 1 : "one", 2 : "two" }
    assert isinstance(dict_1, dict) is True

    #init from a sequence of tuple pairs, useful in many cases.
    dict_2 = dict([(1, "one"), (2, "two")])
    assert dict_2[1] == 'one'
    assert dict_2[2] == 'two'

def test_dictionary_length():
    '''length of the dictionary'''
    word_to_digit = { "one" : 1, "two" : 2}
    assert len(word_to_digit) == 2 
    #note that a key value pair is treated as one item

def test_dictionary_is_indexed_by_key():
    ''' dictionary indexing can be done using keys'''
    word_to_digit = { "one" : 1, "two" : 2}
    assert word_to_digit["one"] == 1
    assert word_to_digit["two"] == 2

    try:
        word_to_digit[1]
    except Exception:
    #Note that numeric indicies don't mean much like in case of lists and tuples
  # ex=1(value from dict key-value pair stored in exception)
        assert True

def test_dictionary_is_mutable():
    '''dictionaries are mutable'''
    word_to_digit = { "one" : 1, "two" : 2}

    word_to_digit["three"] = 3
    assert word_to_digit == {"one" : 1, "two" : 2,"three":3}

    del word_to_digit["one"]
    assert word_to_digit == {"two" : 2,"three":3}

    word_to_digit["one"] = 10
    assert word_to_digit == {"two" : 2,"three":3,"one":10}
    #  A regular dictionary doesn’t track the insertion order.
    #  So when iterating over it, items are returned in an arbitrary order.
    #  When we want to make sure that items are returned in the order they
    #  were inserted, we can use OrderedDict.


def test_dictionary_is_unordered():
    ''' dictionaries are unordered'''
    dict1 = { 'one': 1, 'two': 2 }
    dict2 = { 'two': 2, 'one': 1}

    equal = (dict1 == dict2)
    assert equal is True # True or False?

def test_dictionary_keys_and_values():
    ''' testing dictionary keys and there values'''
    word_to_digit = { "one" : 1, "two" : 2}
    assert len(word_to_digit.keys()) == 2
    assert len(word_to_digit.values()) == 2
    keys = list(word_to_digit.keys())
    #sort to get a deterministic order
    keys.sort()
    assert keys == ['one','two']
    values = list(word_to_digit.values())
    values.sort()
    assert values == [1, 2]

def test_dictionary_contains():
    ''' elements contained in dictionaries '''
    word_to_digit = { "one" : 1, "two" : 2}

    assert ("one" in word_to_digit) is True
    assert ("two" in word_to_digit) is True

    assert ("one" in word_to_digit.keys()) is True
    assert ("two" in word_to_digit.keys()) is True

    assert (1 in word_to_digit) is False
    assert (2 in word_to_digit) is False

    assert (1 in word_to_digit.values()) is True
    assert (2 in word_to_digit.values()) is True

def test_valid_dictionary_keys():
    ''' testing the keys are valid ?'''
    test_dict = {}
    test_dict[1] = 1
    test_dict["one"] = "string"
    try:
        key = []
        test_dict[key] = "list"
    except TypeError:
        # print (te)  #observe the error message.
        assert True

    try:
        key = (1,2)
        test_dict[key] = "tuple with immutable elements"
    except TypeError:
        # print (te)
        assert False # do we reach here?

    try:
        key = (1, [])
        test_dict[key] = "tuple with mutable element"
    except TypeError:
        # print (te)
        assert True #do we reach here?

    assert {1:1,'one':'string',(1, 2): 'tuple with immutable elements'} == test_dict


THREE_THINGS_I_LEARNT = """
- Dictionary
- Dictionary Methods
"""

TIME_TAKEN_MINUTES = 20

NOTES2= '''
It is  a good idea to figure out how dictionaries are generally implemented
under the hood. Go through the thread at
http://stackoverflow.com/questions/730620/how-does-a-hash-table-work
and discuss in the group if required.
'''