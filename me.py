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
        if(data < node.data):
            node.left = self.insertNode(node.left,data)
        else:
            node.right = self.insertNode(node.right,data)

        return node

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)


tree = Tree()
root = tree.createNode(70)
tree.insertNode(root,60)
tree.insertNode(root,30)
tree.insertNode(root,86)

tree.inorder(root)