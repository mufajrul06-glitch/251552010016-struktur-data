class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        print(" " * level + f"- {self.value}")
        for child in self.children:
            child.print_tree(level + 1)
            
    def get_degree(self):
        return len(self.children)
    
    def get_height(self):
        if not self.children:
            return 1
        return 1 + max(child.get_height() for child in self.children)

root = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")

root.add_child(node_b)
root.add_child(node_c)

node_b.add_child(node_d)
node_b.add_child(node_e)

node_c.add_child(node_f)
node_c.add_child(node_g)

print("Struktur Tree:")
root.print_tree()

print(f"\nDerajat Node A: {root.get_degree()}")
print(f"Derajat Node B: {node_b.get_degree()}")
print(f"Derajat Node F: {node_f.get_degree()}")    
print(f"Derajat Node G: {node_g.get_degree()}")

print(f"\nTinggi pohon dari root A: {root.get_height()}")