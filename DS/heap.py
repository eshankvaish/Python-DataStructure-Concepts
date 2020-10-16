from heapq import heappush,heappop, heapify
class MinHeap:
    def __init__(self):
        self.heap=[]
    def parent(self,i):
        return (i-1)//2
    
    def insertKey(self,key):
        heappush(self.heap,key)
    
    def decreaseKey(self,i,new_val):
        self.heap[i]  = new_val  
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]): 
            # Swap heap[i] with heap[parent(i)] 
            self.heap[i] , self.heap[self.parent(i)] = ( 
            self.heap[self.parent(i)], self.heap[i])

    def extractMin(self):
        return heappop(self.heap)
    
    def deleteKey(self,i):
        self.decreaseKey(i,float("-inf"))
        self.extractMin()
    
    def getMin(self):
        return self.heap[0]


heap = MinHeap()
heap.insertKey(3)
heap.insertKey(2)
heap.insertKey(1)
heap.deleteKey(2)
heap.insertKey(15)
heap.insertKey(5)
heap.insertKey(40)
heap.insertKey(20)

print(heap.extractMin())
print (heap.getMin())
heap.decreaseKey(2,1)