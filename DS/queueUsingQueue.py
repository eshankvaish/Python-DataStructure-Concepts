from queue import Queue

q=Queue(maxsize=3)
print(q.qsize())

q.put('a')
q.put('b')
q.put('c')

print("\nFull: ",q.full())

print("Elements dequed from queue: ",q.get(),q.get())

print("Empty: ",q.empty())

print(q)