class Queue(object):
    def __init__(self):
        self.item = []

    def isEmpty(self):
        ...

    def size(self):
        ...

    def enqueue(self,item):
        self.item.insert(0,item)

    def dequeue(self):
        self.item.pop()

