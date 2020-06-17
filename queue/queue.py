"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. i.e.:
The element inserted at the first, is the first element to come out of the list.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
"""


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         # if the array is empty, return None
#         if len(self) == 0:
#             return None

#         # set the value to be dequeued, since it's a queue it will be from the top of the index [0]
#         dequeued = self.storage[0]
#         self.storage.pop(0)
#         return dequeued


"""
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.size = 0
        self.first_node = None

    def __len__(self):
        return self.size

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass


"""
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
"""

"""
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
