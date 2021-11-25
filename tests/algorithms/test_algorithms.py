'''Testing assessment programs/Algorithms'''

import algorithms as algo

def test_binary_to_decimal():
    '''testing binary to decimal number conversion'''
    assert algo.binary_to_decimal("1010") == 10
    assert algo.binary_to_decimal("0") == 0
    assert algo.binary_to_decimal("11111") == 31

def test_decimal_to_binary():
    '''testing decimal to binary number conversion'''
    assert algo.decimal_to_binary(10) == "1010"
    assert algo.decimal_to_binary(0) == "0"
    assert algo.decimal_to_binary(31) == "11111"

def test_calculator_expression():
    '''testing calculator'''
    assert algo.calculator_expression("1/2") == 0.5
    assert algo.calculator_expression("-1*8") == -8
    assert algo.calculator_expression("8*10/29-6+4/2/4") == -2.7413793103448274

def test_fibnoacci_series():
    '''test fibnoacci serires of returning n numbers'''
    assert algo.fibnoacci_series(10) == [0,1,1,2,3,5,8,13,21,34]
    assert algo.fibnoacci_series(2) == [0,1]

def test_prime_number():
    '''test given number is prime or not'''
    assert algo.check_prime_or_not(5) is True
    assert algo.check_prime_or_not(24) is False
    assert algo.check_prime_or_not(83) is True

def test_linear_search():
    '''test linear search'''
    assert algo.linear_search([-4, 8, 96, 3, -45], 84) is False
    assert algo.linear_search([-4, 8, 96, 3, -45], -45) is True
    assert algo.linear_search([-4, 8, 96, 3, -45], 3) is True

def test_binary_search():
    '''test binary search'''
    assert algo.binary_search([-4, 8, 96, 3, -45], 84) is False
    assert algo.binary_search([-4, 8, 96, 3, -45], -45) is True
    assert algo.binary_search([-4, 8, 96, 3, -45], 3) is True

def test_palindrome():
    '''checking whether given string is palindrome or not'''
    assert algo.check_palindrome_or_not("abcdefg") is False
    assert algo.check_palindrome_or_not("redvelevder") is True
    assert algo.check_palindrome_or_not("-1-2-3-2-1") is False
    assert algo.check_palindrome_or_not("-1-2-3-2-1-") is True

def test_rotation_matrix():
    '''testing rotation of a matrix in clockwise direction'''
    assert algo.rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]) == [[7,4,1],[8,5,2],[9,6,3]]
    assert algo.rotate_matrix([[1,2],[4,5],[7,8]]) == [[7,4,1],[8,5,2]]
    assert algo.rotate_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) ==\
         [[9,5,1],[10,6,2],[11,7,3],[12,8,4]]
