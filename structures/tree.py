"""Tree structure implementation"""


class Node:
    """Tree structure implementation"""
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    
    def is_operator(self):
        return self.value in ['+', '-', '*', '/', '^']

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value
