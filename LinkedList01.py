
from mimetypes import types_map


class Node:

    def __init__(self, value):
        self.value=value
        self.next= None


class LinkedList:

    def __init__(self,value):        
        new_node = Node(value)
        self.head= new_node
        self.tail= new_node
        self.length = 1
 
 
    def print_linkedlist(self):

        temp = self.head
        while temp is not None:
            print(temp.value)
            temp= temp.next


    def append(self, value):
        
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True



    def preappend(self, value): 

        #append at the begining

        new_node = Node(value)

        if self.length ==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.length +=1

        return True



    def pop(self):

        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        
        while(temp.next):
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -=1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value    




    def pop2(self):
        if self.length == 0:
            return None

        temp = self.head
        
        while(temp.next.next):
            temp = temp.next
        
        self.tail = temp
        pop_value = temp.next.value
        self.tail.next = None
        self.length -=1

        return pop_value



    def pop_first(self):

        if self.length == 0:
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            pop_value = self.head.value
            self.head = self.head.next
        
        self.length -=1

            
        return pop_value
            


    def get(self, index):

        if index < 0 or index > self.length:
            print("Index is out of Range")
            return None
        
        temp = self.head
        
        for _ in range(index):
            temp = temp.next
        return temp.value

    
    
    def insert_at_index(self, index, value):
        
        if index < 0 or index >self.length:
            print("Index is out of Range")
            return None
        if index ==0:
            return self.preappend(value)
        if index ==self.length:
            return self.append(value)


        new_node = Node(value)
        temp = self.head

        for _ in range(index-1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node
        self.length +=1

        return True


    def set(self, index, value):
        
        if index < 0:
            print("Index is out of Range")
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next

        temp.value = value

        return True


    def remove_at_index(self,index):

        if index < 0 or index >self.length:
            print("Index is out of range")
        if index==0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        
        temp = self.head
        for _ in range(index-1):
            temp = temp.next
        
        temp.next= temp.next.next
        self.length -=1    

        return True

        
    def reverse(self):
        
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


  
LL1 = LinkedList(0)
LL1.append(1)
LL1.append(2)
LL1.append(3)
LL1.append(4)
LL1.append(5)

print("Before removing the element")
LL1.print_linkedlist()

LL1.reverse()

print("Reverse")
LL1.print_linkedlist()