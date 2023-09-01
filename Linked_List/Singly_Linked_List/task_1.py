class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def cycle_check(node: Node):
    temp1 = node
    temp2 = node
    while temp2 is not None and temp2.next is not None:
        temp1 = temp1.next
        temp2 = temp2.next.next
        if temp2 == temp1:
            return True
    return False




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
d.next = a

print(cycle_check(a))
