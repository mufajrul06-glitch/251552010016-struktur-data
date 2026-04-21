class mangkok:

    def __init__(self) :
        self.items = []

    def push (self, item) :
        self.items.append(item)

    def pop (self) :
        if not self.is_empty() :
            return self.items.pop()
        return 'mangkok kosong!'

    def peek(self) :
        if not self.is_empty() :
            return self.items[-1]

    def is_empty(self) :
        return len (self.items) == 0

    def size(self) :
        return len (self.items)

    def __str__(self) :
        return str(self.items)