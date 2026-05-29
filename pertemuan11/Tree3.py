class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_balanced(root):
    def check(node):
        if node is None:
            return 0, True
        left_height, left_balanced = check(node.left)
        right_height, right_balanced = check(node.right)

        height = max(left_height, right_height) + 1
        balanced = (
            left_balanced and right_balanced and abs(left_height - right_height) <= 1
        )
        return height, balanced

    _, balanced = check(root)
    return balanced

def print_tree(node, prefix="", is_left=True):
    if node.right:
        print_tree(node.right, prefix + ("|   " if is_left else "    "), False)

    print(prefix + ("└── " if is_left else "┌── ") + str(node.key))

    if node.left:
        print_tree(node.left, prefix + ("    " if is_left else "|   "), True)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

print("Visualisasi Balanced Tree:")
print_tree(root)

print("\nApakah tree seimbang (balanced)?", is_balanced(root))