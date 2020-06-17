"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
"""


"""
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) < 1:
#             return None

#         return self.storage.pop()


"""
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.size = 0
        self.first_node = None

    def __len__(self):
        return self.size

    def push(self, value):
        pass

    def pop(self):
        pass


"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
