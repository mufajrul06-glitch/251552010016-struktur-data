class node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = node(data)
    new_node.next = head
    return new_node

head = node("A")
head = insert_at_beginning(head,"A")

def print_linked_list(head):
    while head:
        next_id = id(head.next) if head.next else None
        print(f"[{head.data}({id(head)})]->", end="")
        head = head.next
    print("null")

A = node("A")
B = node("B")
C = node("C")

A.next = B
B.next = C

print_linked_list(head)