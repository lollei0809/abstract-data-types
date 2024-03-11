class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        temp_list = []
        i = 1
        if len(self.items)!=0:
            while self.items[-i][1] >= item[1]:
                temp_list.append(self.items[-i])
                self.items.pop(-i)
                if i>= len(self.items):
                    break
                else:
                    i+=1

        self.items.append(item)
        self.items.extend(temp_list)



    def dequeue(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return "Queue empty"

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

    def showFront(self):
        print(self.items[0])
