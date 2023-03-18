class Queue:
    def __init__(self):
        self.elements = {}
        self.head = 0
        self.tail = 0

    def enqueue(self, element):
        self.elements[self.tail] = element
        self.tail += 1

    def dequeue(self):
        item = self.elements[self.head]
        del self.elements[self.head]
        self.head += 1
        return item

    def peek(self):
        return self.elements[self.head]

    @property
    def length(self):
        return self.tail - self.head

    @property
    def isEmpty(self):
        return self.length == 0