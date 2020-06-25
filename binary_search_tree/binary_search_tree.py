from queue import Queue
from stack import Stack

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        if self.value is None:
            return None
        # compare to the new value we want to insert
        if self.value > value:
            # If self.left isn't already taken by a node,
            if self.left is None:
                # set the left child to the new node with the new value
                self.left = BSTNode(value)
            else:
                # make that (left) node call insert
                self.left.insert(value)

        else:
            # If self.right isn't already taken by a node,
            if self.right is None:
                # set the right child to the new node with new value
                self.right = BSTNode(value)
            else:
                # otherwise, make that (right) node call insert
                self.right.insert(value)
    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True

        # compare the target to the current value
        # if current value > target
        if self.value > target:
            # check the left subtree
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # if current value <= target
        elif self.value <= target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        if self.right:
            return self.right.get_max()
        else:
            # if we cannot go right, return the current value
            return self.value

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # call function on the current value fn(self.value)
        fn(self.value)
        # if you can go left, call for_each on the left tree
        if self.left:
            self.left.for_each(fn)
        # if you can go right, call for_each on the right tree
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # traverse the left side of the tree
        if node.left:
            # print left side values
            self.in_order_print(node.left)
        # visit and print root value
        print(node.value)
        # traverse the right side of the tree
        if node.right:
            # print right side values
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # create a queue for nodes (FIFO)
        queue = Queue()
        # add the first node (root) to the queue
        queue.enqueue(node)
        # while queue is not empty
        while queue.size > 0:
            # remove the node from the queue
            dequeued = queue.dequeue()
            # print the value of the node
            print(dequeued.value)

            # add all children into the queue
            # if the queued node has children on the left
            if dequeued.left:
                # add child to the queue
                queue.enqueue(dequeued.left)
            # if the queued node has children on the right
            if dequeued.right:
                # add child to the queue
                queue.enqueue(dequeued.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        # create a stack for nodes
        stack = Stack()
        # add the first node to the stack
        stack.push(node)

        # while stack is not empty
        while stack.size != 0:
            # get the current node from the top of the stack
            popped = stack.pop()
        # print that node
            print(popped.value)

        # add all children to the stack
        # keep in mind the order you add children will matter
            if popped.left:
                stack.push(popped.left)
            if popped.right:
                stack.push(popped.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Preorder & Postorder visit the root node at different times
    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # visit and print root value
        print(node.value)

        # traverse the left side of the tree
        if node.left:
            # print left side values
            node.pre_order_dft(node.left)
        # traverse the right side of the tree
        if node.right:
            # print right side values
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # traverse the left side of the tree
        if node.left:
            # print left side values
            node.post_order_dft(node.left)
        # traverse the right side of the tree
        if node.right:
            # print right side values
            node.post_order_dft(node.right)
        # visit and print root value
        print(node.value)
