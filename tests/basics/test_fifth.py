import pytest

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def begining(self,data):
        NewNode=Node(data)
        NewNode.next=self.head
        self.head=NewNode
        return llist.convertArr()

    def between(self, prev_node,data):
        if self.head is None:
            return "List is empty"
        if prev_node is None:
            return "The given previous node must inLinkedList."
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        return llist.convertArr()
    
    def end(self,data):
        NewNode=Node(data)
        if self.head is None:
            self.head=NewNode
            return llist.convertArr()
        last=self.head
        while(last.next):
            last=last.next
        last.next=NewNode
        return llist.convertArr()

    def remove_node(self,key):
        temp=self.head
        if (temp is None):
            return "List is empty"
        if (temp.data==key):
            self.head=temp.next
            temp=None
            return llist.convertArr()
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
        return llist.convertArr()

    def search(self,value):
        temp=self.head
        if (temp is None):
            return "List is empty"
        if (temp.data==value):
            return "Given value is present in the List"
        while(temp is not None):
            if temp.data==value:
                return "Given value is present in the List"
            temp=temp.next
        return "Given value is 'not' present in the List"

    def loopFinding(self):
        slow_p=fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            if slow_p==fast_p:
                return True
        return False
    
    def rotate(self, k):
        if k==0:
            return llist.convertArr()
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
        return llist.convertArr()

    def sort(self):
        list=[]
        current=self.head
        while(current is not None):
            list.append(current.data)
            current=current.next
        list.sort()
        print(list)
        current=self.head
        i=0
        while(current is not None):
            current.data=list[i]
            i+=1
            current=current.next
        return llist.convertArr()

    def printList(self):
        temp=self.head
        while (temp):
            print(temp.data,end=" ")
            temp=temp.next

    def convertArr(self):
        arr = []  
        curr = self.head
        while (curr):
            arr.append(curr.data)
            curr = curr.next
        return arr

llist = LinkedList()
llist.end(6)
llist.begining(7)
llist.begining(1)
llist.end(4)
llist.between(llist.head.next, 8)
#print(llist.convertArr())
#print(llist.remove_node(8))
#print(llist.search(8))                                     # For searching
#llist.printList()
#llist.head.next.next.next.next.next = llist.head.next.next # For LoopFinding
#print(llist.loopFinding())                                 # For LoopFinding
#print(llist.rotate(1))                                     # For Anti-Clockwise rotation
#print(llist.sort())                                        # For Sorting
print(llist.convertArr())

def test_add_begining():
    assert llist.begining(0)==[0,1,7,8,6,4]
def test_add_between():
    assert llist.between(llist.head.next,5)==[1,7,5,8,6,4]

def test_add_end():
    assert llist.end(6)==[1,7,8,6,4,6]
def test_search_present():
    assert llist.search(8)== "Given value is present in the List"

def test_search_not_present():
    assert llist.search(9)== "Given value is 'not' present in the List"

def test_loop_present():
    llist.head.next.next.next.next.next = llist.head.next.next
    assert llist.loopFinding()==True

def test_loop_not_present():
    assert llist.loopFinding()==False

def test_rotate():
    assert llist.rotate(1)==[7, 8, 6, 4, 1]

def test_sort():
    assert llist.sort()==[1, 4, 6, 7, 8]

def test_remove_present():
    assert llist.remove_node(8)== [1, 7, 6, 4]

def test_remove_not_present():
    assert llist.remove_node(9)== "Node with data '9' not found"