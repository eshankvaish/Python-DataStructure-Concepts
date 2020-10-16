class newNode:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

#inorder traversal
def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.key,end='  ')
    inorder(temp.right)

def insert(temp,key):  #to insert at the first empty position
    q=[]
    q.append(temp)

    while(len(q)):
        temp=q[0]
        q.pop(0)
        if not temp.left:
            temp.left=newNode(key)
            break
        else:
            q.append(temp.left)
        
        if not temp.right:
            temp.right=newNode(key)
            break
        else:
            q.append(temp.right)

def deleteDeepest(root,d_node):
    q=[]
    q.append(root)
    while(len(q)):
        temp=q.pop()
        if temp is d_node:
            temp=None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right=None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left=None
                return
            else:
                q.append(temp.left)

def deletion(root,key):
    if root==None:
        return None
    if root.left==None and root.right==None:
        if root.key==key:
            return None
        else:
            return root
    key_node=None
    q=[]
    q.append(root)
    while(len(q)):
        temp=q.pop(0)
        if temp.key==key:
            key_node=temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.key
        deleteDeepest(root,temp)
        key_node.key=x
    return root

root = newNode(10)
root.left=newNode(11)
root.left.left=newNode(7)
root.left.right=newNode(12)
root.right=newNode(9)
root.right.left=newNode(15)
root.right.right=newNode(8)

print("Inorder traversal before insertion: ")
inorder(root)

insert(root,12)

print()
print("Inorder traversal after insertion: ")
inorder(root)

print("Tree before deletion:")
inorder(root)
root=deletion(root,11)
print()
print("Tree after deletion: ")
inorder(root)