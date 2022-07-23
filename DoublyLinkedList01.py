from multiprocessing.sharedctypes import Value
from types import new_class


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None



class DoublyLinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1



    def print_list(self):

        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next 




    def append(self, value):

        new_node = Node(value)
        temp=self.head
        
        if self.head == None:
            self.head = new_class
            self.tail = new_class
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length +=1

    


    def prepend(self,value):

        new_node = Node(value)
        
        if self.length == 0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1  
        return True





    def pop(self):

        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            temp.next = None
            temp.prev = None
            self.tail.next = None

        self.length -= 1
        return temp.value




    def pop_first(self):
        
        if self.length ==0:
            print("No element exist")
            return None
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length-=1

        return temp.value





    def get(self, index):

        if index < 0 or index >= self.length:
            return None

        if index <self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp



   
   
    def set_value(self,index,value):
        
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False



    
    def insert_at_index(self, value, index):

        if index < 0 or index > self.length:
            print("index is out of range")
            return None
        
        if index==0:
            return self.prepend(value)
        
        if index==self.length:
            return self.append(value)
        else:
            new_node = Node(value)
            temp = self.head
            
            for _ in range(index-1):
                temp=temp.next
        
            temp_next_node = temp.next
            temp_next_node.prev= new_node

            new_node.next = temp.next
            new_node.prev = temp

            temp.next = new_node

        return True


    def remove_at_index(self, index):

        if index<0 or index>self.length:
            print("Index is out of range")
            return False
        if index==0:
            return self.pop_first()
        if index==self.length:
            return self.pop()
        else:
            temp = self.head

            for i in range(index):
                temp = temp.next
            
            temp.next.prev = temp.prev
            temp.prev.next = temp.next

            temp.next = None
            temp.prev = None
        
        self.length-=1
        return True



DD1 = DoublyLinkedList(1)

DD1.append(2)
DD1.append(3)
DD1.append(4)
DD1.append(5)

DD1.print_list()

print("Removing element 2")

DD1.remove_at_index(2)


print("Printing again")
DD1.print_list()