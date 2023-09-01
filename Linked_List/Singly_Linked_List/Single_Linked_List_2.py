class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def print_LList(self):
        temp = self.head
        while temp:
            print(temp.value, end=' ')
            temp = temp.next


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)

llist.print_LList()

