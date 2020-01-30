from dll_stack import Stack
from dll_queue import Queue
import sys


class BinarySearchTree:  # a node of the tree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.stack = Stack()

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left is None:  # or, 'if not self.left'
                self.left = BinarySearchTree(value)
            else:
                # Recursive
                self.left.insert(value)
        else:  # value is >= node
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                # Recursive
                # Doesn't return bc operation is performed w/o returning anything.
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is self.value:
            return True
        elif target > self.value:
            if self.right is None:
                return False
            else:
                # Must return, bc it returns T or F
                return self.right.contains(target)
        elif target < self.value:
            if self.left is None:
                return False
            else:
                # Must return, bc it returns T or F
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):  # <-- SEARCH, visit every right node.
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)  # <-- TRAVERSAL

        # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # create a stack
        stack = Stack()
        # create a base case
        if node.left is None:
            print(node.value)
        if node.left and node.right is None:
            stack.pop()
            node.in_order_print(stack.pop())
        # check values of left and right
        if node.left:
            # add node to stack
            stack.push(node.left)
            # Recurse
            node.in_order_print(node.left)
        if node.right:
            # add node to stack
            stack.push(node.right)
            # Recurse
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
