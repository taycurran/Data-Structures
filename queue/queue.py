"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from sing_linklist import Node, LinkedList
class Queue:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.head = None
        self.tail = None
    
    def __len__(self):
        if not self.head:
            self.size = 0
            return self.size
        else:
            cont = []
            current_node = self.head
            while current_node.next_node:
                cont.append(current_node.value)
                current_node = current_node.next_node
            cont.append(self.tail.value)  
            self.size = len(cont)
            return self.size

    def enqueue(self, value):
        if not self.head:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
        else:
            orig_head = self.head
            self.head = Node(value, orig_head)

    def dequeue(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value
# class Queue:
#     def __init__(self):
#         self.items = []

#     def isEmpty(self):
#         return self.items == []

#     def enqueue(self, item):
#         self.items.insert(0,item)

#     def dequeue(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)