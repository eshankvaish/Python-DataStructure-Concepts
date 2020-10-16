class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)

        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while(current.next):
            current=current.next
        current.next=new_node

    def deleteNode(self,key):
        temp=self.head
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return
        while temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            return
        prev.next=temp.next
        temp=None

    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp=temp.next

llist=LinkedList()
llist.push(6)
llist.push(5)
llist.push(7)
llist.push(10)
llist.deleteNode(5)

llist.printList()

