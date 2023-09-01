class Dequeue(object):
    def __init__(self):
        self.items = []

    def isEmty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self,item):
        self.items.pop()

    def removeRear(self,item):
        self.items.pop(0)

