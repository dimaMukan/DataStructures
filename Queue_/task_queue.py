class Queue2Stacks__MySolutoin(object):

    def __init__(self):
        # Two Stacks
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            for i in self.stack1[::-1]:
                self.stack2.append(i)
        print(self.stack2)
        return self.stack2.pop()

# class Queue2Stacks(object):
#     def __init__(self):
#         self.instack = []
#         self.outstack = []
#
#     def enqueue(self,item):
#         self.instack.append(item)
#
#     def dequeue(self):
#         if not self.outstack:
#             while self.instack:
#                 self.outstack.append(self.instack.pop())
#         return self.outstack.pop()





a = Queue2Stacks()
for i in range(5):
    a.enqueue(i)

for i in range(5):
    print(a.dequeue())















