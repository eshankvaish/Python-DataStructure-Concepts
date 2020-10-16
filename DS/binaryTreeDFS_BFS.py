class newNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printLevelOrder(root):
    h=height(root)
    for i in range(1,h+1):
        printGivenLevel(root,i)

def printGivenLevel(root,level):
    if root is None:
        return
    if level==1:
        print(root.data,end="  ")
    elif level>1:
        printGivenLevel(root.left,level-1)
        printGivenLevel(root.right, level-1)

def height(node):
    if node is None:
        return 0
    else:
        lheight=height(node.left)
        rheight=height(node.right)

        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1

def printInorder(root):
    if root==None:
        return
    else:
        printInorder(root.left)
        print(root.data, end="  ")
        printInorder(root.right)

def printPostorder(root):
    if root==None:
        return
    else:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data, end="  ")

def printPreorder(root):
    if root==None:
        return
    else:
        print(root.data, end="  ")
        printPreorder(root.left)
        printPreorder(root.right)

root = newNode(10)
root.left=newNode(11)
root.left.left=newNode(7)
root.left.right=newNode(12)
root.right=newNode(9)
root.right.left=newNode(15)
root.right.right=newNode(8)

print("\nPreorder: ")
printPreorder(root)
print("\n\nInorder: ")
printInorder(root)
print("\n\nPostorder: ")
printPostorder(root)
print("\n\nLevelorder: ")
printLevelOrder(root)