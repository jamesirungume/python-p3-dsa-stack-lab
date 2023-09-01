class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        if self.full():
            return False
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) ==self.limit
    
    def search(self,target):
        for i, item in enumerate(self.items[:: -1]):
            if item == target:
                return i
        return -1