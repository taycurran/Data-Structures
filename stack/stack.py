# from singly_linked_list/singly_linked_list.py import Node, LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

from sing_linklist import Node, LinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.head = None
        #self.tail = None

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

    def push(self, value):
        if not self.head:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
        else:
            orig_head = self.head
            new_node = Node(value, orig_head)
            new_head = new_node
            self.head = new_head
            
    def pop(self):
        if not self.head:
            self.head = None
            self.tail = None
        else:
            orig_head_value = self.head.value
            self.head = self.head.next_node
            return orig_head_value


# class Stack:
#      def __init__(self):
#          self.size = 0
#         #self.storage = ?
#          self.items = []

#      def isEmpty(self):
#          return self.items == []

#      def push(self, item):
#          self.items.append(item)

#      def pop(self):
#          return self.items.pop()

#      def peek(self):
#          return self.items[len(self.items)-1]

#      def size(self):
#          return len(self.items)