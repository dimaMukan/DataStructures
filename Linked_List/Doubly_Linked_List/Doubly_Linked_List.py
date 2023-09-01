class DoublylinkedList(object):
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

a = DoublylinkedList(1)
b = DoublylinkedList(2)
c = DoublylinkedList(3)

a.next = b
b.prev = a
b.next = c
c.prev = b

print(c.prev.value)