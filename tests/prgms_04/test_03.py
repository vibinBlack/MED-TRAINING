
def remove_even(num):
    
    odd_num = [n for n in num if n % 2 != 0]
    		
    return odd_num
    
def test1():
	  num = [7, 8, 120, 25, 44, 20, 27]
	  assert remove_even(num) == [7, 25, 27]
	  
def test2():
	  assert remove_even([1,2,3,4,5]) == [1,3,5]
	  
def test3():
	  assert remove_even([2,4,8,6,3,5]) == [3,5]
