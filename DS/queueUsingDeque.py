from collections import deque
q=deque()
q.append('a')
q.append('b')
q.append('c')

print("Initial Queue is:")
print(q)

print("Elements deleted from queue: ", q.popleft(), q.popleft())

print("Queue after removing elements: ",q)
