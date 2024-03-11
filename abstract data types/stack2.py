class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def Push(self, item):
        self.items.append(item)

    def Pop(self):
        return self.items.pop()

    def Peek(self):
        return self.items[len(self.items) - 1]

    def Size(self):
        return len(self.items)


# define a Queue
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop(0)
        else:
            return "Queue empty"

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

    def showFront(self):
        print(self.items[0])