
def top_three_items(s_dict):
		
	sort_dict=sorted(s_dict.items(), key=lambda x:x[1], reverse = True)     

#sorted(iterable,key=key,reverse=reverse)# reverese=True will sort descending.
	
#	for i,j in sort_dict[:3]:
#		print(i," ",j)  
	
	return sort_dict[:3]

def test1():
	s_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
	
	assert [('item4', 55), ('item1', 45.5), ('item3', 41.3)] == top_three_items(s_dict) 

 
def test2():
	
	assert [('i9', 90), ('i8', 80), ('i7', 70)] == top_three_items({'i1':10, 'i2':20, 'i3':30, 'i4':40, 'i5':50, 'i6':60, 'i7':70, 'i8':80, 'i9':90})

