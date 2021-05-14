
def diff(list1, list2):
	
	return list(set(list1) - set(list2)) + list(set(list2) - set(list1))
 
def test1():
	list1 = [10 , 20, 25, 30, 35, 40]
	list2 = [25, 40, 35]
	assert [10, 20, 30] ==  diff(list1, list2) 
	
def test2():
	assert [5, 6, 2, 3] == diff([1, 4, 5, 6], [1, 3, 2, 4])

def test3():
	assert diff([],[]) == []
