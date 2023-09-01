class Node(object):
    def __init__(self,data):
        self.prev = None
        self.next = None
        self.data = data

class Double_linkedList(object):
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
