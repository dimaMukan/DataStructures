class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print('\n')

    def to_last_node(self, number):
        temp = self.head
        temp1 = self.head
        temp_num = 0

        while temp:
            temp_num += 1
            temp = temp.next

        target = temp_num - (temp_num-number)
        temp_num = 0
        while temp1:
            temp_num += 1
            if temp_num == target:
                print(temp1.data)
            temp1 = temp1.next


llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.print()
llist.print()
llist.to_last_node(2)

