class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def printLinkedList(self):
        temp = self.head
        if(temp==None):
            print('Empty List')
        else:
            while(temp != None):
                print(temp.data,"->",end='')
                temp = temp.next
            print('Null')

    def insertAtBeginning(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp    
        return self.LinkedListtoList()    

    def insertAtEnd(self,value):
        if self.head == None:
            self.head = Node(value)
        else:
            temp = self.head
            while(temp.next != None):
                temp=temp.next
            temp.next = Node(value)
        return self.LinkedListtoList()

    def insertAtIndex(self,value,index):
        if index > ll.getLength():
            return 'Index out of Range'
        temp = self.head
        if self.head == None and index == 0:
            self.head = Node(value)
        elif index==0:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
        else:
            for i in range(index-1):
                temp=temp.next
            # print(temp.data,value,index)
            # ll.printLinkedList()
            nextNode = temp.next
            temp.next = Node(value)
            temp.next.next = nextNode
        return self.LinkedListtoList()
    
    def deleteNode(self,value):
        if self.head == None:
            return 'List is Empty'
        else:
            temp = self.head
            if temp.data == value  and temp.next == None:
                self.head=None
            elif temp.data == value  and temp.next != None:
                self.head = self.head.next
            else:
                while(temp!=None and temp.next!=None):
                    if temp.next.data == value:
                        temp.next = temp.next.next
                        break
                    temp=temp.next
                else:
                    return 'Node not Exist'
        return self.LinkedListtoList()

    def searchNode(self,value):
        temp = self.head
        while(temp != None):
            if temp.data == value:
                return True
            temp=temp.next
        return False


    def findLoop(self):
        slow = self.head 
        fast = self.head

        while slow!=None and fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow == fast:
                return True
        return False


    def getLength(self):
        length=0
        temp = self.head
        while(temp!=None):
            length+=1
            temp=temp.next
        return length

    def reverseLinkedList(self):
        prev=None
        while(self.head != None):
            next = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = next
        self.head = prev
        

    def rightShift(self,k):
        tempHead = self.head
        temp = self.head
        length = self.getLength()
        k=k%length

        for i in range(length-k-1):
            temp=temp.next
        tail = temp
        while tail.next != None:
            tail=tail.next

        tail.next = tempHead
        tempHead = temp.next
        temp.next = None
        self.head = tempHead
        return self.LinkedListtoList()

    def leftShift(self,k):
        self.reverseLinkedList()
        self.rightShift(k)
        self.reverseLinkedList()
        return self.LinkedListtoList()
    
    def sortList(self):
        i=self.head

        while(i.next!=None):
            j=i.next
            value = j.data
            minNode = j
            while(j!=None):
                # value = min(value,j.data)
                if j.data < value:
                    minNode = j
                j = j.next
            if minNode.data < i.data:
                temp = minNode.data
                minNode.data = i.data
                i.data = temp
            i=i.next
        return self.LinkedListtoList()

    def LinkedListtoList(self):
        arr=[]
        temp = self.head

        while(temp!=None):
            arr.append(temp.data)
            temp=temp.next
        return arr

ll = LinkedList()

def test_1():
    assert ll.insertAtEnd(10) == [10]
    assert ll.insertAtEnd(21) == [10,21]
    assert ll.insertAtEnd(5) == [10,21,5]
    assert ll.insertAtEnd(1) == [10,21,5,1]
    assert ll.insertAtEnd(22) == [10,21,5,1,22]

def test_2():
    assert ll.searchNode(21) == True
    assert ll.searchNode(5) == True
    assert ll.searchNode(6) == False

def test_3():
    assert ll.rightShift(2) == [1,22,10,21,5]
    assert ll.rightShift(11) == [5,1,22,10,21]
    assert ll.rightShift(5) == [5,1,22,10,21]
    assert ll.rightShift(0) == [5,1,22,10,21]

def test_4():
    assert ll.leftShift(2) == [22,10,21,5,1]
    assert ll.leftShift(11) == [10,21,5,1,22]
    assert ll.leftShift(5) == [10,21,5,1,22]
    assert ll.leftShift(3) == [1,22,10,21,5]

def test_5():
    assert ll.sortList() == [1,5,10,21,22]

def test_6():
    assert ll.deleteNode(10) == [1,5,21,22]
    assert ll.deleteNode(7) == 'Node not Exist'
    assert ll.deleteNode(1) == [5,21,22]
    assert ll.deleteNode(5) == [21,22]
    assert ll.deleteNode(21) == [22]
    assert ll.deleteNode(22) == []
    assert ll.deleteNode(10) == 'List is Empty'

def test_7():
    assert ll.insertAtBeginning(5) == [5]
    assert ll.insertAtBeginning(12) == [12,5]
    assert ll.insertAtBeginning(10) == [10,12,5]

def test_8():
    assert ll.LinkedListtoList() == [10,12,5]
    assert ll.insertAtIndex(20,1) == [10,20,12,5]
    assert ll.insertAtIndex(15,0) == [15,10,20,12,5]
    assert ll.insertAtIndex(2,4) == [15,10,20,12,2,5]
    assert ll.insertAtIndex(7,6) == [15,10,20,12,2,5,7]
    assert ll.insertAtIndex(22,10) == 'Index out of Range'

def test_9():
    assert ll.findLoop() == False

# ll.head = Node(1)
# ll.insertAtEnd(10)
# ll.insertAtEnd(20)
# ll.insertAtEnd(3)
# ll.insertAtEnd(12)
# ll.insertAtEnd(1)



# ll.printLinkedList()

# print(ll.searchNode(31))
# print(ll.searchNode(2))
# print(ll.searchNode(98))

# ll.deleteNode(10)
# ll.printLinkedList()

# ll.deleteNode(12)
# ll.printLinkedList()

# ll.deleteNode(31)
# ll.printLinkedList()

# ll.deleteNode(3)
# ll.deleteNode(2)
# ll.printLinkedList()

# ll.head.next.next.next = ll.head.next
# print(ll.findLoop())

# ll.rightShift(6)
# ll.printLinkedList()

# ll.reverseLinkedList()
# ll.printLinkedList()

# ll.leftShift(1)
# ll.printLinkedList()

# ll.sortList()
# ll.printLinkedList()