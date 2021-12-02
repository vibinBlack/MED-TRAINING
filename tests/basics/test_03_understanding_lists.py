"""
Lists and It's Methods
"""
__author__ = 'Hari'


# from placeholders import *

def test_list_type():
    """ list type"""
    fruits = ["banana", "orange", "grape"]
    assert type(fruits).__name__ == 'list'


def test_list_len():
    """ length of the list """
    fruits = ["banana", "orange", "grape"]
    assert len(fruits) == 3


def test_list_can_be_indexed():
    """List Indexing"""
    fruits = ["banana", "orange", "grape"]
    assert fruits[0] == 'banana'
    assert fruits[1] == 'orange'
    assert fruits[2] == 'grape'
    assert fruits[-1] == 'grape'
    assert fruits[-2] == 'orange'
    assert fruits[-3] == 'banana'


def test_list_is_mutable():
    """ testing the lists are mutable or not"""
    fruits = ["banana", "orange", "grape"]
    fruits[0] = "mango"
    assert fruits == ["mango", "orange", "grape"]
    # replace __ with expected contents of list


def test_list_can_be_sliced():
    """
     Slicing works the same as on strings
    """
    fruits = ["banana", "orange", "grape"]
    assert fruits[0:0] == []

    # begin : end
    assert fruits[0:2] == ["banana", "orange"]
    assert fruits[0:5] == ["banana", "orange", "grape"]
    assert fruits[1:-1] == ["orange"]

    # begin :
    assert fruits[0:] == ["banana", "orange", "grape"]
    assert fruits[2:] == ["grape"]
    assert fruits[0:] == ["banana", "orange", "grape"]

    #: end
    assert fruits[:0] == []
    assert fruits[:2] == ["banana", "orange"]
    assert fruits[:5] == ["banana", "orange", "grape"]

    # note the invariant
    assert fruits[:1] + fruits[1:] == ["banana", "orange", "grape"]


def test_slice_creates_a_new_list():
    """ creating new list"""
    fruits = ["banana", "orange", "grape"]
    slice = fruits[0:2]
    slice.append("guava")

    assert fruits == ["banana", "orange", "grape"]  # did this change?  No
    assert slice == ['banana', 'orange', 'guava']


def test_list_merge():
    """merging the list"""
    fruits = ["banana", "orange", "grape"]
    veggies = ["beetroot", "tomato"]
    all = fruits + veggies

    assert all == ['banana', 'orange', 'grape', 'beetroot', 'tomato']
    assert fruits == ["banana", "orange", "grape"]
    assert veggies == ["beetroot", "tomato"]
    assert fruits[1:] + veggies[:1] == ['orange', 'grape', 'beetroot']


def test_list_slice_replacement_is_inplace():
    """ replacing the elements inplace in list using slicing"""
    fruits = ["banana", "orange", "grape"]

    fruits[1:2] = ["litchi", "guava"]
    assert fruits == ["banana", "litchi", "guava", "grape"]

    fruits[3:] = ['grape1']
    assert fruits == ["banana", "litchi", "guava", "grape1"]

    fruits[:2] = ["banana1", "litchi"]
    assert fruits == ["banana1", "litchi", "guava", 'grape1']


def test_list_common_methods():
    """
     You can find methods supported by lists by entering help([]) in the python console.
     Ignore the methods that start with __ for now.

     For help on a specific function like pop enter help([].pop)
    """
    fruits = []
    fruits.append("orange")

    assert fruits == ['orange']

    fruits.insert(0, "banana")
    assert fruits == ['banana', 'orange']

    fruits.extend(["litchi", "guava"])
    assert fruits == ['banana', 'orange', 'litchi', 'guava']

    fruits.reverse()
    assert fruits == ['guava', 'litchi', 'orange', 'banana']

    fruits.pop()
    assert fruits == ['guava', 'litchi', 'orange']

    fruits.pop(0)
    assert fruits == ['litchi', 'orange']


def test_list_can_contain_lists():
    """ testing the elements contain in list"""
    fruits = ["orange", "banana"]
    veggies = ["beetroot", "tomato"]
    all = [fruits, veggies]

    assert len(all) == 2
    assert all[0] == ['orange', 'banana']
    assert all[1] == ['beetroot', 'tomato']


def test_list_can_contain_objects_of_different_types():
    """ list can contain different types pf objects"""
    mixed = ["string", 10]
    assert mixed[0] == "string"
    assert mixed[1] == 10


def test_list_sort():
    """ sorting the list"""
    numbers = [5, 4, 3, 8]
    numbers.sort()
    assert numbers == [3, 4, 5, 8]
    numbers.sort(reverse=True)
    assert numbers == [8, 5, 4, 3]


# if something unexpected happens see,
# http://docs.python.org/2/reference/expressions.html#operator-precedence
# and fix accordingly.
def test_list_membership():
    """ testing the members of a list"""
    numbers = [5, 4, 3]
    assert (5 in numbers) is True
    assert (10 in numbers) is False


def test_list_range():
    """ testing the range of the list"""
    numbers = range(1, 5)
    assert numbers == range(1, 5)

    numbers = range(1, 5, 2)
    assert numbers == range(1, 5, 2)


THREE_THINGS_I_LEARNT = """
- Lists
- List Methods
-
"""

TIME_TAKEN_MINUTES = 20
