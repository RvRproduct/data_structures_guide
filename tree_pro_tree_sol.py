class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.root = None

class MyTree():

    def __init__(self):
        self.tree = Node()

    def add_roots(self):
        nodes = int(input("\nHow many nodes? "))
        for r in range(0, nodes):
            r = input("\nAdd a Value: ")
            if not self.tree.root:
                self.tree.root = r
            else:
                while True:
                    link = ""
                    l_n = input("\nLeft or Right? ")
                    if l_n not in("left", "right"):
                        print("\nEnter only 'left' or 'right'")
                    else:
                        link += f"{l_n}, "
                        coutin = ""
                        while coutin not in ("yes", "y", "no", "n"):
                            contin = input("\n Continue? ")
                            if contin in ("yes", "y"):
                                break
                            elif contin in ("no, n"):
                                if not self.tree.root.link:
                                    print("""\nThe previous link/root wasn't implemented first
can't add link root needed. Try again Please""")
                                else:
                                    self.tree.root.link = r

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + "is no supported.")
            return False

    def preorder_print(self, start, traversal):
        # Root->Left->Right
        if start:
            traversal += (str(start.value + "-"))
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        # Left->Root->Right
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
        
    def postorder_print(self, start, traversal):
        # Left->Right->Root
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
        
    def menu(self):
        self.add_roots()
        self.print_tree("preorder")


make_tree = MyTree()
make_tree.menu()