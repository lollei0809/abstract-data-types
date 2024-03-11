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


