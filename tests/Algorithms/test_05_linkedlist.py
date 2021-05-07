#Node class
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

#Linked list class
class Linkedlist:

    def __init__(self):
        self.head=None
    
    def display(self): # conevrts nodes to list and returns
        res=[]
        if(self.head):
            cur=self.head
            while(cur.next):
                #print(cur.data,end="->")
                res.append(cur.data)
                cur=cur.next
           # print(cur.data)
            res.append(cur.data)
        return res

    
    def addEnd(self,data):  #adds the nodes at last
        newNode = Node(data)
        if (self.head):
            cur = self.head
            while (cur.next):
                cur=cur.next
            cur.next=newNode
        else:
            self.head=newNode
            cur=self.head
        return self.display()

    def addBeggining(self,data):   # adds the nodes at begining
        newNode = Node(data)
        if (self.head):
            newNode.next = self.head
            self.head = newNode
            cur = self.head
        else:
            self.head=newNode
            cur=self.head
        return self.display()

    def addatspecificValue(self,pos,data):
        newNode = Node(data)
        if(pos < 1):
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
        return self.display()
        
    def delete(self,data):       #deleting the node based on data
        if(self.head==None):
            return "Empty Node"
        if(self.head.data==data and self.head.next != None):
            cur=self.head
            self.head=cur.next
            return self.display()
        if (self.head.data == data and self.head.next==None):
            self.head=None
            return self.display()
        cur=self.head
        prev=cur
        while (cur.data is not data and cur.next!=None):
            prev=cur
            cur=cur.next
        prev.next=cur.next
        return self.display()
     

    def search(self,data):      #searching for a particular data 
        count=0                 #returns true if found else False
        if(self.head):
            cur=self.head
            temp=0
            while (cur.next):
                count+=1
                if(cur.data==data):
                    #print("data found at Node : "+str(count))
                    return True
                cur=cur.next
            if (cur.data==data):
                #print("Data is found at Node:"+str(count+1))
                return  True
        return False
    
    def loopFinding(self):    #detecting occurnace of looping
        s = set()
        cur = self.head
        while (cur):
            if (cur in s):
                return True
            s.add(cur)
            cur = cur.next
        return False
    
    def rotateleft(self,n):      # rotating data to left by n moves
        if n==0:
            return self.display()
        count=1
        cur=self.head
        while (count < n and cur is not None ):
            cur=cur.next
            count+=1
        nthNode = cur
        while(cur.next is not None):
            cur = cur.next
        cur.next = self.head
        self.head = nthNode.next
        nthNode.next = None
        return self.display()
    
    def rotateright(self,n): #rotating data to right by n moves
        if (not self.head):
            return self.display()
        tmp = self.head
        len = 1
        while (tmp.next != None):
            tmp = tmp.next
            len += 1
        if (n > len):
            n = n % len
        n = len - n
        if (n == 0 or n == len):
            return self.display()
        cur = self.head
        count = 1
        while (count < n and cur != None):
            cur = cur.next
            count += 1
        if (cur == None):
            return self.display()
        nthnode = cur
        tmp.next = self.head
        self.head = nthnode.next
        nthnode.next = None
        return self.display()

    def sortNode(self):       # sorting the data in increasing order
        c=self.head
        n=None
        if (self.head):
            while(c != None):
                n=c.next
                while(n != None):
                    if(c.data > n.data):
                        temp=c.data
                        c.data=n.data
                        n.data=temp
                    n=n.next
                c=c.next
        else:
            return None
        return self.display()
            


LL = Linkedlist()
LL.addBeggining(10)


def test_case1_addBeggining():
    assert LL.addBeggining(2) == [2,10]
    assert LL.addBeggining(5) == [5,2,10]
    assert LL.addBeggining(7) == [7,5,2,10]  #Since a node is created outside the function same node is used for all methods



def test_case_addEnd():
    assert LL.addEnd(6) == [7,5,2,10,6]
    assert LL.addEnd(3) == [7,5,2,10,6,3]

def test_case_addinMiddle():
    assert LL.addatspecificValue(3,9) == [7,5,9,2,10,6,3]
    assert LL.addatspecificValue(-1, 5) == "Invalid position"

""" Note:
    Run the above to test cases for the succesful testing of below test cases,Otherwise AttributeError occurs.
    Because nodes are created by above test cases."""

def test_case_search():
    assert LL.search(10) == True
    assert LL.search(20) == False


def test_case_rotateright():
    assert LL.rotateright(2) == [6,3,7,5,9,2,10]
    assert LL.rotateright(0) == [6,3,7,5,9,2,10]


def test_case_rotateleft():
    assert LL.rotateleft(2) == [7,5,9,2,10,6,3]
    assert LL.rotateleft(2) == [9,2,10,6,3,7,5]
    assert LL.rotateleft(0) == [9,2,10,6,3,7,5]


def test_case_sort():
    assert LL.sortNode() == [2,3,5,6,7,9,10]


def test_case_delete():
    #please run all above 
    test_case_sort()
    assert LL.delete(6) == [2,3,5,7,9,10]
    assert LL.delete(3) == [2,5,7,9,10]
    assert LL.delete(7) == [2,5,9,10]
    assert LL.delete(2) == [5,9,10]
    assert LL.delete(10) ==[5,9]
    assert LL.delete(5) == [9]
    assert LL.delete(2) == [9]  #2 is not present in nodes so retuns the present nodes available
    assert LL.delete(9) == []
    assert LL.delete(2) == "Empty Node"

def test_case_noNodes():
     assert LL.sortNode() == None


def test_case_loopfinding():
    LL.addBeggining(20)
    LL.addEnd(4)
    LL.addEnd(15)
    LL.addEnd(10)
    assert LL.loopFinding()== False
    LL.head.next.next.next.next = LL.head  # creating a loop
    assert LL.loopFinding() == True

