class BinaryNode:
    def __init__(self, Value):
        self.value = Value
        self.left = None
        self.right = None

root = BinaryNode("A")
root.left = BinaryNode("B")
root.right = BinaryNode("C")
root.left.left = BinaryNode("D")
root.left.right = BinaryNode("E")

def preorder(node):
    if node:
        print(node.value, end=' ')
        preorder(node.left)
        preorder(node.right)

print("binary tree - preorder traversal:")
preorder(root)