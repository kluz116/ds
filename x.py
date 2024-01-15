class Node:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        left (Node): The left child node.
        right (Node): The right child node.
        data (Any): The data value stored in the node.
    """
    
    def __init__(self, value):
        """
        Initializes a new instance of the Node class.
        
        Args:
            value (Any): The data value to be stored in the node.
        """
        self.left = None
        self.right = None
        self.data = value
    

class Tree:
    def createNode(self,node):
        return Node(node)
    
    def insert(self,node,data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        else:
            node.right = self.insert(node.right,data)
        
        return node
    def inorder_tranverse(self,root):
        if root is not None:
            self.inorder_tranverse(root.left)
            print(root.data)
            self.inorder_tranverse(root.right)
    
tree = Tree()
root = tree.createNode(5)
tree.insert(root,6)
tree.insert(root,10)
tree.insert(root,4)
tree.insert(root,15)
tree.insert(root,9)
tree.insert(root,8)
tree.insert(root,2)
tree.inorder_tranverse(root=root)