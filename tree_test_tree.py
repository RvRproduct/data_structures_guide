"""
Name
Tree
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        # add pre-order and post-order form here
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        pass

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        pass

# in-order-> 4-2-5-1-6-3-7-8-
# pre-order-> 1-2-4-5-3-6-7-8-
# post-order-> 4-2-5-6-3-7-8-1-
#             1
#          /     \
#         2       3
#        / \     / \
#       4   5   6   7
#                    \
#                     8

# Set up tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)
print(tree)

# in-order form
print(tree.print_tree("inorder"))
# pre-order form
# post-order form

