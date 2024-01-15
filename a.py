class Node:
    def __init__(self,value):
        self.right = None
        self.left = None
        self.data = value

class Tree:
    def createNode(self,node):
        return Node(node)
    
    def insertNode(self,node,data):
        if node is None:
            return self.createNode(data)
        
        if data < node.data:
            node.left = self.insertNode(node.left,data)
        else:
            node.right = self.insertNode(node.right,data)

        return node
    def inorder_traversal(self,root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data)
            self.inorder_traversal(root.right)

tree = Tree()
root = tree.createNode(8)
tree.insertNode(root,9)
tree.insertNode(root,7)
tree.insertNode(root,10)
tree.insertNode(root,5)
tree.insertNode(root,15)
tree.insertNode(root,12)
tree.insertNode(root,4)
tree.insertNode(root,19)
tree.insertNode(root,6)


tree.inorder_traversal(root)
