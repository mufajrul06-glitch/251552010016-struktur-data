class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")

def dfs_preorder(node):
    if node:
        print(node.value, end=' ')
        dfs_preorder(node.left)
        dfs_preorder(node.right)

def dfs_inorder(node):
    if node:
        dfs_inorder(node.left)
        print(node.value, end=' ')
        dfs_inorder(node.right)

def dfs_postorder(node):
    if node:
        dfs_postorder(node.left)
        dfs_postorder(node.right)
        print(node.value, end=' ')

print("DFS Preorder:")
dfs_preorder(root)

print("\nDFS Inorder:")
dfs_inorder(root)

print("\nDFS Postorder:")
dfs_postorder(root)