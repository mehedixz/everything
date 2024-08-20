class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class BST:
    def create_node(self,data):
        return Node(data)

    def insert(self,node,data):
        if node is None:
            return self.create_node(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        return node

    def traverse(self,node):
        if node is None:
            return
        self.traverse(node.left)
        print(node.data)
        self.traverse(node.right)


tree = BST()
root = tree.create_node(5)
tree.insert(root,8)
tree.insert(root,3)
tree.insert(root,11)
tree.insert(root,4)
tree.insert(root,1)
tree.insert(root,7)
tree.traverse(root)


