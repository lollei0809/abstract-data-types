class Stack:
    def __init__(self, pList, max_size):
        self.stack = list(pList)
        self.size = len(self.stack)
        self.max_size = max_size

    def Pop(self):
        self.stack.pop()

    def Push(self, val):
        self.stack.append(val)

    def Peek(self, ):
        return self.stack[-1]

    def IsEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def IsFull(self):
        if self.size == self.max_size:
            return True
        else:
            return False


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
    temp = stack1.Pop()
    if temp == item:


