
def add_dict(d1,d2):
	counter = {} 
	
	for i, j in d1.items():
		
		for x, y in d2.items():
			
			if i == x:
				counter[i]=(j+y) 
				
			elif x not in counter.keys():
			     	counter[x]=y
		
		if i not in counter.keys():
		      	counter[i]=j
	
	return counter


d1 = {'a': 100, 'b': 200, 'c':300}

d2 = {'a': 300, 'b': 200, 'd':400} 

def test1_add_dict():
	assert  {'a': 400, 'b': 400, 'd': 400, 'c': 300}==add_dict(d1,d2)

def test2_add_dict():
	assert {'a':2,'b':2,'c':4} == add_dict({'a':1,'b':2,'c':2},{'a':1,'c':2})   
	
def test3_add_dict():
	assert {1:50, 2:25,3:99} == add_dict({1:23,2:25,3:66},{1:27,3:33})
	


 
""" 
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)
"""