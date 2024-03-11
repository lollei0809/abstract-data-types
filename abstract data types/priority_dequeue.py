class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        found = False
        current_priority = 0
        if len(self.items) > 0:
            while not found:
                current_priority += 1
                for item in self.items:
                    if item[1] == current_priority:
                        found = True
                        self.items.remove(item)
                        return item

        else:
            return "Queue empty"

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

    def showFront(self):
        print(self.items[0])
