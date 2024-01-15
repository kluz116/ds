class Node:
    def __init__(self,value) -> None:
        self.right = None
        self.data = value
        self.left = None


class Tree:

    def createNode(self,data):
        if data is None:
            return Node(data)
    
    def insertNode(self,node,data):
        if node is None:
            self.createNode(node)

        if data < node.data:
            node.left = self.insertNode(node.left,data)
        else:
            node.right = self.insertNode(node.right,data)

        return node