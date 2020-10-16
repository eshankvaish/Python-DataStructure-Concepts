from queue import LifoQueue
stack = LifoQueue(maxsize=3)  #maxsize=0 means infinite length

stack.put('a')
stack.put('a')
stack.put('a')

print("Full: ", stack.full())
print("Size: ",stack.qsize())
print("Elements popped from stack: ", stack.get())

print("\nEmpty: ", stack.empty())