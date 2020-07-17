class Node(object):
    """
    A single node of a BST.
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self):
        """Check to see if this is a left node."""
        if not self.left and not self.right:
            return True
        return False

    def print_tree(self, type="inorder"):
        print(f"Printing Tree {type}")
        getattr(self, f"{type}_print")()

    def preorder_print(self):
        """Pre-Order Traversal"""
        print(f"{self.value}")
        if self.left:
            self.left.preorder_print()
        if self.right:
            self.right.preorder_print()

    def inorder_print(self):
        """In-Order Traversal
        
        Prints items in a sorted way, low to high."""
        if self.left:
            self.left.inorder_print()
        print(f"{self.value}")
        if self.right:
            self.right.inorder_print()

    def postorder_print(self):
        """Post-Order Traversal"""
        if self.left:
            self.left.postorder_print()
        if self.right:
            self.right.postorder_print()
        print(f"{self.value}")

    def insert(self, number: int):
        """
        Insert a node into the proper place.
        
        Does not allow duplicate nodes.
        """
        if self.value == number:
            return False
        elif number < self.value:
            if self.left:
                return self.left.insert(number)
            else:
                self.left = Node(number)
                return True
        else:
            if self.right:
                return self.right.insert(number)
            else:
                self.right = Node(number)
                return True

    def find(self, number: int):
        """
        Find a number in the tree. Return False if not.
        """
        if self.value == number:
            return True
        elif number < self.value and self.left:
            return self.left.find(number)
        elif number > self.value and self.right:
            return self.right.find(number)
        return False

    def remove(self, number: int):
        """
        Remove node if number is found.
        """
        if self.value == number:
            raise Exception("Can not delete root node.")
        elif number < self.value and self.left:
            if self.left.value == number:
                self.left = None
                return True
            return self.left.remove(number)
        elif number > self.value and self.right:
            if self.right.value == number:
                self.right = None
                return True
            return self.right.remove(number)
        return False

# Build up an example tree:

print("Create a tree manually.")
root_node = Node(10)
root_node.left = Node(7)
root_node.left.left = Node(6)
root_node.left.right = Node(8)

root_node.right = Node(12)
root_node.right.left = Node(11)
root_node.right.right = Node(15)

# Print out tree using breadth-first search allowing each layer
# to be printed at a time.
root_node.print_tree()


print("Using magic `insert_node` function:")
bst_1 = Node(10)
bst_1.insert(7)
bst_1.insert(6)
bst_1.insert(8)
bst_1.insert(12)
bst_1.insert(11)
bst_1.insert(15)
bst_1.insert(17)

bst_1.print_tree()

assert bst_1.find(17)
assert not bst_1.find(22)

bst_1.remove(17)

assert not bst_1.find(17)

bst_1.print_tree(type="preorder")

bst_1.print_tree(type="inorder")

bst_1.print_tree(type="postorder")