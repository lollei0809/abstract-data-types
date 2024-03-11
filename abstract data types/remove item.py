from stack1 import Stack
list1 = ['h', 'e', 'l', 'l', 'o']
stack1 = Stack(list1, 10)
stack2 = Stack([], 10)

item = 'e'
"""
initial_size = stack1.size
for i in range (initial_size):
    if stack1.Peek() == item:
        stack1.Pop()
    else:
        stack2.Push(stack1.Pop())
for i in stack2.stack:
    stack1.Push(stack2.Pop())
print(stack1.stack)
print(stack2.stack)
"""

while not stack1.IsEmpty():
    for item in stack1.stack:
        temp=stack1.Pop()
        if temp != item:
            stack2.push(item)

    for item in stack2.stack:
        stack1.push(stack1.pop())


