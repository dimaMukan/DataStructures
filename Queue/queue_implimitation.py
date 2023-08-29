class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmty(self):
        return self.items == []

    def size(self):
        return len(self.items)

q = Queue()
print(q.size())
print(q.isEmty())
q.enqueue(2)
print(q.size())
print(q.dequeue())
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.size())



