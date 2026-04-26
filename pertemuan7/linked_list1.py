class node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = node("a")
b = node("b")
c = node("c")

a.next = b
b.next = c

current = a
while current:
    print(f"node @ {id(current)}|data:{current.data}|next:{id(current.next)if current.next else None}")
    current = current.next