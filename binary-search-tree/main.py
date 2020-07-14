

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
        getattr(self, f"{type}_print")()

    def inorder_print(self, level=1):
        if level == 1:
            print("In Order Print:")
        preceding_space = " " + ("-" * level) + " "
        print(f"{preceding_space}{self.value}")
        if self.left:
            self.left.inorder_print(level=level+1)
        if self.right:
            self.right.inorder_print(level=level+1)

# Build up an example tree:

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
