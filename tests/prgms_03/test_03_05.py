

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next 
        
        
class Single_Linked_List:

    def __init__(self):
        self.head=None 
        
    def add_at_begin(self,data):
        NewNode=Node(data)
        NewNode.next=self.head
        self.head=NewNode   
        
        
    def add_at_position(self, pos,data):
      newNode = Node(data)
      if (pos < 1) :
            return "Invalid position"
      elif (pos == 1):
            newNode.next = self.head
            self.head = newNode
      else:    
            temp = self.head
            for i in range(1, pos-1):
                if(temp != None):
                    temp = temp.next   

            if(temp != None):
                newNode.next = temp.next
                temp.next = newNode  
            else:
                return "Node is null"
      
        
                
    def add_at_end(self,data):
        NewNode=Node(data)
        if self.head is None:
            self.head=NewNode 
        else:
               last=self.head
               while(last.next):
                last=last.next
               last.next=NewNode   
                
                   
    def delete_node(self,key):
        temp=self.head
        if (temp is None):
            return "List is empty"
        if (temp.data==key):
            self.head=temp.next
            temp=None
        prev=temp
        temp=temp.next
        while(temp is not None):
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if(temp==None):
            return "Node with data '%s' not found" % key
        prev.next=temp.next 
        
       
    def search(self,value):
        temp=self.head
        if (temp is None):
            return "List is empty"
        if (temp.data==value):
            return "Given value is present in the List at 0 index"
        c=0
        while(temp is not None):
            if temp.data==value:
                return "Given value is present in the List at %d index"% c
            temp=temp.next
            c=c+1
        return "Given value is 'not' present in the List"
        
        
    def loop_finding(self):
        s_p=f_p= self.head
        while(s_p and f_p and f_p.next):
            s_p=s_p.next
            f_p=f_p.next.next
            if s_p==f_p:
                return True
        return False
        
        
        
    def rotate(self, k):
        if k==0:
            return llist.convert_to_list()
        current=self.head
        count=1
        while(count<k and current is not None):
            current=current.next
            count+=1
        if current is None:
            count-=1
            k-=(k//count)*count
            if k==0:
                return llist.convertArr()
            current=self.head
            count=1
            while(count<k and current is not None):
                current=current.next
                count+=1
        kthNode=current
        while(current.next is not None):
            current=current.next
        current.next=self.head
        self.head=kthNode.next
        kthNode.next=None
        
        
    
    
    def sort(self):
        list=[]
        current=self.head
        while(current is not None):
            list.append(current.data)
            current=current.next
        list.sort()
        #print(list)
        current=self.head
        i=0
        while(current is not None):
            current.data=list[i]
            i+=1
            current=current.next        
            
            
            
    def print(self):
        temp=self.head
        while (temp):
            print(temp.data,end=" ")
            temp=temp.next 
            
      
                  
    def convert_to_list(self):
        lst = []  
        curr = self.head
        while (curr):
            lst.append(curr.data)
            curr = curr.next
        return lst
        
        
slist=Single_Linked_List() 
slist.add_at_end(5) 
#slist.print() 
slist.add_at_begin(4)   
slist.add_at_position(3,6) 
slist.add_at_begin(2) 
slist.add_at_position(2,3) 
print(slist.convert_to_list())
#aa=(list)slist.print() 
#print(aa) 

def test_add_at_begin():
    slist.add_at_begin(1) 
    assert [1, 2, 3, 4, 5, 6] == slist.convert_to_list() 


def test_add_at_position():
   slist.add_at_position(2,2.5) 
   assert [2, 2.5, 3, 4, 5, 6] == slist.convert_to_list() 
   
   
def test_add_at_end():
 slist.add_at_end(8) 
 assert [2, 3, 4, 5, 6, 8] == slist.convert_to_list()
	
 
 
def test_delete_node():
 slist.delete_node(8) 
	
 if 8 in slist.convert_to_list():
    assert [2, 3, 4, 5] == slist.convert_to_list() 
	
	

def test_search():
    assert slist.search(2) == "Given value is present in the List at 0 index" 
    assert slist.search(5) == "Given value is present in the List at 3 index" 
    assert slist.search(8) == "Given value is 'not' present in the List"
   
   

def test_loop_finding():
 assert slist.loop_finding() == False
 slist.head.next.next =slist.head.next # creating loop 
 assert slist.loop_finding() == True
	
	
	
def test_rotate(): 
 slist.rotate(2) # shifting 2 left positions and here in single linked list right shift is not possible
 assert [4, 5, 6, 2, 3] == slist.convert_to_list()
 slist.rotate(1) 
 assert [5, 6, 2, 3, 4] == slist.convert_to_list()

   

   
def test_sort():
 slist.add_at_begin(10)
 #print(slist.convert_to_list()) #[10, 2, 3, 4, 5, 6]
 slist.sort()
 assert slist.convert_to_list() == [2, 3, 4, 5, 6, 10]
 
 