from collections import deque

stack = deque()


stack.append(1)
stack.append(3)
stack.append(7)

print('Initial Stack: ')
print(stack)

print("Elements being popped from stack: ")
print(stack.pop())
print(stack.pop())

print("Stack after elements are popped: ")
print(stack)
for i in stack:
    print(i)