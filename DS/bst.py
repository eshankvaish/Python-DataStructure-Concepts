class newNode:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key


def insert(root,node):
    if root is None:
        root=node
    else:
        if root.data<node.val:
            if root.right is None:
                root.right=node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)

def inorder(root):
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def search(root, key):
    if root is None or root.val==key:
        return root
    if root.val<key:
        return search(root.right,key)
    return search(root.left,key)

def minValueNode(node):
    current = node
    while(current.left is not None):
        current=current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key<root.key:
        root.left=deleteNode(root.left,key)
    elif(key>root.key):
        root.right=deleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp

        temp=minValueNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right, temp.key)
    return root


root = newNode(10)
root.left=newNode(11)
root.left.left=newNode(7)
root.left.right=newNode(12)
root.right=newNode(9)
root.right.left=newNode(15)
root.right.right=newNode(8)

