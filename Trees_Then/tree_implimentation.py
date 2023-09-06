def BinaryTree(r):
    return [r,[],[]]

def insertLeft(root,NewBranch):
    t = root.pop(1)
    if len(t) < 1:
        root.insert(1,[NewBranch,t,[]])
    else:
        root.insert(1,[NewBranch,[],[]])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,NewValue):
    root[0] = NewValue

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = BinaryTree(3)
print(insertLeft(r,4))
print(insertLeft(r,4))
print(insertRight(r,5))
print(insertRight(r,5))

