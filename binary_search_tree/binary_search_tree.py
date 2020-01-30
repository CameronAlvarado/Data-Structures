from dll_stack import Stack
from dll_queue import Queue
import sys


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):  # MVP
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                # Recursive
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                # Recursive
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):  # MVP
        if target is not self.value:
            if target is not self.left:
                new_value = self.left
                if self.contains(new_value) is False:
                    return False
            if target is not self.right:
                new_value = self.right
                if self.contains(new_value) is False:
                    return False
            else:
                return True
        else:
            return True

        # Return the maximum value found in the tree

    def get_max(self):  # MVP
        pass

        # Call the function `cb` on the value of each node
        # You may use a recursive or iterative approach
    def for_each(self, cb):  # MVP
        pass

        # DAY 2 Project -----------------------

        # Print all the values in order from low to high
        # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

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
