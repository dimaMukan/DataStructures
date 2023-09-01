class Stack(object):
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def peek(self):
        return self.item[-1]

    def pop(self):
        self.item.pop()

    def push(self,item):
        self.item.append(item)

