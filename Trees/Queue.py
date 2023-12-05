class Queue:
    def __init__(self, cap=10):
        self.cap = cap
        self.size = 0
        self.data = [None] * self.cap
        self.front = 0
        self.rear = -1

    def capacity(self):
        return self.cap

    def resize(self, new_cap):
        new_data = [None] * new_cap
        for i in range(self.size):
            new_data[i] = self.data[(self.front + i) % self.cap]
        self.data = new_data
        self.cap = new_cap
        self.front = 0
        self.rear = self.size - 1

    def enqueue(self, data):
        if self.size == self.cap:
            self.resize(self.cap * 2)
        self.rear = (self.rear + 1) % self.cap
        self.data[self.rear] = data
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError('dequeue() used on empty queue')
        value = self.data[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return value

    def get_front(self):
        if self.size == 0:
            return None
        return self.data[self.front]

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size