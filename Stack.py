class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def push(self, this):
        self.items.append(this)

    def peek(self):
        if not self.isEmpty():
            return self.items[self.size() - 1]
        return None

    def size(self):
        return len(self.items)