class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_linked_list(node):
        while node:
            next_id = id(node.next) if node.next else None
            print(f"[{node.data}]|{next_id}]->", end="")
            node = node.next
        print("null")

a = node("a")
b = node("b")
c = node("c")

a.next = b
b.next = c

print_linked_list(a)